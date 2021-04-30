---
description: The value of the ProductVersion property is the version of the product in string format.
ms.assetid: 551fca7e-a827-482d-bc56-ff2fe5a17025
title: ProductVersion property
ms.topic: reference
ms.date: 05/31/2018
---

# ProductVersion property

The value of the **ProductVersion** property is the version of the product in string format. This property is REQUIRED.

The format of the string is as follows:

<dl> major.minor.build  
</dl>

The first field is the major version and has a maximum value of 255. The second field is the minor version and has a maximum value of 255. The third field is called the build version or the update version and has a maximum value of 65,535.

## Remarks

At least one of the three fields of **ProductVersion** must change for an upgrade using the [Upgrade table](upgrade-table.md). Any update that changes only the package code, but leaves **ProductVersion** and [**ProductCode**](productcode.md) unchanged is called a [small update](small-updates.md). The three versions fields are provided primarily for convenience. For example, if you want to change **ProductVersion**, but do not want to change either the major or minor versions, you can change the build version.

Note that Windows Installer uses only the first three fields of the product version. If you include a fourth field in your product version, the installer ignores the fourth field.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> <dt>

[Patching and Upgrades](patching-and-upgrades.md)
</dt> <dt>

[small update](small-updates.md)
</dt> </dl>

 

 




