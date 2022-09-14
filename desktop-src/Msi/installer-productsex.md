---
description: Returns a RecordList object that enumerates the list of products.
ms.assetid: 30735b9f-091b-4915-9b07-9688c9be2d26
title: Installer.ProductsEx property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.ProductsEx
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer.ProductsEx property

The **ProductsEx** property returns a [**RecordList**](recordlist-object.md) object that enumerates the list of products. This property calls [**MsiEnumProductsEx**](/windows/desktop/api/Msi/nf-msi-msienumproductsexa).

This property is read-only.

## Syntax


```JScript
propVal = Installer.ProductsEx
```



## Property value

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer 3.0 or later on Windows Server 2003 or Windows XP.<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                                    |
| IID<br/>     | IID\_IInstaller is defined as 000C1090-0000-0000-C000-000000000046<br/>                                                                                                                                                                                         |



## See also

<dl> <dt>

[**Installer**](installer-object.md)
</dt> <dt>

[**MsiEnumProductsEx**](/windows/desktop/api/Msi/nf-msi-msienumproductsexa)
</dt> <dt>

[**Product**](product-object.md)
</dt> <dt>

[Not Supported in Windows Installer 2.0 and earlier](not-supported-in-windows-installer-version-2-0.md)
</dt> </dl>

 

 




