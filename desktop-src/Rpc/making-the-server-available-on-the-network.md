---
title: Making the server available on the network
description: Before a server application can accept remote procedure calls, it must be available on the network.
ms.assetid: 1fad55e2-7221-4153-b530-b36ea42e03e1
keywords:
- Remote Procedure Call RPC, tasks, making the server available
ms.topic: concept-article
ms.date: 10/17/2023
---

# Making the server available on the network

Before a server application can accept remote procedure calls, it must be available on the network. To do this, the server indicates to the RPC runtime that it's willing to accept calls on one or more protocol sequences. Choosing the protocol sequences that a server application supports is an important decision; different protocol sequences have very different capabilities. Servers that expect calls to be received locally should use **ncalrpc**. Servers that accept remote calls should use **ncacn_ip_tcp**. Servers shouldn't verify that the protocol sequence on which they receive calls is the protocol sequence on which they expect to receive calls. For more info, see [Be wary of other RPC endpoints running in the same process](/windows/win32/rpc/be-wary-of-other-rpc-endpoints-running-in-the-same-process).

The following code example uses **ncacn_ip_tcp**.

Most server programs use all protocol sequences available on the network. To do that, they invoke the [**RpcServerUseProtseq**](/windows/win32/api/rpcdce/nf-rpcdce-rpcserveruseprotseq) function, as shown in the following code fragment:

```cpp
RPC_STATUS status;
status = RpcServerUseProtseq(
    L"ncacn_ip_tcp",
    RPC_C_PROTSEQ_MAX_REQS_DEFAULT,    // Protseq-dependent parameter
    NULL);                             // Always specify NULL here.
```

The first parameter to the [**RpcServerUseProtseq**](/windows/win32/api/rpcdce/nf-rpcdce-rpcserveruseprotseq) function is the protocol sequence. The second parameter is dependent on the protocol sequence. As illustrated in the code example, most server programs set that parameter to **RPC_C_PROTSEQ_MAX_REQS_DEFAULT**. That value sets the RPC library to use the default value. The third parameter is a security descriptor, and shouldn't be used in apps. For more info, see [**Security (RPC)**](./security.md).

You can also call the [**RpcServerUseAllProtseqs**](/windows/win32/api/rpcdce/nf-rpcdce-rpcserveruseallprotseqs), [**RpcServerUseProtseqEx**](/windows/win32/api/rpcdce/nf-rpcdce-rpcserveruseprotseqex), [**RpcServerUseProtseqEp**](/windows/win32/api/rpcdce/nf-rpcdce-rpcserveruseprotseqep), or [**RpcServerUseProtseqEpEx**](/windows/win32/api/rpcdce/nf-rpcdce-rpcserveruseprotseqepex) functions.

After a server application selects at least one protocol sequence, servers that use dynamic endpoints must create binding information for each protocol sequence it uses. The server stores the binding information in a binding vector that it can then export to the endpoint mapper service.

Use the [**RpcServerInqBindings**](/windows/win32/api/rpcdce/nf-rpcdce-rpcserverinqbindings) function to obtain a binding vector for the server application, as shown in the following example:

```cpp
RPC_STATUS status;
RPC_BINDING_VECTOR *rpcBindingVector;
 
status = RpcServerInqBindings(&rpcBindingVector);
```

The only parameter passed to the [**RpcServerInqBindings**](/windows/win32/api/rpcdce/nf-rpcdce-rpcserverinqbindings) function is a pointer to a pointer to an [**RPC_BINDING_VECTOR**](/windows/win32/api/rpcdce/ns-rpcdce-rpc_binding_vector) structure. The RPC run-time library dynamically allocates an array of binding vectors, and stores the address of the array in that parameter variable (in this case, **rpcBindingVector**). Once the server app has finished using that binding vector (for example, after it has passed it to the appropriate functions), the server app is responsible for freeing that binding vector by using the [**RpcBindingVectorFree**](/windows/win32/api/rpcdce/nf-rpcdce-rpcbindingvectorfree) function.
