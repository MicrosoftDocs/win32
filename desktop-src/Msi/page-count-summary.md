---
description: The Page Count Summary property contains the minimum installer version required by the installation package.
ms.assetid: ee3aaeed-166c-4591-ae3e-642c1204a5ca
title: Page Count Summary property
ms.topic: reference
ms.date: 05/31/2018
---

# Page Count Summary property

The **Page Count Summary** property contains the minimum installer version required by the installation package. For a minimum of Windows Installer 2.0, this property must be set to the integer 200. For a minimum of Windows Installer 3.0, this property must be set to the integer 300. For a minimum of Windows Installer 3.1, this property must be set to 301. For a minimum of Windows Installer 4.5, this property must be set to 405. For a minimum of Windows Installer 5.0, this property must be set to 500.

For [64-bit Windows Installer Packages](64-bit-windows-installer-packages.md), this property must be set to the integer 200 or greater. For 64-bit Windows Installer Packages on the Arm64 platform, this property must be set to the integer 500 or greater.

For a transform package, the **Page Count Summary** property contains the minimum installer version required to process the transform. Set to the greater of the two **Page Count Summary** property values that belong to the databases used to generate the transform.

For a patch package, the **Page Count Summary** property is set to Null.

This summary property is required.

This property can be used to author a package that can be installed only by the specified minimum or later version of the Windows Installer.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |



## See also

<dl> <dt>

[Summary Property Descriptions](summary-property-descriptions.md)
</dt> </dl>

 

 




