---
description: The ProductInfo property is a read-only property that returns the value of the specified attribute for an installed or published product.
ms.assetid: 144cbba7-ec2b-44cd-acc8-868c210ccebd
title: Installer.ProductInfo property (Oemupgex.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.ProductInfo
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer.ProductInfo property

The **ProductInfo** property is a read-only property that returns the value of the specified attribute for an installed or published product.

This property is read-only.

## Syntax


```JScript
propVal = Installer.ProductInfo
```



## Property value

## Remarks

The **ProductInfo** property ("LocalPackage") does not necessarily return a path to the cached package. Maintenance mode installations should be not be invoked from the LocalPackage. The cached package is for internal uses only.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer 3.0 or later on Windows Server 2003 or Windows XP.<br/> |
| Header<br/>  | <dl> <dt>Oemupgex.h</dt> </dl>                                                                                                                                                                                 |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                                    |
| IID<br/>     | IID\_IInstaller is defined as 000C1090-0000-0000-C000-000000000046<br/>                                                                                                                                                                                         |



## See also

<dl> <dt>

[**MsiGetProductInfo**](/windows/desktop/api/Msi/nf-msi-msigetproductinfoa)
</dt> <dt>

[**MsiGetUserInfo**](/windows/desktop/api/Msi/nf-msi-msigetuserinfoa)
</dt> <dt>

[Not Supported in Windows Installer 2.0 and earlier](not-supported-in-windows-installer-version-2-0.md)
</dt> </dl>

 

 




