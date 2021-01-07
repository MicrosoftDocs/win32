---
description: System Restore automatically monitors and records key system changes on a user's computer. For more information, see System Restore.
ms.assetid: 5fc345ff-8a47-4372-806f-64b8c271fd2d
title: System Restore Points and the Windows Installer
ms.topic: article
ms.date: 05/31/2018
---

# System Restore Points and the Windows Installer

System Restore automatically monitors and records key system changes on a user's computer. For more information, see [System Restore](../sr/system-restore-portal.md).

System restore points are created by the system and are also created by Windows Installer when software is installed or removed.

On Windows XP, the installer may create checkpoints during the first installation of an application, and during its removal. The installer only creates checkpoints in these cases when the change is run with at least a [*basic UI*](b-gly.md). Installations having the [user interface level](user-interface-levels.md) set to None are usually initiated by the system or an application that should handle creating a checkpoint. For more information, see [System Restore](../sr/system-restore-portal.md).

In corporations with many small applications, administrators may decide to disable checkpointing from within the installer to improve performance. For more information, see [LimitSystemRestoreCheckpointing](limitsystemrestorecheckpointing.md) or [Setting a Restore Point from a Custom Action](setting-a-restore-point-from-a-custom-action.md).

Beginning with Windows Installer 5.0, the [**MSIFASTINSTALL**](msifastinstall.md) property can be set to prevent an installation from generating a system restore point.

 

 
