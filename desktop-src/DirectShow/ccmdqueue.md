---
description: The CCmdQueue class is a base class that provides a queue of CDeferredCommand objects and member functions to add, remove, check status, and invoke the queued commands.
ms.assetid: 6bd0f0f3-3c56-47d2-9fd8-e2863a2afa33
title: CCmdQueue class
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CCmdQueue
api_type: 
- COM
api_location: 
ms.custom: UpdateFrequency5
---

# CCmdQueue class

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `CCmdQueue` class is a base class that provides a queue of [**CDeferredCommand**](cdeferredcommand.md) objects and member functions to add, remove, check status, and invoke the queued commands. A `CCmdQueue` object is a part of an object that implements [**IQueueCommand**](/windows/desktop/api/Control/nn-control-iqueuecommand) methods. The filter graph manager implements **IQueueCommand** methods so that applications can queue commands to the filter graph. Filters that implement the **IQueueCommand** interface directly use this class. If you want to use **CDeferredCommand** objects, your queue must be derived from this class.

There are two modes of synchronization: coarse and accurate. In coarse mode, the application waits until a specified time arrives and then executes the command. In accurate mode, the application waits until processing begins on the sample that appears at the time, and then executes the command. The filter determines which one it will implement. The filter graph manager always implements coarse mode for commands that are queued at the filter graph manager.

If you want coarse synchronization, you probably want to wait until there is a command due, and then execute it. You can do this by calling [**CCmdQueue::GetDueCommand**](ccmdqueue-getduecommand.md). If you have several things to wait for, get the event handle from [**CCmdQueue::GetDueHandle**](ccmdqueue-getduehandle.md) and then call **CCmdQueue::GetDueCommand** when this is signaled. [**stream time**](stream-time.md) will advance only between calls to the [**CCmdQueue::Run**](ccmdqueue-run.md) and [**CCmdQueue::EndRun**](ccmdqueue-endrun.md) member functions. There is no guarantee that if the handle is set, there will be a command ready. Each time the event is signaled, call the **GetDueCommand** member function (probably with a time-out of zero); this can return E\_ABORT if no command is ready.

If you want accurate synchronization, call the [**CCmdQueue::GetCommandDueFor**](ccmdqueue-getcommandduefor.md) member function and pass the samples you are about to process as a parameter. This returns the following:

-   A stream-time command due at or before that stream time.
-   A presentation-time command due at or before the presentation of the stream time. Do this only between the [**CCmdQueue::Run**](ccmdqueue-run.md) and [**CCmdQueue::EndRun**](ccmdqueue-endrun.md) member functions, because outside of this, the mapping from stream time to presentation time is not known.
-   Any presentation-time command due now.

If you want accurate synchronization for samples that might be processed during paused mode, you must use stream-time commands.

In all cases, commands remain queued until called or canceled. The setting and resetting of the event handle is managed entirely by this queue object.



| Protected Data Members                                 | Description                                                                                            |
|--------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| m\_bRunning                                            | Flag for running state; set **TRUE** when running.                                                     |
| m\_dwAdvise                                            | Advise identifier from the reference clock (zero if no outstanding advise).                            |
| m\_evDue                                               | Sets the time when any commands are due.                                                               |
| m\_listPresentation                                    | Stores commands queued in presentation time.                                                           |
| m\_listStream                                          | Stores commands queued in stream time.                                                                 |
| m\_Lock                                                | Protects access to lists.                                                                              |
| m\_pClock                                              | Current reference clock.                                                                               |
| m\_StreamTimeOffset                                    | Contains the stream time offset when **m\_bRunning** is **TRUE**.                                      |
| m\_StreamTimeOffset                                    | Contains the stream time offset when **m\_bRunning** is **TRUE**.                                      |
| Member Functions                                       | Description                                                                                            |
| [**CCmdQueue**](ccmdqueue-ccmdqueue.md)               | Constructs a **CCmdQueue** object.                                                                     |
| [**CheckTime**](ccmdqueue-checktime.md)               | Determines if a given time is due.                                                                     |
| [**GetDueHandle**](ccmdqueue-getduehandle.md)         | Retrieves the event handle that will be signaled.                                                      |
| Overridable Member Functions                           | Description                                                                                            |
| [**EndRun**](ccmdqueue-endrun.md)                     | Switches to stopped or paused mode.                                                                    |
| [**GetCommandDueFor**](ccmdqueue-getcommandduefor.md) | Retrieves a deferred command that is scheduled at a specified time.                                    |
| [**GetDueCommand**](ccmdqueue-getduecommand.md)       | Retrieves a pointer to the next command that is due.                                                   |
| [**Insert**](ccmdqueue-insert.md)                     | Adds the [**CDeferredCommand**](cdeferredcommand.md) object to the queue.                             |
| [**New**](ccmdqueue-new.md)                           | Initializes a command to be run and returns a new [**CDeferredCommand**](cdeferredcommand.md) object. |
| [**Remove**](ccmdqueue-remove.md)                     | Removes the [**CDeferredCommand**](cdeferredcommand.md) object from the queue.                        |
| [**Run**](ccmdqueue-run.md)                           | Switches to running mode.                                                                              |
| [**SetSyncSource**](ccmdqueue-setsyncsource.md)       | Sets the clock used for timing.                                                                        |
| [**SetTimeAdvise**](ccmdqueue-settimeadvise.md)       | Sets up a timer event with the reference clock.                                                        |



 

 

 



