---
description: The installer sets the MsiTabletPC property to a nonzero value if the current operating system is Windows XP Tablet PC Edition.
ms.assetid: b178a98e-b6f8-4ff8-b554-e47c3b39f892
title: MsiTabletPC property
ms.topic: reference
ms.date: 05/31/2018
---

# MsiTabletPC property

The installer sets the **MsiTabletPC** property to a nonzero value if the current operating system is Windows XP Tablet PC Edition. The installer uses the [**GetSystemMetrics**](/windows/win32/api/winuser/nf-winuser-getsystemmetrics) function with **SM\_TABLETPC**, and the property receives the nonzero value returned by this function. If the current system is not Windows XP Tablet PC Edition, the **GetSystemMetrics** function returns zero and the installer does not set this property.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer 4.5 on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> <dt>

[Not Supported in Windows Installer 3.1 and earlier versions](not-supported-in-windows-installer-version-3-1.md)
</dt> </dl>

 

 
