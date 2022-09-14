---
description: The value of the COMPADDLOCAL property is a list of component GUIDs from the ComponentId column of the Component table, delimited by commas, that are to be installed locally.
ms.assetid: 10c178c5-1eae-4191-b79c-9285810efb6a
title: COMPADDLOCAL property
ms.topic: reference
ms.date: 05/31/2018
---

# COMPADDLOCAL property

The value of the **COMPADDLOCAL** property is a list of component GUIDs from the ComponentId column of the [Component table](component-table.md), delimited by commas, that are to be installed locally. The installer uses this list to determine which features are set to be installed locally, based on the specified components. For each listed component ID, the installer examines all features linked to that component through the [FeatureComponents](featurecomponents-table.md) table, and installs the feature that requires the least amount of disk space to install. The components listed must be present in the Component column of the [Component](component-table.md) table.

## Remarks

Note that the component names are case-sensitive. Also note that if the SourceOnly bit flag is set in the Attributes column of the [Component](component-table.md) table for a component, then the component is installed to run from source.

The installer always evaluates the following properties in the following order.

1.  [**ADDLOCAL**](addlocal.md)
2.  [**REMOVE**](remove.md)
3.  [**ADDSOURCE**](addsource.md)
4.  [**ADDDEFAULT**](adddefault.md)
5.  [**REINSTALL**](reinstall.md)
6.  [**ADVERTISE**](advertise.md)
7.  **COMPADDLOCAL**
8.  [**COMPADDSOURCE**](compaddsource.md)
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

 

 




