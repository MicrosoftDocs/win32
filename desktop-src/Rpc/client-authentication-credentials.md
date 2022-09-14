---
title: Client Authentication Credentials
description: Each authenticated client must provide authentication credentials to the server.
ms.assetid: d567e944-8d68-4d95-be6a-840e30f57ba9
ms.topic: article
ms.date: 05/31/2018
---

# Client Authentication Credentials

Each authenticated client must provide authentication credentials to the server. Under RPC, the client stores its authentication credentials in the binding between the client and the server. To do this, the client calls [**RpcBindingSetAuthInfo**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingsetauthinfo) or [**RpcBindingSetAuthInfoEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingsetauthinfoexa).

There are two types of credentials—implicit and explicit:

-   Explicit credentials exist when the client supplies username, password, and domain.
-   Implicit credentials exist when the client uses credentials from the thread or process token calling the **RpcBindingSetAuthInfo** or **RpcBindingSetAuthInfoEx** functions.

Clients should refrain from supplying explicit credentials because storing, manipulating, and retrieving a user password can introduce a security vulnerability into a distributed system if explicit credentials are used.

To use implicit credentials, the client calls **RpcBindingSetAuthInfo**(*Ex*). The security system and RPC obtain credentials from the thread or process token for use in the authentication session.

If the client uses explicit credentials, the fifth parameter of these two functions is of type [**RPC\_AUTH\_IDENTITY\_HANDLE**](rpc-auth-identity-handle.md). This is a flexible type that is a pointer to a data structure. The contents of the data structure can differ with each authentication service. Currently, the SSPs that RPC supports require that your application set **RPC\_AUTH\_IDENTITY\_HANDLE** to point to a [**SEC\_WINNT\_AUTH\_IDENTITY**](/windows/desktop/api/Rpcdce/ns-rpcdce-sec_winnt_auth_identity_a) structure. The **SEC\_WINNT\_AUTH\_IDENTITY** structure contains fields for a user name, domain, and password.

 

 




