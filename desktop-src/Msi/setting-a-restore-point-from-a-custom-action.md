---
Description: Custom actions must not call the SRSetRestorePoint function because this may result in a restore entry point being written into the middle of a Windows Installer installation.
ms.assetid: 5c3df769-e24d-47b4-af6a-b58e3cbcf00c
title: Setting a Restore Point from a Custom Action
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Setting a Restore Point from a Custom Action

Custom actions must not call the [**SRSetRestorePoint**](https://msdn.microsoft.com/46f0094d-9079-41b5-9efc-ef07082653d3) function because this may result in a restore entry point being written into the middle of a Windows Installer installation.

For more information, see [System Restore Points and the Windows Installer](system-restore-points-and-the-windows-installer.md).

 

 



