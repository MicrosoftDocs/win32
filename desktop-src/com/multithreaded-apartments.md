---
title: Multithreaded Apartments
description: Multithreaded Apartments
ms.assetid: d3e6acd9-cd5c-4a2c-8526-4f43db3b606b
ms.topic: article
ms.date: 05/31/2018
---

# Multithreaded Apartments

In a multithreaded apartment model, all the threads in the process that have been initialized as free-threaded reside in a single apartment. Therefore, there is no need to marshal between threads. The threads need not retrieve and dispatch messages because COM does not use window messages in this model.

Calls to methods of objects in the multithreaded apartment can be run on any thread in the apartment. There is no serialization of calls; many calls may occur to the same method or to the same object simultaneously. Objects created in the multithreaded apartment must be able to handle calls on their methods from other threads at any time.

Because calls to objects are not serialized in any way, multithreaded object concurrency offers the highest performance and takes the best advantage of multiprocessor hardware for cross-thread, cross-process, and cross-machine calling. This means, however, that the code for objects must provide synchronization in their interface implementations, typically through the use of synchronization primitives such as event objects, critical sections, mutexes, or semaphores, which are described later in this section. In addition, because the object doesn't control the lifetime of the threads that are accessing it, no thread-specific state may be stored in the object (in thread local storage).

Following are some important considerations regarding synchronization for multithreaded apartments:

-   COM provides call synchronization for single-threaded apartments only.
-   Multithreaded apartments do not receive calls while making calls (on the same thread).
-   Multithreaded apartments cannot make input-synchronized calls.
-   Asynchronous calls are converted to synchronous calls in multithreaded apartments.
-   The message filter is not called for any thread in a multithreaded apartment.

To initialize a thread as free-threaded, call [**CoInitializeEx**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializeex), specifying COINIT\_MULTITHREADED. For information on in-process server threading, see [In-Process Server Threading Issues](in-process-server-threading-issues.md).

Multiple clients can simultaneously call, from different threads, an object that supports free-threading. In free-threaded out-of-process servers, COM, through the RPC subsystem, creates a pool of threads in the server process and a client call (or multiple client calls) can be delivered by any of these threads at any time. An out-of-process server must also implement synchronization in its class factory. Free-threaded, in-process objects can receive direct calls from multiple threads of the client.

The client can do COM work in multiple threads. All threads belong to the same multithreaded apartment. Interface pointers are passed directly from thread to thread within a multithreaded apartment, so interface pointers are not marshaled between its threads. Message filters (implementations of [**IMessageFilter**](/windows/desktop/api/ObjIdl/nn-objidl-imessagefilter)) are not used in multithreaded apartments. The client thread will suspend when it makes a COM call to out-of-apartment objects and will resume when the call returns. Calls between processes are still handled by RPC.

Threads initialized with the free-threaded model must implement their own synchronization. As mentioned earlier in this section, Windows enables this implementation through the following synchronization primitives:

-   Event objects provide a way of signaling one or more threads that an event has occurred. Any thread within a process can create an event object. A handle to the event is returned by the event-creating function, [**CreateEvent**](/windows/desktop/api/synchapi/nf-synchapi-createeventa). Once an event object has been created, threads with a handle to the object can wait on it before continuing execution.
-   Critical sections are used for a section of code that requires exclusive access to some set of shared data before it can be executed and that is used only by the threads within a single process. A critical section is like a turnstile through which only one thread at a time may pass, working as follows:
    -   To ensure that no more than one thread at a time accesses shared data, a process's primary thread allocates a global CRITICAL\_SECTION data structure and initializes its members. A thread entering a critical section calls the [**EnterCriticalSection**](/windows/desktop/api/synchapi/nf-synchapi-entercriticalsection) function and modifies the data structure's members.
    -   A thread attempting to enter a critical section calls [**EnterCriticalSection**](/windows/desktop/api/synchapi/nf-synchapi-entercriticalsection) which checks to see whether the CRITICAL\_SECTION data structure has been modified. If so, another thread is currently in the critical section and the subsequent thread is put to sleep. A thread leaving a critical section calls [**LeaveCriticalSection**](/windows/desktop/api/synchapi/nf-synchapi-leavecriticalsection), which resets the data structure. When a thread leaves a critical section, the system wakes one of the sleeping threads, which then enters the critical section.
-   Mutexes performs the same function as a critical section, except that the mutex is accessible to threads running in different processes. Owning a mutex object is like having the floor in a debate. A process creates a mutex object by calling the [**CreateMutex**](/windows/desktop/api/synchapi/nf-synchapi-createmutexa) function, which returns a handle. The first thread requesting a mutex object obtains ownership of it. When the thread has finished with the mutex, ownership passes to other threads on a first-come, first-served basis.
-   Semaphores are used to maintain a reference count on some available resource. A thread creates a semaphore for a resource by calling the [**CreateSemaphore**](/windows/desktop/api/winbase/nf-winbase-createsemaphorea) function and passing a pointer to the resource, an initial resource count, and the maximum resource count. This function returns a handle. A thread requesting a resource passes its semaphore handle in a call to the [**WaitForSingleObject**](/windows/desktop/api/synchapi/nf-synchapi-waitforsingleobject) function. The semaphore object polls the resource to determine whether it is available. If so, the semaphore decrements the resource count and wakes the waiting thread. If the count is zero, the thread remains asleep until another thread releases a resource, causing the semaphore to increment the count to one.

## Related topics

<dl> <dt>

[Accessing Interfaces Across Apartments](accessing-interfaces-across-apartments.md)
</dt> <dt>

[Choosing the Threading Model](choosing-the-threading-model.md)
</dt> <dt>

[In-Process Server Threading Issues](in-process-server-threading-issues.md)
</dt> <dt>

[Processes, Threads, and Apartments](processes--threads--and-apartments.md)
</dt> <dt>

[Single-Threaded and Multithreaded Communication](single-threaded-and-multithreaded-communication.md)
</dt> <dt>

[Single-Threaded Apartments](single-threaded-apartments.md)
</dt> </dl>

 

 