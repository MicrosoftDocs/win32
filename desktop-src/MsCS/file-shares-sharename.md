---
title: ShareName
description: Describes the name of the file share present on the network.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '51a6fbda-8017-4877-bf57-2db6da9abf1a'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["ShareName Failover Cluster ,for file shares", "ShareName Failover Cluster"]
topic_type:
- apiref
api_name:
- ShareName
api_type:
- NA
---

# ShareName

\[The **ShareName** property is no longer available for use as of Windows Server 2012.\]

This property is not supported.

**Windows Server 2003:  **

Describes the name of the [file share](file-share.md) present on the [network](networks.md). The following table summarizes the attributes of the **ShareName** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read/write](read-write-properties.md)                          |
| Status    | Required                                                         |
| Structure | [**CLUSPROP\_SZ**](clusprop-sz.md)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

All **ShareName** values within a given cluster must be unique.

The [**CLUSPROP\_SZ\_DECLARE**](clusprop-sz-declare.md) macro creates a [**CLUSPROP\_SZ**](clusprop-sz.md) structure with an array of the correct size.

## Examples

The property value portion of a [property list](property-lists.md) entry for **ShareName** can be set with the following example code.


```C++
WCHAR szShareNameData[]  = L"Sharename";
CLUSPROP_SZ_DECLARE( ShareNameValue, 
                     sizeof( szShareNameData ) / sizeof( WCHAR ) );

ShareNameValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_SZ;
ShareNameValue.cbLength  = sizeof( szShareNameData );
StringCbCopy( ShareNameValue.sz, ShareNameValue.cbLength, szShareNameData );
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2003 Enterprise, Windows Server 2003 Datacenter<br/> |
| End of server support<br/>    | Windows Server 2003 Datacenter, Windows Server 2003 Enterprise<br/> |



## See also

<dl> <dt>

[File Share Private Properties](file-share-private-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](clusprop-sz.md)
</dt> <dt>

[**CLUSPROP\_SZ\_DECLARE**](clusprop-sz-declare.md)
</dt> </dl>

 

 





