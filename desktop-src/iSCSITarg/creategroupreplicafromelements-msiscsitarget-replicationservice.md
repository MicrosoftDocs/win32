---
title: CreateGroupReplicaFromElements method of the MSISCSITARGET\_ReplicationService class
description: Creates or starts a job to create new storage objects, which are replicas of the specified source storage objects. This method combines the functionality of the CreateGroup and CreateGroupReplica, in one call.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ff56e95c-cecf-47d7-b9af-cc6fd44cd824
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CreateGroupReplicaFromElements method iSCSI Software Target API
- CreateGroupReplicaFromElements method iSCSI Software Target API , MSISCSITARGET_ReplicationService class
- MSISCSITARGET_ReplicationService class iSCSI Software Target API , CreateGroupReplicaFromElements method
topic_type:
- apiref
api_name:
- MSISCSITARGET_ReplicationService.CreateGroupReplicaFromElements
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CreateGroupReplicaFromElements method of the MSISCSITARGET\_ReplicationService class

Creates or starts a job to create new storage objects, which are replicas of the specified source storage objects. This method combines the functionality of the [**CreateGroup**](creategroup-msiscsitarget-replicationservice.md) and [**CreateGroupReplica**](creategroupreplica-msiscsitarget-replicationservice.md), in one call.

This method is inherited from the **CIM\_ReplicationService** class.

## Syntax


```mof
uint32 CreateGroupReplicaFromElements(
  [in, optional]      string                     RelationshipName,
  [in]                uint16                     SyncType,
  [in, optional]      uint16                     Mode,
  [in]                CIM_LogicalElement     REF SourceElements[],
  [in, out, optional] string                     SourceGroupName,
  [in, optional]      CIM_ServiceAccessPoint REF SourceAccessPoint,
  [in, out]           CIM_ReplicationGroup   REF TargetGroup,
  [in, optional]      CIM_ServiceAccessPoint REF TargetAccessPoint,
  [in, optional]      uint16                     Consistency,
  [in, optional]      string                     ReplicationSettingData,
  [out]               CIM_ConcreteJob        REF Job,
  [out]               CIM_Synchronized       REF Synchronization,
  [in, optional]      CIM_SettingData        REF TargetSettingGoal,
  [in, optional]      CIM_ResourcePool       REF TargetPool,
  [in, optional]      uint16                     WaitForCopyState
);
```



## Parameters

<dl> <dt>

*RelationshipName* \[in, optional\]
</dt> <dd>

Specifies a user relevant name for the relationship between the source and target groups or between a source element and a target group. If **NULL**, the implementation assigns a name. If the individual target elements require an **ElementName**, the implementation constructs an appropriate **ElementName** using the **RelationshipName**. For example, by using the **RelationshipName** as a prefix followed by "\_*n*" sequence number, where *n* is a number beginning with 1.

</dd> <dt>

*SyncType* \[in\]
</dt> <dd>

Specifies the type of copy that will be made. Required.

The possible values are.

<dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd> *value* = 5</dd> <dt>

<span id="Mirror"></span><span id="mirror"></span><span id="MIRROR"></span>

**Mirror** (6)


</dt> <dd></dd> <dt>

<span id="Snapshot"></span><span id="snapshot"></span><span id="SNAPSHOT"></span>

**Snapshot** (7)


</dt> <dd></dd> <dt>

<span id="Clone"></span><span id="clone"></span><span id="CLONE"></span>

**Clone** (8)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>9 0x7FFF</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>0x8000 = *value* </dd> </dl> </dd> <dt>

*Mode* \[in, optional\]
</dt> <dd>

Specifies whether the target elements will be updated synchronously or asynchronously. If **NULL**, implementation decides the mode.

The possible values are.

<dt>

<span id="Synchronous"></span><span id="synchronous"></span><span id="SYNCHRONOUS"></span>

**Synchronous** (2)


</dt> <dd></dd> <dt>

