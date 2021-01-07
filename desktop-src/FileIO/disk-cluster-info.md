---
description: Represents information maintained on the partition manager about a disk that is part of a cluster.
ms.assetid: 9138F61A-E295-4F5B-AD65-361FCCB3C4B7
title: DISK_CLUSTER_INFO structure (Ntdddisk.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DISK_CLUSTER_INFO
api_type: 
- HeaderDef
api_location: 
- Ntdddisk.h
---

# DISK\_CLUSTER\_INFO structure

Represents information maintained on the partition manager about a disk that is part of a cluster.

## Syntax


```C++
typedef struct _DISK_CLUSTER_INFO {
  ULONG     Version;
  ULONGLONG Flags;
  ULONGLONG FlagsMask;
  BOOLEAN   Notify;
} DISK_CLUSTER_INFO, *PDISK_CLUSTER_INFO;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

The version number. This value must be set to the size of this structure.

</dd> <dt>

**Flags**
</dt> <dd>

A combination of flags related to disks and clusters.



| Value                                                                                                                                                                                                                                                                                               | Meaning                                                                                                                 |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| <span id="DISK_CLUSTER_FLAG_ENABLED"></span><span id="disk_cluster_flag_enabled"></span><dl> <dt>**DISK\_CLUSTER\_FLAG\_ENABLED**</dt> <dt>1</dt> </dl>                                          | The disk is used as part of the cluster service.<br/>                                                             |
| <span id="DISK_CLUSTER_FLAG_CSV"></span><span id="disk_cluster_flag_csv"></span><dl> <dt>**DISK\_CLUSTER\_FLAG\_CSV**</dt> <dt>2</dt> </dl>                                                      | Volumes on the disk are exposed by CSVFS on all nodes of the cluster.<br/>                                        |
| <span id="DISK_CLUSTER_FLAG_IN_MAINTENANCE"></span><span id="disk_cluster_flag_in_maintenance"></span><dl> <dt>**DISK\_CLUSTER\_FLAG\_IN\_MAINTENANCE**</dt> <dt>4</dt> </dl>                    | The cluster resource associated with this disk is in maintenance mode.<br/>                                       |
| <span id="DISK_CLUSTER_FLAG_PNP_ARRIVAL_COMPLETE"></span><span id="disk_cluster_flag_pnp_arrival_complete"></span><dl> <dt>**DISK\_CLUSTER\_FLAG\_PNP\_ARRIVAL\_COMPLETE**</dt> <dt>8</dt> </dl> | The cluster disk driver for kernel mode (clusdisk) has received PnP notification of the arrival of the disk.<br/> |



 

</dd> <dt>

**FlagsMask**
</dt> <dd>

The flags that are being modified in the **Flags** member.

</dd> <dt>

**Notify**
</dt> <dd>

**TRUE** to send a layout change notification; otherwise, **FALSE**.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Ntdddisk.h</dt> </dl> |



## See also

<dl> <dt>

[Disk Management Structures](disk-management-structures.md)
</dt> <dt>

[**IOCTL\_DISK\_GET\_CLUSTER\_INFO**](ioctl-disk-get-cluster-info.md)
</dt> <dt>

[**IOCTL\_DISK\_SET\_CLUSTER\_INFO**](ioctl-disk-set-cluster-info.md)
</dt> </dl>

 

 




