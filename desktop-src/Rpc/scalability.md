---
title: Scalability
description: Scalability
ms.assetid: 39327621-b536-4494-9319-9e9d4f534123
keywords:
- Scalability
- Remote Procedure Call RPC , best practices, scalability
ms.topic: article
ms.date: 05/31/2018
---

# Scalability

The term, scalability, is often misused. For this section, a dual definition is provided:

-   Scalability is the ability to fully utilize available processing power on a multiprocessor system (2, 4, 8, 32, or more processors).
-   Scalability is the ability to service a large number of clients.

These two related definitions are commonly referred to as *scaling up*. The end of this topic provides tips about *scaling out*.

This discussion focuses exclusively on writing scalable servers, not scalable clients, because scalable servers are more common requirements. This section also addresses scalability in the context of RPC and RPC servers only. Best practices for scalability, such as reducing contention, avoiding frequent cache misses on global memory locations, or avoiding false sharing, are not discussed here.

## RPC Threading Model

When an RPC call is received by a server, the server routine (manager routine) is called on a thread supplied by RPC. RPC uses an adaptive thread pool that increases and decreases as workload fluctuates. Starting with Windows 2000, the core of the RPC thread pool is a completion port. The completion port and its usage by RPC are tuned for zero to low contention server routines. This means that the RPC thread pool aggressively increases the number of servicing threads if some become blocked. It operates on the presumption that blocking is rare, and if a thread gets blocked, this is a temporary condition that is quickly resolved. This approach enables efficiency for low contention servers. For example, a void call RPC server operating on an eight-processor 550MHz server accessed over a high speed system area network (SAN) serves over 30,000 void calls per second from over 200 remote clients. This represents more than 108 million calls per hour.

The result is that the aggressive thread pool actually gets in the way when contention on the server is high. To illustrate, imagine a heavy-duty server used to remotely access files. Assume the server adopts the most straightforward approach: it simply reads/writes the file synchronously on the thread on which that RPC invokes the server routine. Also, assume we have a four-processor server serving many clients.

The server will start with five threads (this actually varies, but five threads is used for simplicity). Once RPC picks up the first RPC call, it dispatches the call to the server routine, and the server routine issues the I/O. Infrequently, it misses the file cache and then blocks waiting for the result. As soon as it blocks, the fifth thread is released to pick up a request, and a sixth thread is created as a hot standby. Assuming each tenth I/O operation misses the cache and will block for 100 milliseconds (an arbitrary time value), and assuming the four-processor server serves about 20,000 calls per second (5,000 calls per processor), a simplistic modeling would predict that each processor will spawn approximately 50 threads. This assumes a call that will block comes every 2 milliseconds, and after 100 milliseconds the first thread is freed again so the pool will stabilize at about 200 threads (50 per processor).

The actual behavior is more complicated, as the high number of threads will cause extra context switches which slow the server, and also slow the rate of creation of new threads, but the basic idea is clear. The number of threads goes up quickly as threads on the server start blocking and waiting for something (be it an I/O, or access to a resource).

RPC and the completion port that gates incoming requests will try to maintain the number of usable RPC threads in the server to be equal to the number of processors on the machine. This means that on a four-processor server, once a thread returns to RPC, if there are four or more usable RPC threads, the fifth thread is not allowed to pick up a new request, and instead will sit in a hot standby state in case one of the currently usable threads blocks. If the fifth thread waits long enough as a hot standby without the number of usable RPC threads dropping below the number of processors, it will be released, that is, the thread pool will decrease.

Imagine a server with many threads. As previously explained, an RPC server ends up with many threads, but only if the threads block often. On a server where threads often block, a thread that returns to RPC is soon taken out of the hot standby list, because all currently usable threads block, and is given a request to process. When a thread blocks, the thread dispatcher in the kernel switches context to another thread. This context switch by itself consumes CPU cycles. The next thread will be executing different code, accessing different data structures, and will have a different stack, which means the memory cache hit rate (the L1 and L2 caches) will be much lower, resulting in slower execution. The numerous threads executing simultaneously increases contention for existing resources, such as heap, critical sections in the server code, and so on. This further increases contention as convoys on resources form. If memory is low, the memory pressure exerted by the large and growing number of threads will cause page faults, which further increase the rate at which the threads block, and cause even more threads to be created. Depending on how often it blocks and how much physical memory is available, the server may either stabilize at some lower level of performance with a high context switch rate, or it may deteriorate to the point where it is only repeatedly accessing the hard disk and context switching without performing any actual work. This situation will not show under light workload, of course, but a heavy workload quickly brings the problem to the surface.

How can this be prevented? If threads are expected to block, declare calls as asynchronous, and once the request enters the server routine, queue it to a pool of worker threads that use the asynchronous capabilities of the I/O system and/or RPC. If the server is in turn making RPC calls make those asynchronous, and make sure the queue does not grow too large. If the server routine is performing file I/O, use asynchronous file I/O to queue multiple requests to the I/O system and have only a few threads queue them and pick up the results. If the server routine is doing network I/O, again, use the asynchronous capabilities of the system to issue the requests and pick up the replies asynchronously, and use as few threads as possible. When the I/O is done, or the RPC call the server made is complete, complete the asynchronous RPC call that delivered the request. This will enable the server to run with as few threads as possible, which increases the performance and the number of clients a server can service.

## Scale Out

RPC can be configured to work with Network Load Balancing (NLB) if NLB is configured such that all requests from a given client address go to the same server. Because each RPC client opens a connection pool (for more information, see [RPC and the Network](rpc-and-the-network.md)), it is essential that all connections from the pool of the given client end up on the same server computer. As long as this condition is met, an NLB cluster can be configured to function as one large RPC server with potentially excellent scalability.

 

 




