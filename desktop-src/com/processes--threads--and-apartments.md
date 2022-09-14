---
title: Processes, Threads, and Apartments
description: A process is a collection of virtual memory space, code, data, and system resources.
ms.assetid: cb62412a-d079-40f9-89dc-cce0bf3889af
ms.topic: article
ms.date: 05/31/2018
---

# Processes, Threads, and Apartments

A *process* is a collection of virtual memory space, code, data, and system resources. A *thread* is code that is to be serially executed within a process. A processor executes threads, not processes, so each application has at least one process, and a process always has at least one thread of execution, known as the primary thread. A process can have multiple threads in addition to the primary thread.

Processes communicate with one another through messages, using Microsoft's Remote Procedure Call (RPC) technology to pass information to one another. There is no difference to the caller between a call coming from a process on a remote machine and a call coming from another process on the same machine.

When a thread begins to execute, it continues until it is killed or until it is interrupted by a thread with higher priority (by a user action or the kernel's thread scheduler). Each thread can run separate sections of code, or multiple threads can execute the same section of code. Threads executing the same block of code maintain separate stacks. Each thread in a process shares that process's global variables and resources.

The thread scheduler determines when and how often to execute a thread, according to a combination of the process's priority class attribute and the thread's base priority. You set a process's priority class attribute by calling the [**SetPriorityClass**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-setpriorityclass) function , and you set a thread's base priority with a call to [**SetThreadPriority**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-setthreadpriority).

Multithreaded applications must avoid two threading problems: *deadlocks* and *races*. A deadlock occurs when each thread is waiting for the other to do something. The COM call control helps prevent deadlocks in calls between objects. A race condition occurs when one thread finishes before another on which it depends, causing the former to use an uninitialized value because the latter has not yet supplied a valid one. COM supplies some functions specifically designed to help avoid race conditions in out-of-process servers. (See [Out-of-Process Server Implementation Helpers](out-of-process-server-implementation-helpers.md).)

## The Apartment and the COM Threading Architecture

While COM supports the single-thread-per-process model prevalent before the introduction of multiple threads of execution, you can write code to take advantage of multiple threads, resulting in more efficient applications, by allowing one thread to be executed while another thread waits for some time-consuming operation to complete.

> [!Note]  
> Using multiple threads is not a guarantee of better performance. In fact, because thread factoring is a difficult problem, using multiple threads often causes performance problems. The key is to use multiple threads only if you are very sure of what you are doing.

 

In general, the simplest way to view the COM threading architecture is to think of all the COM objects in the process as divided into groups called *apartments*. A COM object lives in exactly one apartment, in the sense that its methods can legally be directly called only by a thread that belongs to that apartment. Any other thread that wants to call the object must go through a proxy.

There are two types of apartments: [single-threaded apartments](single-threaded-apartments.md), and [multithreaded apartments](multithreaded-apartments.md).

-   Single-threaded apartments consist of exactly one thread, so all COM objects that live in a single-threaded apartment can receive method calls only from the one thread that belongs to that apartment. All method calls to a COM object in a single-threaded apartment are synchronized with the windows message queue for the single-threaded apartment's thread. A process with a single thread of execution is simply a special case of this model.
-   Multithreaded apartments consist of one or more threads, so all COM objects that live in an multithreaded apartment can receive method calls directly from any of the threads that belong to the multithreaded apartment. Threads in a multithreaded apartment use a model called *free-threading*. Calls to COM objects in a multithreaded apartment are synchronized by the objects themselves.

> [!Note]  
> For a description of communication between single-threaded apartments and multithreaded apartments within the same process, see [Single-Threaded and Multithreaded Communication](single-threaded-and-multithreaded-communication.md).

 

A process can have zero or more single-threaded apartments and zero or one multithreaded apartment.

In a process, the main apartment is the first to be initialized. In a single-threaded process, this is the only apartment. Call parameters are marshaled between apartments, and COM handles the synchronization through messaging. If you designate multiple threads in a process to be free-threaded, all free threads reside in a single apartment, parameters are passed directly to any thread in the apartment, and you must handle all synchronization. In a process with both free-threading and apartment threading, all free threads reside in a single apartment and all other apartments are single-threaded apartments. A process that does COM work is a collection of apartments with, at most, one multithreaded apartment but any number of single-threaded apartments.

The threading models in COM provide the mechanism for clients and servers that use different threading architectures to work together. Calls among objects with different threading models in different processes are naturally supported. From the perspective of the calling object, all calls to objects outside a process behave identically, no matter how the object being called is threaded. Likewise, from the perspective of the object being called, arriving calls behave identically, regardless of the threading model of the caller.

Interaction between a client and an out-of-process object is straightforward, even when they use different threading models because the client and object are in different processes. COM, interposed between the client and the server, can provide the code for the threading models to interoperate, using standard marshaling and RPC. For example, if a single-threaded object is called simultaneously by multiple free-threaded clients, the calls will be synchronized by COM by placing corresponding window messages in the server's message queue. The object's apartment will receive one call each time it retrieves and dispatches messages. However, some care must be taken to ensure that in-process servers interact properly with their clients. (See [In-Process Server Threading Issues](in-process-server-threading-issues.md).)

The most important issue in programming with a multithreaded model is to make your code thread-safe so that messages intended for a particular thread go only to that thread and access to threads is protected.

For more information, see the following topics:

-   [Choosing the Threading Model](choosing-the-threading-model.md)
-   [Single-Threaded Apartments](single-threaded-apartments.md)
-   [Multithreaded Apartments](multithreaded-apartments.md)
-   [Single-Threaded and Multithreaded Communication](single-threaded-and-multithreaded-communication.md)
-   [In-Process Server Threading Issues](in-process-server-threading-issues.md)
-   [Accessing Interfaces Across Apartments](accessing-interfaces-across-apartments.md)

 

 