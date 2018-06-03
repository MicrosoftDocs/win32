---
title: CurrentDirectory
description: Describes the directory in which the script should be run.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 59b31cbe-c4d8-4764-9793-6ebda3ae6094
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CurrentDirectory Failover Cluster ,for generic scripts
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

\[This property is no longer available for use as of Windows Server 2012.\]

This property is not supported.

**Windows Server 2008 R2 and Windows Server 2008:  **

Describes the directory in which the script should be run. The following table summarizes the attributes of the **CurrentDirectory** property.



| Attribute            | Value                                                                     |
|----------------------|---------------------------------------------------------------------------|
| Data type<br/> | Null-terminated Unicode string<br/>                                 |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>                        |
| Status<br/>    | Required<br/>                                                       |
| Structure<br/> | [**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/)<br/>                            |
| Minimum<br/>   | **NULL**<br/>                                                       |
| Maximum<br/>   | None (but see [Maximum String Size](maximum-string-size.md)).<br/> |
| Default<br/>   | **NULL**<br/>                                                       |



 

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



|                                     |                                                                                 |
|-------------------------------------|---------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                       |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/>       |
| End of client support<br/>    | None supported<br/>                                                       |
| End of server support<br/>    | Windows Server 2008 R2 Datacenter, Windows Server 2008 R2 Enterprise<br/> |



## See also

<dl> <dt>

[Generic Script Private Properties](generic-script-private-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> <dt>

[**CLUSPROP\_SZ\_DECLARE**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusprop_sz_declare)
</dt> </dl>

 

 





