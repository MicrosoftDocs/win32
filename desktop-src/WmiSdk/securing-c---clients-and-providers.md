---
description: Both C++ providers and client applications must perform many of the same operations to maintain WMI security.
ms.assetid: 0199f469-2666-4794-b364-36c54aa360a8
ms.tgt_platform: multiple
title: Securing C++ Clients and Providers
ms.topic: article
ms.date: 05/31/2018
---

# Securing C++ Clients and Providers

Both C++ providers and client applications must perform many of the same operations to maintain WMI security.

Client applications must set DCOM [impersonation](setting-the-default-process-security-level-using-c-.md) and [authentication](setting-authentication-in-wmi.md) levels correctly when connecting to WMI. Callbacks from [asynchronous calls](setting-security-on-an-asynchronous-call.md) have security risks, so client applications must [perform access checks](performing-access-checks.md) to ensure the callback is from a trusted source. Clients need to secure both [temporary and permanent event consumers](securing-wmi-events.md).

A provider may [perform access checks](performing-access-checks.md) to ensure that the resources it creates are only accessed by appropriate clients.

Both providers and clients also can set the security on a [specific proxy](setting-the-security-on-iwbemservices-and-other-proxies.md) connection. Both can also enable [privileges](executing-privileged-operations.md). An event provider must ensure that the client consumer has privileges to [receive a requested event](providing-events-securely.md).

Either a client or provider may need to make a remote connection that requires a different authentication service, NTLM instead of Kerberos for example.

 

 



