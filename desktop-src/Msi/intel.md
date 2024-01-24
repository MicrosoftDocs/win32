---
description: The Intel property is set by the Windows Installer to the numeric processor level when running on an Intel processor.
ms.assetid: c1190df2-0440-4dd1-bce5-61d899f71437
title: Intel property
ms.topic: reference
ms.date: 05/31/2018
---

# Intel property

The **Intel** property is set by the Windows Installer to the numeric processor level when running on an Intel processor. The values are the same as the *wProcessorLevel* field of the [**SYSTEM\_INFO**](/windows/win32/api/sysinfoapi/ns-sysinfoapi-system_info) structure. When running on a x64 processor, the Windows Installer sets the **Intel** property to reflect the x86 processor emulated by the x64 computer as reported by the operating system.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 
