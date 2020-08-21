---
title: Using MSMQ as an RPC Transport
description: The RPC subsystem supports using MSMQ as a transport in synchronous and asynchronous modes.
ms.assetid: c3f96a91-b7bb-4c2a-8699-2100324af165
ms.topic: article
ms.date: 05/31/2018
---

# Using MSMQ as an RPC Transport

The RPC subsystem supports using MSMQ as a transport in synchronous and asynchronous modes.

Synchronous mode uses conventional remote procedure calls. These calls use well-known endpoints and the message queue transport, [ncadg\_mq](/windows/desktop/Midl/ncadg-mq), as the transport protocol. In synchronous mode, your remote procedures can have \[ [in](/windows/desktop/Midl/in)\] and \[ [out](/windows/desktop/Midl/out-idl)\] parameters and can use the standard RPC security services. The RPC subsystem creates a reply queue for remote calls containing **\[out\]** parameters. The synchronous mode is useful for applications where the client needs to receive data from the server. The main limitation of this mode is that, as with conventional remote procedure calls, both the client and server must be running and remain running for the duration of the call.

Asynchronous mode lets client applications make calls to the server and return immediately, regardless of the state of the server application or the server computer. It also makes a subset of MSMQ features available for managing message queues and information flow. The [**RpcBindingSetOption**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingsetoption) function lets you control quality of service, call priority, journaling, security, and the lifetime of the server process queue. The [**RpcServerUseProtseqEpEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserveruseprotseqepex) function lets you specify attributes of the server process queue, such as queue persistence, authentication, and encryption.

You implement asynchronous MSMQ as you would synchronous MSMQ. You must use well-known endpoints, and define the transport protocol to be [ncadg\_mq](/windows/desktop/Midl/ncadg-mq). In your IDL file, apply the [message](/windows/desktop/Midl/message) attribute to the functions that use asynchronous message queuing. Note that message functions can have \[in\] parameters only.

 

 