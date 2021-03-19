---
description: The presence of the MSIINSTANCEGUID property indicates that a product code&\#8211;changing transform is registered to the product.
ms.assetid: c39be15d-e10a-4055-bd81-aa7510a19fe4
title: MSIINSTANCEGUID property
ms.topic: reference
ms.date: 05/31/2018
---

# MSIINSTANCEGUID property

The presence of the **MSIINSTANCEGUID** property indicates that a product code–changing transform is registered to the product. The value of the **MSIINSTANCEGUID** property specifies which instance of a product is to be used for installation. The **MSIINSTANCEGUID** property can only reference a product that has already been installed with an instance transform.

Instance transforms are product code–changing transforms available with the installer running on either Windows Server 2003 or Windows XP. For more information, see [Installing Multiple Instances of Products and Patches](installing-multiple-instances-of-products-and-patches.md).

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

 

 




