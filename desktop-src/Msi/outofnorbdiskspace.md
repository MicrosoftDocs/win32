---
description: The installer sets the OutOfNoRbDiskSpace property to True if any volume that is a target of the installation has insufficient disk space to accommodate the installation.
ms.assetid: 910d6c1d-38d3-4680-b256-2bf30689ce11
title: OutOfNoRbDiskSpace property
ms.topic: reference
ms.date: 05/31/2018
---

# OutOfNoRbDiskSpace property

The installer sets the **OutOfNoRbDiskSpace** property to True if any volume that is a target of the installation has insufficient disk space to accommodate the installation. In this case, the **OutOfNoRbDiskSpace** property is set to True even if rollback has been disabled. If all volumes have sufficient space, the value is False.

A developer of an installation package can handle the situation when the [**OutOfDiskSpace**](outofdiskspace.md) property is True and the **OutOfNoRbDiskSpace** property is False by authoring a user interface that presents the user with an option to disable rollback and continue the installation. For information about conditionally displaying a dialog box, see [ControlEvent Overview](controlevent-overview.md). For information about disabling rollback, see [EnableRollback ControlEvent](enablerollback-controlevent.md).

The **OutOfNoRbDiskSpace** property is valid at any time after the [CostFinalize action](costfinalize-action.md) has been executed. The **OutOfNoRbDiskSpace** property status is dynamically updated any time the total installation cost is recalculated (for example, any time the installation state of any feature is changed through the [Selection dialog](selection-dialog.md)). Selection resolution actions use this value to cancel an installation and generate a dialog box.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> <dt>

[ControlEvent Overview](controlevent-overview.md)
</dt> <dt>

[**OutOfDiskSpace property**](outofdiskspace.md)
</dt> <dt>

[EnableRollback ControlEvent](enablerollback-controlevent.md)
</dt> <dt>

[CostFinalize action](costfinalize-action.md)
</dt> <dt>

[Selection dialog](selection-dialog.md)
</dt> </dl>

 

 




