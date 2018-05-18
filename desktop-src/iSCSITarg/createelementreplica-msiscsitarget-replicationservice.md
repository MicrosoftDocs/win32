---
title: CreateElementReplica method of the MSISCSITARGET\_ReplicationService class
description: Creates or starts a job to create a new storage object that is a replica of the specified source storage object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '262858ec-ba7a-4e34-8d54-d4795f9f8ac5'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CreateElementReplica method iSCSI Software Target API", "CreateElementReplica method iSCSI Software Target API , MSISCSITARGET_ReplicationService class", "MSISCSITARGET_ReplicationService class iSCSI Software Target API , CreateElementReplica method"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_ReplicationService.CreateElementReplica
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
---

# CreateElementReplica method of the MSISCSITARGET\_ReplicationService class

Creates or starts a job to create a new storage object that is a replica of the specified source storage object. This method can be used to instantiate the replica and to create an ongoing association between the source and the replica by using the *SyncType* input parameter.

This method overrides the method inherited from the **CIM\_ReplicationService** class.

## Syntax


```mof
uint32 CreateElementReplica(
  [in]      string                     ElementName,
  [in]      uint16                     SyncType,
  [in]      uint16                     Mode,
  [in]      CIM_LogicalElement     REF SourceElement,
  [in]      CIM_ServiceAccessPoint REF SourceAccessPoint,
  [in, out] CIM_LogicalElement     REF TargetElement,
  [in]      CIM_ServiceAccessPoint REF TargetAccessPoint,
  [in]      string                     ReplicationSettingData,
  [out]     CIM_ConcreteJob        REF Job,
  [out]     CIM_Synchronized       REF Synchronization,
  [in]      CIM_SettingData        REF TargetSettingGoal,
  [in]      CIM_ResourcePool       REF TargetPool,
  [in]      uint16                     WaitForCopyState
);
```



## Parameters

<dl> <dt>

*ElementName* \[in\]
</dt> <dd>

Specifies a name that is meaningful to the end user for the element that is being created. If **NULL**, then a system-supplied default name can be used. The value is stored in the **ElementName** property for the created element.

</dd> <dt>

*SyncType* \[in\]
</dt> <dd>

Specifies the type of copy to be made. Required.

The possible values are.

<dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>0–5</dd> <dt>

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


</dt> <dd>9–32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 = *value* </dd> </dl> </dd> <dt>

*Mode* \[in\]
</dt> <dd>

Specifies whether the target elements is to be updated synchronously or asynchronously. If **NULL**, the implementation determines the mode.

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


</dt> <dd>4–32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 = *value* </dd> </dl> </dd> <dt>

*SourceElement* \[in\]
</dt> <dd>

Specifies the source storage object that can be a [**MSISCSITARGET\_StorageVolume**](msiscsitarget-storagevolume.md) or storage object. Required.

</dd> <dt>

*SourceAccessPoint* \[in\]
</dt> <dd>

Specifies source access point information. Can be **NULL**, if the service does not require access information to access the source element.

</dd> <dt>

*TargetElement* \[in, out\]
</dt> <dd>

On input, optionally specifies a target element to use. On return, contains a reference to the created target storage element, the replica. If a job is created, the target element might not be available immediately.

</dd> <dt>

*TargetAccessPoint* \[in\]
</dt> <dd>

Specifies target access point information. Can be **NULL**, if the service does not require access information to access the target elements.

</dd> <dt>

*ReplicationSettingData* \[in\]
</dt> <dd>

If provided, specifies the replication setting data for the given *SyncType* input parameter in the form of an embedded **CIM\_ReplicationSettingData** instance. If not provided, the management server uses the default replication setting data. Optional.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

On return, contains a reference to the job. Can be **NULL**, if the job is completed.

</dd> <dt>

*Synchronization* \[out\]
</dt> <dd>

On return, contains a reference to the created association between the source and the target element. If a job is created, this parameter can be **NULL** unless the association is actually formed.

</dd> <dt>

*TargetSettingGoal* \[in\]
</dt> <dd>

Specifies configuration-related and operational parameters for the target storage object, the replica. If a *TargetElement* parameter is supplied, this parameter must be **NULL**.

</dd> <dt>

*TargetPool* \[in\]
</dt> <dd>

Specifies the underlying storage for the target element if specified; otherwise the allocation is implementation-specific. If a *TargetElement* parameter is supplied, this parameter must be **NULL**.

</dd> <dt>

*WaitForCopyState* \[in\]
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

**DMTF Reserved** (7–4095)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Method Reserved** (4097–32767)
</dt> <dt>

**Vendor Specific** (32768 = *value* )
</dt> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSISCSITARGET\_ReplicationService**](msiscsitarget-replicationservice.md)
</dt> <dt>

[**MSISCSITARGET\_StorageVolume**](msiscsitarget-storagevolume.md)
</dt> </dl>

 

 





