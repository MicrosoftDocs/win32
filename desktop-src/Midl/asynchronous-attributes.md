---
title: Asynchronous Attributes
description: When a program invokes a procedure in an interface, the procedure may execute synchronously or asynchronously.
ms.assetid: 3e6c6c13-1524-41b2-96dc-3885eadb847c
keywords:
- IDL MIDL , attributes MIDL , asynchronous
ms.topic: article
ms.date: 05/31/2018
---

# Asynchronous Attributes

When a program invokes a procedure in an interface, the procedure may execute synchronously or asynchronously. A synchronous procedure causes the calling program to wait until the procedure returns before the program can proceed. An asynchronous procedure returns immediately without waiting for results. The calling program must later resynchronize with the interface procedure to receive data. For more information, see [Asynchronous RPC](/windows/desktop/Rpc/asynchronous-rpc).

You can use the following attributes to provide support for asynchronous remote procedure calls.



| Attribute                         | Usage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**async**](async.md)            | When applied to a function parameter, defines a handle that allows the caller to make an asynchronous call and return immediately without waiting for results, and later resynchronize with the called function to receive data after the call completes. The [**async**](async.md) attribute is also used in ACF files to define an asynchronous handle for a procedure or an entire interface. For COM interfaces, this interface is obsolete and cannot be used for new interfaces. |
| [**async\_uuid**](async-uuid.md) | Directs the MIDL compiler to define both synchronous and asynchronous versions of a COM interface.                                                                                                                                                                                                                                                                                                                                                                                      |
| [**maybe**](maybe.md)            | The client making this remote procedure call does not expect any response indicating delivery or completion of the call, and delivery is not guaranteed. This is in contrast to **message** operations where no response is expected but the delivery is guaranteed.                                                                                                                                                                                                                    |
| [**message**](message.md)        | The remote procedure call is to be treated as an asynchronous message from the client to the server. The client makes the call and returns immediately, while the actual call is handled by the message-queuing transport ([**ncadg\_mq**](ncadg-mq.md)).                                                                                                                                                                                                                              |



 

 

 