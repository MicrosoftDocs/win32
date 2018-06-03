---
title: BackupPath
description: Specifies the path to the DHCP backup file.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 197a8042-dc1e-4b8d-a78d-63318f587509
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- BackupPath Failover Cluster ,for the DHCP service
- BackupPath Failover Cluster
topic_type:
- apiref
api_name:
- BackupPath
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# BackupPath

Specifies the path to the DHCP backup file. The following table summarizes the attributes of the **BackupPath** property.



| Attribute | Value                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                                                                                                                                                                                                                                                                                                                                                                                              |
| Access    | [Read/write](read-write-properties.md)                                                                                                                                                                                                                                                                                                                                                                                                     |
| Status    | Required                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Structure | [**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/)                                                                                                                                                                                                                                                                                                                                                                                                         |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).)                                                                                                                                                                                                                                                                                                                                                                            |
| Default   | The DHCP **BackupPath** property defaults to a value of the form *drive*:\\*old path* where *drive* is the drive letter of the [Physical Disk](physical-disk.md) dependency and *old path* is the former path to the DHCP backup file. For example, if a [DHCP Service resource](dhcp-service.md) depends on drive K: and the former path was C:\\WinNT\\System32\\dhcp, the default for this property will be K:\\WinNT\\System32\\dhcp. |



 

## Remarks

The DHCP backup path does not include a file name or a trailing backslash.

The [**CLUSPROP\_SZ\_DECLARE**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusprop_sz_declare) macro creates a [**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/) structure with an array of the correct size.

## Examples

The property value portion of a [property list](property-lists.md) entry for **BackupPath** can be set with the following example code.


```C++
WCHAR szBackupPathData[] = L"\\\\DHCP\\BackupDirectory";
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
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[DHCP Service Private Properties](dhcp-service-private-properties.md)
</dt> <dt>

[**DatabasePath**](the-dhcp-service-databasepath.md)
</dt> <dt>

[**LogFilePath**](the-dhcp-service-logfilepath.md)
</dt> <dt>

[**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> <dt>

[**CLUSPROP\_SZ\_DECLARE**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusprop_sz_declare)
</dt> </dl>

 

 





