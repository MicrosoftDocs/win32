---
title: Drive
description: Specifies the drive letter for the Physical Disk resource. The following table summarizes the attributes of the Drive property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 49fe0faa-f6bb-4845-9bd7-8e1dfb2805ab
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Drive Failover Cluster ,for physical disks
- Drive Failover Cluster
topic_type:
- apiref
api_name:
- Drive
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Drive

\[The **Drive** property is available for use in Windows Server 2003. It may be altered or unavailable in subsequent versions.\]

Specifies the drive letter for the [Physical Disk](physical-disk.md) resource. The following table summarizes the attributes of the **Drive** property.



| Attribute            | Value                                                                     |
|----------------------|---------------------------------------------------------------------------|
| Data type<br/> | Null-terminated Unicode string<br/>                                 |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>                        |
| Status<br/>    | Required<br/>                                                       |
| Structure<br/> | [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)<br/>                            |
| Minimum<br/>   | **NULL**<br/>                                                       |
| Maximum<br/>   | None (but see [Maximum String Size](maximum-string-size.md)).<br/> |
| Default<br/>   | **NULL**<br/>                                                       |



 

## Remarks

The **Drive** property is used to create [Physical Disk](physical-disk.md) resources with the command-line tool [Cluster.exe](cluster-exe.md). Make sure that the assigned drive letter does not conflict with existing drive letters anywhere in the cluster, including each [node's](nodes.md) local drives.

The [**CLUSPROP\_SZ\_DECLARE**](/windows/previous-versions/ClusAPI/nf-clusapi-clusprop_sz_declare?branch=master) macro creates a [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master) structure with an array of the correct size.

## Examples

The property value portion of a [property list](property-lists.md) entry for **Drive** can be set with the following example code.


```C++
WCHAR                szDriveData[] = L"D:";
CLUSPROP_SZ_DECLARE( DriveValue, 
                     sizeof( szDriveData ) / sizeof( WCHAR ) );

DriveValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_SZ;
DriveValue.cbLength  = sizeof( szDriveData );
StringCbCopy( DriveValue.sz, DriveValue.cbLength, szDriveData );
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2003 Enterprise, Windows Server 2003 Datacenter<br/> |
| End of server support<br/>    | Windows Server 2003 Datacenter, Windows Server 2003 Enterprise<br/> |



## See also

<dl> <dt>

[Physical Disk Private Properties](physical-disk-private-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> <dt>

[**CLUSPROP\_SZ\_DECLARE**](/windows/previous-versions/ClusAPI/nf-clusapi-clusprop_sz_declare?branch=master)
</dt> </dl>

 

 