<span id="Asynchronous"></span><span id="asynchronous"></span><span id="ASYNCHRONOUS"></span>

**Asynchronous** (3)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>4 0x7FFF</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>0x8000 = *value* </dd> </dl> </dd> <dt>

*SourceElements* \[in\]
</dt> <dd>

Specifies a list of source storage objects which may be [**MSISCSITARGET\_StorageVolume**](msiscsitarget-storagevolume.md) or other storage objects. All of the source elements shall be of the same type.

</dd> <dt>

*SourceGroupName* \[in, out, optional\]
</dt> <dd>

On input, specifies the name of the group to be created. If the name is not specified, the implementation may assign a group name and return it in this parameter.

</dd> <dt>

*SourceAccessPoint* \[in, optional\]
</dt> <dd>

Specifies source access point information. May be **NULL**, if the service does not need access information to access the source element.

</dd> <dt>

*TargetGroup* \[in, out\]
</dt> <dd>

On input, optionally specifies a target group to use. On return contains references to the created target group, the replica group. If a job is created, the target group may not be available immediately.

</dd> <dt>

*TargetAccessPoint* \[in, optional\]
</dt> <dd>

Specifies target access point information. May be **NULL**, if the service does not need access information to access the target elements.

</dd> <dt>

*Consistency* \[in, optional\]
</dt> <dd>

Specifies consistency for the replica. Overrides the default group consistency.

The possible values are.

<dt>

<span id="No_Consistency"></span><span id="no_consistency"></span><span id="NO_CONSISTENCY"></span>

**No Consistency** (2)


</dt> <dd></dd> <dt>

<span id="Sequential_Consistency"></span><span id="sequential_consistency"></span><span id="SEQUENTIAL_CONSISTENCY"></span>

**Sequential Consistency** (3)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>4 0x7FFF</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>0x8000 = *value* </dd> </dl> </dd> <dt>

*ReplicationSettingData* \[in, optional\]
</dt> <dd>

If provided, specifies the replication setting data for the given *SyncType* in the form of an embedded **CIM\_ReplicationSettingData** instance. If not provided, the management server uses the default replication setting data. Optional.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

On return contains a reference to the job, may be **NULL** if the job is completed.

</dd> <dt>

*Synchronization* \[out\]
</dt> <dd>

On return, contains a reference to the created group association between the source and the target elements. If a job is created, this parameter may be **NULL** until the association is instantiated.

</dd> <dt>

*TargetSettingGoal* \[in, optional\]
</dt> <dd>

Specifies configuration-related and operational parameters for the target storage objects, the replicas. If a *TargetElement* parameter is supplied, this parameter must be NULL.

</dd> <dt>

*TargetPool* \[in, optional\]
</dt> <dd>

Specifies the underlying storage for the target elements if specified, otherwise the allocation is implementation specific. If a *TargetElement* parameter is supplied, this parameter must be **NULL**.

</dd> <dt>

*WaitForCopyState* \[in, optional\]
</dt> <dd>

Specifies the **CopyState** that must be reached before this method returns. Only a subset of valid values apply.

For example.

-   **Initialized**: Associations have been established, but there is no data flow.
-   **Inactive**: Initialization is complete, but the data flow remains idle until it is activated.
-   **Synchronized**: Replicas are an exact copy of the source.
-   **UnSynchronized**: Copy operation is in progress.

</dd> </dl>

## Return value

This method returns one of the following values.

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unknown** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Invalid Parameter** (5)
</dt> <dt>

**In Use** (6)
</dt> <dt>

**DMTF Reserved** (7 4095)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Method Reserved** (4097 32767)
</dt> <dt>

**Vendor Specific** (0x8000 = *value* )
</dt> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SmIScsiTargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSISCSITARGET\_ReplicationService**](msiscsitarget-replicationservice.md)
</dt> <dt>

[**MSISCSITARGET\_StorageVolume**](msiscsitarget-storagevolume.md)
</dt> </dl>

 

 





