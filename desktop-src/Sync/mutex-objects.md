---
description: A mutex object is a synchronization object whose state is set to signaled when it is not owned by any thread, and nonsignaled when it is owned.
ms.assetid: eca0795a-1fd0-4034-9d61-9416670919cf
title: Mutex Objects
ms.topic: article
ms.date: 05/31/2018
---

# Mutex Objects

A *mutex object* is a synchronization object whose state is set to signaled when it is not owned by any thread, and nonsignaled when it is owned. Only one thread at a time can own a mutex object, whose name comes from the fact that it is useful in coordinating mutually exclusive access to a shared resource. For example, to prevent two threads from writing to shared memory at the same time, each thread waits for ownership of a mutex object before executing the code that accesses the memory. After writing to the shared memory, the thread releases the mutex object.

A thread uses the [**CreateMutex**](/windows/win32/api/synchapi/nf-synchapi-createmutexa) or [**CreateMutexEx**](/windows/win32/api/synchapi/nf-synchapi-createmutexexa) function to create a mutex object. The creating thread can request immediate ownership of the mutex object and can also specify a name for the mutex object. It can also create an unnamed mutex. For additional information about names for mutex, event, semaphore, and timer objects, see [Interprocess Synchronization](interprocess-synchronization.md).

Threads in other processes can open a handle to an existing named mutex object by specifying its name in a call to the [**OpenMutex**](/windows/win32/api/synchapi/nf-synchapi-openmutexw) function. To pass a handle to an unnamed mutex to another process, use the [**DuplicateHandle**](/windows/win32/api/handleapi/nf-handleapi-duplicatehandle) function or parent-child handle inheritance.

Any thread with a handle to a mutex object can use one of the [wait functions](wait-functions.md) to request ownership of the mutex object. If the mutex object is owned by another thread, the wait function blocks the requesting thread until the owning thread releases the mutex object using the [**ReleaseMutex**](/windows/win32/api/synchapi/nf-synchapi-releasemutex) function. The return value of the wait function indicates whether the function returned for some reason other than the state of the mutex being set to signaled.

If more than one thread is waiting on a mutex, a waiting thread is selected. Do not assume a first-in, first-out (FIFO) order. External events such as kernel-mode APCs can change the wait order.

After a thread obtains ownership of a mutex, it can specify the same mutex in repeated calls to the [wait-functions](wait-functions.md) without blocking its execution. This prevents a thread from deadlocking itself while waiting for a mutex that it already owns. To release its ownership under such circumstances, the thread must call [**ReleaseMutex**](/windows/win32/api/synchapi/nf-synchapi-releasemutex) once for each time that the mutex satisfied the conditions of a wait function.

If a thread terminates without releasing its ownership of a mutex object, the mutex object is considered to be abandoned. A waiting thread can acquire ownership of an abandoned mutex object, but the wait function will return **WAIT\_ABANDONED** to indicate that the mutex object is abandoned. An abandoned mutex object indicates that an error has occurred and that any shared resource being protected by the mutex object is in an undefined state. If the thread proceeds as though the mutex object had not been abandoned, it is no longer considered abandoned after the thread releases its ownership. This restores normal behavior if a handle to the mutex object is subsequently specified in a wait function.

Note that [critical section objects](critical-section-objects.md) provide synchronization similar to that provided by mutex objects, except that critical section objects can be used only by the threads of a single process.

## Related topics

<dl> <dt>

[Using Mutex Objects](using-mutex-objects.md)
</dt> </dl>

 

 
