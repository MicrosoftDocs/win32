---
title: Developing RPC-Message Queuing Applications
description: Very little effort is necessary to take advantage of the MSMQ transport in your RPC application.
ms.assetid: 1ea97df8-cdf5-43b8-88aa-9e8fa6ae845a
keywords:
- Remote Procedure Call RPC , tasks, developing message queuing applications
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Developing RPC-Message Queuing Applications

Very little effort is necessary to take advantage of the MSMQ transport in your RPC application. For synchronous messaging you need only specify the message queue transport ([**ncadg\_mq**](https://msdn.microsoft.com/library/windows/desktop/aa367114)) as the protocol sequence. The **ncadg\_mq** protocol supports all of the standard datagram features except broadcasting calls. Also, note that currently the message-queue transport does not support dynamic endpoints.

By applying the \[[**message**](https://msdn.microsoft.com/library/windows/desktop/aa367077)\] attribute to remote procedure declarations in the IDL file, you automatically implement asynchronous-mode message queuing for those calls. This makes it possible for the client and server applications to control many of the properties associated with messages and message queues, including:

-   Quality of service
-   Acknowledgment of receipt
-   Journaling
-   Call priority
-   Persistence of Server Process Queue

Quality of service is the effort that the transport will make to deliver the call to the server process. An express delivery will be queued in memory, so it is fairly fast, but the call will be lost if a computer or network connection goes down at the wrong time. A recoverable delivery will be posted to a disk file until it is delivered, so the call will not be lost, even in the face of a computer crash. This gives guaranteed delivery, but at a cost in performance as each call is written to disk.

You can also tell the MSMQ transport to wait for acknowledgment that the call reached the destination (server) queue before returning. Choosing this option blocks the client until the server acknowledges the call, otherwise control returns to the client immediately upon making the call.

By using journaling, calls can be logged to disk. If journaling is turned on, each call is logged to disk as it is transmitted to the next hop on its way to the server process.

Call priority can be used in conjunction with the RPC \[[**message**](https://msdn.microsoft.com/library/windows/desktop/aa367077)\] function attribute to allow calls with higher priority to take precedence over calls with lower priority, even if the high priority calls arrive later. Call priority will also work in a limited fashion with synchronous RPC, but synchronous RPC calls cannot stack up in the same manner as asynchronous calls.

The client process controls all of the above properties by calling [**RpcBindingSetOption**](/windows/win32/Rpcdce/nf-rpcdce-rpcbindingsetoption?branch=master). Once set, these properties remain in effect until they are changed in another call to **RpcBindingSetOption**.

The RPC server process can control the lifetime of its receive queue. By default the queue is deleted when the server process exits. However, the server process can use [**RpcServerUseProtseqEpEx**](/windows/win32/Rpcdce/nf-rpcdce-rpcserveruseprotseqepex?branch=master) when setting up its endpoint to tell the transport to allow the queue to continue to exist and to accept call requests even when the server process is not running. In this case, the calls are queued up and executed later, when the server process comes back online.

> [!Note]  
> If you are using asynchronous \[[**message**](https://msdn.microsoft.com/library/windows/desktop/aa367077)\] calls in an interface, you must register the interface by calling [**RpcServerRegisterIf**](/windows/win32/Rpcdce/nf-rpcdce-rpcserverregisterif?branch=master) or [**RpcServerRegisterIfEx**](/windows/win32/Rpcdce/nf-rpcdce-rpcserverregisterifex?branch=master) before calling [**RpcServerUseProtseqEpEx**](/windows/win32/Rpcdce/nf-rpcdce-rpcserveruseprotseqepex?branch=master)**(ncadg\_mq)**. Once you turn on the protocol sequence, any calls already waiting on the queue for the server will begin to be read off the queue. If the corresponding RPC interface has not been registered, the calls will fail. This situation can happen if you have a setup a permanent endpoint for your remote procedure calls, the server has been shut down, and clients have continued to send calls to the server. These calls will be stacked up in the queue, waiting to be read once the server comes back online.

 

For more information, see [**RpcBindingSetOption**](/windows/win32/Rpcdce/nf-rpcdce-rpcbindingsetoption?branch=master), [**RpcServerUseProtseqEpEx**](/windows/win32/Rpcdce/nf-rpcdce-rpcserveruseprotseqepex?branch=master), and \[[**message**](https://msdn.microsoft.com/library/windows/desktop/aa367077)\], [**ncadg\_mq**](https://msdn.microsoft.com/library/windows/desktop/aa367114).

 

 




