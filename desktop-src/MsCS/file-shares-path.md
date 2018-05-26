---
title: Path
description: Describes the path to the directory being shared.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 340f7ebc-d9d3-4cf8-9dd4-b0ec6fe6b4a4
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Path Failover Cluster ,for file shares
- Path Failover Cluster
topic_type:
- apiref
api_name:
- Path
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Path

\[The **Path** property is no longer available for use as of Windows Server 2012.\]

This property is not supported.

**Windows Server 2003:  **

Describes the path to the directory being shared. The following table summarizes the attributes of the **Path** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read/write](read-write-properties.md)                          |
| Status    | Required                                                         |
| Structure | [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

The [**CLUSPROP\_SZ\_DECLARE**](/windows/previous-versions/ClusAPI/nf-clusapi-clusprop_sz_declare?branch=master) macro creates a [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master) structure with an array of the correct size.

## Examples

The property value portion of a [property list](property-lists.md) entry for **Path** can be set with the following example code.


```C++
WCHAR szPathData[] = L"G:\\ShareDirectory";
CLUSPROP_SZ_DECLARE( PathValue, 
                     sizeof(szPathData) / sizeof(WCHAR) );

PathValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_SZ;
PathValue.cbLength  = sizeof( szPathData );
StringCbCopy( PathValue.sz, PathValue.cbLength, szPathData );
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2003 Enterprise, Windows Server 2003 Datacenter<br/> |
| End of server support<br/>    | Windows Server 2003 Datacenter, Windows Server 2003 Enterprise<br/> |



## See also

<dl> <dt>

[File Share Private Properties](file-share-private-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> <dt>

[**CLUSPROP\_SZ\_DECLARE**](/windows/previous-versions/ClusAPI/nf-clusapi-clusprop_sz_declare?branch=master)
</dt> </dl>

 

 





