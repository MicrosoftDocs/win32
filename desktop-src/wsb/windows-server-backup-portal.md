---
title: Windows Server Backup
description: Automatically back up and restore data for an application that contains a Volume Shadow Copy Service (VSS) writer. Implement additional operations by creating an add-in as an out-of-process COM server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 63d8b64e-2ec7-4dd0-b993-c465bdec2dd0
ms.prod: windows-server-dev
ms.technology: windows-server-backup
ms.tgt_platform: multiple
keywords:
- Windows Server Backup Windows Server Backup
- Windows Server Backup Windows Server Backup , home page
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Windows Server Backup

## Purpose

The [Windows Server Backup](http://go.microsoft.com/fwlink/p/?linkid=111182) feature automatically backs up and restores application data.

Windows Server Backup also provides registry keys and APIs that:

-   Allow your application to appear in the Recovery Wizard as a separately recoverable item.
-   Allow your cloud backup provider to report its status in the Windows Server Backup Microsoft Management Console (MMC) snap-in.

## Developer audience

The Windows Server Backup API is designed for C and C++ developers.

## Run-time requirements

The Windows Server Backup API requires Windows Server 2008.

The Cloud Backup Provider API in Windows Server Backup requires Windows Server 2012.

## In this section

<dl> <dt>

[About the Windows Server Backup API](about-the-windows-server-backup-api.md)
</dt> <dd>

Overview of the Windows Server Backup API.

</dd> <dt>

[About the Cloud Backup Provider API](about-the-windows-server-backup-cloud-backup-provider-api.md)
</dt> <dd>

Overview of the Cloud Backup Provider API.

</dd> <dt>

[Windows Server Backup API Reference](windows-server-backup-api-reference.md)
</dt> <dd>

Documentation of Windows Server Backup API elements.

</dd> <dt>

[Cloud Backup Provider API Reference](cloud-backup-provider-api-reference.md)
</dt> <dd>

Documentation of Cloud Backup Provider API elements.

</dd> </dl>

 

 




