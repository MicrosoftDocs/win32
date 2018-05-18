---
Description: 'This topic describes improvements in Windows 8 for work queues and threading in the Microsoft Media Foundation platform.'
ms.assetid: '9E2A1D94-BF82-488E-8297-D524683ABE17'
title: Work Queue and Threading Improvements
---

# Work Queue and Threading Improvements

This topic describes improvements in Windows 8 for work queues and threading in the Microsoft Media Foundation platform.

-   [Windows 7 Behavior](#windows-7-behavior)
    -   [Work Queues](#work-queues)
    -   [MMCSS Support](#mmcss-support)
    -   [IMFRealTimeClient](#imfrealtimeclientex)
-   [Windows 8 Improvements](#windows-8-improvements)
    -   [Multithreaded Work Queues](#multithreaded-work-queues)
    -   [Shared Task Work Queues](#shared-task-work-queues)
    -   [Wait Queue](#wait-queue)
    -   [Enhancements to MMCSS Support](#enhancements-to-mmcss-support)
    -   [IMFRealTimeClientEx](#imfrealtimeclientex)
    -   [Topology Branches](#topology-branches)
-   [Recommendations](#recommendations)
-   [Summary](#summary)
-   [Related topics](#related-topics)

## Windows 7 Behavior

This section summarizes the behavior of Media Foundation work queues in Windows 7.

### Work Queues

The Media Foundation platform creates several standard work queues. Only two are documented as being for general application use:

-   **MFASYNC\_CALLBACK\_QUEUE\_STANDARD**
-   **MFASYNC\_CALLBACK\_QUEUE\_LONG\_FUNCTION**

An application or component can allocate new work queues by calling [**MFAllocateWorkQueue**](mfallocateworkqueue.md) or [**MFAllocateWorkQueueEx**](mfallocateworkqueueex.md). The **MFAllocateWorkQueueEx** function defines two types of work queue:

-   **MF\_STANDARD\_WORKQUEUE** creates a work queue without a message loop.
-   **MF\_WINDOW\_WORKQUEUE** creates a work queue with a message loop.

To queue a work item, call [**MFPutWorkItem**](mfputworkitem.md) or [**MFPutWorkItemEx**](mfputworkitemex.md). The platform executes the work item by invoking the caller-provided implementation of [**IMFAsyncCallback**](imfasynccallback.md). In Windows 7 and earlier, the platform creates one thread per work queue.

### MMCSS Support

The [Multimedia Class Scheduler Service](base.multimedia_class_scheduler_service) (MMCSS) manages thread priorities so that multimedia applications get regular slices of CPU time, without denying CPU resources to lower-priority applications. MMCSS defines a set of *tasks* that have different CPU utilization profiles. When a thread joins an MMCSS task, MMCSS sets the priority of the thread based on several factors:

-   The base priority of the task, which is set in the registry.
-   The relative thread priority, which is set at run time by calling [**AvSetMmThreadPriority**](base.avsetmmthreadpriority).
-   Various run-time characteristics, such as whether the application is in the foreground, and how much CPU time is being consumed by the threads in each MMCSS class.

An application can register a work queue with MMCSS by calling [**MFBeginRegisterWorkQueueWithMMCSS**](mfbeginregisterworkqueuewithmmcss.md). This function takes a work queue ID, an MMCSS class (task name), and the MMCSS task identifier. Internally, it calls [**AvSetMmThreadCharacteristics**](base.avsetmmthreadcharacteristics) with the task name and task ID. After a work queue is registered with MMCSS, you can get the class and task ID by calling [**MFGetWorkQueueMMCSSClass**](mfgetworkqueuemmcssclass.md) and [**MFGetWorkQueueMMCSSTaskId**](mfgetworkqueuemmcsstaskid.md).

The [Media Session](media-session.md) provides somewhat higher-level access to these APIs, through the [**IMFWorkQueueServices**](imfworkqueueservices.md) interface. This interface provides two primary methods:

| Method                                                                                                            | Description                                                                                                                                                                                                                                                                                   |
|-------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BeginRegisterPlatformWorkQueueWithMMCSS**](imfworkqueueservices-beginregisterplatformworkqueuewithmmcss.md)   | Registers a work queue with an MMCSS task. This method is essentially a thin wrapper around [**MFBeginRegisterWorkQueueWithMMCSS**](mfbeginregisterworkqueuewithmmcss.md), but you can pass the value **MFASYNC\_CALLBACK\_QUEUE\_ALL** to register all of the platform work queues at once. |
| [**BeginRegisterTopologyWorkQueuesWithMMCSS**](imfworkqueueservices-beginregistertopologyworkqueueswithmmcss.md) | Registers a branch of the topology with a work queue.                                                                                                                                                                                                                                         |



 

To register a topology branch, do the following.

1.  Set the [MF\_TOPONODE\_WORKQUEUE\_ID](mf-toponode-workqueue-id-attribute.md) attribute on the source node for the branch. Use any application-defined value.
2.  Optionally, set the **MF\_TOPONODE\_WORKQUEUE\_MMCSS\_CLASS** to join the work queue to an MMCSS task.
3.  Call [**BeginRegisterTopologyWorkQueuesWithMMCSS**](imfworkqueueservices-beginregistertopologyworkqueueswithmmcss.md) on the resolved topology.

The Media Session allocates a new work queue for each unique value of [MF\_TOPONODE\_WORKQUEUE\_ID](mf-toponode-workqueue-id-attribute.md). For each topology branch, asynchronous pipeline operations are performed on the work queue that is assigned to the branch.

### IMFRealTimeClient

The [**IMFRealTimeClient**](imfrealtimeclient.md) interface is intended for pipeline components that either create their own threads or use work queues for asynchronous operations. The Media Session uses this interface to notify the pipeline component of the correct behavior, as follows:

-   If the pipeline component creates a worker thread, the [**IMFRealTimeClient::RegisterThreads**](imfrealtimeclient-registerthreads.md) method notifies the component which MMCSS class to join.
-   If the pipeline component uses a work queue, the [**IMFRealTimeClient::SetWorkQueue**](imfrealtimeclient-setworkqueue.md) method tells the component which work queue to use.

Typically, a pipeline component uses either a thread or a work queue to perform asynchronous tasks, but not both.

## Windows 8 Improvements

### Multithreaded Work Queues

In Windows 8, Media Foundation supports a new type of work queue called the *multithreaded queue*. A multithreaded queue uses a system thread pool to dispatch work items. The multithreaded queue scales better than the previous single-threaded queues. For example,

-   Several components can share a multithreaded queue without blocking one another, requiring the creation of fewer threads.

-   Work items are optimized to avoid context switches if an event is already set. This is more efficient than creating your own threads to wait on events.

When using [**IMFRealTimeClientEx**](imfrealtimeclientex.md), applications should avoid spinning up threads and instead should use the work queues. To accomplish this, applications should implement [**SetWorkQueueEx**](imfrealtimeclientex-setworkqueueex.md) and not use [**RegisterThreads**](imfrealtimeclientex-registerthreadsex.md) and [**UnregisterThreads**](imfrealtimeclientex-unregisterthreads.md).

When the Media Foundation platform is initialized, it creates a multithreaded queue with the identifier **MFASYNC\_CALLBACK\_QUEUE\_MULTITHREADED**.

A multithreaded queue does not serialize work items. Whenever a thread from the thread pool becomes available, the next work item on the queue is dispatched. The caller must ensure that work is serialized correctly. To make this easier, Media Foundation defines a *serial work queue*. A serial queue wraps another work queue but guarantees fully serialized execution. The next item on the queue is not dispatched until the previous item completes.

The following code creates a serializer queue over the platform multithreaded queue.


```C++
DWORD workQueueID;
hr = MFAllocateSerialWorkQueue(MFASYNC_CALLBACK_QUEUE_MULTITHREADED, &amp;workQueueID); 
```



More than one serial queue can wrap the same multithreaded queue. The serial queues then share the same thread pool, and serialized execution is enforced within each queue.

The standard work queues that existed prior to Windows 8 are now implemented as serial work queues that wrap the platform multithreaded queue. This change preserves backward compatibility.

### Shared Task Work Queues

To work correctly with the kernel scheduler, there should be one multithreaded work queue for each MMCSS task that you use. The Media Foundation platform allocates these as needed, up to one per MMCSS task, per process. To get the shared work queue for a particular MMCSS task, call [**MFLockSharedWorkQueue**](mflocksharedworkqueue.md) and specify the task name. The function looks up the task name in a table. If a work queue does not already exist for this task, the function allocates a new MT work queue and immediately joins it to the MMCSS task. If a work queue already exists for that task, the function returns the identifier of the existing work queue.

### Wait Queue

The *wait queue* is a special platform work queue that waits on events to be signaled. If a component needs to wait for an event to be signaled, it can use the wait queue instead of creating a worker thread to wait on the event.

To use the wait queue, call [**MFPutWaitingWorkItem**](mfputwaitingworkitem.md). The parameters include the event handle and an [**IMFAsyncResult**](imfasyncresult.md) pointer. When the event is signaled, the wait queue invokes your callback. There is a single platform wait queue; applications cannot create their own wait queues.

### Enhancements to MMCSS Support

The following new Media Foundation platform functions relate to MMCSS.



| Function                                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                           |
|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MFBeginRegisterWorkQueueWithMMCSSEx**](mfbeginregisterworkqueuewithmmcssex.md) | Registers a work queue with MMCSS. This function includes a parameter to specify relative thread priority. Internally, this value is translated into a call to [**AvSetMmThreadPriority**](base.avsetmmthreadpriority).                                                                                                                                                                               |
| [**MFGetWorkQueueMMCSSPriority**](mfgetworkqueuemmcsspriority.md)                 | Queries the priority of a work queue.                                                                                                                                                                                                                                                                                                                                                                 |
| [**MFRegisterPlatformWithMMCSS**](mfregisterplatformwithmmcss.md)                 | Registers all of the platform work queues with an MMCSS task. This function is similar to the [**IMFWorkQueueServices::BeginRegisterPlatformWorkQueueWithMMCSS**](imfworkqueueservices-beginregisterplatformworkqueuewithmmcss.md) method, but it can be used without creating an instance of the Media Session. In addition, the function includes a parameter to specify the base thread priority. |



 

Applications that use the Media Session should set the [MF\_TOPONODE\_WORKQUEUE\_MMCSS\_CLASS](mf-toponode-workqueue-mmcss-class-attribute.md) attribute to "Audio" for the audio rendering branch. Set the attribute to "Playback" for the video rendering branch.

### IMFRealTimeClientEx

The [**IMFRealTimeClientEx**](imfrealtimeclientex.md) interface to replaces IMFRealTimeClient, for pipeline components that perform asynchronous operations.



| Method                                                             | Description                                                                                                                                                                                                                    |
|--------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**RegisterThreadsEx**](imfrealtimeclientex-registerthreadsex.md) | Notifies the component to register its threads with MMCSS. This method is equivalent to [**IMFRealTimeClient::RegisterThreads**](imfrealtimeclient-registerthreads.md), but it adds a parameter for the base thread priority. |
| [**SetWorkQueueEx**](imfrealtimeclientex-setworkqueueex.md)       | Notifies the component to use a specific work queue. This method is equivalent to [**IMFReadTimeClient::SetWorkQueue**](imfrealtimeclient-setworkqueue.md), but it adds a parameter for the work item priority.               |
| [**UnregisterThreads**](imfrealtimeclientex-unregisterthreads.md) | Notifies the component to unregister its threads from MMCSS. This method is identical to the [**IMFRealTimeClient::UnregisterThreads**](imfrealtimeclient-unregisterthreads.md) method.                                       |



 

Pipeline components should use work queues, and should not create worker threads, for the following reasons:

-   Work queues scale better, because they use the OS thread pools.
-   The platform handles the details of registering work queues with MMCSS.
-   A worker thread can easily cause a deadlock that is hard to debug.

Also, consider using the serializer work queue if you need to serialize your asynchronous operations.

### Topology Branches

If the [MF\_TOPONODE\_WORKQUEUE\_MMCSS\_CLASS](mf-toponode-workqueue-mmcss-class-attribute.md) attribute registers a topology branch with MMCSS, in Windows 8 the Media Session uses the shared MT work queues. In earlier versions of Windows, the Media Session allocated a new work queue.

Two new attributes are defined for registering a topology branch with MMCSS.



| Attribute                                                                            | Description                         |
|--------------------------------------------------------------------------------------|-------------------------------------|
| [MF\_TOPONODE\_WORKQUEUE\_MMCSS\_PRIORITY](mf-toponode-workqueue-mmcss-priority.md) | Specifies the base thread priority. |
| [MF\_TOPONODE\_WORKQUEUE\_ITEM\_PRIORITY](mf-toponode-workqueue-item-priority.md)   | Specifies the work item priority.   |



 

## Recommendations

-   Applications that use the Media Session should set [MF\_TOPONODE\_WORKQUEUE\_MMCSS\_CLASS](mf-toponode-workqueue-mmcss-class-attribute.md) to "Audio" for the audio rendering branch and "Playback" for the video rendering branch.
-   Applications that use the Media Session should call [**IMFWorkQueueServices::BeginRegisterTopologyWorkQueuesWithMMCSS**](imfworkqueueservices-beginregistertopologyworkqueueswithmmcss.md) on the topology.
-   For pipeline components, work queues are recommended instead of worker threads. If the component uses either work queues or worker threads, implement [**IMFRealTimeClientEx**](imfrealtimeclientex.md).
-   Do not create private work queues, as this defeats the purpose of the platform work queues. Use either the platform multithreaded queue or a serial queue that wraps the platform multithreaded queue.
-   If you need to serialize asynchronous operations, use a serial queue.

## Summary

The following Media Foundation platform APIs that relate to threads and work queues are new for Windows 8.

-   [MF\_TOPONODE\_WORKQUEUE\_ITEM\_PRIORITY](mf-toponode-workqueue-item-priority.md)
-   [MF\_TOPONODE\_WORKQUEUE\_MMCSS\_PRIORITY](mf-toponode-workqueue-mmcss-priority.md)
-   [**MFAllocateSerialWorkQueue**](mfallocateserialworkqueue.md)
-   [**MFBeginRegisterWorkQueueWithMMCSSEx**](mfbeginregisterworkqueuewithmmcssex.md)
-   [**MFGetWorkQueueMMCSSPriority**](mfgetworkqueuemmcsspriority.md)
-   [**MFPutWaitingWorkItem**](mfputwaitingworkitem.md)
-   [**MFPutWorkItem2**](mfputworkitem2.md)
-   [**MFPutWorkItemEx2**](mfputworkitemex2.md)
-   [**MFRegisterPlatformWithMMCSS**](mfregisterplatformwithmmcss.md)
-   [**MFUnregisterPlatformFromMMCSS**](mfunregisterplatformfrommmcss.md)
-   [**MFLockSharedWorkQueue**](mflocksharedworkqueue.md)
-   [**IMFRealTimeClientEx**](imfrealtimeclientex.md)

## Related topics

<dl> <dt>

[Work Queues](work-queues.md)
</dt> </dl>

 

 



