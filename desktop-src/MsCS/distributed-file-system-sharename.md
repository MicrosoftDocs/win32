---
title: ShareName
description: Name of the Distributed File System resources present on the network.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: cd79be7c-3704-483a-be4c-53aaa886b982
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ShareName Failover Cluster ,for file system
- ShareName Failover Cluster
topic_type:
- apiref
api_name:
- ShareName
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ShareName

Describes the name of the Distributed File System resources present on the [network](networks.md). The following table summarizes the attributes of the **ShareName** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read/write](read-write-properties.md)                          |
| Status    | Required                                                         |
| Structure | [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

All **ShareName** values within a given cluster must be unique.

The [**CLUSPROP\_SZ\_DECLARE**](/windows/previous-versions/ClusAPI/nf-clusapi-clusprop_sz_declare?branch=master) macro creates a [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master) structure with an array of the correct size.

## Examples

The property value portion of a [property list](property-lists.md) entry for **ShareName** can be set with the following example code.


```C++
WCHAR                szShareNameData[]  = L"Sharename";
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
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[Distributed File System Private Properties](distributed-file-system-private-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> <dt>

[**CLUSPROP\_SZ\_DECLARE**](/windows/previous-versions/ClusAPI/nf-clusapi-clusprop_sz_declare?branch=master)
</dt> </dl>

 

 





