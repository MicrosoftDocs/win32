---
description: The CMsgThread class is a worker-thread class that queues requests to the queuing thread for completion asynchronously.
ms.assetid: 57e50abf-c90d-4c8f-afd8-25f29b6a0376
title: CMsgThread class
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMsgThread
api_type: 
- COM
api_location: 
ms.custom: UpdateFrequency5
---

# CMsgThread class

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `CMsgThread` class is a worker-thread class that queues requests to the queuing thread for completion asynchronously. To use this class, derive your class from it and override the [**CMsgThread::ThreadMessageProc**](cmsgthread-threadmessageproc.md) member function. The **ThreadMessageProc** member function carries out each request. Your client functions and the **ThreadMessageProc** member function must share a common definition of the parameters in the [**CMsg**](cmsg.md) object.

A negotiated mechanism tells the worker thread to exit. Typically, this will be one value of the [**CMsg**](cmsg.md) class's **uMsg** message code.

It is a good idea to send this message from the destructor of your derived class, and call the [**CMsgThread::WaitForThreadExit**](cmsgthread-waitforthreadexit.md) member function before completing the destruction of the derived class.



| Protected Data Members                                    | Description                                                                                                                           |
|-----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| m\_hSem                                                   | Indicates a handle used for signaling.                                                                                                |
| m\_Lock                                                   | Protects access to lists.                                                                                                             |
| m\_lWaiting                                               | Indicates waiting for a free thread.                                                                                                  |
| m\_ThreadQueue                                            | Overrides the [**CMsgThread::GetThreadMsg**](cmsgthread-getthreadmsg.md) member function and blocks on things other than this queue. |
| Member Functions                                          | Description                                                                                                                           |
| [**CMsgThread**](cmsgthread-cmsgthread.md)               | Constructs a **CMsgThread** object.                                                                                                   |
| [**CreateThread**](cmsgthread-createthread.md)           | Creates a thread.                                                                                                                     |
| [**GetThreadHandle**](cmsgthread-getthreadhandle.md)     | Retrieves the thread handle.                                                                                                          |
| [**GetThreadID**](cmsgthread-getthreadid.md)             | Retrieves the identifier of the thread.                                                                                               |
| [**GetThreadPriority**](cmsgthread-getthreadpriority.md) | Retrieves the current thread priority.                                                                                                |
| [**PutThreadMsg**](cmsgthread-putthreadmsg.md)           | Queues a request for execution by the worker thread.                                                                                  |
| [**ResumeThread**](cmsgthread-resumethread.md)           | Continues the operation of the worker thread.                                                                                         |
| [**SetThreadPriority**](cmsgthread-setthreadpriority.md) | Sets the priority of the thread to a new value.                                                                                       |
| [**SuspendThread**](cmsgthread-suspendthread.md)         | Suspends the operation of a running thread.                                                                                           |
| [**WaitForThreadExit**](cmsgthread-waitforthreadexit.md) | Blocks until the thread has exited after a call to the [**CMsgThread::SuspendThread**](cmsgthread-suspendthread.md) member function. |
| Overridable Member Functions                              | Description                                                                                                                           |
| [**GetThreadMsg**](cmsgthread-getthreadmsg.md)           | Retrieves a queued [**CMsg**](cmsg.md) object containing a request.                                                                  |
| [**OnThreadInit**](cmsgthread-onthreadinit.md)           | Provides initialization on a thread.                                                                                                  |
| [**ThreadMessageProc**](cmsgthread-threadmessageproc.md) | Processes requests. This is a pure virtual member function.                                                                           |



 

 

 



