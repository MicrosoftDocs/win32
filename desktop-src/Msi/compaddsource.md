---
description: The value of the COMPADDSOURCE property is a list of component GUIDs from the ComponentId column of the Component table, delimited by commas, that are to be installed to run from the source media.
ms.assetid: ee1e0650-674d-4189-8ef7-3d2ece89cc28
title: COMPADDSOURCE property
ms.topic: reference
ms.date: 05/31/2018
---

# COMPADDSOURCE property

The value of the **COMPADDSOURCE** property is a list of component GUIDs from the ComponentId column of the [Component](component-table.md) table, delimited by commas, that are to be installed to run from the source media. The installer uses this value to determine which features are set to be installed to run from source, based on the specified components. For each listed component ID, the installer examines all features linked (through the [FeatureComponents](featurecomponents-table.md) table) to that component, and installs the feature that requires the least amount of disk space to install. The components listed must be present in the Component column of the [Component](component-table.md) table.

## Remarks

Note that the component names are case-sensitive. Also note that if the LocalOnly bit flag is set in the Attributes column of the [Component](component-table.md) table for a component, then the component is installed to run locally.

The installer always evaluates the following properties in the following order:

1.  [**ADDLOCAL**](addlocal.md)
2.  [**REMOVE**](remove.md)
3.  [**ADDSOURCE**](addsource.md)
4.  [**ADDDEFAULT**](adddefault.md)
5.  [**REINSTALL**](reinstall.md)
6.  [**ADVERTISE**](advertise.md)
7.  [**COMPADDLOCAL**](compaddlocal.md)
8.  **COMPADDSOURCE**
9.  [**COMPADDDEFAULT**](compadddefault.md)
10. [**FILEADDLOCAL**](fileaddlocal.md)
11. [**FILEADDSOURCE**](fileaddsource.md)
12. [**FILEADDDEFAULT**](fileadddefault.md)

For example, if the command line specifies: ADDLOCAL=ALL, ADDSOURCE = MyFeature, all the features are first set to run-local and then MyFeature is set to run-from-source. If the command line is: ADDSOURCE=ALL, ADDLOCAL=MyFeature, first MyFeature is set to run-local, and then when ADDSOURCE=ALL is evaluated, all features (including MyFeature) are reset to run-from-source.

The installer sets the [**Preselected**](preselected.md) property to a value of "1" during the resumption of a suspended installation or when any of the above properties are specified on the command line.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




