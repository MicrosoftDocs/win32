---
title: Integrity and Privacy
description: Client/service communications that require mutual authentication must protect the traffic they exchange after successful authentication.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 5ae3ede3-6eed-4532-9b02-448d2f4ca674
ms.tgt_platform: multiple
keywords:
- Integrity and Privacy AD
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Integrity and Privacy

Client/service communications that require mutual authentication must protect the traffic they exchange after successful authentication. It is unwise to mutually authenticate at the time of the initial connection to the service if the traffic is later subject to modification by an unauthorized user. SSPI, RPC, and COM all provide utilities for digitally signing and encrypting messages. Applying digital signatures prevents modified traffic from going undetected and discourages eavesdropping. Traffic can be intercepted of course, but decrypting the traffic is sufficiently difficult to deter most unauthorized users.

Unless performance requirements are severe, use of both signing and encryption is recommended, especially for administrative functions. Even when performance is an issue, some customers choose tighter security over better performance. In such cases, make integrity and privacy configurable options with higher security the default and higher performance the option.

RPC clients can specify the level of integrity and privacy when they call the [**RpcBindingSetAuthInfoEx**](https://msdn.microsoft.com/library/windows/desktop/aa375608) function to set the authentication data for the RPC binding. Use **RPC\_C\_AUTHN\_LEVEL\_PKT\_INTEGRITY** for signing and **RPC\_C\_AUTHN\_LEVEL\_PKT\_PRIVACY** for encryption. For more information, see [Mutual Authentication in RPC Applications](mutual-authentication-in-rpc-applications.md).

Services that use an SSPI package for mutual authentication can query the package to determine whether it supports the [**MakeSignature**](https://msdn.microsoft.com/library/windows/desktop/aa378736), [**VerifySignature**](https://msdn.microsoft.com/library/windows/desktop/aa380540), [**EncryptMessage**](https://msdn.microsoft.com/library/windows/desktop/aa375378), and [**DecryptMessage**](https://msdn.microsoft.com/library/windows/desktop/aa375211) functions for signing and encrypting messages. For more information and a code example, see [Ensuring Communication Integrity During Message Exchange](https://msdn.microsoft.com/library/windows/desktop/aa375395).

 

 




