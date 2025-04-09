---
description: An example that shows how apps can use IsActivityCoordinatorResourceSupported to detect support for resources.
title: Checking for Activity Coordinator resource support
ms.topic: concept-article
ms.date: 06/12/2024
---

# Checking for Activity Coordinator resource support

This example shows how apps can use [IsActivityCoordinatorResourceSupported](/windows/win32/api/activitycoordinator/nf-activitycoordinator-isactivitycoordinatorresourcesupported) to detect support for resources prior to creating a policy. You can use the `IsActivityCoordinatorResourceSupported` to check for any supported [ACTIVITY_COORDINATOR_RESOURCE](/windows/win32/api/activitycoordinatortypes/ne-activitycoordinatortypes-activity_coordinator_resource) at runtime.

## Check for NPU support example

The following example demonstrates how to check for NPU support using the new capability-check API for resources. This API allows apps to check for supported resource types at runtime and will return `true` if the NPU resource is supported on the current system. This example creates an Activity Coordinator policy and sets the NPU resource condition to `ACTIVITY_COORDINATOR_CONDITION_GOOD` if it is supported.

```cpp
#include <Windows.h>
#include <ActivityCoordinator.h>
#include <wil/resource.h>
#include <apiquery2.h>

// Declare RAII wrappers for the Activity Coordinator policy and subscription.
// These behave like traditional smart pointers and will call their associated
// API cleanup functions when they go out of scope.
using unique_policy = wil::unique_any<
          ACTIVITY_COORDINATOR_POLICY,
          decltype(&DestroyActivityCoordinatorPolicy),
          DestroyActivityCoordinatorPolicy>;

bool
CanUseNpuPolicy()
{
    // Check that the Activity Coordinator feature check API is implemented
    // before calling.
    if (IsApiSetImplemented("ext-ms-win-resourcemanager-activitycoordinator-l1-1-1")) {
        if (IsActivityCoordinatorResourceSupported(ACTIVITY_COORDINATOR_RESOURCE_NPU)) {
            return true;
        }
    }

    return false;
}

int
__cdecl
wmain()
{
    unique_policy policy;

    // Activity Coordinator support for NPUs does not indicate their actual
    // presence on the system. Applications must still detect and target desired
    // hardware using their API or framework of choice.
    //
    // When using system resources not supported by Activity Coordinator, it is
    // recommended that policies always include USER_IDLE in the GOOD condition.
    // This will help minimize the potential for interference with a user's
    // foreground applications utilizing the same resource.
    //
    // The GOOD policy template covers this scenario in addition to other
    // resources that most applications are likely to affect even when targeting
    // dedicated hardware.
    RETURN_IF_FAILED(CreateActivityCoordinatorPolicy(
        ACTIVITY_COORDINATOR_POLICY_TEMPLATE_GOOD,
        &policy));

    if (CanUseNpuPolicy()) {
        RETURN_IF_FAILED(SetActivityCoordinatorPolicyResourceCondition(
            policy.get(),
            ACTIVITY_COORDINATOR_RESOURCE_NPU,
            ACTIVITY_COORDINATOR_CONDITION_GOOD));
    }

    // Proceed to use Activity Coordinator to run opportunistic work. See the
    // example project in the documentation for further details.

    return S_OK;
}
```

## See also

- [IsActivityCoordinatorResourceSupported](/windows/win32/api/activitycoordinator/nf-activitycoordinator-isactivitycoordinatorresourcesupported)
- [SetActivityCoordinatorPolicyResourceCondition](/windows/win32/api/activitycoordinator/nf-activitycoordinator-setactivitycoordinatorpolicyresourcecondition)
- [Activity Coordinator example project](activity-coordinator-example-project.md)
- [ACTIVITY_COORDINATOR_RESOURCE](/windows/win32/api/activitycoordinatortypes/ne-activitycoordinatortypes-activity_coordinator_resource)
