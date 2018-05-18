---
title: Using Transport-level Security on the Server
description: Using transport-level security on the server with Remote Procedure Call (RPC).
ms.assetid: '8ad86d46-cdc8-44f0-bb56-4d5069f33e64'
keywords: ["Remote Procedure Call RPC , tasks, using transport-level security on the server"]
---

# Using Transport-level Security on the Server

This section presents discussions of transport-level security, divided into the following topics:

-   [Using Transport-Level Security on the Client](using-transport-level-security-on-the-client.md)

When you use [ncacn\_np](https://msdn.microsoft.com/library/windows/desktop/aa367108) or [ncalrpc](https://msdn.microsoft.com/library/windows/desktop/aa367115) as the protocol sequence, the server specifies a security descriptor for the endpoint at the time it selects the protocol sequence. For more information on protocol sequences, see [Specifying Protocol Sequences](specifying-protocol-sequences.md). Your application provides the security descriptor as an additional parameter (an extension to the standard OSF-DCE parameters) on all functions that start with the prefixes [**RpcServerUseProtseq**](rpcserveruseprotseq.md) and [**RpcServerUseAllProtseqs**](rpcserveruseallprotseqs.md). The security descriptor controls whether a client can connect to the endpoint.

Each process and thread is associated with a security token. This token includes a default security descriptor that is used for any objects that the process creates, such as the endpoint. If your application does not specify a security descriptor when calling a function with the prefixes [**RpcServerUseProtseq**](rpcserveruseprotseq.md) and [**RpcServerUseAllProtseqs**](rpcserveruseallprotseqs.md), the RPC run-time library applies the default security descriptor from the process security token to the endpoint.

To guarantee that the server application is accessible to all clients, the administrator should start the server application on a process that has a default security descriptor that all clients can use. Generally, only system processes have a default security descriptor.

For more information about these functions and the functions [**RpcImpersonateClient**](rpcimpersonateclient.md) and [**RpcRevertToSelf**](rpcreverttoself.md).

 

 




