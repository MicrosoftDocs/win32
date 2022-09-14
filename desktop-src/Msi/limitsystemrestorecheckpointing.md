---
description: This per-machine system policy turns off the creation of checkpoints by Windows Installer.
ms.assetid: 706d6c85-3876-4205-b7da-b0fd709e65dd
title: LimitSystemRestoreCheckpointing
ms.topic: article
ms.date: 05/31/2018
---

# LimitSystemRestoreCheckpointing

This per-machine [system policy](system-policy.md) turns off the creation of checkpoints by Windows Installer.

Set to 0 or absent, the installer does normal checkpointing for install or uninstall. Set to 1, the installer creates no checkpoints.

This policy affects only checkpoints set by Windows Installer. On Windows XP computers, administrators may decide to disable checkpointing from within Windows Installer to improve performance. [**System Restore**](../sr/system-restore-portal.md) also creates additional checkpoints. For more information, see [System Restore Points and the Windows Installer](system-restore-points-and-the-windows-installer.md) and [Setting a Restore Point from a Custom Action](setting-a-restore-point-from-a-custom-action.md).

## Registry Key

Set the value named LimitSystemRestoreCheckpointing under the following registry key.

**HKEY\_LOCAL\_MACHINE\\Software\\Policies\\Microsoft\\Windows\\Installer**

## Data Type

**REG\_DWORD**

 

 
