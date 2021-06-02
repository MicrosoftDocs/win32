---
description: The PROMPTROLLBACKCOST property specifies the action the installer takes if rollback installation capabilities are enabled and there is insufficient disk space to complete the installation.The possible values of PROMPTROLLBACKCOST are as follows.ValueActionPDisplay a dialog box asking whether to continue without a rollback.DDisable rollback and continue without asking user.FFail with the out-of-disk-space error prompt.
ms.assetid: 6ffd0b3f-79b8-4ce3-a262-4d27ffc5a175
title: PROMPTROLLBACKCOST property
ms.topic: reference
ms.date: 05/31/2018
---

# PROMPTROLLBACKCOST property

The **PROMPTROLLBACKCOST** property specifies the action the installer takes if [rollback installation](rollback-installation.md) capabilities are enabled and there is insufficient disk space to complete the installation.

The possible values of **PROMPTROLLBACKCOST** are as follows.



| Value | Action                                                              |
|-------|---------------------------------------------------------------------|
| P     | Display a dialog box asking whether to continue without a rollback. |
| D     | Disable rollback and continue without asking user.                  |
| F     | Fail with the out-of-disk-space error prompt.                       |



 

## Remarks

When the user interface is run at the Basic or no UI level, the installer handles all the out-of-disk-space logic automatically.

When the user interface runs at the Full level, the user can be given additional options, such as prompting before proceeding with a rollback, disabling rollback, or proceeding without rollback when the disk is full. It is up to the package developer to author the dialog box sequence to provide the appropriate choices to the user. The elements available to do this are the [EnableRollback ControlEvent](enablerollback-controlevent.md), [**OutOfDiskSpace**](outofdiskspace.md) property, [**OutOfNoRbDiskSpace**](outofnorbdiskspace.md) property, and the **PROMPTROLLBACKCOST** property.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




