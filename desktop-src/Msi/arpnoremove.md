---
description: Setting the ARPNOREMOVE property disables the Add or Remove Programs functionality in Control Panel that removes the product.
ms.assetid: f86c1af8-c984-4075-9c6b-0a71000b01a1
title: ARPNOREMOVE property
ms.topic: reference
ms.date: 05/31/2018
---

# ARPNOREMOVE property

Setting the **ARPNOREMOVE** property disables the **Add or Remove Programs** functionality in **Control Panel** that removes the product. For Windows 2000, this disables the **Remove** button for the product from the **Add or Remove Programs** in **Control Panel**. For earlier operating systems, this has the effect of removing the product from the list of installed products on the **Add or Remove Programs** in **Control Panel**.

If the **ARPNOREMOVE** property is set, the [RegisterProduct action](registerproduct-action.md) writes the value "NoRemove" under the registry key:

**HKLM**\\**Software**\\**Microsoft**\\**Windows**\\**CurrentVersion**\\**Uninstall**\\**{*product key*}**

Setting the **ARPNOREMOVE** property prevents the UninstallString value from being written under this key. The UnistallString value is a command line for removing the product, rather than reconfiguring the product.

## Remarks

For example, this property can be set during a customization transform to prevent users from removing an administrator customization.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 or later on Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




