---
title: DeleteReplicationRelationship method of the MSFT\_StorageSubSystem class
description: Deletes a replication relationship between groups. The groups themselves are deleted if they have no more relationships with other groups. The method is only available on subsystems that support fully discovered replication.
ms.assetid: 'FCACCFF1-A80C-4B51-888A-90E31760C067'
keywords: ["DeleteReplicationRelationship method Windows Storage Management API", "DeleteReplicationRelationship method Windows Storage Management API , MSFT_StorageSubSystem interface", "MSFT_StorageSubSystem interface Windows Storage Management API , DeleteReplicationRelationship method"]
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystem.DeleteReplicationRelationship
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
---

# DeleteReplicationRelationship method of the MSFT\_StorageSubSystem class

Deletes a replication relationship between groups. The groups themselves are deleted if they have no more relationships with other groups. The method is only available on subsystems that support fully discovered replication.

## Syntax


```mof
UInt32 DeleteReplicationRelationship(
  [in]  String              SourceReplicationGroup,
  [in]  String              TargetGroupReplicaPeer,
  [out] MSFT_StorageJob REF CreatedStorageJob,
  [out] String              ExtendedStatus
);
```



## Parameters

<dl> <dt>

*SourceReplicationGroup* \[in\]
</dt> <dd>

A string that contains an embedded [**MSFT\_ReplicationGroup**](msft-replicationgroup.md) object, specifying the source replication group.

</dd> <dt>

*TargetGroupReplicaPeer* \[in\]
</dt> <dd>

A string that contains an embedded [**MSFT\_ReplicaPeer**](msft-replicapeer.md) object, specifying the target replication group.

</dd> <dt>

*CreatedStorageJob* \[out\]
</dt> <dd>

Returns a reference to the storage job object used to track the long-running operation.

</dd> <dt>

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

**Access denied** (40001)
</dt> <dt>

**There are not enough resources to complete the operation.** (40002)
</dt> <dt>

**Cannot connect to the storage provider.** (46000)
</dt> <dt>

**The storage provider cannot connect to the storage subsystem.** (46001)
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

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
</dt> </dl>

 

 





