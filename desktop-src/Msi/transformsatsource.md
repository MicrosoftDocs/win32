---
description: Setting this property is like setting the TransformsAtSource policy policy except that the scope is different.
ms.assetid: b78c3757-d969-4684-84b9-b2acfd9f5c82
title: TRANSFORMSATSOURCE property
ms.topic: reference
ms.date: 05/31/2018
---

# TRANSFORMSATSOURCE property

Setting this property is like setting the [TransformsAtSource policy](transformsatsource-policy.md) policy except that the scope is different. Setting TransformsAtSource policy applies to all packages installed by a given user. Setting the **TRANSFORMSATSOURCE** property applies to the package regardless of the users.

## Remarks

Windows Installer interprets the **TRANSFORMSATSOURCE** property as though it were the [**TRANSFORMSSECURE**](transformssecure.md) property. If the @ flag is passed in the [**TRANSFORMS**](transforms.md) property, Windows Installer treats the transforms in the list as [secure-at-source transforms](secure-at-source-transforms.md).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




