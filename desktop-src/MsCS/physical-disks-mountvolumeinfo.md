---
title: MountVolumeInfo
description: Stores information used by Disk Management. Disk Management is a graphical tool for managing disks and volumes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 73a1372b-0e1a-4998-9f73-faf133da081d
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- MountVolumeInfo Failover Cluster ,for physical disks
- MountVolumeInfo Failover Cluster
topic_type:
- apiref
api_name:
- MountVolumeInfo
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MountVolumeInfo

\[**MountVolumeInfo** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, use [**DiskVolumeInfo**](diskvolumeinfo.md), [CLUSCTL\_RESOURCE\_STORAGE\_GET\_DISK\_INFO](clusctl-resource-storage-get-disk-info.md), or [CLUSCTL\_RESOURCE\_STORAGE\_GET\_DISK\_INFO\_EX](clusctl-resource-storage-get-disk-info-ex.md).\]

Stores information used by Disk Management. Disk Management is a graphical tool for managing disks and volumes. The following table summarizes the attributes of the **MountVolumeInfo** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | byte array                                                       |
| Access    | [Read/write](read-write-properties.md)                          |
| Status    | Optional                                                         |
| Structure | [**CLUSPROP\_BINARY**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_binary)                      |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | 0                                                                |



 

## Remarks

The **MountVolumeInfo** property is used to track changes made in the Disk Manager user interface.

When a disk resource is brought online, the [Cluster service](cluster-service.md) checks the physical disk configuration, and then updates the property data. The Cluster service also updates **MountVolumeInfo** when the drive letter of a disk resource is changed from Disk Manager.

**MountVolumeInfo** data consists of a byte array organized as follows.

-   An 8-byte "header" consisting of the disk signature (first 4 bytes) and the number of volumes (second 4 bytes).
-   One or more 24-byte entries describing the following information.



| Position      | Data             |
|---------------|------------------|
| First 8 bytes | Starting Offset  |
| Next 8 bytes  | Partition Length |
| Next 4 bytes  | Volume Number    |
| Next 1 byte   | Disk Type        |
| Next 1 byte   | Drive Letter     |
| Last 2 bytes  | Padding          |



 

For example, the following **MountVolumeInfo** data

``` syntax
D3 DB 5C 54 04 00 00 00 00 02 00 00 00 00 00 00 
00 00 40 06 00 00 00 00 01 00 00 00 07 46 00 00 
00 02 40 06 00 00 00 00 00 FE 3F 06 00 00 00 00 
02 00 00 00 07 4B 00 00 00 00 80 0C 00 00 00 00 
00 00 40 06 00 00 00 00 03 00 00 00 07 4C 00 00 
00 40 C0 12 00 00 00 00 00 C0 3F 06 00 00 00 00 
04 00 00 00 07 49 00 00
```

would be interpreted as follows

``` syntax
Signature Volumes
--------- --------
545CDBD3  00000004

 Starting Offset  Partition Length  Volume#  Type Letter  Pad
----------------- ----------------- -------- ---- ------- ----
00000000.00000200 00000000.06400000 00000001  07  46 (F:) 0000
00000000.06400200 00000000.063FFE00 00000002  07  4B (K:) 0000
00000000.0C800000 00000000.06400000 00000003  07  4C (L:) 0000
00000000.12C04000 00000000.063FC000 00000004  07  49 (I:) 0000
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

[**DiskInfo**](physical-disks-diskinfo.md)
</dt> <dt>

[CLUSCTL\_RESOURCE\_STORAGE\_GET\_DISK\_INFO](clusctl-resource-storage-get-disk-info.md)
</dt> <dt>

[CLUSCTL\_RESOURCE\_STORAGE\_GET\_DISK\_INFO\_EX](clusctl-resource-storage-get-disk-info-ex.md)
</dt> </dl>

 

 





