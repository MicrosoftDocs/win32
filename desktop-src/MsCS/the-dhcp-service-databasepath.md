---
title: DatabasePath
description: Specifies the path to the DHCP database.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '51807cf5-1c8b-40a1-9221-a22f4c980635'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["DatabasePath Failover Cluster ,for the DHCP service", "DatabasePath Failover Cluster"]
topic_type:
- apiref
api_name:
- DatabasePath
api_type:
- NA
---

# DatabasePath

Specifies the path to the DHCP database. The following table summarizes the attributes of the **DatabasePath** property.



| Attribute | Value                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                                                                                                                                                                                                                                                                                                                                                                                        |
| Access    | [Read/write](read-write-properties.md)                                                                                                                                                                                                                                                                                                                                                                                               |
| Status    | Required                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Structure | [**CLUSPROP\_SZ**](clusprop-sz.md)                                                                                                                                                                                                                                                                                                                                                                                                   |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).)                                                                                                                                                                                                                                                                                                                                                                      |
| Default   | The DHCP **DatabasePath** property defaults to a value of the form *drive*:\\*old path* where *drive* is the drive letter of the [Physical Disk](physical-disk.md) dependency and *old path* is the former path to the database. For example, if a [DHCP Service resource](dhcp-service.md) depends on drive K: and the former path was C:\\WinNT\\System32\\dhcp, the default for this property will be K:\\WinNT\\System32\\dhcp. |



 

## Remarks

The DHCP database path does not include a file name or a trailing backslash.

The [**CLUSPROP\_SZ\_DECLARE**](clusprop-sz-declare.md) macro creates a [**CLUSPROP\_SZ**](clusprop-sz.md) structure with an array of the correct size.

## Examples

The property value portion of a [property list](property-lists.md) entry for **DatabasePath** can be set with the following example code.


```C++
WCHAR szDatabasePathData[] = L"\\\\DHCP\\DBDirectory";
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
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[DHCP Service Private Properties](dhcp-service-private-properties.md)
</dt> <dt>

[**BackupPath**](the-dhcp-service-backuppath.md)
</dt> <dt>

[**LogFilePath**](the-dhcp-service-logfilepath.md)
</dt> <dt>

[**CLUSPROP\_SZ**](clusprop-sz.md)
</dt> <dt>

[**CLUSPROP\_SZ\_DECLARE**](clusprop-sz-declare.md)
</dt> </dl>

 

 





