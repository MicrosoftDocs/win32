---
description: A simple example project for the Activity Coordinator API.
ms.assetid: 722acf59-ee17-4033-b191-cb0bf53e22ae
title: Activity Coordinator example project
ms.topic: article
ms.date: 04/28/2022
---

# Activity Coordinator example project

## Example project overview

Let's consider the case of a music editing app. This app has high-priority background tasks that service user requests, like publishing content to cloud storage. There are also low-priority background tasks that support user interaction, like providing automatic recommendations to improve a composition while editing. Lastly, there are a set of deferred tasks that do not need to happen at any specific time without the user’s request, which is our focus in this example. In particular, we would like to periodically retrain the recommendation model when user impact is minimal. We can use the Activity Coordinator API to achieve this.

For this scenario, we would like to retrain the model when the user isn’t present. The retraining workflow in this scenario is also a GPU consumer, so we also want to run when it's a good time to use the GPU. We can specify these requirements using Activity Coordinator policies. The Activity Coordinator API will use our policy to determine when the requirements are met and send notifications for when to start or stop running our work.

In this case, the **GOOD** policy template meets most our needs as it tracks CPU, memory, system disk, power, and user-idle. We simply need to explicitly set a condition for GPU. It's important to remember that even though our workload will primarily utilize the GPU, the execution of our activity still inherently consumes CPU, memory, disk, and power. Our impact to these resources may also vary greatly between system configurations. For instance, a faster GPU could result in the CPU spending more time feeding the GPU with data, which may then result in more data being read or saved to disk. The speed of this disk may also affect CPU consumption in a similar fashion. By configuring all the resources we affect, we can be sure we don't inadvertently interfere with the user experience or degrade system performance. Additionally, the work itself has been broken down to happen in small chunks, so that we can adequately respond to coordination notifications to avoid running outside of the desired conditions.

To demonstrate how developers can change or downgrade policies, we also add the requirement that we want retraining to complete within 48-hours. The first 24-hours, our soft deadline, we attempt to run with our ideal policy, and the last 24-hours we downgrade to a lesser policy.

## Example project code

The following code is the music editing sample application. It leverages the Activity Coordinator API to perform background tasks, as described in the overview.

