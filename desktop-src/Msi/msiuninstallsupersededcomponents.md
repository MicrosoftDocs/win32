---
description: Set the MSIUNINSTALLSUPERSEDEDCOMPONENTS property to 1 in the Property table or on a command line.
ms.assetid: ba9b1b2d-1667-48c8-8f1a-9958a1d170da
title: MSIUNINSTALLSUPERSEDEDCOMPONENTS property
ms.topic: reference
ms.date: 05/31/2018
---

# MSIUNINSTALLSUPERSEDEDCOMPONENTS property

Set the **MSIUNINSTALLSUPERSEDEDCOMPONENTS** property to 1 in the [Property table](property-table.md) or on a command line. When this property has been set to 1, the installer determines whether the components in any superseded patches are becoming redundant. The installer can unregister and uninstall redundant components to prevent leaving behind orphan components on the computer.

Setting this property affects the components in all patches being superseded. To enable this functionality for single components, use the **msidbComponentAttributesUninstallOnSupersedence** attribute in the [Component table](component-table.md).

**[Windows Installer 4.0 and earlier](not-supported-in-windows-installer-4-0.md):** Not supported. Versions earlier than Windows Installer 4.5 ignore the **MSIUNINSTALLSUPERSEDEDCOMPONENTS** Property.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.5 or Windows Installer 4.5 on Windows Vista, Windows XP, Windows Server 2003, and Windows Server 2008. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




