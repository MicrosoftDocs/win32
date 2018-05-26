---
title: DatabaseStorage
description: Provides the drive letter where the Internet Storage Name Service (iSNS) resource stores the database. The following table summarizes the attributes of the DatabaseStorage property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e6b48e42-cec0-4ec9-8f33-b60c9d3671de
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- DatabaseStorage Failover Cluster , for iSNS private properties
- DatabaseStorage Failover Cluster
topic_type:
- apiref
api_name:
- DatabaseStorage
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DatabaseStorage

Provides the drive letter where the Internet Storage Name Service (iSNS) [resource](resources.md) stores the database. The following table summarizes the attributes of the **DatabaseStorage** property.



| Attribute            | Value                                              |
|----------------------|----------------------------------------------------|
| Data type<br/> | Null-terminated Unicode string<br/>          |
| Access<br/>    | [Read/write](read-write-properties.md)<br/> |
| Status<br/>    | TBD<br/>                                     |
| Structure<br/> | [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)<br/>     |
| Minimum<br/>   | **NULL**<br/>                                |
| Maximum<br/>   | Z:<br/>                                      |
| Default<br/>   | **NULL**<br/>                                |



 

## Examples

The property value portion of a [property list](property-lists.md) entry for **DatabaseStorage** can be set with the following example code:


```C++
WCHAR                szDatabaseStorageData[] = L"R:";
CLUSPROP_SZ_DECLARE( DatabaseStorageValue, 
                     sizeof(szDatabaseStorageData) / sizeof(WCHAR) );

DatabaseStorageValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_SZ;
DatabaseStorageValue.cbLength  = sizeof( szDatabaseStorageData );
StringCbCopy( DatabaseStorageValue.sz, 
              DatabaseStorageValue.cbLength, 
              szDatabaseStorageData );
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[iSNS Private Properties](isns-private-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> <dt>

[**CLUSPROP\_SZ\_DECLARE**](/windows/previous-versions/ClusAPI/nf-clusapi-clusprop_sz_declare?branch=master)
</dt> </dl>

 

 





