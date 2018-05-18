---
title: DefaultSpoolDirectory
description: Provides the name of the spooler folder for the Print Spooler resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c357b3fc-c088-4f13-934c-a49d43aacec0'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["DefaultSpoolDirectory Failover Cluster ,for print spoolers", "DefaultSpoolDirectory Failover Cluster"]
topic_type:
- apiref
api_name:
- DefaultSpoolDirectory
api_type:
- NA
---

# DefaultSpoolDirectory

Provides the name of the spooler folder for the [Print Spooler](print-spooler.md) resource. The following table summarizes the attributes of the **DefaultSpoolDirectory** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read/write](read-write-properties.md)                          |
| Status    | Required                                                         |
| Structure | [**CLUSPROP\_SZ**](clusprop-sz.md)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

The [**CLUSPROP\_SZ\_DECLARE**](clusprop-sz-declare.md) macro creates a [**CLUSPROP\_SZ**](clusprop-sz.md) structure with an array of the correct size.

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
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[Print Spooler Private Properties](print-spooler-private-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](clusprop-sz.md)
</dt> <dt>

[**CLUSPROP\_SZ\_DECLARE**](clusprop-sz-declare.md)
</dt> </dl>

 

 





