---
title: CreateReplicationRelationship method of the MSFT\_StorageSubSystem class
description: Creates two replication groups and a replication relationship between them. This method requires the subsystem to support fully discovered replication.
ms.assetid: 354EDEDE-CE2F-4865-9A79-0B664D705649
keywords:
- CreateReplicationRelationship method Windows Storage Management API
- CreateReplicationRelationship method Windows Storage Management API , MSFT_StorageSubSystem interface
- MSFT_StorageSubSystem interface Windows Storage Management API , CreateReplicationRelationship method
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystem.CreateReplicationRelationship
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CreateReplicationRelationship method of the MSFT\_StorageSubSystem class

Creates two replication groups and a replication relationship between them. This method requires the subsystem to support fully discovered replication.

## Syntax


```mof
UInt32 CreateReplicationRelationship(
  [in]  String              FriendlyName,
  [in]  Uint16              SyncType,
  [in]  String              TargetStorageSubsystem,
  [in]  String              SourceReplicationGroupFriendlyName,
  [in]  String              SourceReplicationGroupDescription,
  [in]  String              SourceStorageElements[],
  [in]  String              SourceGroupSettings,
  [in]  String              TargetReplicationGroupFriendlyName,
  [in]  String              TargetReplicationGroupDescription,
  [in]  String              TargetStorageElements[],
  [in]  String              TargetStoragePool,
  [in]  String              TargetStoragePools[],
  [in]  String              TargetGroupSettings,
  [in]  UInt16              RecoveryPointObjective,
  [out] String              SourceGroup,
  [out] String              TargetGroup,
  [out] String              CreatedReplicaPeer,
  [out] MSFT_StorageJob REF CreatedStorageJob,
  [out] String              ExtendedStatus
);
```



## Parameters

<dl> <dt>

*FriendlyName* \[in\]
</dt> <dd>

A user-relevant name for the relationship between the source and target groups, or between a source element and a target group (that is, one-to-many). If **NULL**, the implementation assigns a name. If the individual target elements require an **ElementName**, the implementation constructs an appropriate **ElementName** using the **RelationshipName**; for example, **RelationshipName** as a prefix followed by a "\_n" sequence number, where n is a number beginning with 1.

</dd> <dt>

*SyncType* \[in\]
</dt> <dd>

Describes the type of copy that will be made.

<dl> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved** (..)
</dt> <dt>

<span id="Mirror"></span><span id="mirror"></span><span id="MIRROR"></span>**Mirror** (6)
</dt> <dt>

<span id="Snapshot"></span><span id="snapshot"></span><span id="SNAPSHOT"></span>**Snapshot** (7)
</dt> <dt>

<span id="Clone"></span><span id="clone"></span><span id="CLONE"></span>**Clone** (8)
</dt> <dt>

<span id="TokenizedClone"></span><span id="tokenizedclone"></span><span id="TOKENIZEDCLONE"></span>**TokenizedClone** (9)
</dt> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved** (..)
</dt> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>**Vendor Specific** (0x8000..)
</dt> </dl> </dd> <dt>

*TargetStorageSubsystem* \[in\]
</dt> <dd>

A string that contains an embedded [**MSFT\_ReplicaPeer**](msft-replicapeer.md) object. This allows the user to specify the replica target subsystem when setting up a relationship with another subsystem.

</dd> <dt>

*SourceReplicationGroupFriendlyName* \[in\]
</dt> <dd>

The name of the source replication group to be created.

</dd> <dt>

*SourceReplicationGroupDescription* \[in\]
</dt> <dd>

A description of the purpose of the source replication group.

</dd> <dt>

*SourceStorageElements* \[in\]
</dt> <dd>

Specifies an array of strings that contain embedded [**MSFT\_StorageObject**](msft-storageobject.md) objects. This is an ordered list of storage objects that are to be a part of the source replication group.

</dd> <dt>

*SourceGroupSettings* \[in\]
</dt> <dd>

A string that contains an embedded [**MSFT\_ReplicationSettings**](msft-replicationsettings.md) object to be applied to the source replication group.

</dd> <dt>

*TargetReplicationGroupFriendlyName* \[in\]
</dt> <dd>

The name of the target replication group to be created.

</dd> <dt>

*TargetReplicationGroupDescription* \[in\]
</dt> <dd>

A description of the purpose of the target replication group.

</dd> <dt>

*TargetStorageElements* \[in\]
</dt> <dd>

Specifies an array of strings that contain embedded [**MSFT\_StorageObject**](msft-storageobject.md) objects. This is an ordered list of storage objects that are to be a part of the target replication group.

</dd> <dt>

*TargetStoragePool* \[in\]
</dt> <dd>

A string that contains an embedded [**MSFT\_StoragePool**](msft-storagepool.md) object. This is a storage pool on the target to be used as the source for creating the necessary *TargetStorageElements*. This parameter can be specified in lieu of *TargetStorageElements*.

</dd> <dt>

*TargetStoragePools* \[in\]
</dt> <dd>

A array of strings containing embedded [**MSFT\_StoragePool**](msft-storagepool.md) objects. The underlying storage for the target elements (the replicas) will be drawn from *TargetStoragePool* if specified. Otherwise the allocation is implementation specific. If target elements are supplied, this parameter shall be **NULL**. If *TargetStoragePools* is supplied, *TargetStoragePool* shall be **NULL**.

</dd> <dt>

*TargetGroupSettings* \[in\]
</dt> <dd>

A string that contains an embedded [**MSFT\_ReplicationSettings**](msft-replicationsettings.md) object to be applied to the target replication group.

</dd> <dt>

*RecoveryPointObjective* \[in\]
</dt> <dd>

Indicates the maximum interval in which data might be lost. For synchronous copy operations, *RecoveryPointObjective* is 0. For asynchronous copy operations *RecoveryPointObjective* represents the interval since the most recent transmission of data to the target element.

</dd> <dt>

*SourceGroup* \[out\]
</dt> <dd>

If the replication groups and relationship are created successfully, this parameter receives a string that contains an embedded [**MSFT\_ReplicationGroup**](msft-replicationgroup.md) object representing the source replication group.

</dd> <dt>

*TargetGroup* \[out\]
</dt> <dd>

If the replication groups and relationship are created successfully, this parameter receives a string that contains an embedded [**MSFT\_ReplicationGroup**](msft-replicationgroup.md) object representing the target replication group.

</dd> <dt>

*CreatedReplicaPeer* \[out\]
</dt> <dd>

If the replication groups and relationship are created successfully, this parameter receives a string that contains an embedded [**MSFT\_ReplicaPeer**](msft-replicapeer.md) object representing the replica peer for the target replication group.

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

**Object Not Found** (8)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Access denied** (40001)
</dt> <dt>

**There are not enough resources to complete the operation.** (40002)
</dt> <dt>

**Cache out of date** (40003)
</dt> <dt>

**The operation is not supported while the cluster is being upgraded.** (40009)
</dt> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
</dt> </dl>

 

 





