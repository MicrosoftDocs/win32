---
Description: This topic describes how to use work queues in Microsoft Media Foundation.
ms.assetid: 6be05df7-e8ff-4110-8f73-a62eb31fd414
title: Using Work Queues
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using Work Queues

This topic describes how to use work queues in Microsoft Media Foundation.

-   [Using Work Queues](#using-work-queues)
-   [Shutting Down Work Queues](#shutting-down-work-queues)
-   [Using Scheduled Work Items](#using-scheduled-work-items)
-   [Using Periodic Callbacks](#using-periodic-callbacks)
-   [Related topics](#related-topics)

## Using Work Queues

A work queue is an efficient way to perform asynchronous operations on another thread. Conceptually, you put work items in the queue, and the queue has a thread that pulls each item from the queue and dispatches it. Work items are implemented as callbacks by using the [**IMFAsyncCallback**](/windows/win32/mfobjects/nn-mfobjects-imfasynccallback?branch=master) interface.

Media Foundation creates several standard work queues, called *platform work queues*. Applications can also create their own work queues, called *private work queues*. For a list of the platform work queues, see [Work Queue Identifiers](work-queue-identifiers.md). To create a private work queue, call [**MFAllocateWorkQueue**](/windows/win32/mfapi/nf-mfapi-mfallocateworkqueue?branch=master). This function returns an identifier for the new work queue. To put an item in the queue, call [**MFPutWorkItem**](/windows/win32/mfapi/nf-mfapi-mfputworkitem?branch=master) or [**MFPutWorkItemEx**](/windows/win32/mfapi/nf-mfapi-mfputworkitemex?branch=master). In both cases, you must specify a callback interface.

-   [**MFPutWorkItem**](/windows/win32/mfapi/nf-mfapi-mfputworkitem?branch=master) takes a pointer to the [**IMFAsyncCallback**](/windows/win32/mfobjects/nn-mfobjects-imfasynccallback?branch=master) interface, plus an optional state object that implements **IUnknown**. These are the same parameters used in asynchronous methods, as described in the topic [Asynchronous Callback Methods](asynchronous-callback-methods.md). Internally, this function creates an asynchronous result object, which is passed to the callback's [**Invoke**](/windows/win32/mfobjects/nf-mfobjects-imfasynccallback-invoke?branch=master) method.
-   [**MFPutWorkItemEx**](/windows/win32/mfapi/nf-mfapi-mfputworkitemex?branch=master) takes a pointer to the [**IMFAsyncResult**](/windows/win32/mfobjects/nn-mfobjects-imfasyncresult?branch=master) interface. This interface represents an asynchronous result object. Create this object by calling [**MFCreateAsyncResult**](/windows/win32/mfapi/nf-mfapi-mfcreateasyncresult?branch=master) and specifying your callback interface and, optionally, a state object.

In both cases, the work queue thread calls your [**IMFAsyncCallback::Invoke**](/windows/win32/mfobjects/nf-mfobjects-imfasynccallback-invoke?branch=master) method. Use the **Invoke** method to perform the work item.

If more than one thread or component shares the same work queue, you can call [**MFLockWorkQueue**](/windows/win32/mfapi/nf-mfapi-mflockworkqueue?branch=master) to lock the work queue, which prevents the platform from releasing it. For each call to [**MFAllocateWorkQueue**](/windows/win32/mfapi/nf-mfapi-mfallocateworkqueue?branch=master) or **MFLockWorkQueue**, you must call [**MFUnlockWorkQueue**](/windows/win32/mfapi/nf-mfapi-mfunlockworkqueue?branch=master) once to release the work queue. For example, if you create a new work queue and then lock it once, you must call **MFUnlockWorkQueue** twice, once for the call to **MFAllocateWorkQueue** and once for the call to **MFLockWorkQueue**.

The following code shows how to create a new work queue, put a work item in the queue, and release the work queue.

See [Work Queue and Threading Improvements](media-foundation-work-queue-and-threading-improvements.md) for additional information on work queues in Windows 8.


```C++
DWORD idWorkQueue = 0;
HRESULT hr = S_OK;

// Create a new work queue.
hr = MFAllocateWorkQueue(&amp;idWorkQueue);

// Put an item on the queue.
if (SUCCEEDED(hr))
{
    hr = MFPutWorkItem(idWorkQueue, pCallback, NULL);
}

// Wait for the callback to be invoked.
if (SUCCEEDED(hr))
{
    WaitForSingleObject(hEvent, INFINITE);
}

// Release the work queue.
if (SUCCEEDED(hr))
{
    hr = MFUnlockWorkQueue(idWorkQueue);
}
```



This example assumes that *pCallback* is a pointer to the application's [**IMFAsyncCallback**](/windows/win32/mfobjects/nn-mfobjects-imfasynccallback?branch=master) interface. It also assumes that the callback sets the *hEvent* event handle. The code waits for this event to be set before calling [**MFUnlockWorkQueue**](/windows/win32/mfapi/nf-mfapi-mfunlockworkqueue?branch=master).

Work queue threads are always created in the caller's process. Within each work queue, the callbacks are serialized. If you call [**MFPutWorkItem**](/windows/win32/mfapi/nf-mfapi-mfputworkitem?branch=master) twice with the same work queue, the second callback is not invoked until the first callback has returned.

## Shutting Down Work Queues

Before calling [**MFShutdown**](/windows/win32/mfapi/nf-mfapi-mfshutdown?branch=master), release any resources that are being used by work queue threads. To synchronize this process, you can lock the Media Foundation platform, which prevents the **MFShutdown** function from closing any work queue threads. If **MFShutdown** is called while the platform is locked, **MFShutdown** waits a few hundred milliseconds for the platform to be unlocked. If it is not unlocked within that time, **MFShutdown** closes the work queue threads.

The default implementation of [**IMFAsyncResult**](/windows/win32/mfobjects/nn-mfobjects-imfasyncresult?branch=master) automatically locks the Media Foundation platform when the result object is created. Releasing the interface unlocks the platform. Therefore, you will almost never need to lock the platform directly. But if you write your own custom implementation of **IMFAsyncResult**, then you should manually lock and unlock the platform. To lock the platform, call [**MFLockPlatform**](/windows/win32/mfapi/nf-mfapi-mflockplatform?branch=master). To unlock the platform, call [**MFUnlockPlatform**](/windows/win32/mfapi/nf-mfapi-mfunlockplatform?branch=master). For an example, see [Custom Asynchronous Result Objects](custom-asynchronous-result-objects.md).

After you call [**MFShutdown**](/windows/win32/mfapi/nf-mfapi-mfshutdown?branch=master), you need to ensure that the platform is unlocked within the 5-second time-out period. Do this by releasing all [**IMFAsyncResult**](/windows/win32/mfobjects/nn-mfobjects-imfasyncresult?branch=master) pointers, and by calling [**MFUnlockPlatform**](/windows/win32/mfapi/nf-mfapi-mfunlockplatform?branch=master) if you locked the platform manually. Make sure to release any resources that are being used by work queue threads, or your application might leak memory.

Typically, if your application shuts down and releases every Media Foundation object before calling [**MFShutdown**](/windows/win32/mfapi/nf-mfapi-mfshutdown?branch=master), you do not have to worry about locking. The locking mechanism simply allows work queue threads to exit gracefully after you call **MFShutdown**.

## Using Scheduled Work Items

You can schedule a callback to occur after a set period of time by calling [**MFScheduleWorkItem**](/windows/win32/mfapi/nf-mfapi-mfscheduleworkitem?branch=master) or [**MFScheduleWorkItemEx**](/windows/win32/mfapi/nf-mfapi-mfscheduleworkitemex?branch=master).

-   [**MFScheduleWorkItem**](/windows/win32/mfapi/nf-mfapi-mfscheduleworkitem?branch=master) takes a pointer to your callback, an optional state object, and a time-out interval.
-   [**MFScheduleWorkItemEx**](/windows/win32/mfapi/nf-mfapi-mfscheduleworkitemex?branch=master) takes a pointer to an asynchronous result object and a time-out value.

Specify the time-out as a negative value in milliseconds. For example, to schedule a callback to be invoked in 5 seconds, use the value −5000. Both functions return an **MFWORKITEM\_KEY** value, which you can use to cancel the callback by passing it to the [**MFCancelWorkItem**](/windows/win32/mfapi/nf-mfapi-mfcancelworkitem?branch=master) function.

Scheduled work items always use the MFASYNC\_CALLBACK\_QUEUE\_TIMER platform work queue.

## Using Periodic Callbacks

The [**MFAddPeriodicCallback**](/windows/win32/mfapi/nf-mfapi-mfaddperiodiccallback?branch=master) function schedules a callback to be invoked periodically until you cancel it. The callback interval is fixed; applications cannot change it. To find out the exact interval, call [**MFGetTimerPeriodicity**](/windows/win32/mfapi/nf-mfapi-mfgettimerperiodicity?branch=master). The interval is on the order of 10 milliseconds, so this function is meant for situations where you need a frequent "tick," such as implementing a presentation clock. If you want to schedule an operation to occur less frequently, use a scheduled work item, as described previously.

Unlike the other callbacks described in this topic, the periodic callback does not use the [**IMFAsyncCallback**](/windows/win32/mfobjects/nn-mfobjects-imfasynccallback?branch=master) interface. Instead, it uses a function pointer. For more information, see [**MFPERIODICCALLBACK Callback**](mfperiodiccallback-callback.md).

To cancel the periodic callback, call [**MFRemovePeriodicCallback**](/windows/win32/mfapi/nf-mfapi-mfremoveperiodiccallback?branch=master).

Periodic callbacks use the MFASYNC\_CALLBACK\_QUEUE\_TIMER platform work queue.

## Related topics

<dl> <dt>

[Work Queues](work-queues.md)
</dt> <dt>

[**MFASYNCRESULT**](/windows/win32/mfapi/ns-mfapi-tagmfasyncresult?branch=master)
</dt> <dt>

[Work Queue and Threading Improvements](media-foundation-work-queue-and-threading-improvements.md)
</dt> </dl>

 

 



