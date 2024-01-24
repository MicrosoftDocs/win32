---
description: Setting the DISABLEADVTSHORTCUTS property disables the generation of shortcuts supporting installation-on-demand and advertisement. Setting this property specifies that these shortcuts should instead be replaced by regular shortcuts.
ms.assetid: 1b55ecbe-932f-4f08-98b1-8c5e7a57d2e8
title: DISABLEADVTSHORTCUTS property
ms.topic: reference
ms.date: 05/31/2018
---

# DISABLEADVTSHORTCUTS property

Setting the **DISABLEADVTSHORTCUTS** property disables the generation of shortcuts supporting [installation-on-demand](installation-on-demand.md) and [advertisement](advertisement.md). Setting this property specifies that these shortcuts should instead be replaced by regular shortcuts.

## Default Value

By default, installation-on-demand shortcut generation is enabled.

## Remarks

The shortcuts that support advertisement have the name of a feature, rather than a formatted file path of the form \[\#filekey\], entered in the Target column of the [Shortcut table](shortcut-table.md). If this property is set and the feature is installed, the installer generates a regular shortcut to the feature.

This property is commonly used by administrators for users who roam between environments that do and do not support advertising. This property can be set by a transform, in the administrative stream, or in the [Property table](property-table.md). If it is set using the command line or by a call to [**MsiSetProperty**](/windows/desktop/api/Msiquery/nf-msiquery-msisetpropertya), then it must be reset again during each subsequent installation.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




