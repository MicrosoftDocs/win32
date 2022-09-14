---
description: Microsoft Message Queuing (MSMQ) - SHA 2 Is the Default Hash Algorithm
ms.assetid: 43cca5bc-6675-4f29-925e-19d3fb19ef0f
title: Microsoft Message Queuing (MSMQ) - SHA 2 Is the Default Hash Algorithm
ms.topic: article
ms.date: 05/31/2018
---

# Microsoft Message Queuing (MSMQ) - SHA 2 Is the Default Hash Algorithm

## Affected Platforms

 **Clients** - Windows XP, Windows Vista, Windows 7  
**Servers** - Windows Server 2003, Windows Server 2008, Windows Server 2008 R2  










## Feature Impact

 **Severity** - Low  
**Frequency** - Low  





## Description

In Windows 7, MSMQ uses SHA-2 as the default when signing an outgoing message. Additionally, all incoming messages must be signed with SHA-2. You can enable support for a lower encryption algorithm through an administrator-accessible registry key.

## Manifestation of Impact

-   MSMQ in Windows 2003 or below will not accept signed messages originating from MSMQ in Windows 7
-   MSMQ in Windows 7 will not accept signed messages originating from Windows 2008 or below

## Mitigation

Users should consider upgrading to Windows 7 to leverage the stronger signing algorithm. To enable seamless signed message exchange between Windows 7 and any down-level operating system, the Administrator must add appropriate exceptions on the MSMQ machines.

 

 



