---
description: The Installed property is set only if the product is installed per-machine or for the current user.
ms.assetid: 139a6324-58fb-485e-8b3e-c5cf2881d5d1
title: Installed property
ms.topic: reference
ms.date: 05/31/2018
---

# Installed property

The **Installed** property is set only if the product is installed per-machine or for the current user. This property is not set if the product is installed for a different user.

The **Installed** property can be used in conditional expressions to determine whether a product is installed per-computer or for the current user. For example, the property can be used in the conditional column of a sequence table or to differentiate between a first installation and a maintenance installation.

To determine whether the product is installed for a different user, check the [**ProductState**](productstate.md) property.

The value of the [**ProductVersion**](productversion.md) property is the version of the product in string format.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




