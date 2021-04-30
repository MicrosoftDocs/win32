---
description: The MSIFASTINSTALL property can be used to reduce the time required to install a large Windows Installer package.
ms.assetid: 011668da-da04-4b80-989e-192b0daa3060
title: MSIFASTINSTALL property
ms.topic: reference
ms.date: 05/31/2018
---

# MSIFASTINSTALL property

The **MSIFASTINSTALL** property can be used to reduce the time required to install a large Windows Installer package. The property can be set on the command line or in the [Property](property-table.md) table to configure operations that the user or developer determines are non-essential for the installation.

The value of the **MSIFASTINSTALL** property can be a combination of the following values.



| Value | Meaning                                                                      |
|-------|------------------------------------------------------------------------------|
| 0     | Default value                                                                |
| 1     | No system restore point is saved for this installation.                      |
| 2     | Perform only [File Costing](file-costing.md) and skip checking other costs. |
| 4     | Reduce the frequency of progress messages.                                   |



 

**[Windows Installer 4.5 or earlier](not-supported-in-windows-installer-4-5.md):** Not supported. This property is available beginning with Windows Installer 5.0.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



 

 




