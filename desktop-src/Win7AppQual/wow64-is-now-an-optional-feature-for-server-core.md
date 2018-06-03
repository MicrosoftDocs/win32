---
Description: .
ms.assetid: 9a918cd3-60a0-4231-975a-bee12de5c812
title: WoW64 Is Now an Optional Feature for Server Core
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WoW64 Is Now an Optional Feature for Server Core

## Affected Platforms

<dl> **Servers** - Windows Server 2008 R2  
</dl>

## Feature Impact

<dl> **Severity** - Low  
**Frequency** - Low  
</dl>

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

-   [WOW64 Implementation Details](https://msdn.microsoft.com/windows/desktop/93daf9d0-dfdb-42c3-8c3d-397b21991e83)
-   [Debugging WOW64](https://msdn.microsoft.com/windows/desktop/e0945bdd-998d-4531-869f-21c505cb2135)
-   [Server Core](https://msdn.microsoft.com/windows/desktop/38d5312d-a21f-4f85-a728-12ebf392999f)

 

 



