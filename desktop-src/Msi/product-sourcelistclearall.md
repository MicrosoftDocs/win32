---
description: The SourceListClearAll method the Product object removes all sources for the product. The type of source to remove can be specified.
ms.assetid: c8a63b54-7be6-424a-8653-0182b561faab
title: Product.SourceListClearAll method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Product.SourceListClearAll
api_type: 
- COM
api_location: 
- Msi.dll
---

# Product.SourceListClearAll method

The **SourceListClearAll** method the [**Product**](product-object.md) object removes all sources for the product. The type of source to remove can be specified.

## Syntax


```JScript
Product.SourceListClearAll(
  Type
)
```



## Parameters

<dl> <dt>

*Type* 
</dt> <dd>

Type of source to be removed: MSISOURCETYPE\_MEDIA, MSISOURCETYPE\_NETWORK or MSISOURCETYPE\_URL.

</dd> </dl>

## Return value

This method does not return a value.

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

[**MsiSourceListClearSource**](/windows/desktop/api/Msi/nf-msi-msisourcelistclearsourcea)
</dt> <dt>

[Not Supported in Windows Installer 2.0 and earlier](not-supported-in-windows-installer-version-2-0.md)
</dt> </dl>

 

 




