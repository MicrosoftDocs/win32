---
title: Mutual Authentication in Windows Sockets Applications
description: Microsoft Windows Sockets services can use the Registration and Resolution (RnR) APIs to publish services, or they can use service connection points.
ms.assetid: 2b73a754-4f16-41a2-8441-a4ee5f80035c
ms.tgt_platform: multiple
keywords:
- Mutual Authentication in Windows Sockets Applications
- Active Directory, using, mutual authentication, in Windows sockets applications
ms.topic: article
ms.date: 05/31/2018
---

# Mutual Authentication in Windows Sockets Applications

Microsoft Windows Sockets services can use the Registration and Resolution (RnR) APIs to publish services, or they can use service connection points.

For more information and a code example that shows how to perform mutual authentication for a Windows Sockets service that publishes using a service connection point, see [Mutual Authentication in a Windows Sockets Service with an SCP](mutual-authentication-in-a-windows-sockets-service-with-an-scp.md). This code example uses an SSPI security package to manage the authentication negotiations between a client and the WinSock service.

A WinSock RnR service can use similar code to perform mutual authentication using an SSPI package. In this case, the service would compose its SPNs using the distinguished name of the service's entry in the WinsockServices container in the directory.

For example, if the service registers itself with the name "WinSockRnRSampleService", you would compose the service's SPN from the following distinguished name:


```C++
cn=WinSockRnRSampleService,cn=WinsockServices,cn=System,<domain DN>
```



 

 




