---
title: LogFilePath
description: Specifies the path to the DHCP log file.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 48bc7b32-9a33-4359-9f74-42ba91823d31
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- LogFilePath Failover Cluster ,for the DHCP service
- LogFilePath Failover Cluster
topic_type:
- apiref
api_name:
- LogFilePath
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LogFilePath

Specifies the path to the DHCP log file. The following table summarizes the attributes of the **LogFilePath** property.



| Attribute | Value                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                                                                                                                                                                                                                                                                                                                                                                                       |
| Access    | [Read/write](read-write-properties.md)                                                                                                                                                                                                                                                                                                                                                                                              |
| Status    | Required                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Structure | [**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/)                                                                                                                                                                                                                                                                                                                                                                                                  |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).)                                                                                                                                                                                                                                                                                                                                                                     |
| Default   | The DHCP **LogFilePath** property defaults to a value of the form *drive*:\\*old path* where *drive* is the drive letter of the [Physical Disk](physical-disk.md) dependency and *old path* is the former path to the log file. For example, if a [DHCP Service resource](dhcp-service.md) depends on drive K: and the former path was C:\\WinNT\\System32\\dhcp, the default for this property will be K:\\WinNT\\System32\\dhcp. |



 

## Remarks

The DHCP log file path does not include a file name or a trailing backslash.

The [**CLUSPROP\_SZ\_DECLARE**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusprop_sz_declare) macro creates a [**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/) structure with an array of the correct size.

## Examples

The property value portion of a [property list](property-lists.md) entry for **LogFilePath** can be set with the following example code.


```C++
WCHAR szLogFilePathData[] = L"\\\\DHCP\\Log";
CLUSPROP_SZ_DECLARE( LogFilePathValue, 
                     sizeof( szLogFilePathData ) / sizeof( WCHAR ) );
LogFilePathValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_SZ;
LogFilePathValue.cbLength = sizeof( szLogFilePathData );
StringCbCopy( LogFilePathValue.sz, LogFilePathValue.cbLength, szLogFilePathData );
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[DHCP Service Private Properties](dhcp-service-private-properties.md)
</dt> <dt>

[**BackupPath**](the-dhcp-service-backuppath.md)
</dt> <dt>

[**DatabasePath**](the-dhcp-service-databasepath.md)
</dt> <dt>

[**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> <dt>

[**CLUSPROP\_SZ\_DECLARE**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusprop_sz_declare)
</dt> </dl>

 

 





