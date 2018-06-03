---
title: MSFT\_StorageNodeToPhysicalDisk class
description: Association between a MSFT\_StorageNode and a MSFT\_PhysicalDisk.
ms.assetid: B9C7B6DA-2BBC-4D67-95FF-635458A60FCF
keywords:
- MSFT_StorageNodeToPhysicalDisk class Windows Storage Management API
- MSFT_StorageNodeToPhysicalDisk class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StorageNodeToPhysicalDisk
- MSFT_StorageNodeToPhysicalDisk.StorageNode
- MSFT_StorageNodeToPhysicalDisk.PhysicalDisk
- MSFT_StorageNodeToPhysicalDisk.OperationalStatus
- MSFT_StorageNodeToPhysicalDisk.HealthStatus
- MSFT_StorageNodeToPhysicalDisk.DiskNumber
- MSFT_StorageNodeToPhysicalDisk.IsMpioEnabled
- MSFT_StorageNodeToPhysicalDisk.LoadBalancePolicy
- MSFT_StorageNodeToPhysicalDisk.PathId
- MSFT_StorageNodeToPhysicalDisk.PathState
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_StorageNodeToPhysicalDisk class

Association between a [**MSFT\_StorageNode**](msft-storagenode.md) and a [**MSFT\_PhysicalDisk**](msft-physicaldisk.md).

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association]
class MSFT_StorageNodeToPhysicalDisk
{
  MSFT_StorageNode  REF StorageNode;
  MSFT_PhysicalDisk REF PhysicalDisk;
  UInt16                OperationalStatus[];
  UInt16                HealthStatus;
  UInt32                DiskNumber;
  Boolean               IsMpioEnabled;
  UInt16                LoadBalancePolicy;
  String                PathId[];
  UInt16                PathState[];
};
```

## Members

The **MSFT\_StorageNodeToPhysicalDisk** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageNodeToPhysicalDisk** class has these properties.

<dl> <dt>

**DiskNumber**
</dt> <dd> <dl> <dt>

Data type: **UInt32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The operating system's number for the disk on this storage node. Disk 0 is typically the boot device. Disk numbers may not necessarily remain the same across reboot, and are not necessarily the same on different nodes.

</dd> <dt>

**HealthStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

Denotes the health status of the physical disk on this storage node.

<dl> <dt>

<span id="Healthy"></span><span id="healthy"></span><span id="HEALTHY"></span>**Healthy** (0)
</dt> <dt>

<span id="Warning"></span><span id="warning"></span><span id="WARNING"></span>**Warning** (1)
</dt> <dt>

<span id="Unhealthy"></span><span id="unhealthy"></span><span id="UNHEALTHY"></span>**Unhealthy** (2)
</dt> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (5)
</dt> </dl>

</dd> <dt>

**IsMpioEnabled**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the physical disk uses MPIO.

</dd> <dt>

**LoadBalancePolicy**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The MPIO load balance policy being used by the disk.

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Fail_Over"></span><span id="fail_over"></span><span id="FAIL_OVER"></span>**Fail Over** (1)
</dt> <dt>

<span id="Round_Robin"></span><span id="round_robin"></span><span id="ROUND_ROBIN"></span>**Round Robin** (2)
</dt> <dt>

<span id="Round_Robin_with_Subset"></span><span id="round_robin_with_subset"></span><span id="ROUND_ROBIN_WITH_SUBSET"></span>**Round Robin with Subset** (3)
</dt> <dt>

<span id="Least_Queue_Depth"></span><span id="least_queue_depth"></span><span id="LEAST_QUEUE_DEPTH"></span>**Least Queue Depth** (4)
</dt> <dt>

<span id="Weighted_Paths"></span><span id="weighted_paths"></span><span id="WEIGHTED_PATHS"></span>**Weighted Paths** (5)
</dt> <dt>

<span id="Least_Blocks"></span><span id="least_blocks"></span><span id="LEAST_BLOCKS"></span>**Least Blocks** (6)
</dt> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>**Vendor Specific** (7)
</dt> </dl>

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

**Starting in Windows 10:** Denotes the operational status of the physical disk:

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)
</dt> <dt>

<span id="OK"></span><span id="ok"></span>**OK** (2)
</dt> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>**Degraded** (3)
</dt> <dt>

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>**Stressed** (4)
</dt> <dt>

<span id="Predictive_Failure"></span><span id="predictive_failure"></span><span id="PREDICTIVE_FAILURE"></span>**Predictive Failure** (5)
</dt> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>**Error** (6)
</dt> <dt>

<span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>**Non-Recoverable Error** (7)
</dt> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>**Starting** (8)
</dt> <dt>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>**Stopping** (9)
</dt> <dt>

<span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span>**Stopped** (10)
</dt> <dt>

<span id="In_Service"></span><span id="in_service"></span><span id="IN_SERVICE"></span>**In Service** (11)
</dt> <dt>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>**No Contact** (12)
</dt> <dt>

<span id="Lost_Communication"></span><span id="lost_communication"></span><span id="LOST_COMMUNICATION"></span>**Lost Communication** (13)
</dt> <dt>

<span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span>**Aborted** (14)
</dt> <dt>

<span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span>**Dormant** (15)
</dt> <dt>

<span id="Supporting_Entity_in_Error"></span><span id="supporting_entity_in_error"></span><span id="SUPPORTING_ENTITY_IN_ERROR"></span>**Supporting Entity in Error** (16)
</dt> <dt>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>**Completed** (17)
</dt> <dt>

<span id="Power_Mode"></span><span id="power_mode"></span><span id="POWER_MODE"></span>**Power Mode** (18)
</dt> <dt>

<span id="Relocating"></span><span id="relocating"></span><span id="RELOCATING"></span>**Relocating** (19)
</dt> <dt>

<span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span>**Microsoft Reserved** (..)
</dt> <dt>

<span id="Failed_Media"></span><span id="failed_media"></span><span id="FAILED_MEDIA"></span>**Failed Media** (0xD004)
</dt> <dt>

<span id="Split"></span><span id="split"></span><span id="SPLIT"></span>**Split** (0xD005)
</dt> <dt>

<span id="Stale_Metadata"></span><span id="stale_metadata"></span><span id="STALE_METADATA"></span>**Stale Metadata** (0xD006)
</dt> <dt>

<span id="IO_Error"></span><span id="io_error"></span><span id="IO_ERROR"></span>**IO Error** (0xD007)
</dt> <dt>

<span id="Unrecognized_Metadata"></span><span id="unrecognized_metadata"></span><span id="UNRECOGNIZED_METADATA"></span>**Unrecognized Metadata** (0xD008)
</dt> <dt>

<span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span>**Microsoft Reserved** (0xD009..)
</dt> </dl>

</dd> <dt>

**PathId**
</dt> <dd> <dl> <dt>

Data type: **String** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Collection of MPIO path IDs, reported by the MPIO DSM, when applicable.

</dd> <dt>

**PathState**
</dt> <dd> <dl> <dt>

Data type: **UInt16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current state of MPIO paths between the node and physical disk.

<dl> <dt>

<span id="Unavailable"></span><span id="unavailable"></span><span id="UNAVAILABLE"></span>**Unavailable** (0)
</dt> <dt>

<span id="Active_Unoptimized"></span><span id="active_unoptimized"></span><span id="ACTIVE_UNOPTIMIZED"></span>**Active/Unoptimized** (1)
</dt> <dt>

<span id="Standby"></span><span id="standby"></span><span id="STANDBY"></span>**Standby** (2)
</dt> <dt>

<span id="Active_Optimized"></span><span id="active_optimized"></span><span id="ACTIVE_OPTIMIZED"></span>**Active/Optimized** (3)
</dt> </dl>

</dd> <dt>

**PhysicalDisk**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_PhysicalDisk**](msft-physicaldisk.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> <dt>

**StorageNode**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_StorageNode**](msft-storagenode.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                   |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_PhysicalDisk**](msft-physicaldisk.md)
</dt> <dt>

[**MSFT\_StorageNode**](msft-storagenode.md)
</dt> </dl>

 

 