```cpp
#include <chrono>
#include <mutex>
#include <condition_variable>
#include <Windows.h>
#include <ActivityCoordinator.h>
#include <wil/resource.h>

// To use ActivityCoordinator, we must link to the OneCoreUAP library.

#pragma comment(lib, "OneCoreUAP.lib")

using namespace std;
using namespace chrono;
using namespace wil;

// Declare RAII wrappers for the Activity Coordinator policy and subscription.
// These behave like traditional smart pointers and will call their associated
// API cleanup functions when they go out of scope.

typedef wil::unique_any<
        ACTIVITY_COORDINATOR_POLICY,
        decltype(&DestroyActivityCoordinatorPolicy),
        DestroyActivityCoordinatorPolicy>
    unique_policy;

typedef wil::unique_any<
        ACTIVITY_COORDINATOR_SUBSCRIPTION,
        decltype(&UnsubscribeActivityCoordinatorPolicy),
        UnsubscribeActivityCoordinatorPolicy>
    unique_subscription;

struct WORKER_CONTEXT {
    mutex ContextLock;
    unique_threadpool_work Worker;
    bool ShouldRun;
    bool IsRunning;
    bool IsComplete;
    std::condition_variable CompletionSignal;
};

_Requires_lock_held_(workerContext->ContextLock)
void
ResumeWorker(
    _In_ WORKER_CONTEXT* workerContext
    )
{
    workerContext->ShouldRun = true;
    if (!workerContext->IsRunning && !workerContext->IsComplete) {

        // No active workers, so start a new one.

        workerContext->IsRunning = true;
        SubmitThreadpoolWork(workerContext->Worker.get());
    }
}

void
DeferredWorkEventCallback(
    _In_ ACTIVITY_COORDINATOR_NOTIFICATION notificationType,
    _In_ void* callbackContext
    )
{
    WORKER_CONTEXT* workerContext = reinterpret_cast<WORKER_CONTEXT*>(callbackContext);

    // Use this callback thread to dispatch notifications to a worker thread
    // about whether or not it should process the next chunk of deferred work.

    // Note: Do not use this thread to perform your activity's workload.

    lock_guard<mutex> scopedLock(workerContext->ContextLock);
    switch (notificationType) {
    case ACTIVITY_COORDINATOR_NOTIFICATION_RUN:

        // Allow deferred work to be processed.

        ResumeWorker(workerContext);

        break;

    case ACTIVITY_COORDINATOR_NOTIFICATION_STOP:

        // Stop processing deferred work.

        workerContext->ShouldRun = false;

        break;

    default:
        FAIL_FAST();
        break;
    }
}

bool
TrainNextModelChunk(
    )
{
    //
    // Returns true if all work is completed, or false if there is more work.
    //

    return false;
}

void
DeferredModelTrainingWorker(
    _Inout_ PTP_CALLBACK_INSTANCE callbackInstance,
    _Inout_opt_ PVOID callbackContext,
    _Inout_ PTP_WORK work
    )
{
    // Threadpool callback instance and work are not needed for this sample.

    UNREFERENCED_PARAMETER(callbackInstance);
    UNREFERENCED_PARAMETER(work);

    WORKER_CONTEXT* workerContext = reinterpret_cast<WORKER_CONTEXT*>(callbackContext);
    bool workComplete = false;

    // Keep processing work until being told to stop or all work has been completed.

    while (true) {
        {
            lock_guard<mutex> scopedLock(workerContext->ContextLock);

            if (workComplete) {
                workerContext->IsComplete = true;
            }

            if (!workerContext->ShouldRun || workerContext->IsComplete) {
                workerContext->IsRunning = false;
                break;
            }
        }

        // TrainNextModelChunk returns true when there is no more work to do.

        workComplete = TrainNextModelChunk();
    }

    workerContext->CompletionSignal.notify_all();
}

int
__cdecl
wmain(
    )
{
    WORKER_CONTEXT workerContext;
    workerContext.ShouldRun = false;
    workerContext.IsRunning = false;
    workerContext.IsComplete = false;

    // Create the worker that will be started by our subscription callback.

    workerContext.Worker.reset(CreateThreadpoolWork(
        DeferredModelTrainingWorker,
        &workerContext,
        nullptr));
    RETURN_LAST_ERROR_IF_NULL(workerContext.Worker);

    // Allocate a policy suited for tasks that are best run when unlikely
    // to cause impact to the user or system performance.

    unique_policy policy;
    RETURN_IF_FAILED(CreateActivityCoordinatorPolicy(
        ACTIVITY_COORDINATOR_POLICY_TEMPLATE_GOOD,
        &policy));

    // The model training in this sample consumes GPU. As per the MSDN docs, the
    // GOOD policy template doesn't currently include the GPU resource. We
    // therefore customize the policy to include good GPU conditions to minimize
    // the impact of running our work.

    RETURN_IF_FAILED(SetActivityCoordinatorPolicyResourceCondition(
        policy.get(),
        ACTIVITY_COORDINATOR_RESOURCE_GPU,
        ACTIVITY_COORDINATOR_CONDITION_GOOD));

    // Subscribe to the policy for coordination notifications.

    unique_subscription subscription;
    RETURN_IF_FAILED(SubscribeActivityCoordinatorPolicy(
        policy.get(),
        DeferredWorkEventCallback,
        &workerContext,
        &subscription));;

    // Destroy the policy because we no longer need it.

    policy.reset();

    // We want our task to complete within 48h, so we allocate 24h under our
    // ideal policy and before falling back to a downgraded policy.

    bool workerCompleted;

    {
        unique_lock<mutex> scopedLock(workerContext.ContextLock);
        workerCompleted = workerContext.CompletionSignal.wait_for(
            scopedLock,
            hours(24),
            [&workerContext] { return workerContext.IsComplete; });
    }

    if (workerCompleted) {

        // Since our work is complete, we should clean up our subscription by
        // unsubscribing. This would normally be handled quietly by our RAII
        // types, but we release them explicitly to demonstrate API flow for
        // developers manually managing resources.

        subscription.reset();
        return S_OK;
    }

    // We passed our soft deadline, so downgrade the policy and wait the
    // remaining 24h until our hard deadline has been reached. Since
    // Subscriptions and policies are independent of each other, we need to
    // create a new subscription with our downgraded policy to receive
    // notifications based on its configuration.
    // 
    // The downgraded policy uses medium conditions for all needed resources.
    // This gives us the best chance to run while helping to prevent us from
    // critically degrading the user experience, which we are more likely to do
    // when falling back to manual execution.

    RETURN_IF_FAILED(CreateActivityCoordinatorPolicy(
        ACTIVITY_COORDINATOR_POLICY_TEMPLATE_MEDIUM,
        &policy));

    RETURN_IF_FAILED(SetActivityCoordinatorPolicyResourceCondition(
        policy.get(),
        ACTIVITY_COORDINATOR_RESOURCE_GPU,
        ACTIVITY_COORDINATOR_CONDITION_MEDIUM));

    subscription.reset();
    RETURN_IF_FAILED(SubscribeActivityCoordinatorPolicy(
        policy.get(),
        DeferredWorkEventCallback,
        &workerContext,
        &subscription));

    {
        unique_lock<mutex> scopedLock(workerContext.ContextLock);
        workerCompleted = workerContext.CompletionSignal.wait_for(
            scopedLock,
            hours(24),
            [&workerContext] { return workerContext.IsComplete; });
    }

    // We passed our deadline, so unsubscribe and manually resume our task.

    subscription.reset();
    ResumeWorker(&workerContext);

    // We destroyed our subscription, so we wait indefinitely for completion as
    // there's nothing to pause execution of our task.

    unique_lock<mutex> scopedLock(workerContext.ContextLock);
    workerContext.CompletionSignal.wait(
        scopedLock,
        [&workerContext] { return workerContext.IsComplete; });

    return S_OK;
}
```

## Related topics

[Activity Coordinator API overview](activity-coordinator-api-overview.md)

[Activity Coordinator API and terminology](activity-coordinator-api-and-terminology.md)

[Choosing the right Activity Coordinator policy](choosing-the-right-activity-coordinator-policy.md)
