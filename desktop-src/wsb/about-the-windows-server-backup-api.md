---
title: About the Windows Server Backup API
description: Automatically backs up and restores your application's data.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 239ead55-6137-47da-8506-5718060350e7
ms.prod: windows-server-dev
ms.technology: windows-server-backup
ms.tgt_platform: multiple
keywords:
- Windows Server Backup Windows Server Backup , about
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# About the Windows Server Backup API

The Windows Server Backup API automatically backs up and restores your application's data.

By default, your applicationâ€™s data files are included in the volume backup for the volume where the application is installed, and they can be recovered in either of the following ways:

-   As part of the volume recovery.
-   As part of recovery of the files on the volume.

However, in both cases, the application does not appear as a separate recoverable item, even if it contains a VSS writer.

In order for your application to appear as a separate item in the [Windows Server Backup Recovery Wizard](http://go.microsoft.com/fwlink/p/?linkid=251096), it must register with Windows Server Backup.

In addition, some applications need to perform specialized operations during backup and recovery. For example, an application may need to stop a service before performing a restore operation and start the service again afterward. Such an application can implement these additional operations by creating an add-in as an out-of-process COM server using the [Windows Server Backup API interfaces](windows-server-backup-api-interfaces.md). In this case, the application and the add-in need to be registered with Windows Server Backup.

To register the application and add-in with Windows Server Backup, the application must set the **Application Support**, **Application Identifier**, and **CLSID** registry keys as described in [Windows Server Backup API Registry Keys](windows-server-backup-api-registry-keys.md). An application that does not include a add-in should set the **Application Support** and **Application Identifier** keys but not the **CLSID** key.

 

 




