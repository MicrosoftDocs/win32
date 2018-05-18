---
title: BackupPath
description: Specifies the path to the WINS backup file.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '16bbe0b6-1677-4bdd-9052-298d22aea68f'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["BackupPath Failover Cluster ,for the WINS service", "BackupPath Failover Cluster"]
topic_type:
- apiref
api_name:
- BackupPath
api_type:
- NA
---

# BackupPath

Specifies the path to the WINS backup file. The following table summarizes the attributes of the **BackupPath** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read/write](read-write-properties.md)                          |
| Status    | Required                                                         |
| Structure | [**CLUSPROP\_SZ**](clusprop-sz.md)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | %SystemRoot%\\wins\\backup                                       |



 

## Remarks

The WINS backup path does not include a file name or a trailing backslash.

The [**CLUSPROP\_SZ\_DECLARE**](clusprop-sz-declare.md) macro creates a [**CLUSPROP\_SZ**](clusprop-sz.md) structure with an array of the correct size.

## Examples

The property value portion of a [property list](property-lists.md) entry for **BackupPath** can be set with the following example code.


```C++
WCHAR szBackupPathData[] = L"\\\\WINS\\BackupDirectory";
CLUSPROP_SZ_DECLARE( BackupPathValue, 
                     sizeof( szBackupPathData ) / sizeof( WCHAR ) );
BackupPathValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_SZ;
BackupPathValue.cbLength = sizeof( szBackupPathData );
StringCbCopy( BackupPathValue.sz, 
              BackupPathValue.cbLength, 
              szBackupPathData );
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[WINS Service Private Properties](wins-service-private-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](clusprop-sz.md)
</dt> <dt>

[**CLUSPROP\_SZ\_DECLARE**](clusprop-sz-declare.md)
</dt> </dl>

 

 





