---
description: This Windows Installer property indicates when the internal user interface level has been set to hide the cancel button.
ms.assetid: 0e842bee-32c2-41ae-97f3-bc8b34960a44
title: MsiUIHideCancel property
ms.topic: reference
ms.date: 05/31/2018
---

# MsiUIHideCancel property

The installer sets the **MsiUIHideCancel** property to 1 when the internal user interface level has been set to include INSTALLUILEVEL\_HIDECANCEL with the [**MsiSetInternalUI**](/windows/desktop/api/Msi/nf-msi-msisetinternalui) function or the [UILevel](installer-uilevel.md)property of the [**Installer**](installer-object.md) object or by using [Command Line Options](command-line-options.md).

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer 3.0 or later on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> <dt>

[Not Supported in Windows Installer 2.0 and earlier](not-supported-in-windows-installer-version-2-0.md)
</dt> </dl>

 

 




