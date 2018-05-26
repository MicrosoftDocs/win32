---
title: CreateSynchronizationAspect method of the CIM\_ReplicationService class
description: Create (or start a job to create) a new point-in-time representation of a source element.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 036d6ab2-c834-491f-a9eb-4d9c9d96118e
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CreateSynchronizationAspect method iSCSI Software Target API
- CreateSynchronizationAspect method iSCSI Software Target API , CIM_ReplicationService class
- CIM_ReplicationService class iSCSI Software Target API , CreateSynchronizationAspect method
topic_type:
- apiref
api_name:
- CIM_ReplicationService.CreateSynchronizationAspect
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CreateSynchronizationAspect method of the CIM\_ReplicationService class

Create (or start a job to create) a new point-in-time representation of a source element. This representation may be of a form of pointers that keep track of data at the time the point-in-time was created, or a series checkpoints that capture the view of data on the source elements at the time of point-in-time. This method does not include a target element, however, a target element can be added subsequently using the ModifySettingsDefineState method. If the method executes successfully, a SettingsDefineState association is created between the source element and the SynchronizationAspect, which will have the datetime of the point-in-time.

## Syntax


```mof
uint32 CreateSynchronizationAspect(
  [in]  string                      Name,
  [in]  uint16                      SyncType,
  [in]  uint16                      Mode,
  [in]  CIM_ReplicationGroup    REF SourceGroup,
  [in]  CIM_LogicalElement      REF SourceElement,
  [in]  CIM_ServiceAccessPoint  REF SourceAccessPoint,
  [in]  uint16                      Consistency,
  [in]  string                      ReplicationSettingData,
  [out] CIM_ConcreteJob         REF Job,
  [out] CIM_SettingsDefineState REF SettingsState
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

A end user relevant name for the element or relationship being created. If NULL, then a system supplied default name can be used. The value will be stored in the ElementName or relationship name depending on whether an element is created or a group.

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

*SourceGroup* \[in\]
</dt> <dd>

A group of source storage objects which may be a StorageVolume or storage object. If this parameter is not supplied, SourceElement is required. Both SourceGroup and SourceElement shall not be supplied.

</dd> <dt>

*SourceElement* \[in\]
</dt> <dd>

The source storage object which may be a StorageVolume or storage object. If this parameter is not supplied, SourceGroup is required. Both SourceGroup and SourceElement shall not be supplied.

</dd> <dt>

*SourceAccessPoint* \[in\]
</dt> <dd>

Reference to source access point information. If NULL, service does not need access information to access the source element/group.

</dd> <dt>

*Consistency* \[in\]
</dt> <dd>

Overrides the default group consistency.

<dt>

<span id="No_Consistency"></span><span id="no_consistency"></span><span id="NO_CONSISTENCY"></span>

**No Consistency** (2)


</dt> <dd></dd> <dt>

<span id="Sequential_Consistency"></span><span id="sequential_consistency"></span><span id="SEQUENTIAL_CONSISTENCY"></span>

**Sequential Consistency** (3)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>4 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl> </dd> <dt>

*ReplicationSettingData* \[in\]
</dt> <dd>

If provided, it overrides the default replication setting data for the given SyncType. If not provided, the management server uses the default replication setting data.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

Reference to the job (may be NULL if job is completed).

</dd> <dt>

*SettingsState* \[out\]
</dt> <dd>

Reference to the created association between the source element or group and an instance of SynchronizationAspect. If a job is created, this parameter may be NULL unless the association is actually formed.

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

 

 





