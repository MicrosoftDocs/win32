---
description: The SourceListAddSource method adds a network or URL source. Accepts SourcePath,Type, and Index as parameters. This method calls MsiSourceListAddSourceEx.
ms.assetid: 61a8873f-c4ad-43d7-8bbb-5a2534ef2de7
title: Product.SourceListAddSource method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Product.SourceListAddSource
api_type: 
- COM
api_location: 
- Msi.dll
---

# Product.SourceListAddSource method

The **SourceListAddSource** method adds a network or URL source. Accepts *SourcePath*,*Type*, and *Index* as parameters. This method calls [**MsiSourceListAddSourceEx**](/windows/desktop/api/Msi/nf-msi-msisourcelistaddsourceexa).

## Syntax


```JScript
Product.SourceListAddSource(
  Type,
  SourcePath,
  Index
)
```



## Parameters

<dl> <dt>

*Type* 
</dt> <dd>

Type of source to be added: MSISOURCETYPE\_NETWORK or MSISOURCETYPE\_URL.

</dd> <dt>

*SourcePath* 
</dt> <dd>

Path to the source to be added.

</dd> <dt>

*Index* 
</dt> <dd>

If **SourceListAddSource** is called with a new source and *Index* is set to 0, the installer adds the source to the end of the source list.

If this function is called with a source already existing in the source list and *Index* is set to 0, the installer retains the source's existing index.

If the function is called with an existing source in the source list and *Index* is set to a non-zero value, the source is removed from its current location in the list and inserted at the position specified by *Index*, before any source that already exists at that position.

If the function is called with a new source and *Index* is set to a non-zero value, the source is inserted at the position specified by *Index*, before any source that already exists at that position. The index value for all sources in the list after the index specified by *Index* are updated to ensure unique index values and the pre-existing order is guaranteed to remain unchanged.

If *Index* is greater than the number of sources in the list, the source is placed at the end of the list with an index value one larger than any existing source.

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

[**MsiSourceListAddSourceEx**](/windows/desktop/api/Msi/nf-msi-msisourcelistaddsourceexa)
</dt> <dt>

[Not Supported in Windows Installer 2.0 and earlier](not-supported-in-windows-installer-version-2-0.md)
</dt> </dl>

 

 




