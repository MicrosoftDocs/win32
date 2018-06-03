---
title: CreateSynchronizationAspect method of the MSISCSITARGET\_ReplicationService class
description: Creates a new representation of a source element as it currently exists.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f7259c28-2f48-4d25-a9c1-75e09ac52705
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CreateSynchronizationAspect method iSCSI Software Target API
- CreateSynchronizationAspect method iSCSI Software Target API , MSISCSITARGET_ReplicationService class
- MSISCSITARGET_ReplicationService class iSCSI Software Target API , CreateSynchronizationAspect method
topic_type:
- apiref
api_name:
- MSISCSITARGET_ReplicationService.CreateSynchronizationAspect
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreateSynchronizationAspect method of the MSISCSITARGET\_ReplicationService class

Creates a new representation of a source element as it currently exists.

This method does not include a target element; however, a target element can be added by using the [**ModifySettingsDefineState**](modifysettingsdefinestate-msiscsitarget-replicationservice.md) method. If the method succeeds, a [**CIM\_SettingsDefineState**](https://msdn.microsoft.com/library/cc136915) association is created between the source element and the synchronization aspect instance.

This method is inherited from the **CIM\_ReplicationService** class.

## Syntax


```mof
uint32 CreateSynchronizationAspect(
  [in, optional] string                      Name,
  [in]           uint16                      SyncType,
  [in, optional] uint16                      Mode,
  [in]           CIM_ReplicationGroup Ref    SourceGroup,
  [in]           CIM_LogicalElement Ref      SourceElement,
  [in, optional] CIM_ServiceAccessPoint Ref  SourceAccessPoint,
  [in, optional] uint16                      Consistency,
  [in, optional] string                      ReplicationSettingData,
  [out]          CIM_ConcreteJob Ref         Job,
  [out]          CIM_SettingsDefineState Ref SettingsState
);
```



## Parameters

<dl> <dt>

*Name* \[in, optional\]
</dt> <dd>

Specifies a name that is meaningful to the user for the element or relationship to be created. If **NULL**, a system-supplied default name is used. The value is stored in the **ElementName** property or the relationship name, depending on whether an element or a group is created.

</dd> <dt>

*SyncType* \[in\]
</dt> <dd>

Specifies the type of copy to be made. Required.

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

Specifies whether the target elements is updated synchronously or asynchronously. If **NULL**, the implementation decides the mode.

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

*SourceGroup* \[in\]
</dt> <dd>

Specifies a group of source storage objects, which can be [**MSISCSITARGET\_StorageVolume**](msiscsitarget-storagevolume.md) objects or other storage objects. Required.

If this parameter is **NULL**, the *SourceElement* parameter is required. You cannot specify both the *SourceGroup* and the *SourceElement* parameters.

</dd> <dt>

*SourceElement* \[in\]
</dt> <dd>

Specifies the source storage object, which can be a [**MSISCSITARGET\_StorageVolume**](msiscsitarget-storagevolume.md) object or a storage object.

If this parameter is **NULL**, the *SourceGroup* parameter is required. You cannot specify both the *SourceGroup* and the *SourceElement* parameters.

</dd> <dt>

*SourceAccessPoint* \[in, optional\]
</dt> <dd>

Specifies source access point information. Can be **NULL**, if the service does not require access information to access the source element.

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

</dd> <dt>

*Job* \[out\]
</dt> <dd>

On return, contains a reference to the job, which can be **NULL**, if the job is completed.

</dd> <dt>

*SettingsState* \[out\]
</dt> <dd>

On return, contains a reference to the created association between the source element or group and an instance of synchronization aspect. If a job is created, this parameter can be **NULL**, if the association is not actually formed.

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

**Method Reserved** (4097 0x7FFF)
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

[**ModifySettingsDefineState**](modifysettingsdefinestate-msiscsitarget-replicationservice.md)
</dt> <dt>

[**MSISCSITARGET\_StorageVolume**](msiscsitarget-storagevolume.md)
</dt> </dl>

 

 





