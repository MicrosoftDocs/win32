---
description: The installer sets the System64Folder property to the full path to the predefined System64 folder. The existing System64Folder property is set to the corresponding 32-bit folder.
ms.assetid: ce25c95e-cff5-44ec-81cb-b3104fb9b987
title: System64Folder property
ms.topic: reference
ms.date: 05/31/2018
---

# System64Folder property

The installer sets the **System64Folder** property to the full path to the predefined System64 folder. The existing **System64Folder** property is set to the corresponding 32-bit folder.

## Remarks

The installer sets this property on 64-bit Windows. For example, on 64-bit Windows, the value may be C:\\Window\\System32. This property is not used on 32-bit Windows.

This folder is normally a subdirectory of the Windows folder. However, it resides on a server when configured for Shared Windows.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




