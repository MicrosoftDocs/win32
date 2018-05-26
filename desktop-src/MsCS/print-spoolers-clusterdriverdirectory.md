---
title: ClusterDriverDirectory
description: Provides the name of the cluster driver folder for the Print Spooler resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 95c0ab84-4f4f-41e7-b460-64b32ff7fb8f
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ClusterDriverDirectory Failover Cluster ,for print spoolers
- ClusterDriverDirectory Failover Cluster
topic_type:
- apiref
api_name:
- ClusterDriverDirectory
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusterDriverDirectory

Provides the name of the cluster driver folder for the [Print Spooler](print-spooler.md) resource. The following table summarizes the attributes of the **ClusterDriverDirectory** property.



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

The property value portion of a [property list](property-lists.md) entry for **ClusterDriverDirectory** can be set with the following example code.


```C++
WCHAR                szClusterDriverDirData[] = L"C:\\ClusDriverA";
CLUSPROP_SZ_DECLARE( ClusterDriverDirValue, 
                     sizeof( szClusterDriverDirData ) / sizeof( WCHAR ) );

ClusterDriverDirValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_SZ;
ClusterDriverDirValue.cbLength  = sizeof( szClusterDriverDirData );
StringCbCopy( ClusterDriverDirValue.sz, 
              ClusterDriverDirValue.cbLength, 
              szClusterDriverDirData );
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[Print Spooler Private Properties](print-spooler-private-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> <dt>

[**CLUSPROP\_SZ\_DECLARE**](/windows/previous-versions/ClusAPI/nf-clusapi-clusprop_sz_declare?branch=master)
</dt> </dl>

 

 





