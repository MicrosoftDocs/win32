---
title: DefaultSpoolDirectory
description: Provides the name of the spooler folder for the Print Spooler resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c357b3fc-c088-4f13-934c-a49d43aacec0
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- DefaultSpoolDirectory Failover Cluster ,for print spoolers
- DefaultSpoolDirectory Failover Cluster
topic_type:
- apiref
api_name:
- DefaultSpoolDirectory
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DefaultSpoolDirectory

Provides the name of the spooler folder for the [Print Spooler](print-spooler.md) resource. The following table summarizes the attributes of the **DefaultSpoolDirectory** property.



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

The property value portion of a [property list](property-lists.md) entry for **DefaultSpoolDirectory** can be set with the following example code.


```C++
WCHAR                szDefaultSpoolDirData[] = L"C:\\ClusSpoolA";
CLUSPROP_SZ_DECLARE( DefaultSpoolDirValue, 
                     sizeof( szDefaultSpoolDirData ) / sizeof( WCHAR ) );

DefaultSpoolDirValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_SZ;
DefaultSpoolDirValue.cbLength  = sizeof( szDefaultSpoolDirData );
StringCbCopy( DefaultSpoolDirValue.sz, 
              DefaultSpoolDirValue.cbLength, 
              szDefaultSpoolDirData );
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[Print Spooler Private Properties](print-spooler-private-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> <dt>

[**CLUSPROP\_SZ\_DECLARE**](/windows/previous-versions/ClusAPI/nf-clusapi-clusprop_sz_declare?branch=master)
</dt> </dl>

 

 





