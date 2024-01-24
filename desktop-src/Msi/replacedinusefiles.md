---
description: The ReplacedInUseFiles property is set if the installer writes over a file that is being held in use.
ms.assetid: cef7d36e-c721-4d47-beaa-53e6749334b6
title: ReplacedInUseFiles property
ms.topic: reference
ms.date: 05/31/2018
---

# ReplacedInUseFiles property

The **ReplacedInUseFiles** property is set if the installer writes over a file that is being held in use. This property is used by custom actions to detect that a reboot is required to complete the installation.

Set during the [InstallExecute](installexecute-action.md) and [InstallFinalize](installfinalize-action.md) actions.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




