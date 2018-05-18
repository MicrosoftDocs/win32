---
title: DiskInfo
description: Provides disk information. The following table summarizes the attributes of the DiskInfo property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '28dde3c7-1f8e-418e-a4cc-7ec20e3e67d0'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["DiskInfo Failover Cluster ,for physical disks", "DiskInfo Failover Cluster"]
topic_type:
- apiref
api_name:
- DiskInfo
api_type:
- NA
---

# DiskInfo

\[The **DiskInfo** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, use [**DiskVolumeInfo**](diskvolumeinfo.md), [CLUSCTL\_RESOURCE\_STORAGE\_GET\_DISK\_INFO](clusctl-resource-storage-get-disk-info.md), or [CLUSCTL\_RESOURCE\_STORAGE\_GET\_DISK\_INFO\_EX](clusctl-resource-storage-get-disk-info-ex.md).\]

Provides disk information. The following table summarizes the attributes of the **DiskInfo** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | byte array                                                       |
| Access    | [Read/write](read-write-properties.md)                          |
| Status    | Optional                                                         |
| Structure | [**CLUSPROP\_BINARY**](clusprop-binary.md)                      |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | 0                                                                |



 

## Remarks

For information on interpreting the **DiskInfo** byte array, see the [**MountVolumeInfo**](physical-disks-mountvolumeinfo.md) property.

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2003 Enterprise, Windows Server 2003 Datacenter<br/> |
| End of server support<br/>    | Windows Server 2003 Datacenter, Windows Server 2003 Enterprise<br/> |



## See also

<dl> <dt>

[Physical Disk Private Properties](physical-disk-private-properties.md)
</dt> <dt>

[**MountVolumeInfo**](physical-disks-mountvolumeinfo.md)
</dt> </dl>

 

 





