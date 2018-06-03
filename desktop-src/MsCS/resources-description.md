---
title: Description
description: Provides comments about the resource. The following table summarizes the attributes of the Description property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d9524a90-f533-48cc-9822-f3dc271c026b
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Description Failover Cluster ,for resources
- Description Failover Cluster
topic_type:
- apiref
api_name:
- Description
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Description

Provides comments about the [resource](resources.md). The following table summarizes the attributes of the **Description** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read/write](read-write-properties.md)                          |
| Structure | [**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

The [**CLUSPROP\_SZ\_DECLARE**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusprop_sz_declare) macro creates a [**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/) structure with an array of the correct size.

## Examples

The property value portion of a [property list](property-lists.md) entry for **Description** can be set with the following example code:


```C++
WCHAR szDescriptionData[] = L"Word processing resource";
CLUSPROP_SZ_DECLARE( DescriptionValue, 
                     sizeof( szDescriptionData ) / sizeof( WCHAR ) );
DescriptionValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_SZ;
DescriptionValue.cbLength = sizeof( szDescriptionData );
StringCbCopy( DescriptionValue.sz, 
              DescriptionValue.cbLength, 
              szDescriptionData );
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> <dt>

[**CLUSPROP\_SZ\_DECLARE**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusprop_sz_declare)
</dt> </dl>

 

 





