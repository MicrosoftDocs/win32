---
description: The value of the COMPADDDEFAULT property is a list of component GUIDs from the ComponentId column of the Component table, delimited by commas, that are installed in their default configuration.
ms.assetid: 1bf05680-fcba-4fbb-8f8c-4203a90346ce
title: COMPADDDEFAULT property
ms.topic: reference
ms.date: 05/31/2018
---

# COMPADDDEFAULT property

The value of the **COMPADDDEFAULT** property is a list of component GUIDs from the ComponentId column of the [Component table](component-table.md), delimited by commas, that are installed in their default configuration. For each component ID in the list, the installer installs the feature that requires the least disk space. The component IDs in the list must be present in the ComponentId column of the [Component table](component-table.md). A feature is installed in the same installation state as if the user had requested an installation-on-demand of the feature. The state is determined by which bits are set for the feature in the Attributes column of the [Feature table](feature-table.md), and which bits are set for the feature's components in the Attributes column of the Component table.

## Remarks

Note that if the SourceOnly bit flag is set in the Attributes column of the [Component](component-table.md) table for a component, then the component is installed to run from source.

The installer always evaluates the following properties in the following order.

1.  [**ADDLOCAL**](addlocal.md)
2.  [**REMOVE**](remove.md)
3.  [**ADDSOURCE**](addsource.md)
4.  [**ADDDEFAULT**](adddefault.md)
5.  [**REINSTALL**](reinstall.md)
6.  [**ADVERTISE**](advertise.md)
7.  [**COMPADDLOCAL**](compaddlocal.md)
8.  [**COMPADDSOURCE**](compaddsource.md)
9.  **COMPADDDEFAULT**
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

 

 




