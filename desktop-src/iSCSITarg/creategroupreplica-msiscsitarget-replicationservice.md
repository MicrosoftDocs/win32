---
title: CreateGroupReplica method of the MSISCSITARGET\_ReplicationService class
description: Creates a new group of storage objects that are replicas of the specified source storage or a group of source storage objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 99713c75-de87-4427-9ddf-ae63f588843f
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CreateGroupReplica method iSCSI Software Target API
- CreateGroupReplica method iSCSI Software Target API , MSISCSITARGET_ReplicationService class
- MSISCSITARGET_ReplicationService class iSCSI Software Target API , CreateGroupReplica method
topic_type:
- apiref
api_name:
- MSISCSITARGET_ReplicationService.CreateGroupReplica
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CreateGroupReplica method of the MSISCSITARGET\_ReplicationService class

Creates a new group of storage objects that are replicas of the specified source storage or a group of source storage objects. This method can be used to instantiate the replicas and to create an ongoing association between the source and replica by using the *SyncType* input parameter.

This method is inherited from the **CIM\_ReplicationService** class.

## Syntax


```mof
uint32 CreateGroupReplica(
  [in, optional] string                     RelationshipName,
  [in]           uint16                     SyncType,
  [in, optional] uint16                     Mode,
  [in, optional] CIM_ReplicationGroup Ref   SourceGroup,
  [in, optional] CIM_LogicalElement Ref     SourceElement,
  [in, optional] CIM_ServiceAccessPoint Ref SourceAccessPoint,
  [in, out]      CIM_ReplicationGroup Ref   TargetGroup,
  [in, optional] uint64                     TargetElementCount,
  [in, optional] CIM_ServiceAccessPoint Ref TargetAccessPoint,
  [in, optional] uint16                     Consistency,
  [in, optional] string                     ReplicationSettingData,
  [out]          CIM_ConcreteJob Ref        Job,
  [out]          CIM_Synchronized Ref       Synchronization,
  [in, optional] CIM_SettingData Ref        TargetSettingGoal,
  [in, optional] CIM_ResourcePool Ref       TargetPool,
  [in, optional] uint16                     WaitForCopyState
);
```



## Parameters

<dl> <dt>

*RelationshipName* \[in, optional\]
</dt> <dd>

Specifies a user name that is meaningful for the relationship between the source and target groups or between a source element and a target group. If **NULL**, the implementation assigns a name. If the individual target elements require an **ElementName** property, the implementation constructs an appropriate **ElementName** value by using the **RelationshipName** property. For example, by using the **RelationshipName** property as a prefix that is followed by the "\_*n*" sequence number, where *n* is a number that begins with 1.

</dd> <dt>

*SyncType* \[in\]
</dt> <dd>

Specifies the type of copy to make. Required.

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

Specifies whether the target elements are updated synchronously or asynchronously. If **NULL**, implementation decides the mode.

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

*SourceGroup* \[in, optional\]
</dt> <dd>

Specifies a group of source storage objects that can be a **CIM\_StorageVolume** instance or a storage object. If this parameter is not specified, the *SourceElement* parameter is required. You cannot specify both the *SourceGroup* and *SourceElement* parameters, but you must specify one of them.

</dd> <dt>

*SourceElement* \[in, optional\]
</dt> <dd>

Specifies the source storage object that can be a [**MSISCSITARGET\_StorageVolume**](msiscsitarget-storagevolume.md) instance or a storage object. If this parameter is not specified, the *SourceGroup* parameter is required. You cannot specify both the *SourceGroup* and *SourceElement* parameters, but you must specify one of them.

</dd> <dt>

*SourceAccessPoint* \[in, optional\]
</dt> <dd>

Specifies the source access point information. Can be **NULL**, if the service does not require access information to access the source element.

</dd> <dt>

*TargetGroup* \[in, out\]
</dt> <dd>

On input, optionally specifies a target group to use. On output, refers to the created target group that is the replica group. If a job is created, the target group might not be available immediately. If you specify the *TargetGroup* parameter, the *TargetElementCount* parameter must be **NULL**.

</dd> <dt>

*TargetElementCount* \[in, optional\]
</dt> <dd>

Specifies how many target elements to create. Use this parameter to create multiple copies of a source element. If you specify the *TargetElementCount* parameter, the *TargetGroup* parameter must be **NULL**.

</dd> <dt>

*TargetAccessPoint* \[in, optional\]
</dt> <dd>

Specifies the target access point information. Can be **NULL**, if the service does not require access information to access the target element or target group.

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

If provided, specifies the replication setting data for the given *SyncType* input parameter in the form of an embedded **CIM\_ReplicationSettingData** instance. If not provided, the management server uses the default replication setting data.

If provided, it overrides the default replication setting data for the given *SyncType* input parameter. If **NULL**, the management server uses the default replication setting data.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

On return, contains a reference to the job, which can be **NULL** if the job is completed.

</dd> <dt>

*Synchronization* \[out\]
</dt> <dd>

On return, contains a reference to the created group association between the source and the target elements. If a job is created, this parameter can be **NULL** until the association is instantiated.

</dd> <dt>

*TargetSettingGoal* \[in, optional\]
</dt> <dd>

Specifies configuration-related and operational parameters for the target, replica, and storage objects. If existing target elements are specified, this parameter is **NULL**.

</dd> <dt>

*TargetPool* \[in, optional\]
</dt> <dd>

Specifies the underlying storage for the new target elements. If **NULL**, the allocation is implementation-specific. If existing target elements are supplied, this parameter is **NULL**.

</dd> <dt>

*WaitForCopyState* \[in, optional\]
</dt> <dd>

Specifies the **CopyState** value that must be reached before this method returns. Only a subset of valid values apply.

For example:

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

 

 





