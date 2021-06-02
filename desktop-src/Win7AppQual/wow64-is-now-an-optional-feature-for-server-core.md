---
description: WoW64 Is Now an Optional Feature for Server Core
ms.assetid: 9a918cd3-60a0-4231-975a-bee12de5c812
title: WoW64 status in Server Core
ms.topic: article
ms.date: 05/31/2018
---

# WoW64 Is Now an Optional Feature for Server Core

## Affected Platforms

**Servers** - Windows Server 2008 R2  



## Feature Impact

 **Severity** - Low  
**Frequency** - Low  





## Description

The Server Core installation option for Windows Server 2008 R2 allows you to uninstall WoW64. WoW64 is now an optional feature that you can uninstall if it is not necessary to run 32-bit code.

In addition, the Active Directory and Active Directory Lightweight Directory Services roles require WoW64 in order to run in Windows Server 2008 R2.

## Manifestation of Impact

If you uninstall WoW64, Administrators running 32-bit code on Server Core will receive an error message that the application cannot be executed. If Administrators attempt to run Active Directory and Active Directory Lightweight Directory Services, they will receive an error message.

## Mitigation

Install WoW64.

## Solution

The preferred solution is to provide a 64-bit version of the code to enable it to run on Server Core without needing WoW64.

At a minimum, provide user documentation noting that to run 32-bit code they must install WoW64.

## Compatibility, Performance, Reliability, and Usability Testing

Verify that all code used is 64-bit.

## Links to Other Resources

-   [WOW64 Implementation Details](../winprog64/wow64-implementation-details.md)
-   [Debugging WOW64](../winprog64/debugging-wow64.md)
-   [Server Core](/previous-versions/windows/desktop/legacy/ms723891(v=vs.85))

 

 
