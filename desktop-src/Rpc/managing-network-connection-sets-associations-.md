---
title: Managing Network Connection Sets (Associations)
description: Starting with Windows 2000, the RPC run time may maintain more than one connection between the client and the server.
ms.assetid: 9b9c42e9-8ed5-46a6-b6ec-4093ce0128bb
keywords:
- Managing Network Connection Sets
ms.topic: article
ms.date: 05/31/2018
---

# Managing Network Connection Sets (Associations)

Starting with Windows 2000, the RPC run time may maintain more than one connection between the client and the server. This facilitates operation on transports that do not support changing the client identity without reestablishing the connection, multithreaded clients, and asynchronous clients. The set of connections between a client process and a server endpoint is called an *association* in RPC terminology. Understanding associations can improve the implementation of RPC.

In a single-thread, single-client identity scenario, RPC opens one connection between a client process and a server endpoint to make RPC calls. When a synchronous RPC call is made, the client sends the request to the server on this connection, and receives the reply on it as well. When the number of threads making RPC calls in the client process grows, the security identity of the client can change. When asynchronous/pipe calls are mixed with synchronous calls on the client, RPC may need more than one network connection. All connections in the set are put in a connection pool called an association.

A synchronous remote procedure call exclusively uses a given connection to conform with RPC standards. A connection used by a synchronous RPC call is considered busy if a request has been sent, but a response has not been received. No other traffic is allowed on that connection until the response is received. The RPC run time attempts to multiplex asynchronous and pipe RPC calls on the same connection. Synchronous and asynchronous/pipe calls cannot be mixed on the same connection, which means that a given connection can be used for either synchronous RPC calls or for asynchronous/pipe RPC calls.

RPC aggressively tries to reuse connections from the pool. When a new RPC call is made, RPC attempts to find a suitable connection from the pool, and creates a new connection only if a suitable connection cannot be found. For a connection to be considered suitable, it must:

-   Be of the appropriate type (synchronous, or asynchronous/pipe).
-   Be free.
-   Have the same security identity as the binding handle on which the call is made. If dynamic identity tracking is used, the identity of the binding handle is refreshed from the thread token at the beginning of the call. If static identity tracking is used, the client identity stamped on the binding handle is used.

When the call is complete, once the response is received, the connection is marked as free and can be used for other RPC calls.

The security identity on a connection cannot change. For example, if a large number of calls to the same server are made under different security identities, the number of connections in the thread pool grows. The association itself is reference-counted, and when all references are gone, it stops and closes all connections. Every binding handle and every context handle hold a reference on the association. When all are closed, the association disappears. On Windows XP, associations do not necessarily disappear immediately; they may remain for a short period (the target period is 20 seconds, but the RPC run time may choose to delay destroying the association if no threads are available to execute the task). If you do not want the association to stay alive after the last context handle/binding handle is closed, use the RPC\_C\_OPT\_DONT\_LINGER option to force the RPC Runtime to immediately close the connection.

 

 




