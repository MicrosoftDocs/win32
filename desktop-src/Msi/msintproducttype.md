---
description: The installer sets the MsiNTProductType property for Windows NT, Windows 2000, and later operating systems.
ms.assetid: 6bbc8283-5911-4fbd-8a0f-09c398280e74
title: MsiNTProductType property
ms.topic: reference
ms.date: 05/31/2018
---

# MsiNTProductType property

The installer sets the **MsiNTProductType** property for Windows NT, Windows 2000, and later operating systems. This property indicates the Windows product type.

For Windows 2000 and later operating systems, the installer sets the following values. Note that values are the same as of the **wProductType** field of the [**OSVERSIONINFOEX**](/windows/win32/api/winnt/ns-winnt-osversioninfoexa) structure.



| Value | Meaning                                  |
|-------|------------------------------------------|
| 1     | Windows 2000 Professional and later      |
| 2     | Windows 2000 domain controller and later |
| 3     | Windows 2000 Server and later            |



 

For operating systems earlier than Windows 2000, the installer sets the following values.



| Value | Meaning                      |
|-------|------------------------------|
| 1     | Windows NT Workstation       |
| 2     | Windows NT domain controller |
| 3     | Windows NT Server            |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 
