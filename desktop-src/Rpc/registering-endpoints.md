---
title: Registering Endpoints
description: Registering the server program in the endpoint map of the server host computer enables client programs to determine which endpoint (usually a TCP/IP port or a named pipe) the server program is listening to.
ms.assetid: d09874f8-2b55-4af2-bfe1-8978301d6692
keywords:
- Remote Procedure Call RPC , tasks, registering endpoints
ms.topic: article
ms.date: 05/31/2018
---

# Registering Endpoints

Registering the server program in the endpoint map of the server host computer enables client programs to determine which endpoint (usually a TCP/IP port or a named pipe) the server program is listening to. To register itself in the server host system's endpoint map, a server program calls the [**RpcEpRegister**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcepregister) function as shown in the following code fragment:


```C++
// This example assumes that MyInterface_v1_0_s_ifspec is a valid data
// structure that represents the interface being registered. The 
// variable is a valid pointer to a binding vector.
RPC_STATUS status;
status = RpcEpRegister(
    MyInterface_v1_0_s_ifspec,
    rpcBindingVector,
    NULL,
    NULL);
```



The first parameter to [**RpcEpRegister**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcepregister) is the structure that represents the interface. You can find it in the header file that the MIDL compiler generated from your MIDL file for this distributed application. See [Developing the Interface](developing-the-interface.md). Next, **RpcEpRegister** needs your application to pass a set of binding handles that are stored in a binding vector.

In addition to registering interface names, your server application can also register object UUIDs in the endpoint map. In this example, there are no object UUIDs to register, so the third parameter to [**RpcEpRegister**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcepregister) is set to **NULL**.

The last parameter is a comment string. Although the RPC run-time library does not use this string, setting the string is recommended, as it improves manageability of the system. A system administrator can use the string to detect which ports are used by which applications, which can then be used to determine which ports to be managed by firewalls.

 

 




