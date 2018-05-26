---
title: CreateListReplica method of the CIM\_ReplicationService class
description: Create (or start a job to create) new storage objects, which are replicas of the specified source storage objects (SourceElements).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4111d4a8-a239-469f-a580-196186428955
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CreateListReplica method iSCSI Software Target API
- CreateListReplica method iSCSI Software Target API , CIM_ReplicationService class
- CIM_ReplicationService class iSCSI Software Target API , CreateListReplica method
topic_type:
- apiref
api_name:
- CIM_ReplicationService.CreateListReplica
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CreateListReplica method of the CIM\_ReplicationService class

Create (or start a job to create) new storage objects, which are replicas of the specified source storage objects (SourceElements). Note that using the input parameter, SyncType, this function can be used to instantiate the replicas, and to create an ongoing association between the source and replica elements. If 0 is returned, the function completed successfully and no ConcreteJob instance created. If 4096/0x1000 is returned, a ConcreteJob is started, a reference to which is returned in the Job output parameter.

## Syntax


```mof
uint32 CreateListReplica(
  [in]      string                     ElementNames[],
  [in]      uint16                     SyncType,
  [in]      uint16                     Mode,
  [in]      CIM_LogicalElement     REF SourceElements[],
  [in]      CIM_ServiceAccessPoint REF SourceAccessPoint,
  [in, out] CIM_LogicalElement     REF TargetElements[],
  [in]      CIM_ServiceAccessPoint REF TargetAccessPoint,
  [in]      string                     ReplicationSettingData,
  [out]     CIM_ConcreteJob        REF Job,
  [out]     CIM_Synchronized       REF Synchronizations[],
  [in]      CIM_SettingData        REF TargetSettingGoal,
  [in]      CIM_ResourcePool       REF TargetPool,
  [in]      uint16                     WaitForCopyState
);
```



## Parameters

<dl> <dt>

*ElementNames* \[in\]
</dt> <dd>

An array of end user relevant names for the elements being created. If NULL, then a system supplied name is used. The value will be stored in the 'ElementName' property for the created element. The first element of the array ElementNames is assigned to the first replica, the second element to the second replica and so on. If there are more SourceElements entries than ElementNames, the system supplied name is used.

</dd> <dt>

*SyncType* \[in\]
</dt> <dd>

SyncType describes the type of copy that will be made. The same SyncType applies to all elements in the list.

<dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>0 5</dd> <dt>

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


</dt> <dd>9 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl> </dd> <dt>

*Mode* \[in\]
</dt> <dd>

Mode describes whether the target elements will be updated synchronously or asynchronously. If NULL, the implementation decides the mode. The same Mode applies to all elements in the list.

<dt>

<span id="Synchronous"></span><span id="synchronous"></span><span id="SYNCHRONOUS"></span>

**Synchronous** (2)


</dt> <dd></dd> <dt>

<span id="Asynchronous"></span><span id="asynchronous"></span><span id="ASYNCHRONOUS"></span>

**Asynchronous** (3)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>4 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl> </dd> <dt>

*SourceElements* \[in\]
</dt> <dd>

A list of source storage objects which may be StorageVolumes or other storage objects. All the source elements shall be of the same type -- for example, all StorageVolumes.

</dd> <dt>

*SourceAccessPoint* \[in\]
</dt> <dd>

Reference to source access point information. If NULL, service does not need access information to access the source element. This parameter applies to all elements in the source list.

</dd> <dt>

*TargetElements* \[in, out\]
</dt> <dd>

Optionally, as an input, refers to the target elements to use. If specified, the elements will match one to one with SourceElements\[\]. As an output, refers to the created target storage elements (i.e., the replicas). If a job is created, the target elements may not be available immediately.

</dd> <dt>

*TargetAccessPoint* \[in\]
</dt> <dd>

Reference to target access point information. If NULL, service does not need access information to access the target elements. This parameter applies to all elements in the target list.

</dd> <dt>

*ReplicationSettingData* \[in\]
</dt> <dd>

If provided, it overrides the default replication setting data for the given SyncType. If not provided, the provider uses the default replication setting data. The same ReplicationSettingData applies to all SourceElements entries.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

Reference to the job (may be NULL if job is completed).

</dd> <dt>

*Synchronizations* \[out\]
</dt> <dd>

Reference to the created associations between the source and the target elements. If a job is created, this parameter may be NULL unless the associations are actually formed.

</dd> <dt>

*TargetSettingGoal* \[in\]
</dt> <dd>

The definition for the SettingData to be maintained by the target storage objects (the replicas). If the target elements are supplied, this parameter shall be NULL. This parameter applies to all elements in the target list.

</dd> <dt>

*TargetPool* \[in\]
</dt> <dd>

The underlying storage for the target elements (the replicas) will be drawn from TargetPool if specified, otherwise the allocation is implementation specific. If the target elements are supplied, this parameter shall be NULL. This parameter applies to all elements in the target list.

</dd> <dt>

*WaitForCopyState* \[in\]
</dt> <dd>

Method must wait until this CopyState is reached before returning. Only a subset of valid CopyStates apply. For example, Initialized: Associations have been established, but there is no data flow. Inactive: Initialization is complete, but the copy operation remains idle until it is activated. Synchronized: Replicas are an exact copy of the sources. UnSynchronized: Copy operation is in progress. If this parameter is supplied, then all the created replication relationships shall have this supplied CopyState before the method returns.

</dd> </dl>

## Return value

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

 

 





