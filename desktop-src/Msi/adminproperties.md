---
description: The AdminProperties should be authored into the Property Table.
ms.assetid: 91dd58cf-6c8c-4d20-a829-c43301a30d7f
title: AdminProperties property
ms.topic: reference
ms.date: 05/31/2018
---

# AdminProperties property

The **AdminProperties** should be authored into the [Property Table](property-table.md). The value of **AdminProperties** is a list of property names separated by semicolons. The installer saves the values of these listed properties at the time of an [administrative installation](administrative-installation.md). When users install from the administrative image, the installation uses the saved values of the properties, rather than the values in the .msi file.

## Remarks

The property names in the list can be uppercase and lowercase letters (private properties), or all uppercase (public properties).

This property must never end with a semicolon.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




