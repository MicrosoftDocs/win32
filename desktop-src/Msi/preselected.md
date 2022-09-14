---
description: The Preselected property indicates that features have already been selected and that the selection dialog need not be shown.Conditional expressions which depend on whether features are already installed use this value.
ms.assetid: 2bbab8b9-084a-4515-904c-d556d183d06e
title: Preselected property
ms.topic: reference
ms.date: 05/31/2018
---

# Preselected property

The **Preselected** property indicates that features have already been selected and that the selection dialog need not be shown.

Conditional expressions which depend on whether features are already installed use this value. For example, the property can be used to suppress any dialogs involving feature selections during the resumption of a suspended installation.

The installer sets the **Preselected** property to a value of "1" during the resumption of a suspended installation or when any of the following properties are specified on the command line. If the **Preselected** property has been set to 1, the installer does not use the [Condition table](condition-table.md) to evaluate the selection of features. Features are installed based upon the following properties. The installer always evaluates these properties in the following order:

1.  [**ADDLOCAL**](addlocal.md)
2.  [**REMOVE**](remove.md)
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

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




