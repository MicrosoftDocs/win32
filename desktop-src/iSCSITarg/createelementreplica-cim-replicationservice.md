---
title: CreateElementReplica method of the CIM\_ReplicationService class
description: Create (or start a job to create) a new storage object, which is a replica of the specified source storage object (SourceElement).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 23cddc68-1d06-4783-a73a-5594b62094ac
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CreateElementReplica method iSCSI Software Target API
- CreateElementReplica method iSCSI Software Target API , CIM_ReplicationService class
- CIM_ReplicationService class iSCSI Software Target API , CreateElementReplica method
topic_type:
- apiref
api_name:
- CIM_ReplicationService.CreateElementReplica
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CreateElementReplica method of the CIM\_ReplicationService class

Create (or start a job to create) a new storage object, which is a replica of the specified source storage object (SourceElement). Note that using the input parameter, SyncType, this function can be used to instantiate the replica, and to create an ongoing association between the source and replica. If 0 is returned, the function completed successfully and no ConcreteJob instance created. If 4096/0x1000 is returned, a ConcreteJob is started, a reference to which is returned in the Job output parameter.

## Syntax


```mof
uint32 CreateElementReplica(
  [in]      string                     ElementName,
  [in]      uint16                     SyncType,
  [in]      uint16                     Mode,
  [in]      CIM_LogicalElement     REF SourceElement,
  [in]      CIM_ServiceAccessPoint REF SourceAccessPoint,
  [in, out] CIM_LogicalElement     REF TargetElement,
  [in]      CIM_ServiceAccessPoint REF TargetAccessPoint,
  [in]      string                     ReplicationSettingData,
  [out]     CIM_ConcreteJob        REF Job,
  [out]     CIM_Synchronized       REF Synchronization,
  [in]      CIM_SettingData        REF TargetSettingGoal,
  [in]      CIM_ResourcePool       REF TargetPool,
  [in]      uint16                     WaitForCopyState
);
```



## Parameters

<dl> <dt>

*ElementName* \[in\]
</dt> <dd>

A end user relevant name for the element being created. If NULL, then a system supplied default name can be used. The value will be stored in the 'ElementName' property for the created element.

</dd> <dt>

*SyncType* \[in\]
</dt> <dd>

SyncType describes the type of copy that will be made.

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

Mode describes whether the target elements will be updated synchronously or asynchronously. If NULL, implementaton decides the mode.

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

*SourceElement* \[in\]
</dt> <dd>

The source storage object which may be a StorageVolume or storage object.

</dd> <dt>

*SourceAccessPoint* \[in\]
</dt> <dd>

Reference to source access point information. If NULL, service does not need access information to access the source element.

</dd> <dt>

*TargetElement* \[in, out\]
</dt> <dd>

Optionally, as an input, refers to a target element to use. As an output, refers to the created target storage element (i.e., the replica). If a job is created, the target element may not be available immediately.

</dd> <dt>

*TargetAccessPoint* \[in\]
</dt> <dd>

Reference to target access point information. If NULL, service does not need access information to access the target elements.

</dd> <dt>

*ReplicationSettingData* \[in\]
</dt> <dd>

If provided, it overrides the default replication setting data for the given SyncType. If not provided, the management server uses the default replication setting data.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

Reference to the job (may be NULL if job is completed).

</dd> <dt>

*Synchronization* \[out\]
</dt> <dd>

Reference to the created association between the source and the target element. If a job is created, this parameter may be NULL unless the association is actually formed.

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

Method must wait until this CopyState is reached before returning. Only a subset of valid CopyStates apply. For example, Initialized: Associations have been established, but there is no data flow. Inactive: Initialization is complete, but the data flow remains idle until it is activated. Synchronized: Replicas are an exact copy of the source. UnSynchronized: Copy operation is in progress.

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

 

 





