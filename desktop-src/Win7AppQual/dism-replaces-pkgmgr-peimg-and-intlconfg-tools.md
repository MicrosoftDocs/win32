---
description: Deployment Image Servicing and Management (DISM)
ms.assetid: bbfee966-121b-4b53-9e3e-08a747559da0
title: Deployment Image Servicing and Management (DISM)
ms.topic: article
ms.date: 05/31/2018
---

# Deployment Image Servicing and Management (DISM)

## Affected Platforms

**Clients** - Windows Vista SP1 and later \| Windows 7  
**Servers** - Windows Server 2008 RTM and later \| Windows Server 2008 R2  


## Description

The Deployment Image Servicing and Management (DISM) tool replaces the pkgmgr, PEImg, and IntlConfg tools that are being retired in Windows 7. DISM provides a single centralized tool for performing all of the functions of these three tools in a more efficient and standardized way, eliminating the source of many of the frustrations experienced by current users of these tools.

DISM includes a shim for Windows Vista SP1 and later, as well as for Windows Server 2008 RTM and later, that redirects pkgmgr calls from legacy applications running on Windows 7 to DISM. If the application is running on one of the supported operating systems, the shim routes the call to pkgmgr. No shims exist for legacy applications that call PEImg or IntlConfg.

## Usage

DISM is transparent to pkgmgr end users on any of the supported platforms. However, if an application calls either PEImg or IntlConfg from Windows 7, the call will fail.

Update any scripts that call pkgmgr, PEImg, or IntlConfg to call DISM instead. It is important to include the updating of pkgmgr scripts in this effort, since the shim that provides backward compatibility for pkgmgr will be removed in future versions of the Windows operating systems.

Check to ensure that calls to DISM have replaced any calls to pkgmgr, PEImg, and IntlConfg, and that the operation executes successfully.

## Related topics

<dl> <dt>

[Deployment Image Servicing and Management (TechNet)](/previous-versions/windows/it-pro/windows-7/dd744256(v=ws.10))
</dt> </dl>

 

 
