---
description: The SourceListClearSource method removes a network or URL source. Accepts Type, the source type, and SourcePath, the source path, as parameters to be removed. This method calls the MsiSourceListClearSource.
ms.assetid: a55676d4-795d-4ffe-8621-ef47c16a936c
title: Product.SourceListClearSource method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Product.SourceListClearSource
api_type: 
- COM
api_location: 
- Msi.dll
---

# Product.SourceListClearSource method

The **SourceListClearSource** method removes a network or URL source. Accepts *Type*, the source type, and *SourcePath*, the source path, as parameters to be removed. This method calls the [**MsiSourceListClearSource**](/windows/desktop/api/Msi/nf-msi-msisourcelistclearsourcea).

## Syntax


```JScript
Product.SourceListClearSource(
  Type,
  SourcePath
)
```



## Parameters

<dl> <dt>

*Type* 
</dt> <dd>

Type of source to be removed: MSISOURCETYPE\_NETWORK or MSISOURCETYPE\_URL.

</dd> <dt>

*SourcePath* 
</dt> <dd>

Path to the source to be removed.

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

 

 




