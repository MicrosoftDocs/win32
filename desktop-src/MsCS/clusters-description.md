---
title: Description
description: Stores administrative comments about the cluster. The following table summarizes the attributes of the Description property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 51620f84-c556-4039-8235-496309c7b2c4
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Description Failover Cluster ,for clusters
- Description Failover Cluster
topic_type:
- apiref
api_name:
- Description
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Description

Stores administrative comments about the [*cluster*](c-gly.md#-wolf-cluster-gly). The following table summarizes the attributes of the **Description** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | **NULL**-terminated Unicode string                               |
| Access    | [Read/write](read-write-properties.md)                          |
| Structure | [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_CLUS\_DESC**.

The [**CLUSPROP\_SZ\_DECLARE**](/windows/previous-versions/ClusAPI/nf-clusapi-clusprop_sz_declare?branch=master) macro creates a [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master) structure with an array of the correct size.

## Examples

The property value portion of a [property list](property-lists.md) entry for **Description** can be set with with the following example code:


```C++
WCHAR szDescriptionData[] = L"Cluster description";
CLUSPROP_SZ_DECLARE( DescriptionValue, sizeof( szDescriptionData ) / sizeof( WCHAR ) );
DescriptionValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_SZ;
DescriptionValue.cbLength = sizeof( szDescriptionData );
StringCbCopy( DescriptionValue.sz, DescriptionValue.cbLength, szDescriptionData );
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> <dt>

[**CLUSPROP\_SZ\_DECLARE**](/windows/previous-versions/ClusAPI/nf-clusapi-clusprop_sz_declare?branch=master)
</dt> </dl>

 

 





