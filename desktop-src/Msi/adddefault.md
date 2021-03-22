---
description: The value of the ADDDEFAULT property is a list of features delimited by commas, which are to be installed in their default configuration.
ms.assetid: 78cec3fc-c653-487a-b41c-a43c42e3a157
title: ADDDEFAULT property
ms.topic: reference
ms.date: 05/31/2018
---

# ADDDEFAULT property

The value of the **ADDDEFAULT** property is a list of features delimited by commas, which are to be installed in their default configuration. The features must be present in the Feature column of the [Feature Table.](feature-table.md) To install all features in their default configurations, use ADDDEFAULT=ALL on the command line.

A feature listed in the **ADDDEFAULT** property is installed in the same installation state as if the user requested an installation-on-demand of the feature. The state is determined by the bits that are set for the feature in the Attributes column of the [Feature Table](feature-table.md), and which bits are set for the feature components in the Attributes column of the [Component Table](component-table.md).

## Remarks

The feature names are case sensitive.

The installer always evaluates the following properties in the following order:

1.  [**ADDLOCAL**](addlocal.md)
2.  [**REMOVE**](remove.md)
3.  [**ADDSOURCE**](addsource.md)
4.  **ADDDEFAULT**
5.  [**REINSTALL**](reinstall.md)
6.  [**ADVERTISE**](advertise.md)
7.  [**COMPADDLOCAL**](compaddlocal.md)
8.  [**COMPADDSOURCE**](compaddsource.md)
9.  [**COMPADDDEFAULT**](compadddefault.md)
10. [**FILEADDLOCAL**](fileaddlocal.md)
11. [**FILEADDSOURCE**](fileaddsource.md)
12. [**FILEADDDEFAULT**](fileadddefault.md)

For example:

-   If the command line specifies: ADDLOCAL=ALL, ADDSOURCE = MyFeature, all the features are first set to run-local and then **MyFeature** is set to run-from-source.
-   If the command line is: ADDSOURCE=ALL, ADDLOCAL=MyFeature, first **MyFeature** is set to run-local, and then when ADDSOURCE=ALL is evaluated, all features (including **MyFeature**) are reset to run-from-source.

The installer sets the [**Preselected**](preselected.md) property to a value of "1" during the resumption of a suspended installation, or when any of the above properties are specified on the command line.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




