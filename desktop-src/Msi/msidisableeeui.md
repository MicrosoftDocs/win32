---
description: To disable the embedded user interface for the installation defined in the MsiEmbeddedUI table, set the MSIDISABLEEEUI property to 1 on the command line.
ms.assetid: c5ada690-c5dd-455f-babe-8c09750525c4
title: MSIDISABLEEEUI property
ms.topic: reference
ms.date: 05/31/2018
---

# MSIDISABLEEEUI property

To disable the embedded user interface for the installation defined in the [MsiEmbeddedUI table](msiembeddedui-table.md), set the MSIDISABLEEEUI property to 1 on the command line.

**[Windows Installer 4.0 and earlier](not-supported-in-windows-installer-4-0.md):** Not supported. Versions earlier than Windows Installer 4.5 ignore the MSIDISABLEEEUI Property.

## Remarks

In a multiple-package installation, a child package should typically use the user interface of the parent package and not initialize its own embedded UI. If the MSIDISABLEEEUI property is not set inside the parent package, the child package uses the embedded UI of the parent package by default and ignores the MSIDISABLEEEUI property within the child package.

The MSIDISABLEEEUI property disables the embedded user interface for a single package. You can use the [MsiDisableEmbeddedUI](msidisableembeddedui.md) policy to disable embedded user interfaces for all packages on the computer.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.5 on Windows Server 2008, Windows Vista, Windows Server 2003, and Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




