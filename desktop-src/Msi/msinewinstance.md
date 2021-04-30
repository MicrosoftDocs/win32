---
description: The MSINEWINSTANCE property indicates the installation of a new instance of a product with instance transforms.
ms.assetid: 35d41fa9-79d3-4baa-b177-5a32239b5051
title: MSINEWINSTANCE property
ms.topic: reference
ms.date: 05/31/2018
---

# MSINEWINSTANCE property

The **MSINEWINSTANCE** property indicates the installation of a new instance of a product with instance transforms. This property supports multiple instances through product code–changing transforms. The value of this property is 1. The presence of this property on the command line requires that the [**TRANSFORMS**](transforms.md) property also be present. The first transform listed in **TRANSFORMS** must be an instance transform. For more information see, [Installing Multiple Instances of Products and Patches](installing-multiple-instances-of-products-and-patches.md)

This property is available with the installer running a system in the Windows Server 2003 or Windows XP.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> <dt>

[Not Supported in Windows Installer 2.0 and earlier](not-supported-in-windows-installer-version-2-0.md)
</dt> </dl>

 

 




