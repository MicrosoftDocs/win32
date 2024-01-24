---
description: The INSTALLLEVEL property is the initial level at which features are selected &\#0034;ON&\#0034; for installation by default.
ms.assetid: 5051cc46-837a-4446-a54c-4bd4081a424c
title: INSTALLLEVEL property
ms.topic: reference
ms.date: 05/31/2018
---

# INSTALLLEVEL property

The **INSTALLLEVEL** property is the initial level at which features are selected "ON" for installation by default. A feature is installed only if the value in the Level field of the [Feature table](feature-table.md) is less than or equal to the current INSTALLLEVEL value. The installation level for any installation is specified by the **INSTALLLEVEL** property, and can be an integral from 1 to 32,767. For further discussion of installation levels, see [Feature Table](feature-table.md).

## Default Value

If no value is specified, the install level defaults to 1.

## Remarks

The installation level specified by the **INSTALLLEVEL** property can be overridden by the following properties:

-   [**ADDLOCAL**](addlocal.md)
-   [**ADDSOURCE**](addsource.md)
-   [**ADDDEFAULT**](adddefault.md)
-   [**COMPADDLOCAL**](compaddlocal.md)
-   [**COMPADDSOURCE**](compaddsource.md)
-   [**FILEADDLOCAL**](fileaddlocal.md)
-   [**FILEADDSOURCE**](fileaddsource.md)
-   [**REMOVE**](remove.md)
-   [**REINSTALL**](reinstall.md)
-   [**ADVERTISE**](advertise.md)

For example, setting ADDLOCAL=ALL installs all features locally regardless of the value of the **INSTALLLEVEL** property. If the value of the Level column in the [Feature table](feature-table.md) is 0, that feature is not installed and not displayed in the UI.

An administrator can permanently disable a feature by applying a customization transform that sets a 0 in the Level column for that feature. The application of the customization transform prevents the installation and display of the feature even if the user selects a complete installation using the UI or by setting ADDLOCAL to ALL on the command line. See [A Customization Transform Example](a-customization-transform-example.md).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




