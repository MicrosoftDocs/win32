---
title: Using Events with Asynchronous Calls
description: Using Events with Asynchronous Calls
ms.assetid: 98c24176-a632-400e-b23b-5e13f1bd9a27
keywords:
- Windows Media Format SDK,events with asynchronous calls
- Windows Media Format SDK,asynchronous call events
- events,asynchronous calls
- asynchronous call events
ms.topic: article
ms.date: 05/31/2018
---

# Using Events with Asynchronous Calls

Frequently, when using methods that are called asynchronously, you will want to halt further processing of your application until after the method completes processing. You can implement any technique you like to handle this situation. This section describes using an event to wait for asynchronous calls in the calling thread. This technique is frequently used with the Windows Media Format SDK, and is demonstrated in some of the sample applications.

The following list summarizes the use of events to wait for asynchronous calls.

1.  Create an event for use with your application by calling the **CreateEvent** function of the Platform SDK.
2.  When implementing the appropriate callbacks for your application, trap the messages for which you need to wait. In the message handling logic for the desired messages, signal the event by calling the **SetEvent** function of the Platform SDK.
3.  After calls to asynchronous events are made in your application, wait for the event to signal by calling the **WaitForSingleObject** function of the Platform SDK. If you are designing a Windows application, you should create a loop to check for Windows messages and include a call to **WaitForSingleObject** in the loop with a short wait time.

## Related topics

<dl> <dt>

[**Using the Callback Methods**](using-the-callback-methods.md)
</dt> </dl>

 

 




