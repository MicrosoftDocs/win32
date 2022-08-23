---
title: Remote data service removed
description: Remote data service server components are removed in Windows 8
ms.assetid: 53ECB92C-8868-4A1A-82BD-4ADE75F7BB59
keywords:
- RDS server
ms.topic: article
ms.date: 05/31/2018
---

# Remote data service server components are removed in Windows 8

## Platforms

 **Clients** - Windows 8  
**Servers** - Windows Server 2012  



## Description

The remote data service (RDS) server is not available in Windows 8:

-   File msadcf.dll, which hosts the default "business object" RDSServer.DataFactory, is removed, and its associated files (msadcfr.dll, msadcfr.dll.mui, handler.reg and handsafe.reg) are removed
-   File msdfmap.dll, which is the default Handler, is removed, and the file msdfmap.ini is removed
-   File msadcs.dll, the ISAPI, is removed

## Manifestation

Customers cannot host an RDS server on Windows 8.

## Mitigation

Customers can keep their RDS server on a machine with Windows 7 or other down-level operating systems.

## Solution

Customers can keep their RDS server on a machine with Windows 7 or other down-level operating systems.

## Resources

[Data Access Technologies Roadmap](/sql/connect/connect-history)

 

 