---
title: File Server Resource Manager
description: The File Server Resource Manager (FSRM) API enables remote configuration of directory quotas, file screens, and storage reports on a server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: afa0a6b8-4327-41ac-8039-bb2ba9eec8a3
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- File Server Resource Manager File Server Resource Manager
- File Server Resource Manager File Server Resource Manager , home page
- FSRM File Server Resource Manager See File Server Resource Manager
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# File Server Resource Manager

## Purpose

The File Server Resource Manager (FSRM) API is used for many file and storage related management tasks, including setting a limit on the size of a given directory using directory quotas, restricting the type of data that can be stored under a given directory using file screens, and generating storage reports that administrators can use to analyze storage utilization. Most FSRM interfaces support remote as well as local server functionality.

## Developer audience

The FSRM API is designed for use by C/C++ and Visual Basic programmers and those writing scripts. Familiarity with COM, file systems, and storage is required.

For conceptual information on FSRM, see [Step-by-Step Guide for File Server Resource Manager](http://go.microsoft.com/fwlink/p/?linkid=93591) in the Windows Server 2008 R2 Technical Library on Technet.

## Run-time requirements

The FSRM API is available starting with Windows Server 2008. Note that the FSRM feature is not installed by default and must be added via Server Manager or related mechanisms. Starting with Windows Server 2012 and Windows 8 a subset of the FSRM APIs are available without installing the FSRM feature.

## In this section

<dl> <dt>

[Using FSRM](using-fsrm.md)
</dt> <dd>

Procedural guide.

</dd> <dt>

[FSRM Reference](fsrm-reference.md)
</dt> <dd>

Reference information for the FSRM API.

</dd> </dl>

 

 




