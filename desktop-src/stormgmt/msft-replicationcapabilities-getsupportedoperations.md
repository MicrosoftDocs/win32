---
title: GetSupportedOperations method of the MSFT\_ReplicationCapabilities class
description: Returns, for a given ReplicationType, the supported operations on a storage synchronized association that can be supplied to the ModifyReplicaSynchronization operation.
ms.assetid: '6D3911FC-CA5B-418D-878F-6630871C3B90'
keywords: ["GetSupportedOperations method Windows Storage Management API", "GetSupportedOperations method Windows Storage Management API , MSFT_ReplicationCapabilities class", "MSFT_ReplicationCapabilities class Windows Storage Management API , GetSupportedOperations method"]
topic_type:
- apiref
api_name:
- MSFT_ReplicationCapabilities.GetSupportedOperations
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
---

# GetSupportedOperations method of the MSFT\_ReplicationCapabilities class

Returns, for a given *ReplicationType*, the supported operations on a storage synchronized association that can be supplied to the **ModifyReplicaSynchronization** operation.

## Syntax


```mof
UInt32 GetSupportedOperations(
  [in]  UInt16 ReplicationType,
  [out] UInt16 SupportedOperations[],
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*ReplicationType* \[in\]
</dt> <dd>

A value representing the replication type. This must be in the enumeration [**MSFT\_ReplicationCapabilities**](msft-replicationcapabilities.md).SupportedReplicationTypes.

</dd> <dt>

*SupportedOperations* \[out\]
</dt> <dd>

An array of supported operations.

<dl> <dt>

<span id="Abort"></span><span id="abort"></span><span id="ABORT"></span>**Abort** (2)
</dt> <dt>

<span id="Activate_Consistency"></span><span id="activate_consistency"></span><span id="ACTIVATE_CONSISTENCY"></span>**Activate Consistency** (3)
</dt> <dt>

<span id="Activate"></span><span id="activate"></span><span id="ACTIVATE"></span>**Activate** (4)
</dt> <dt>

<span id="AddSyncPair"></span><span id="addsyncpair"></span><span id="ADDSYNCPAIR"></span>**AddSyncPair** (5)
</dt> <dt>

<span id="Deactivate_Consistency"></span><span id="deactivate_consistency"></span><span id="DEACTIVATE_CONSISTENCY"></span>**Deactivate Consistency** (6)
</dt> <dt>

<span id="Deactivate"></span><span id="deactivate"></span><span id="DEACTIVATE"></span>**Deactivate** (7)
</dt> <dt>

<span id="Detach"></span><span id="detach"></span><span id="DETACH"></span>**Detach** (8)
</dt> <dt>

<span id="Dissolve"></span><span id="dissolve"></span><span id="DISSOLVE"></span>**Dissolve** (9)
</dt> <dt>

<span id="Failover"></span><span id="failover"></span><span id="FAILOVER"></span>**Failover** (10)
</dt> <dt>

<span id="Failback"></span><span id="failback"></span><span id="FAILBACK"></span>**Failback** (11)
</dt> <dt>

<span id="Fracture"></span><span id="fracture"></span><span id="FRACTURE"></span>**Fracture** (12)
</dt> <dt>

<span id="RemoveSyncPair"></span><span id="removesyncpair"></span><span id="REMOVESYNCPAIR"></span>**RemoveSyncPair** (13)
</dt> <dt>

<span id="Resync_Replica"></span><span id="resync_replica"></span><span id="RESYNC_REPLICA"></span>**Resync Replica** (14)
</dt> <dt>

<span id="Restore_from_Replica"></span><span id="restore_from_replica"></span><span id="RESTORE_FROM_REPLICA"></span>**Restore from Replica** (15)
</dt> <dt>

<span id="Resume"></span><span id="resume"></span><span id="RESUME"></span>**Resume** (16)
</dt> <dt>

<span id="Reset_To_Sync"></span><span id="reset_to_sync"></span><span id="RESET_TO_SYNC"></span>**Reset To Sync** (17)
</dt> <dt>

<span id="Reset_To_Async"></span><span id="reset_to_async"></span><span id="RESET_TO_ASYNC"></span>**Reset To Async** (18)
</dt> <dt>

<span id="Return_To_ResourcePool"></span><span id="return_to_resourcepool"></span><span id="RETURN_TO_RESOURCEPOOL"></span>**Return To ResourcePool** (19)
</dt> <dt>

<span id="Reverse_Roles"></span><span id="reverse_roles"></span><span id="REVERSE_ROLES"></span>**Reverse Roles** (20)
</dt> <dt>

<span id="Split"></span><span id="split"></span><span id="SPLIT"></span>**Split** (21)
</dt> <dt>

<span id="Suspend"></span><span id="suspend"></span><span id="SUSPEND"></span>**Suspend** (22)
</dt> <dt>

<span id="Unprepare"></span><span id="unprepare"></span><span id="UNPREPARE"></span>**Unprepare** (23)
</dt> <dt>

<span id="Prepare"></span><span id="prepare"></span><span id="PREPARE"></span>**Prepare** (24)
</dt> <dt>

<span id="Reset_To_Adaptive"></span><span id="reset_to_adaptive"></span><span id="RESET_TO_ADAPTIVE"></span>**Reset To Adaptive** (25)
</dt> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved** (..)
</dt> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>**Vendor Specific** (0x8000..0xFFFF)
</dt> </dl> </dd> <dt>

*ExtendedStatus* \[out\]
</dt> <dd>

A string that contains an embedded [**MSFT\_StorageExtendedStatus**](msft-storageextendedstatus.md) object.

This parameter allows the storage provider to return extended (implementation-specific) error information.

</dd> </dl>

## Return value

<dl> <dt>

**Success** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unspecified Error** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Invalid Parameter** (5)
</dt> <dt>

**In Use** (6)
</dt> <dt>

**DMTF Reserved** (..)
</dt> <dt>

**Vendor Specific** (0x8000..)
</dt> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_ReplicationCapabilities**](msft-replicationcapabilities.md)
</dt> </dl>

 

 





