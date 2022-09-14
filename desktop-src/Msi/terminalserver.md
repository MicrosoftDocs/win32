---
description: The installer sets the TerminalServer property when the system is a server with Terminal Services.
ms.assetid: 65bc1f73-8b52-4ebb-b408-96123db2176d
title: TerminalServer property
ms.topic: reference
ms.date: 05/31/2018
---

# TerminalServer property

The installer sets the **TerminalServer** property when the system is a server with Terminal Services.

## Default Value

None. The property is undefined when not running on Terminal Services.

## Remarks

The [**RemoteAdminTS**](remoteadmints.md) property can only be set on Microsoft Windows 2000 or later. The **TerminalServer** property can be set on Windows 2000.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> <dt>

[**RemoteAdminTS property**](remoteadmints.md)
</dt> </dl>

 

 




