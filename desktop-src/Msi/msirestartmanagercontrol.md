---
description: The MSIRESTARTMANAGERCONTROL Property specifies whether the Windows Installer package uses the Restart Manager or FilesInUse Dialog functionality.
ms.assetid: fefff18b-892a-440e-9f57-d23aeb99af74
title: MSIRESTARTMANAGERCONTROL property
ms.topic: reference
ms.date: 05/08/2026
---

# MSIRESTARTMANAGERCONTROL property

The **MSIRESTARTMANAGERCONTROL** Property specifies whether the Windows Installer package uses the [Restart Manager](../rstmgr/restart-manager-portal.md) or [FilesInUse Dialog](filesinuse-dialog.md) functionality.

## Value

| Value | Meaning |
|---|---|
| `0` | This is the default value if the property is not set. Windows Installer always attempts to use the [Restart Manager](../rstmgr/restart-manager-portal.md). |
| `"Disable"` | Disables interaction of the package with the [Restart Manager](../rstmgr/restart-manager-portal.md). Windows Installer uses the [FilesInUse Dialog](filesinuse-dialog.md). |
| `"DisableShutdown"` | Windows Installer uses the [FilesInUse Dialog](filesinuse-dialog.md). This setting disables attempts by the [Restart Manager](../rstmgr/restart-manager-portal.md) to mitigate restarts when installing a Windows Installer package that has not been authored to use the Restart Manager. The installer still uses the Restart Manager to detect files in use by applications. |


## Remarks

The **MSIRESTARTMANAGERCONTROL** Property is ignored if the [Restart Manager](../rstmgr/restart-manager-portal.md) is unavailable or disabled.

The value of this property can be modified using customization transforms or upgrades. Changing the value of this property from custom actions has no effect.

## Requirements

| Requirement | Value |
|---|---|
| Version | Windows Installer 4.0 or later. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum service pack required by a Windows Installer version. |


## See also

- [Properties](properties.md)
- [DisableAutomaticApplicationShutdown](disableautomaticapplicationshutdown.md)
- [Not Supported in Windows Installer 3.1 and earlier versions](not-supported-in-windows-installer-version-3-1.md)
