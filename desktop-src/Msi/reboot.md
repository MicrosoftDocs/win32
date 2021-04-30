---
description: The REBOOT property suppresses certain prompts for a restart of the system.
ms.assetid: 'd88752cd-f59d-4214-b5b5-ce126500aa4e'
title: REBOOT property
ms.topic: article
ms.date: 05/31/2018
---

# REBOOT property

The **REBOOT** property suppresses certain prompts for a restart of the system. An administrator typically uses this property with a series of installations to install several products at the same time with only one restart at the end. For more information, see [System Reboots](system-reboots.md).

The [ForceReboot](forcereboot-action.md) and [ScheduleReboot](schedulereboot-action.md) actions inform the installer to prompt the user to restart the system. The installer can also determine that a restart is necessary whether there are any ForceReboot or ScheduleReboot actions in the sequence. For example, the installer automatically prompts for a restart if it needs to replace any files in use during the installation.

You can suppress certain prompts for restarts by setting the **REBOOT** property as follows.



| REBOOT value   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Force          | Always prompt for a restart at the end of the installation. The UI always prompts the user with an option to restart at the end. If there is no user interface, and this is not a [multiple-package installation](multiple-package-installations.md), the system automatically restarts at the end of the installation. If this is a multiple-package installation, there is no automatic restart of the system and the installer returns ERROR\_SUCCESS\_REBOOT\_REQUIRED. |
| Suppress       | Suppress prompts for a restart at the end of the installation. The installer still prompts the user with an option to restart during the installation whenever it encounters the [ForceReboot action](forcereboot-action.md). If there is no user interface, the system automatically restarts at each ForceReboot. Restarts at the end of the installation (for example, caused by an attempt to install a file in use) are suppressed.                                    |
| ReallySuppress | Suppress all restarts and restart prompts initiated by ForceReboot during the installation. Suppress all restarts and restart prompts at the end of the installation. Both the restart prompt and the restart itself are suppressed. For example, restarts at the end of the installation, caused by an attempt to install a file in use, are suppressed.                                                                                                                    |



 

## Remarks

The installer only evaluates the first character of the **REBOOT** property.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> <dt>

[**REBOOTPROMPT Property**](rebootprompt.md)
</dt> <dt>

[System Reboots](system-reboots.md)
</dt> </dl>

 

 




