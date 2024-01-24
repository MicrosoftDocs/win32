---
description: The value of the REMOVE property is a list of features delimited by commas that are to be removed.
ms.assetid: '39f4609a-7bf8-42b3-b23e-0d6a40b69fd3'
title: REMOVE property
ms.topic: article
ms.date: 05/31/2018
---

# REMOVE property

The value of the **REMOVE** property is a list of features delimited by commas that are to be removed. The features must be present in the Feature column of the [Feature table](feature-table.md). Note that if you use REMOVE=ALL on the command line, the installer removes all features having an install level greater than 0. In this case, the installer does not remove features having an install level of 0. For more information about the install level of features see [Feature table](feature-table.md).

## Remarks

To determine whether a product has been set to be completely uninstalled, a package author may use a conditional expression to check whether REMOVE=ALL. Note that if the product is removed by setting its top feature to absent, the **REMOVE** property may not equal ALL until after the [InstallValidate action](installvalidate-action.md). This means that any custom action that depends upon REMOVE=ALL must be sequenced after the InstallValidate. For more information see also [Conditioning Actions to Run During Removal](conditioning-actions-to-run-during-removal.md). Note that the feature names are case-sensitive.

The installer always evaluates the following properties in the following order:

1.  [**ADDLOCAL**](addlocal.md)
2.  **REMOVE**
3.  [**ADDSOURCE**](addsource.md)
4.  [**ADDDEFAULT**](adddefault.md)
5.  [**REINSTALL**](reinstall.md)
6.  [**ADVERTISE**](advertise.md)
7.  [**COMPADDLOCAL**](compaddlocal.md)
8.  [**COMPADDSOURCE**](compaddsource.md)
9.  [**COMPADDDEFAULT**](compadddefault.md)
10. [**FILEADDLOCAL**](fileaddlocal.md)
11. [**FILEADDSOURCE**](fileaddsource.md)
12. [**FILEADDDEFAULT**](fileadddefault.md)

For example, if the command line specifies ADDLOCAL=ALL, ADDSOURCE = MyFeature, all the features are first set to run-local and then MyFeature is set to run-from-source. If the command line is ADDSOURCE=ALL, ADDLOCAL=MyFeature, first MyFeature is set to run-local, then when ADDSOURCE=ALL is evaluated, all features (including MyFeature) are reset to run-from-source.

The installer sets the [**Preselected**](preselected.md) property to a value of "1" during the resumption of a suspended installation or when any of the above properties are specified on the command line.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




