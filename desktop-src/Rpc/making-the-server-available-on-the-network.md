---
title: Making the Server Available on the Network
description: Before a server application can accept remote procedure calls, it must be available on the network.
ms.assetid: 1fad55e2-7221-4153-b530-b36ea42e03e1
keywords:
- Remote Procedure Call RPC , tasks, making the server available
ms.topic: article
ms.date: 05/31/2018
---

# Making the Server Available on the Network

Before a server application can accept remote procedure calls, it must be available on the network. To do this, the server indicates to the RPC Run time that it is willing to accept calls on one or more protocol sequences. Choosing the protocol sequences a server application supports is an important decision; different protocol sequences have very different capabilities. Servers that expect calls to be received locally should use **ncalrpc**. Servers that accept remote calls should use **ncacn\_ip\_tcp**. Servers should not verify that the protocol sequence on which they receive calls is the protocol sequence on which they expect to receive calls. See Be Wary of Other RPC Endpoints Running in the Same Process in Best RPC Programming Practices for more information.

The following example uses **ncacn\_ip\_tcp**.

Most server programs use all protocol sequences available on the network. To do this, they invoke the [**RpcServerUseProtseq**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserveruseprotseq) function, as shown in the following code fragment:


```C++
RPC_STATUS status;
status = RpcServerUseAllProtseq(
    L"ncacn_ip_tcp",
    RPC_C_PROTSEQ_MAX_REQS_DEFAULT,    // Protseq dependent parameter
    NULL);                             // Always specify NULL here.
```



The first parameter to the [**RpcServerUseProtseq**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserveruseprotseq) function is the protocol sequence. The second parameter is dependent on the protocol sequence. As illustrated in the code fragment, most server programs set this parameter to **RPC\_C\_PROTSEQ\_MAX\_REQS\_DEFAULT**. This value sets the RPC library to use the default value. The third parameter is a security descriptor and should not be used in applications. For more information, see [**Security**](security.md).

You can also use the [**RpcServerUseAllProtseqs**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserveruseallprotseqs), [**RpcServerUseProtseqEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserveruseprotseqex), [**RpcServerUseProtseqEp**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserveruseprotseqep), or [**RpcServerUseProtseqEpEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserveruseprotseqepex) functions.

After a server application selects at least one protocol sequence, servers that use dynamic endpoints must create binding information for each protocol sequence it uses. The server stores the binding information in a binding vector that it can then export to the endpoint mapper service.

Use the [**RpcServerInqBindings**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverinqbindings) function to obtain a binding vector for the server application, as shown in the following example:


```C++
RPC_STATUS status;
RPC_BINDING_VECTOR *rpcBindingVector;
 
status = RpcServerInqBindings(&rpcBindingVector);
```



The only parameter passed to the [**RpcServerInqBindings**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverinqbindings) function is a pointer to a pointer to an [**RPC\_BINDING\_VECTOR**](/windows/desktop/api/Rpcdce/ns-rpcdce-rpc_binding_vector) structure. The RPC run-time library dynamically allocates an array of binding vectors and stores the address of the array in the parameter variable (in this case, **rpcBindingVector**). Each server application is responsible for freeing this binding vector using the [**RpcBindingVectorFree**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingvectorfree) function once it has finished using it (for example, after it has passed it to the appropriate functions).

 

 




