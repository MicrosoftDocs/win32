---
description: An event object is a synchronization object whose state can be explicitly set to signaled by use of the SetEvent function. Following are the two types of event object.
ms.assetid: 63dc2991-e070-4981-9e2d-90b4fdaaee7a
title: Event Objects (Synchronization)
ms.topic: article
ms.date: 05/31/2018
---

# Event Objects (Synchronization)

An *event object* is a synchronization object whose state can be explicitly set to signaled by use of the [**SetEvent**](/windows/win32/api/synchapi/nf-synchapi-resetevent) function. Following are the two types of event object.



| Object             | Description                                                                                                                                                                                                                                                                                                                                                                                                                            |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Manual-reset event | An event object whose state remains signaled until it is explicitly reset to nonsignaled by the [**ResetEvent**](/windows/win32/api/synchapi/nf-synchapi-resetevent) function. While it is signaled, any number of waiting threads, or threads that subsequently specify the same event object in one of the [wait functions](wait-functions.md), can be released.                                                                                                        |
| Auto-reset event   | An event object whose state remains signaled until a single waiting thread is released, at which time the system automatically sets the state to nonsignaled. If no threads are waiting, the event object's state remains signaled. If more than one thread is waiting, a waiting thread is selected. Do not assume a first-in, first-out (FIFO) order. External events such as kernel-mode APCs can change the wait order.<br/> |



 

The event object is useful in sending a signal to a thread indicating that a particular event has occurred. For example, in overlapped input and output, the system sets a specified event object to the signaled state when the overlapped operation has been completed. A single thread can specify different event objects in several simultaneous overlapped operations, then use one of the multiple-object [wait functions](wait-functions.md) to wait for the state of any one of the event objects to be signaled.

A thread uses the [**CreateEvent**](/windows/win32/api/synchapi/nf-synchapi-createeventa) or [**CreateEventEx**](/windows/win32/api/synchapi/nf-synchapi-createeventexa) function to create an event object. The creating thread specifies the initial state of the object and whether it is a manual-reset or auto-reset event object. The creating thread can also specify a name for the event object. Threads in other processes can open a handle to an existing event object by specifying its name in a call to the [**OpenEvent**](/windows/win32/api/synchapi/nf-synchapi-openeventa) function. For additional information about names for mutex, event, semaphore, and timer objects, see [Interprocess Synchronization](interprocess-synchronization.md).

## Related topics

<dl> <dt>

[Using Event Objects](using-event-objects.md)
</dt> </dl>

 

 
