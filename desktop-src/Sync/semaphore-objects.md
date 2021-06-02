---
description: A semaphore object is a synchronization object that maintains a count between zero and a specified maximum value.
ms.assetid: d9da1d98-a306-4e2d-a149-1eef6a724751
title: Semaphore Objects
ms.topic: article
ms.date: 05/31/2018
---

# Semaphore Objects

A *semaphore object* is a synchronization object that maintains a count between zero and a specified maximum value. The count is decremented each time a thread completes a wait for the semaphore object and incremented each time a thread releases the semaphore. When the count reaches zero, no more threads can successfully wait for the semaphore object state to become signaled. The state of a semaphore is set to signaled when its count is greater than zero, and nonsignaled when its count is zero.

The semaphore object is useful in controlling a shared resource that can support a limited number of users. It acts as a gate that limits the number of threads sharing the resource to a specified maximum number. For example, an application might place a limit on the number of windows that it creates. It uses a semaphore with a maximum count equal to the window limit, decrementing the count whenever a window is created and incrementing it whenever a window is closed. The application specifies the semaphore object in call to one of the [wait functions](wait-functions.md) before each window is created. When the count is zero—indicating that the window limit has been reached—the wait function blocks execution of the window-creation code.

A thread uses the [**CreateSemaphore**](/windows/desktop/api/WinBase/nf-winbase-createsemaphorea) or [**CreateSemaphoreEx**](/windows/desktop/api/WinBase/nf-winbase-createsemaphoreexa) function to create a semaphore object. The creating thread specifies the initial count and the maximum value of the count for the object. The initial count must be neither less than zero nor greater than the maximum value. The creating thread can also specify a name for the semaphore object. Threads in other processes can open a handle to an existing semaphore object by specifying its name in a call to the [**OpenSemaphore**](/windows/win32/api/synchapi/nf-synchapi-opensemaphorew) function. For additional information about names for mutex, event, semaphore, and timer objects, see [Interprocess Synchronization](interprocess-synchronization.md).

If more than one thread is waiting on a semaphore, a waiting thread is selected. Do not assume a first-in, first-out (FIFO) order. External events such as kernel-mode APCs can change the wait order.

Each time one of the [wait functions](wait-functions.md) returns because the state of a semaphore was set to signaled, the count of the semaphore is decreased by one. The [**ReleaseSemaphore**](/windows/win32/api/synchapi/nf-synchapi-releasesemaphore) function increases a semaphore's count by a specified amount. The count can never be less than zero or greater than the maximum value.

The initial count of a semaphore is typically set to the maximum value. The count is then decremented from that level as the protected resource is consumed. Alternatively, you can create a semaphore with an initial count of zero to block access to the protected resource while the application is being initialized. After initialization, you can use [**ReleaseSemaphore**](/windows/win32/api/synchapi/nf-synchapi-releasesemaphore) to increment the count to the maximum value.

A thread that owns a mutex object can wait repeatedly for the same mutex object to become signaled without its execution becoming blocked. A thread that waits repeatedly for the same semaphore object, however, decrements the semaphore's count each time a wait operation is completed; the thread is blocked when the count gets to zero. Similarly, only the thread that owns a mutex can successfully call the [**ReleaseMutex**](/windows/win32/api/synchapi/nf-synchapi-releasemutex) function, though any thread can use [**ReleaseSemaphore**](/windows/win32/api/synchapi/nf-synchapi-releasesemaphore) to increase the count of a semaphore object.

A thread can decrement a semaphore's count more than once by repeatedly specifying the same semaphore object in calls to any of the [wait functions](wait-functions.md). However, calling one of the multiple-object wait functions with an array that contains multiple handles of the same semaphore does not result in multiple decrements.

When you have finished using the semaphore object, call the [**CloseHandle**](/windows/win32/api/handleapi/nf-handleapi-closehandle) function to close the handle. The semaphore object is destroyed when its last handle has been closed. Closing the handle does not affect the semaphore count; therefore, be sure to call [**ReleaseSemaphore**](/windows/win32/api/synchapi/nf-synchapi-releasesemaphore) before closing the handle or before the process terminates. Otherwise, pending wait operations will either time out or continue indefinitely, depending on whether a time-out value has been specified.

## Related topics

<dl> <dt>

[Using Semaphore Objects](using-semaphore-objects.md)
</dt> </dl>

 

 
