---
Description: Custom actions must not call the SRSetRestorePoint function because this may result in a restore entry point being written into the middle of a Windows Installer installation.
ms.assetid: 5c3df769-e24d-47b4-af6a-b58e3cbcf00c
title: Setting a Restore Point from a Custom Action
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Setting a Restore Point from a Custom Action

Custom actions must not call the [**SRSetRestorePoint**](sr.srsetrestorepoint) function because this may result in a restore entry point being written into the middle of a Windows Installer installation.

For more information, see [System Restore Points and the Windows Installer](system-restore-points-and-the-windows-installer.md).

 

 



