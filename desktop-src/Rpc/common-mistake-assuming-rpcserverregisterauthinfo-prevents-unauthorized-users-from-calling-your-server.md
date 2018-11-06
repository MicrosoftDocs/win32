---
title: Common Mistake Assuming RpcServerRegisterAuthInfo Prevents Unauthorized Users from Calling your Server
description: When security providers are registered on the server with the RpcServerRegisterAuthInfo function, an option is added, not a requirement.
ms.assetid: c8db8973-6d47-47b4-b927-72cfb464e9f0
ms.topic: article
ms.date: 05/31/2018
---

# Common Mistake: Assuming RpcServerRegisterAuthInfo Prevents Unauthorized Users from Calling your Server

When security providers are registered on the server with the [**RpcServerRegisterAuthInfo**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterauthinfo) function, an option is added, not a requirement. This means previous registrations with **RpcServerRegisterAuthInfo** are not replaced. This also means unauthenticated clients still can connect. By calling the **RpcServerRegisterAuthInfo** function, unauthenticated clients are not disallowed from connecting; they can still connect, but function calls such as [**RpcImpersonateClient**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcimpersonateclient) and [**RpcGetAuthorizationContextForClient**](/windows/desktop/api/Rpcasync/nf-rpcasync-rpcgetauthorizationcontextforclient) will fail. So when the **RpcServerRegisterAuthInfo** function is called, potential attackers have not been weeded out—rather, clients that ought to have access are given a chance to prove their identity. Checks must still be in place to determine whether potential attackers are attempting to connect.

 

 




