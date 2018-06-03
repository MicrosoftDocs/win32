---
title: DiskVolumeInfo
description: Stores information about the volumes on a Physical Disk resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 610e8123-8726-4227-93b4-9e7b08b4583a
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- DiskVolumeInfo Failover Cluster , for Physical Disk private properties
- DiskVolumeInfo Failover Cluster
topic_type:
- apiref
api_name:
- DiskVolumeInfo
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DiskVolumeInfo

Stores information about the volumes on a [*Physical Disk resource*](https://www.bing.com/search?q=*Physical Disk resource*). The following table summarizes the attributes of the **DiskVolumeInfo** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | **BYTE**                                                         |
| Access    | [Read/write](read-write-properties.md)                          |
| Status    | Optional                                                         |
| Structure | [**CLUSPROP\_BINARY**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_binary)                      |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | See Remarks                                                      |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_PHYSDISK\_DISKVOLUMEINFO**.

**DiskVolumeInfo** data consists of a byte array organized as follows:

-   A 4-byte integer containing the number of partitions.
-   4 bytes of padding (64-bit Windows only).
-   One or more 40-byte entries describing the volume information.



| Position                 | Data                                                           |
|--------------------------|----------------------------------------------------------------|
| First 8 bytes<br/> | Starting Offset<br/>                                     |
| Next 8 bytes<br/>  | Partition Length<br/>                                    |
| Next 4 bytes<br/>  | Partition Number<br/>                                    |
| Next 4 bytes<br/>  | Drive (0x1 is A:, 0x2 is B:, 0x4 is C:, and so on.)<br/> |
| Next 16 bytes<br/> | Volume **GUID**<br/>                                     |



 

For example, on a 64-bit Windows computer, the following **DiskVolumeInfo** data . . .

``` syntax
04 00 00 00 00 00 00 00 00 02 00 00 00 00 00 00 
00 00 40 06 00 00 00 00 01 00 00 00 20 00 00 00 
90 20 64 65 C8 8B 26 44 21 A3 D2 89 E4 3D 32 8F 
00 02 40 06 00 00 00 00 00 FE 3F 06 00 00 00 00 
02 00 00 00 00 04 00 00 17 E0 53 CD 8C 36 20 4C 
B4 AA 91 D0 EB E1 25 53 00 00 80 0C 00 00 00 00 
00 00 40 06 00 00 00 00 03 00 00 00 00 08 00 00 
D7 69 5F A4 65 91 B5 48 06 AE 61 64 3D 6B B2 4D 
00 40 C0 12 00 00 00 00 00 C0 3F 06 00 00 00 00 
04 00 00 00 00 01 00 00 63 D4 12 F4 BD 29 42 97 
C8 A2 54 DA 35 13 CD D1
```

. . . would be interpreted as follows.

``` syntax
Partitions
----------
 00000004

Padding
--------
00000000

 Starting Offset  Partition Length   Part.#  Drive Letter              Volume GUID
----------------- ----------------- -------- ------------- ------------------------------------
00000000.00000200 00000000.06400000 00000001 00000020 (F:) 65642090-8BC8-4426-A321-8F323DE489D2
00000000.06400200 00000000.063FFE00 00000002 00000400 (K:) CD53E017-368C-4C20-AAB4-5325E1EBD091
00000000.0C800000 00000000.06400000 00000003 00000800 (L:) A45F69D7-9165-48B5-AE06-4DB26B3D6461
00000000.12C04000 00000000.063FC000 00000004 00000100 (I:) F412D463-29BD-4297-A2C8-D1CD1335DA54
```

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[Physical Disk Private Properties](physical-disk-private-properties.md)
</dt> <dt>

[**CLUSPROP\_BINARY**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_binary)
</dt> <dt>

[**MountVolumeInfo**](physical-disks-mountvolumeinfo.md)
</dt> </dl>

 

 





