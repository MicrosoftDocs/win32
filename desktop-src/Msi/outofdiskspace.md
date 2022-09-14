---
description: The installer sets the OutOfDiskSpace property to TRUE if any volume that is a target of the current installation has insufficient disk space to accommodate the installation.
ms.assetid: fb1e3be7-12dd-4036-b657-b91b480fca4a
title: OutOfDiskSpace property
ms.topic: reference
ms.date: 05/31/2018
---

# OutOfDiskSpace property

The installer sets the **OutOfDiskSpace** property to TRUE if any volume that is a target of the current installation has insufficient disk space to accommodate the installation. If all volumes have sufficient space, the value is FALSE. Selection resolution actions use this value to cancel an installation and generate a dialog box.

This property is valid at any time after the [CostFinalize action](costfinalize-action.md) is executed. The [**OutOfNoRbDiskSpace**](outofnorbdiskspace.md) property status is dynamically updated any time the total installation cost is recalculated (for example, any time the installation state of any feature is changed through the [Selection](selection-dialog.md) dialog).

## Remarks

Any dialog relying on the **OutOfDiskSpace** property to determine whether to bring up a dialog must set the [TrackDiskSpace Dialog Style Bit](trackdiskspace-dialog-style-bit.md) for the dialog to dynamically update space on the target volumes.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




