---
title: AdminExtensions
description: This property is not supported.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c4589799-0e41-467d-90e1-276e05098698
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- AdminExtensions Failover Cluster , for clusters
- AdminExtensions Failover Cluster
topic_type:
- apiref
api_name:
- AdminExtensions
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AdminExtensions

\[This property is available for use only in Windows Server 2003.\]

This property is not supported.

**Windows Server 2003:  **

The **AdminExtensions** property provides the class identifiers (CLSIDs) for the [Cluster Administrator](cluster-administrator.md) extensions that are associated with the [*cluster*](https://www.bing.com/search?q=*cluster*). The following table summarizes the attributes of the **AdminExtensions** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | **LPCWSTR** pointer or a **WCHAR** array                         |
| Access    | [Read/write](read-write-properties.md)                          |
| Structure | [**CLUSPROP\_MULTI\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_sz)                 |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

The data value for the **AdminExtensions** property should be set to one or more class identifiers, formatted as a sequence of null-terminated Unicode strings with the entire sequence terminated by an additional **NULL**.

## Examples

The property value portion of a [property list](property-lists.md) entry for **AdminExtensions** can be set with the following example code.


```C++
WCHAR szAdmExData[] = L"{4EC90FB0-D0BB-11CF-B5EF-00A0C90AB505}\0"
                      L"{806EA659-39DC-4BC9-B9DE-B44B671F0236}\0"
                      L"{7904197E-F39E-4458-8848-A56CA675EE4D}\0";

CLUSPROP_SZ_DECLARE( AdmExValue, sizeof( szAdmExData ) / sizeof( WCHAR ) );

AdmExValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_MULTI_SZ;
AdmExValue.cbLength  = sizeof( szAdmExData );
CopyMemory( (PVOID) AdmExValue.sz, 
            (PVOID) szAdmExData, 
            sizeof( szAdmExData ) );
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2003 Enterprise, Windows Server 2003 Datacenter<br/> |
| End of server support<br/>    | Windows Server 2003 Datacenter, Windows Server 2003 Enterprise<br/> |



## See also

<dl> <dt>

[**CLUSPROP\_MULTI\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_sz)
</dt> </dl>

 

 





