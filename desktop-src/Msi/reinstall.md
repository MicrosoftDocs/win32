---
description: The value of the REINSTALL property is a list of features delimited by commas that are to be reinstalled. The features listed must be present in the Feature column of the Feature table. To reinstall all features use REINSTALL=ALL on the command line.
ms.assetid: 14346fef-7923-4f30-bca8-96a29c0f820d
title: REINSTALL property
ms.topic: reference
ms.date: 05/31/2018
---

# REINSTALL property

The value of the **REINSTALL** property is a list of features delimited by commas that are to be reinstalled. The features listed must be present in the Feature column of the [Feature](feature-table.md) table. To reinstall all features use REINSTALL=ALL on the command line.

## Remarks

Note that the feature names are case-sensitive.

If the **REINSTALL** property is set, the [**REINSTALLMODE**](reinstallmode.md) property should also be set, to indicate the type of reinstall to be performed. If the **REINSTALLMODE** property is not set, then by default all files that are currently installed are reinstalled, IF the currently installed file is a lesser version (or is not present). By default, no registry entries are rewritten.

Note that even if **REINSTALL** is set to ALL, only those features that were already installed previously are reinstalled. Thus, if **REINSTALL** is set for a product that is yet to be installed, no installation action will take place at all.

The installer always evaluates the following properties in the following order:

1.  [**ADDLOCAL**](addlocal.md)
2.  [**REMOVE**](remove.md)
3.  [**ADDSOURCE**](addsource.md)
4.  [**ADDDEFAULT**](adddefault.md)
5.  **REINSTALL**
6.  [**ADVERTISE**](advertise.md)
7.  [**COMPADDLOCAL**](compaddlocal.md)
8.  [**COMPADDSOURCE**](compaddsource.md)
9.  [**FILEADDLOCAL**](fileaddlocal.md)
10. [**FILEADDSOURCE**](fileaddsource.md)
11. [**FILEADDDEFAULT**](fileadddefault.md)

For example, if the command line specifies: ADDLOCAL=ALL, ADDSOURCE = MyFeature, all the features are first set to run-local and then MyFeature is set to run-from-source. If the command line is: ADDSOURCE=ALL, ADDLOCAL=MyFeature, first MyFeature is set to run-local, and then when ADDSOURCE=ALL is evaluated, all features (including MyFeature) are reset to run-from-source.

The installer sets the [**Preselected**](preselected.md) property to a value of "1" during the resumption of a suspended installation or when any of the above properties are specified on the command line.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




