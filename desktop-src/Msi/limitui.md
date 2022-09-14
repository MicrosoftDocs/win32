---
description: If the LIMITUI property is set, the user interface (UI) level used when installing the package is restricted to Basic.
ms.assetid: 1a75e66b-958a-4fa8-b13c-ced976c9508e
title: LIMITUI property
ms.topic: reference
ms.date: 05/31/2018
---

# LIMITUI property

If the **LIMITUI** property is set, the user interface (UI) level used when installing the package is restricted to Basic. This property is required in packages that have no authored UI but still contain UI tables such as the [Dialog table](dialog-table.md). For a description of UI levels, see [**MsiSetInternalUI**](/windows/desktop/api/Msi/nf-msi-msisetinternalui)

## Remarks

Installation packages containing the **LIMITUI** property must also contain the [**ARPNOMODIFY**](arpnomodify.md) property. This is required for a user to obtain the correct behavior from the **Add or Remove Programs** in the **Control Panel** utility when attempting to configure a product.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> <dt>

[**MsiSetInternalUI**](/windows/desktop/api/Msi/nf-msi-msisetinternalui)
</dt> <dt>

[**ARPNOMODIFY**](arpnomodify.md)
</dt> </dl>

 

 




