---
title: CreateReplica method of the MSISCSITARGET\_StorageConfigurationService class
description: Creates a new storage object which is a replica of the specified source storage object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 218e828f-7baf-471a-b468-7a06dc2aa1b1
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CreateReplica method iSCSI Software Target API
- CreateReplica method iSCSI Software Target API , MSISCSITARGET_StorageConfigurationService class
- MSISCSITARGET_StorageConfigurationService class iSCSI Software Target API , CreateReplica method
topic_type:
- apiref
api_name:
- MSISCSITARGET_StorageConfigurationService.CreateReplica
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreateReplica method of the MSISCSITARGET\_StorageConfigurationService class

Creates a new storage object which is a replica of the specified source storage object.

This method is inherited from the **CIM\_StorageConfigurationService** class.

## Syntax


```mof
uint32 CreateReplica(
  [in]  string                 ElementName,
  [out] CIM_ConcreteJob Ref    Job,
  [in]  CIM_LogicalElement Ref SourceElement,
  [out] CIM_LogicalElement Ref TargetElement,
  [in]  CIM_StorageSetting Ref TargetSettingGoal,
  [in]  CIM_StoragePool Ref    TargetPool,
  [in]  uint16                 CopyType
);
```



## Parameters

<dl> <dt>

*ElementName* \[in\]
</dt> <dd>

A end user relevant name for the element being created. The value will be propagated to the **ElementName** property of the created element. If **NULL**, a system supplied default name is used.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

On return contains a reference to the job, if a job is created and not completed.

</dd> <dt>

*SourceElement* \[in\]
</dt> <dd>

Specifies the source storage object which may be a [**MSISCSITARGET\_StorageVolume**](msiscsitarget-storagevolume.md) or storage object.

</dd> <dt>

*TargetElement* \[out\]
</dt> <dd>

On return, refers to the created replica storage element.

</dd> <dt>

*TargetSettingGoal* \[in\]
</dt> <dd>

Specifies the [**MSISCSITARGET\_StorageSetting**](msiscsitarget-storagesetting.md) used to configure the replica storage object.

</dd> <dt>

*TargetPool* \[in\]
</dt> <dd>

Specifies the underlying storage from which the replica storage object is allocated. If **NULL**, the allocation is implementation specific.

</dd> <dt>

*CopyType* \[in\]
</dt> <dd>

Specifies the type of copy to make.

<dt>

<span id="Async"></span><span id="async"></span><span id="ASYNC"></span>

<span id="Async"></span><span id="async"></span><span id="ASYNC"></span>**Async** (2)


</dt> <dd>

Create and maintain an asynchronous copy of the source.

</dd> <dt>

<span id="Sync"></span><span id="sync"></span><span id="SYNC"></span>

<span id="Sync"></span><span id="sync"></span><span id="SYNC"></span>**Sync** (3)


</dt> <dd>

Create and maintain a synchronized copy of the source.

</dd> <dt>

<span id="UnSyncAssoc"></span><span id="unsyncassoc"></span><span id="UNSYNCASSOC"></span>

<span id="UnSyncAssoc"></span><span id="unsyncassoc"></span><span id="UNSYNCASSOC"></span>**UnSyncAssoc** (4)


</dt> <dd>

Create an unsynchronized copy and maintain an association to the source.

</dd> <dt>

<span id="UnSyncUnAssoc"></span><span id="unsyncunassoc"></span><span id="UNSYNCUNASSOC"></span>

<span id="UnSyncUnAssoc"></span><span id="unsyncunassoc"></span><span id="UNSYNCUNASSOC"></span>**UnSyncUnAssoc** (5)


</dt> <dd>

Create an unsynchronized and disassociated copy of the source element.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd>

Reserved.

</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>**Vendor Specific**


</dt> <dd>

Reserved.

</dd> </dl> </dd> </dl>

## Return value

This method returns one of the following values.

<dl> <dt>

**Job Completed with No Error** (0)
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

**Size Not Supported** (4097)
</dt> <dt>

**Method Reserved** (4098 32767)
</dt> <dt>

**Vendor Specific** (32768 65535)
</dt> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| Header<br/>                   | <dl> <dt>Adojet.h</dt> </dl>              |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SmIScsiTargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSISCSITARGET\_StorageConfigurationService**](msiscsitarget-storageconfigurationservice.md)
</dt> </dl>

 

 





