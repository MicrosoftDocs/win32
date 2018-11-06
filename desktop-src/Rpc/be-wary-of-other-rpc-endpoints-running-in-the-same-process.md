---
title: Be Wary of Other RPC Endpoints Running in the Same Process
description: When an application resides in a process with other RPC servers, all applications listen on all protocols.
ms.assetid: edb20108-e0c3-4b9b-b57d-45a96d9472ba
ms.topic: article
ms.date: 05/31/2018
---

# Be Wary of Other RPC Endpoints Running in the Same Process

When an application resides in a process with other RPC servers, all applications listen on all protocols. As such, if a component calls [**RpcServerUseProtseq**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserveruseprotseq)\* for LRPC only, it is not necessarily accessible over LRPC only. It may be accessible over other protocols, since other RPC servers in the process may be listening on pipes or sockets (for example).

Similar to strict context handles, not putting another endpoint in the process does not mean another endpoint does not exist. Regardless of how you register your server, there is no special association between your interface and your endpoint; all interfaces are callable on all endpoints in that process. This is another reason why the endpoint security model is ineffective; if a security descriptor is placed on an endpoint, attackers can call the interface on another endpoint.

To ensure a process be called only on a specific protocol sequence, register a security callback function, and in that function, check on which protocol sequence the call is made.

 

 




