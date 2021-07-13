---
description: Microsoft Message Queuing (MSMQ) - Removal of Windows 2000 Client Support Service
ms.assetid: e29b477e-f7e9-413c-8eb9-2e764b7dd910
title: Microsoft Message Queuing (MSMQ) - Removal of Windows 2000 Client Support Service
ms.topic: article
ms.date: 05/31/2018
---

# Microsoft Message Queuing (MSMQ) - Removal of Windows 2000 Client Support Service

## Affected Platforms

**Servers** - Windows Server 2008 R2  



## Feature Impact

 **Severity** - High  
**Frequency** - Low  

## Description

The Windows 2000 Client Support Service is an optional component of the Message Queuing Server that you can install on a Windows 2003 or Windows 2008 domain controller machine. This service allows Windows 2000 clients to operate in a domain-integrated mode with any Message Queuing server installed on Windows 2003/2008 machines. MSMQ Clients operating on Windows XP upwards do not need this service.

### Manifestation of Impact

This change impacts Windows 2000 when interoperating in a Windows 7 domain where all domain controllers are Windows Server 2008 R2. If a customer upgrades to the Windows 7 domain, the existing MSMQ applications on any Windows 2000 machines in the domain will not be able to operate in a domain-integrated mode unless these clients upgrade to a higher Windows version.

### Mitigation

Users who have Windows 2000 Client machines on a Windows 7 domain can configure a Windows 2003/2008 domain controller in the domain and install the MSMQ Windows 2000 Client Support Service on this domain controller.

### Leveraging Feature Capabilities

Users who have Windows 2000 Client machines running MSMQ should upgrade to a higher Windows version in order to take advantage of the Active Directory-based implementation of the MSMQ Server.

### Compatibility, Performance, Reliability, and Usability Testing

Users who have Windows 2000 Client machines running MSMQ on a Windows 7 domain with one or more down-level domain controllers should verify that their applications are functional on this mixed domain.

 

 



