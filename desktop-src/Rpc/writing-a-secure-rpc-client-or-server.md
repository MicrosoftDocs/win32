---
title: Writing a Secure RPC Client or Server
description: This section provides best practice recommendations for writing a secure RPC client or server.
ms.assetid: b738b780-247c-4108-b64d-0a4883895182
keywords:
- Remote Procedure Call RPC , best practices, writing a secure client or server
ms.topic: article
ms.date: 05/31/2018
---

# Writing a Secure RPC Client or Server

This section provides best practice recommendations for writing a secure RPC client or server.

The information in this section applies to Windows 2000 and Windows XP. This section applies to all protocol sequences, including [**ncalrpc**](/windows/desktop/Midl/ncalrpc). Developers tend to think **ncalrpc** is not a probable target for an attack, which is not true on a terminal server where potentially hundreds of users have access to a service, and compromising or even bringing down a service can lead to acquiring extra access.

This section is divided into the following topics:

-   [Which Security Provider To Use](which-security-provider-to-use.md)
-   [Controlling Client Authentication](controlling-client-authentication.md)
-   [Choosing an Authentication Level](choosing-an-authentication-level.md)
-   [Choosing Security QOS Options](choosing-security-qos-options.md)
-   [Common Mistake: Assuming RpcServerRegisterAuthInfo Prevents Unauthorized Users from Calling your Server](common-mistake-assuming-rpcserverregisterauthinfo-prevents-unauthorized-users-from-calling-your-server.md)
-   [Callbacks](callbacks.md)
-   [Null Sessions](null-sessions.md)
-   [Use the /robust Flag](use-the-robust-flag.md)
-   [IDL Techniques for Better Interface and Method Design](idl-techniques-for-better-interface-and-method-design.md)
-   [Strict and Type Strict Context Handles](strict-and-type-strict-context-handles.md)
-   [Do Not Trust Your Peer](do-not-trust-your-peer.md)
-   [Do Not Use Endpoint Security](do-not-use-endpoint-security.md)
-   [Be Wary of Other RPC Endpoints Running in the Same Process](be-wary-of-other-rpc-endpoints-running-in-the-same-process.md)
-   [Verify The Server Is Who It Claims To Be](verify-the-server-is-who-it-claims-to-be.md)
-   [Use Mainstream Protocol Sequences](use-mainstream-protocol-sequences.md)
-   [How Secure is my RPC Server Now?](how-secure-is-my-rpc-server-now.md)

 

 