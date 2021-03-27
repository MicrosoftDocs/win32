---
description: Set the MSIUSEREALADMINDETECTION property to 1 to request that the installer use actual user information when setting the AdminUser property.
ms.assetid: eb0ed6e3-377b-40f4-afee-346a83e310cf
title: MSIUSEREALADMINDETECTION property
ms.topic: reference
ms.date: 05/31/2018
---

# MSIUSEREALADMINDETECTION property

Set the **MSIUSEREALADMINDETECTION** property to 1 to request that the installer use actual user information when setting the [**AdminUser**](adminuser.md) property. When running on Windows Vista, the [**Privileged**](privileged.md) and **AdminUser** are the same. Authors should used the **Privileged** property in new packages. Legacy packages that require distinct **Privileged** and **AdminUser** properties can restore the difference by setting the **MSIUSEREALADMINDETECTION** property.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> <dt>

[Not Supported in Windows Installer 3.1 and earlier versions](not-supported-in-windows-installer-version-3-1.md)
</dt> </dl>

 

 




