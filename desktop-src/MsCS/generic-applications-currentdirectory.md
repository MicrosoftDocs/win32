---
title: CurrentDirectory
description: Describes the directory in which the application should be run.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8a06c242-756d-4503-80b4-7b660cb5971c
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CurrentDirectory Failover Cluster ,for generic applications
- CurrentDirectory Failover Cluster
topic_type:
- apiref
api_name:
- CurrentDirectory
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CurrentDirectory

\[The **CurrentDirectory** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Describes the directory in which the application should be run. The following table summarizes the attributes of the **CurrentDirectory** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read/write](read-write-properties.md)                          |
| Status    | Required                                                         |
| Structure | [**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

The path in the **CurrentDirectory** property must be an absolute path on a [*cluster disk*](https://www.bing.com/search?q=*cluster disk*). An environment variable representing a path cannot be used. A dot (.) defaults to the directory in which the [Cluster service](cluster-service.md) is installed.

The [**CLUSPROP\_SZ\_DECLARE**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusprop_sz_declare) macro creates a [**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/) structure with an array of the correct size.

## Examples

The property value portion of a [property list](property-lists.md) entry for **CurrentDirectory** can be set with the following example code.


```C++
WCHAR                szCurrentDirectoryData[] = L"C:\\Bin";
CLUSPROP_SZ_DECLARE( CurrentDirectoryValue, 
                     sizeof(szCurrentDirectoryData) / sizeof(WCHAR) );

CurrentDirectoryValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_SZ;
CurrentDirectoryValue.cbLength  = sizeof( szCurrentDirectoryData );
StringCbCopy( CurrentDirectoryValue.sz, 
              CurrentDirectoryValue.cbLength, 
              szCurrentDirectoryData );
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2003 Enterprise, Windows Server 2003 Datacenter<br/> |
| End of server support<br/>    | Windows Server 2003 Datacenter, Windows Server 2003 Enterprise<br/> |



## See also

<dl> <dt>

[Generic Application Private Properties](generic-application-private-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> <dt>

[**CLUSPROP\_SZ\_DECLARE**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusprop_sz_declare)
</dt> </dl>

 

 





