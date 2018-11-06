---
title: Registering the Interface
description: Registering the interface that a server program supports enables remote procedure calls from client programs to be dispatched to the proper server routine.
ms.assetid: 953185a7-00e6-442d-b474-a983f4a91c38
keywords:
- Remote Procedure Call RPC , tasks, registering the interface
ms.topic: article
ms.date: 05/31/2018
---

# Registering the Interface

Registering the interface that a server program supports enables remote procedure calls from client programs to be dispatched to the proper server routine. Server programs call [**RpcServerRegisterIf**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif) to register their interfaces. The following code fragment demonstrates its use:


```C++
RPC_STATUS status;
status = RpcServerRegisterIf(MyInterface_v1_0_s_ifspec, NULL, NULL);
```



The first parameter to the [**RpcServerRegisterIf**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif) function is a structure the MIDL compiler generates from the IDL file that defines the interface (or interfaces) for the server. The second and third parameters are a UUID and an entry-point vector, respectively. They are set to **NULL** in this example. In many instances, your server program will set these parameter values to **NULL**. Server programs use the second and third parameters when they provide multiple implementations of the same procedures in an interface. For more information, see [Entry-Point Vectors](registering-interfaces.md).

Server programs can also use [**RpcServerRegisterIfEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterifex) to register an interface. One advantage of using this function is that it provides your application with the ability to set a security-callback function. Using security-callback functions is the recommended approach to securing an interface.

> [!Note]  
> MIDL produces two very similar structures, one for the client and one for the server. The structure passed to the [**RpcServerRegisterIf**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif) function is the server version of the MIDL-produced structure.

 

 

 




