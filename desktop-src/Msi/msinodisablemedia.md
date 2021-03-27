---
description: Set the MSINODISABLEMEDIA property to prevent the installer from setting the DISABLEMEDIA property. Setting the DISABLEMEDIA property prevents the installer from registering any media source, such as a CD-ROM, as a valid source for the product.
ms.assetid: 4e1450aa-bf89-4d44-b463-4016660f5508
title: MSINODISABLEMEDIA property
ms.topic: reference
ms.date: 05/31/2018
---

# MSINODISABLEMEDIA property

Set the **MSINODISABLEMEDIA** property to prevent the installer from setting the [**DISABLEMEDIA**](-disablemedia.md) property. Setting the **DISABLEMEDIA** property prevents the installer from registering any media source, such as a CD-ROM, as a valid source for the product.

When **MSINODISABLEMEDIA** is not set, the installer might add [**DISABLEMEDIA**](-disablemedia.md) to the administrative property stream when performing an [administrative installation](administrative-installation.md). This prevents users who install from the administrative image from ever installing from media, such as a CD-ROM.

-   When performing an administrative installation, the installer only adds [**DISABLEMEDIA**](-disablemedia.md) to the administrative property stream if the [**Page Count Summary**](page-count-summary.md) Property is less than 150.

If [**DISABLEMEDIA**](-disablemedia.md) is listed in the [**AdminProperties**](adminproperties.md) property, setting **MSINODISABLEMEDIA** prevents **DISABLEMEDIA** from being set during an administrative installation. In this case, the installer may register a media source and a user could then have the option to reinstall from the media source if the original administrative installation image became unavailable later.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003, Windows XP, and Windows 2000. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




