---
title: DatabasePath
description: Specifies the path to the WINS database.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d6844d63-282e-4c93-91ba-2fa609cb65b9
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- DatabasePath Failover Cluster ,for the WINS service
- DatabasePath Failover Cluster
topic_type:
- apiref
api_name:
- DatabasePath
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DatabasePath

Specifies the path to the WINS database. The following table summarizes the attributes of the **DatabasePath** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read/write](read-write-properties.md)                          |
| Status    | Required                                                         |
| Structure | [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | %SystemRoot%\\wins\\wins.mdb                                     |



 

## Remarks

Note that the WINS database path includes the file name of the database.

The [**CLUSPROP\_SZ\_DECLARE**](/windows/previous-versions/ClusAPI/nf-clusapi-clusprop_sz_declare?branch=master) macro creates a [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master) structure with an array of the correct size.

## Examples

The property value portion of a [property list](property-lists.md) entry for **DatabasePath** can be set with the following example code.


```C++
WCHAR szDatabasePathData[] = L"\\\\WINS\\DBDirectory\\wins.mdb";
CLUSPROP_SZ_DECLARE( DatabasePathValue, 
                     sizeof( szDatabasePathData ) / sizeof( WCHAR ) );
DatabasePathValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_SZ;
DatabasePathValue.cbLength = sizeof( szDatabasePathData );
StringCbCopy( DatabasePathValue.sz, 
              DatabasePathValue.cbLength, 
              szDatabasePathData );
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[WINS Service Private Properties](wins-service-private-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> <dt>

[**CLUSPROP\_SZ\_DECLARE**](/windows/previous-versions/ClusAPI/nf-clusapi-clusprop_sz_declare?branch=master)
</dt> </dl>

 

 





