---
title: RpcServerRegisterAuthInfo doesn't deny unauthorized users
description: When security providers are registered on the server with the RpcServerRegisterAuthInfo function, an authentication option is added; not an authentication requirement.
ms.assetid: c8db8973-6d47-47b4-b927-72cfb464e9f0
ms.topic: article
ms.date: 02/21/2023
---

# RpcServerRegisterAuthInfo doesn't deny unauthorized users

When security providers are registered on the server with the [**RpcServerRegisterAuthInfo**](/windows/win32/api/Rpcdce/nf-rpcdce-rpcserverregisterauthinfo) function, an authentication *option* is added; not an authentication *requirement*. That means that previous registrations with **RpcServerRegisterAuthInfo** aren't replaced. It also means that an unauthenticated client that could connect before can still connect.

Just calling the **RpcServerRegisterAuthInfo** function doesn't disallow unauthenticated clients from connecting. If they could connect before, then they can still connect; but function calls such as [**RpcImpersonateClient**](/windows/win32/api/Rpcdce/nf-rpcdce-rpcimpersonateclient) and [**RpcGetAuthorizationContextForClient**](/windows/win32/api/Rpcasync/nf-rpcasync-rpcgetauthorizationcontextforclient) will fail. So when the **RpcServerRegisterAuthInfo** function is called, potential attackers have not been weeded out&mdash;rather, authorized clients are given a chance to prove their identity. So you must still put in place checks to determine whether potential attackers are attempting to connect.
