---
title: DiskUniqueIds
description: Contains SCSI Inquiry Data and Vital Product Data page 83 (device identity) information of the disk.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f477ec85-197e-4aff-9095-c3a93f775513
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- DiskUniqueIds Failover Cluster , for Physical Disk private properties
- DiskUniqueIds Failover Cluster
topic_type:
- apiref
api_name:
- DiskUniqueIds
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DiskUniqueIds

Contains SCSI Inquiry Data and Vital Product Data page 83 (device identity) information of the disk, if available. This is used for autorecovery from disk id changes. The following table summarizes the attributes of the **DiskUniqueIds** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | **BYTE**                                                         |
| Access    | [Read/write](read-write-properties.md)                          |
| Status    | Optional                                                         |
| Structure | [**CLUSPROP\_BINARY**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_binary)                      |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | 0                                                                |



 

## Remarks

The content of the **DiskUniqueIds** property is a [STORAGE\_DEVICE\_ID\_DESCRIPTOR](Http://go.microsoft.com/fwlink/p/?linkid=107392) structure.

The [**CLUSPROP\_BINARY\_DECLARE**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusprop_binary_declare) macro creates a [**CLUSPROP\_BINARY**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_binary) structure with an array of the correct size.

The constant for this property is **CLUSREG\_NAME\_PHYSDISK\_DISKUNIQUEIDS**.

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

[**CLUSPROP\_BINARY\_DECLARE**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusprop_binary_declare)
</dt> <dt>

[STORAGE\_DEVICE\_ID\_DESCRIPTOR](Http://go.microsoft.com/fwlink/p/?linkid=107392)
</dt> </dl>

 

 





