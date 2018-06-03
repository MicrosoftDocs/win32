---
title: StartupParameters
description: Describes the command-line to pass to the Generic Service when it is started.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: bd980fa4-28a0-4e4c-b384-1076f9158770
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- StartupParameters Failover Cluster ,for generic services
- StartupParameters Failover Cluster
topic_type:
- apiref
api_name:
- StartupParameters
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# StartupParameters

Describes the command-line to pass to the [Generic Service](generic-service.md) when it is started. The following table summarizes the attributes of the **StartupParameters** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read/write](read-write-properties.md)                          |
| Status    | Optional                                                         |
| Structure | [**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

The [**CLUSPROP\_SZ\_DECLARE**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusprop_sz_declare) macro creates a [**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/) structure with an array of the correct size.

## Examples

The property value portion of a [property list](property-lists.md) entry for **StartupParameters** can be set with the following example code.


```C++
WCHAR szStartupParametersData[] = L"PARAM1,PARAM2";
CLUSPROP_SZ_DECLARE( StartupParametersValue, 
                     sizeof(szStartupParametersData) / sizeof(WCHAR) );
StartupParametersValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_SZ;
StartupParametersValue.cbLength = sizeof( szStartupParametersData );
StringCbCopy( StartupParametersValue.sz, 
              StartupParametersValue.cbLength, 
              szStartupParametersData );
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[Generic Service Private Properties](generic-service-private-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> <dt>

[**CLUSPROP\_SZ\_DECLARE**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusprop_sz_declare)
</dt> </dl>

 

 





