---
title: Remark
description: Provides a description of the File Share resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5c9fbd24-17b1-4c21-95ae-b39d92be117b
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Remark Failover Cluster ,for file shares
- Remark Failover Cluster
topic_type:
- apiref
api_name:
- Remark
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Remark

\[The **Remark** property is no longer available for use as of Windows Server 2012.\]

This property is not supported.

**Windows Server 2003:  **

Provides a description of the [File Share](file-share.md) [resource](resources.md). The following table summarizes the attributes of the **Remark** property.



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

The property value portion of a [property list](property-lists.md) entry for **Remark** can be set with the following example code.


```C++
WCHAR szRemarkData[] = L"File Share Description";
CLUSPROP_SZ_DECLARE( RemarkValue, 
                     sizeof(szRemarkData) / sizeof(WCHAR) );

RemarkValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_SZ;
RemarkValue.cbLength  =  sizeof( szRemarkData );
StringCbCopy( RemarkValue.sz, RemarkValue.cbLength, szRemarkData );
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

[**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> <dt>

[**CLUSPROP\_SZ\_DECLARE**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusprop_sz_declare)
</dt> </dl>

 

 





