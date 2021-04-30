---
description: The installer sets the AFTERREBOOT property to 1 after a reboot invoked by the ForceReboot action. The installer adds AFTERREBOOT=1 to the command line run immediately after the reboot.
ms.assetid: d8a71d9a-64bf-4a38-9c3b-073c216de7fa
title: AFTERREBOOT property
ms.topic: reference
ms.date: 05/31/2018
---

# AFTERREBOOT property

The installer sets the **AFTERREBOOT** property to 1 after a reboot invoked by the [ForceReboot action](forcereboot-action.md). The installer adds AFTERREBOOT=1 to the command line run immediately after the reboot.

## Remarks

The [ForceReboot action](forcereboot-action.md) must always be used with a conditional statement such that the installer triggers a reboot only when necessary. A reboot might be required if a particular file was replaced or a particular component was installed. The case is different for each product and a custom action might be needed to determine whether a reboot is needed. The condition on the ForceReboot action commonly makes use of the **AFTERREBOOT** property.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> <dt>

[System Reboots](system-reboots.md)
</dt> </dl>

 

 




