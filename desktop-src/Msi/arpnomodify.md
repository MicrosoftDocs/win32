---
description: Setting the ARPNOMODIFY property disables Add or Remove Programs functionality in Control Panel that modifies the product.
ms.assetid: dc804910-cf15-4f9e-863f-78dcac248717
title: ARPNOMODIFY property
ms.topic: reference
ms.date: 05/31/2018
---

# ARPNOMODIFY property

Setting the **ARPNOMODIFY** property disables Add or Remove Programs functionality in Control Panel that modifies the product. For Windows 2000, this disables the **Modify** button for the product in **Add or Remove Programs** in **Control Panel**. On earlier operating systems, clicking the **Add or Remove Programs** button uninstalls the product rather than entering the maintenance mode wizard.

If the **ARPNOMODIFY** property is set, the [RegisterProduct action](registerproduct-action.md) writes the value "NoModify" under the registry key:

**HKLM**\\**Software**\\**Microsoft**\\**Windows**\\**CurrentVersion**\\**Uninstall**\\**{*product key*}**

If the **ARPNOMODIFY** property is set and the [**ARPNOREMOVE**](arpnoremove.md) property is not set, the RegisterProduct action also writes the UninstallString value under this key. The UnistallString value is a command line for removing the product, rather than reconfiguring the product.

## Remarks

On Windows 2000, this disables the **Change** button for the product in the **Add or Remove Programs** of the **Control Panel**.

This property can be set by a customization transform to prevent users from changing an administrator's customization through **Add or Remove Programs**. This property only affects **Add or Remove Programs**.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> <dt>

[A Customization Transform Example](a-customization-transform-example.md)
</dt> </dl>

 

 




