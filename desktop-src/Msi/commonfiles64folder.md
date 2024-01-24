---
description: The installer sets the CommonFiles64Folder property to the full path of the predefined 64-bit Common Files folder. The existing CommonFilesFolder property is set to the corresponding 32-bit folder.
ms.assetid: 6730170a-0f73-4a84-b3fb-bd15c72917c7
title: CommonFiles64Folder property
ms.topic: reference
ms.date: 05/31/2018
---

# CommonFiles64Folder property

The installer sets the **CommonFiles64Folder** property to the full path of the predefined 64-bit Common Files folder. The existing [**CommonFilesFolder**](commonfilesfolder.md) property is set to the corresponding 32-bit folder.

## Remarks

The installer sets this property on 64-bit Windows. This property is not used on 32-bit Windows. When using 64-bit Windows, the value may be "C:\\Program Files\\Common Files".

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




