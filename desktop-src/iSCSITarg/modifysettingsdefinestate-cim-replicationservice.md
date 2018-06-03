---
title: ModifySettingsDefineState method of the CIM\_ReplicationService class
description: Modify (or start a job to modify) the SettingsDefineState association between the storage objects and SynchronizationAspect.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e9404019-326a-42a5-8f8b-088fcca3a5ce
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ModifySettingsDefineState method iSCSI Software Target API
- ModifySettingsDefineState method iSCSI Software Target API , CIM_ReplicationService class
- CIM_ReplicationService class iSCSI Software Target API , ModifySettingsDefineState method
topic_type:
- apiref
api_name:
- CIM_ReplicationService.ModifySettingsDefineState
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ModifySettingsDefineState method of the CIM\_ReplicationService class

Modify (or start a job to modify) the SettingsDefineState association between the storage objects and SynchronizationAspect. The modification could range from introducing the target elements, which creates a new StorageSynchronized association to dissolving the SettingsDefineState association. If 0 is returned, the function completed successfully and no ConcreteJob instance was created. If 4096/0x1000 is returned, a ConcreteJob was started and a reference to this Job is returned in the Job output parameter. A return value of 1 indicates the method is not supported. All other values indicate some type of error condition.

## Syntax


```mof
uint32 ModifySettingsDefineState(
  [in]      uint16                      Operation,
  [in]      CIM_SettingsDefineState REF SettingsState,
  [in, out] CIM_LogicalElement      REF TargetElement,
  [in, out] CIM_ReplicationGroup    REF TargetGroup,
  [in]      uint64                      TargetElementCount,
  [in]      CIM_ServiceAccessPoint  REF TargetAccessPoint,
  [out]     CIM_Synchronized        REF Synchronization,
  [in]      string                      ReplicationSettingData,
  [out]     CIM_ConcreteJob         REF Job,
  [in]      CIM_SettingData         REF TargetSettingGoal,
  [in]      CIM_ResourcePool        REF TargetPool,
  [in]      uint16                      WaitForCopyState
);
```



## Parameters

<dl> <dt>

*Operation* \[in\]
</dt> <dd>

Operation describes the type of modification to be made to the related associations. Activate Consistency: if consistency was not requested when CreateSynchronizationAspect was called. If Consistency is already active, no modification is made. Deactivate Consistency: Deactivate consistency. If consistency was not enabled, this operation has no effect. Delete: Remove the SettingsDefineState association. Copy To Target: Introduces the target elements and forms the necessary associations between the source and the target elements i.e. StorageSynchronized and GroupSynchronized.

<dt>

<span id="Activate_Consistency"></span><span id="activate_consistency"></span><span id="ACTIVATE_CONSISTENCY"></span>

**Activate Consistency** (2)


</dt> <dd></dd> <dt>

<span id="Deactivate_Consistency"></span><span id="deactivate_consistency"></span><span id="DEACTIVATE_CONSISTENCY"></span>

**Deactivate Consistency** (3)


</dt> <dd></dd> <dt>

<span id="Delete"></span><span id="delete"></span><span id="DELETE"></span>

**Delete** (4)


</dt> <dd></dd> <dt>

<span id="Copy_To_Target"></span><span id="copy_to_target"></span><span id="COPY_TO_TARGET"></span>

**Copy To Target** (5)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>6 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl> </dd> <dt>

*SettingsState* \[in\]
</dt> <dd>

Reference to the association between the source element and an instance of SynchronizationAspect.

</dd> <dt>

*TargetElement* \[in, out\]
</dt> <dd>

Optionally, as an input, refers to a target element to use. If TargetElement is supplied, TargetGroup and TargetCount shall be NULL. As an output, refers to the created target storage element (i.e., the replica). If a job is created, the target element may not be available immediately.

</dd> <dt>

*TargetGroup* \[in, out\]
</dt> <dd>

Optionally, as an input, refers to a target group to use. If TargetGroup is supplied, TargetElement and TargetCount shall be NULL. As an output, refers to the created target group (i.e., the replica group). If a job is created, the target group may not be available immediately. If TargetGroup is supplied, TargetElementCount shall be NULL.

</dd> <dt>

*TargetElementCount* \[in\]
</dt> <dd>

This parameter applies to one-source-to-many-target- elements. It is possible to create multiple copies of a source element. If TargetCount is supplied, TargetElement and TargetGroup shall be NULL.

</dd> <dt>

*TargetAccessPoint* \[in\]
</dt> <dd>

Reference to target access point information. If NULL, service does not need access information to access the target elements/group.

</dd> <dt>

*Synchronization* \[out\]
</dt> <dd>

The reference to the created replication association describing the elements/groups relationship.

</dd> <dt>

*ReplicationSettingData* \[in\]
</dt> <dd>

If provided, it overrides the default replication setting data for the given SyncType. If not provided, the management server uses the default replication setting data.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

Reference to the job (may be NULL if the task completed).

</dd> <dt>

*TargetSettingGoal* \[in\]
</dt> <dd>

The definition for the SettingData to be maintained by the target storage object (the replica). If a target element is supplied, this parameter shall be NULL.

</dd> <dt>

*TargetPool* \[in\]
</dt> <dd>

The underlying storage for the target element (the replica) will be drawn from TargetPool if specified, otherwise the allocation is implementation specific. If a target element is supplied, this parameter shall be NULL.

</dd> <dt>

*WaitForCopyState* \[in\]
</dt> <dd>

Method must wait until this CopyState is reached before returning. Only a subset of valid CopyStates apply. For example, Initialized: Associations have been established, but there is no data flow. Inactive: Initialization is complete, but the data flow remains idle until it is activated. Synchronized: Replicas are an exact copy of the source. UnSynchronized: Copy operation is in progress. Fractured/Split: Target elements are separated from the source elements. Etc.

</dd> </dl>

## Return value

<dl> <dt>

**Completed with No Error** (0)
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

**DMTF Reserved** (7 4095)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Method Reserved** (4097 32767)
</dt> <dt>

**Vendor Specific** (32768 4294967295)
</dt> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

**CIM\_ReplicationService**
</dt> </dl>

 

 





