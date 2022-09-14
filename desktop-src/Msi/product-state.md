---
description: The State property returns the installation state of this instance of the product.
ms.assetid: ae4c7a43-d4af-4e06-a3f8-d7c2d0715d84
title: Product.State property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Product.State
api_type: 
- COM
api_location: 
- Msi.dll
---

# Product.State property

The **State** property returns the installation state of this instance of the product.

This property is read-only.

## Syntax


```JScript
propVal = Product.State
```



## Property value

## Remarks

This property returns one of the following values.



| Installation State       | Meaning                                |
|--------------------------|----------------------------------------|
| INSTALLSTATE\_DEFAULT    | Instance of product installed locally. |
| INSTALLSTATE\_ADVERTISED | Instance of product advertised.        |
| INSTALLSTATE\_UNKNOWN    | Instance of product unknown.           |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer 3.0 or later on Windows Server 2003, Windows XP, and Windows 2000<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                                                   |
| IID<br/>     | IID\_IProduct is defined as 000C10A0-0000-0000-C000-000000000046<br/>                                                                                                                                                                                                          |



## See also

<dl> <dt>

[**Product**](product-object.md)
</dt> <dt>

[Not Supported in Windows Installer 2.0 and earlier](not-supported-in-windows-installer-version-2-0.md)
</dt> </dl>

 

 




