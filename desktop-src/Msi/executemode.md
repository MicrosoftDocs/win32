---
description: The EXECUTEMODE property specifies how the installer executes system updates.
ms.assetid: 7b90d2e6-d661-412b-b054-2c218c95c02a
title: EXECUTEMODE property
ms.topic: reference
ms.date: 05/31/2018
---

# EXECUTEMODE property

The **EXECUTEMODE** property specifies how the installer executes system updates. This property may be useful when it is necessary to run an installation without actually changing the system. The property can be set to None to disable updating operations such as the installation of files and registry values.

This property can have one of the following two values. The installer only examines the first letter of the value and is case insensitive.

<dl> <dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>None
</dt> <dd>

No changes are made to the system. The installer runs the user interface and then queries the database.

</dd> <dt>

<span id="Script"></span><span id="script"></span><span id="SCRIPT"></span>Script
</dt> <dd>

All changes to the system are made through script execution. This is the default mode.

</dd> </dl>

## Default Value

If this property is not defined, the execution mode defaults to Script.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




