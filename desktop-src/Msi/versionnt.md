---
description: The installer sets the VersionNT property to the version number for the operating system, undefined if the operating system is not Windows NT, Windows 2000, Windows XP, Windows Vista, Windows Server 2008, or Windows 7.
ms.assetid: 49005783-0bcb-458e-8266-56e6ea6afb43
title: VersionNT property
ms.topic: reference
ms.date: 05/31/2018
---

# VersionNT property

The installer sets the **VersionNT** property to the version number for the operating system, undefined if the operating system is not Windows NT, Windows 2000, Windows XP, Windows Vista, Windows Server 2008, or Windows 7. The value is an integer: MajorVersion \* 100 + MinorVersion.

Conditional statements that depend upon the operating system can use this property.

See also [Operating System Property Values](operating-system-property-values.md).

## Remarks

Condition expressions can test for Windows NT, Windows 2000, or Windows XP by using the property name, or may verify the version by using a comparison operator.

## Requirements



| Requirement | Value |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




