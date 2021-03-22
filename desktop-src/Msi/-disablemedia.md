---
description: Setting the DISABLEMEDIA property prevents the installer from registering any media source, such as a CD-ROM, as a valid source for the product. If browsing is enabled, however, a user may still browse to a media source.
ms.assetid: 83c4e7f6-fced-447f-bfa2-847dce660139
title: DISABLEMEDIA property
ms.topic: reference
ms.date: 05/31/2018
---

# DISABLEMEDIA property

Setting the [**DISABLEMEDIA**](disablemedia.md) property prevents the installer from registering any media source, such as a CD-ROM, as a valid source for the product. If browsing is enabled, however, a user may still browse to a media source.

## Remarks

Note that the [**DISABLEMEDIA**](disablemedia.md) property has a different effect than setting the DisableMedia policy. Setting **DISABLEMEDIA** prevents the registration of any media source, and this also prevents the first time installation of an application from a media sources.

For details about securing the media sources of [*managed application*](m-gly.md) against browsing and installation by non-administrative users, see [Source Resiliency](source-resiliency.md).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




