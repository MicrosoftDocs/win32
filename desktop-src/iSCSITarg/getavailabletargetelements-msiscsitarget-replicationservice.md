---
title: GetAvailableTargetElements method of the MSISCSITARGET\_ReplicationService class
description: Gets all of the available target elements for the supplied source element.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3a528ca4-790c-4fb2-8983-06e2cf060243
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetAvailableTargetElements method iSCSI Software Target API
- GetAvailableTargetElements method iSCSI Software Target API , MSISCSITARGET_ReplicationService class
- MSISCSITARGET_ReplicationService class iSCSI Software Target API , GetAvailableTargetElements method
topic_type:
- apiref
api_name:
- MSISCSITARGET_ReplicationService.GetAvailableTargetElements
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetAvailableTargetElements method of the MSISCSITARGET\_ReplicationService class

Gets all of the available target elements for the supplied source element.

This method is inherited from the **CIM\_ReplicationService** class.

## Syntax


```mof
uint32 GetAvailableTargetElements(
  [in]           CIM_LogicalElement Ref     SourceElement,
  [in]           uint16                     SyncType,
  [in, optional] uint16                     Mode,
  [in, optional] string                     ReplicationSettingData,
  [in, optional] CIM_ServiceAccessPoint Ref TargetAccessPoint,
  [in, optional] CIM_SettingData Ref        TargetSettingGoal,
  [in, optional] CIM_ResourcePool Ref       TargetPools[],
  [out]          CIM_ConcreteJob Ref        Job,
  [out]          CIM_LogicalElement Ref     Candidates[]
);
```



## Parameters

<dl> <dt>

*SourceElement* \[in\]
</dt> <dd>

Specifies the source storage object that can be a **CIM\_StorageVolume** class or a storage object. Required.

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

*ReplicationSettingData* \[in, optional\]
</dt> <dd>

If provided, specifies the replication setting data for the given *SyncType* input parameter in the form of an embedded **CIM\_ReplicationSettingData** instance. If not provided, the management server uses the default replication setting data.

</dd> <dt>

*TargetAccessPoint* \[in, optional\]
</dt> <dd>

Specifies the target access point information. If **NULL**, only the local system is examined.

</dd> <dt>

*TargetSettingGoal* \[in, optional\]
</dt> <dd>

Specifies configuration-related and operational parameters for the target element. If **NULL**, the settings of the source element are used.

</dd> <dt>

*TargetPools* \[in, optional\]
</dt> <dd>

Specifies the storage pools for the target elements to examine. If **NULL**, all storage pools on the given system are examined.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

On return, contains a reference to the job that can be **NULL**, if the job is completed.

If a job is started and after the job is completed, you can examine the [**CIM\_AffectedJobElement**](https://msdn.microsoft.com/library/cc150663) associations for candidate targets.

</dd> <dt>

*Candidates* \[out\]
</dt> <dd>

On return, contains the list of the candidate target elements.

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

[**MSISCSITARGET\_AffectedJobElement**](msiscsitarget-affectedjobelement.md)
</dt> </dl>

 

 





