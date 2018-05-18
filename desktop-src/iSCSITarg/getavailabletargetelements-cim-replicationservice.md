---
title: GetAvailableTargetElements method of the CIM\_ReplicationService class
description: Get (or start a job to get) all of the candidate target elements for the supplied source element. If a job is started, once the job completes, examine the AffectedJobElement associations for candidate targets.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '16e405ea-7bb6-4dc3-9df6-57dabfcd717b'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetAvailableTargetElements method iSCSI Software Target API", "GetAvailableTargetElements method iSCSI Software Target API , CIM_ReplicationService class", "CIM_ReplicationService class iSCSI Software Target API , GetAvailableTargetElements method"]
topic_type:
- apiref
api_name:
- CIM_ReplicationService.GetAvailableTargetElements
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
---

# GetAvailableTargetElements method of the CIM\_ReplicationService class

Get (or start a job to get) all of the candidate target elements for the supplied source element. If a job is started, once the job completes, examine the AffectedJobElement associations for candidate targets.

## Syntax


```mof
uint32 GetAvailableTargetElements(
  [in]  CIM_LogicalElement     REF SourceElement,
  [in]  uint16                     SyncType,
  [in]  uint16                     Mode,
  [in]  string                     ReplicationSettingData,
  [in]  CIM_ServiceAccessPoint REF TargetAccessPoint,
  [in]  CIM_SettingData        REF TargetSettingGoal,
  [in]  CIM_ResourcePool       REF TargetPools[],
  [out] CIM_ConcreteJob        REF Job,
  [out] CIM_LogicalElement     REF Candidates[]
);
```



## Parameters

<dl> <dt>

*SourceElement* \[in\]
</dt> <dd>

The source storage object which may be a StorageVolume or storage object.

</dd> <dt>

*SyncType* \[in\]
</dt> <dd>

SyncType describes the type of copy.

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


</dt> <dd>32768–65535</dd> </dl> </dd> <dt>

*Mode* \[in\]
</dt> <dd>

Mode describes whether the target elements will be updated synchronously or asynchronously. If NULL, the implementation decides.

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


</dt> <dd>32768–65535</dd> </dl> </dd> <dt>

*ReplicationSettingData* \[in\]
</dt> <dd>

If provided, it overrides the default replication setting data for the given SyncType. If not provided, the management server uses the default replication setting data.

</dd> <dt>

*TargetAccessPoint* \[in\]
</dt> <dd>

Reference to access point information. If NULL, only local system is examined.

</dd> <dt>

*TargetSettingGoal* \[in\]
</dt> <dd>

Desired target SettingData. If NULL, settings of the source element will be used.

</dd> <dt>

*TargetPools* \[in\]
</dt> <dd>

The storage pools for the target elements. If NULL, all storage pools (on the given system) will be examined.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

Reference to the job (may be NULL if the task completed).

</dd> <dt>

*Candidates* \[out\]
</dt> <dd>

The list of the candidate target elements.

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

**DMTF Reserved** (7–4095)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Method Reserved** (4097–32767)
</dt> <dt>

**Vendor Specific** (32768–4294967295)
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

**CIM\_ReplicationService**
</dt> </dl>

 

 





