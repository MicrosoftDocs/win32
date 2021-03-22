---
description: The installer sets the SystemFolder property to the full path of the System folder.
ms.assetid: 23883638-8d3d-4c2a-8ebf-0c306cf01e05
title: SystemFolder property
ms.topic: reference
ms.date: 05/31/2018
---

# SystemFolder property

The installer sets the **SystemFolder** property to the full path of the System folder.

## Remarks

The installer sets this property. For example, on 32-bit Windows the value may be C:\\Windows\\System32. On 64-bit Windows, the value may be C:\\Windows\\SysWow64.

This folder is normally a subdirectory of the Windows folder. However, it resides on a server when configured for Shared Windows.

This folder is local, even when configured for shared Windows.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




