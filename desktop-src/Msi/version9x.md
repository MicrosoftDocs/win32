---
description: 'The Version9X property gives the version number for 9x versions of Windows operating systems.The value of this property is an integer: MajorVersion \* 100 + MinorVersion.'
ms.assetid: 0a22de88-4958-46be-82c3-6465aec86d33
title: Version9X property
ms.topic: reference
ms.date: 05/31/2018
---

# Version9X property

The **Version9X** property gives the version number for 9x versions of Windows operating systems.

The value of this property is an integer: MajorVersion \* 100 + MinorVersion. The property remains undefined if the operating system is not a 9x version. For more information, see [Operating System Property Values](operating-system-property-values.md).

## Remarks

Condition expressions can test for the version by using the property name or may verify the version by using a comparison operator.

All property names are case-sensitive. Note that the X in the name **Version9X** is uppercase.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




