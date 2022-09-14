---
description: The installer sets the value of the MsiRestartManagerSessionKey property to the session key for the Restart Manager session.
ms.assetid: efbf11f2-38ab-4509-aa01-23fa8cfdaa60
title: MsiRestartManagerSessionKey property
ms.topic: reference
ms.date: 05/31/2018
---

# MsiRestartManagerSessionKey property

The installer sets the value of the **MsiRestartManagerSessionKey** property to the session key for the [Restart Manager](../rstmgr/restart-manager-portal.md) session. Custom actions can use the session key to join the [Restart Manager](../rstmgr/restart-manager-portal.md) session.

## Remarks

The installer sets the value of the **MsiRestartManagerSessionKey** property at initialization, and then clears the value during the [InstallValidate](installvalidate-action.md) action. Custom actions that need the value of the **MsiRestartManagerSessionKey** property must be come before the InstallValidate action in the action sequence.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum service pack required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> <dt>

[Not Supported in Windows Installer 3.1 and earlier versions](not-supported-in-windows-installer-version-3-1.md)
</dt> </dl>

 

 
