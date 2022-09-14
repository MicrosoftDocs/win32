---
description: The Context property returns the context of this product.
ms.assetid: aa772a95-eb4e-45af-9788-9833d62139e8
title: Product.Context property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Product.Context
api_type: 
- COM
api_location: 
- Msi.dll
---

# Product.Context property

The **Context** property returns the context of this product.

This property is read-only.

## Syntax


```JScript
propVal = Product.Context
```



## Property value

## Remarks

This property can return one of the following values.



| Context                        | Value | Meaning                           |
|--------------------------------|-------|-----------------------------------|
| MSIINSTALLCONTEXT\_USERMANAGED | 1     | Products under managed context.   |
| MSIINSTALLCONTEXT\_USER        | 2     | Products under unmanaged context. |
| MSIINSTALLCONTEXT\_MACHINE     | 4     | Products under machine context.   |



 

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

 

 




