---
title: AttachReplica method of the MSISCSITARGET\_StorageConfigurationService class
description: Creates a MSISCSITARGET\_StorageSynchronized relationship between two existing storage objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 66859569-701a-4da6-ae27-6e522c5825fa
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AttachReplica method iSCSI Software Target API
- AttachReplica method iSCSI Software Target API , MSISCSITARGET_StorageConfigurationService class
- MSISCSITARGET_StorageConfigurationService class iSCSI Software Target API , AttachReplica method
topic_type:
- apiref
api_name:
- MSISCSITARGET_StorageConfigurationService.AttachReplica
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AttachReplica method of the MSISCSITARGET\_StorageConfigurationService class

Creates a [**MSISCSITARGET\_StorageSynchronized**](msiscsitarget-storagesynchronized.md) relationship between two existing storage objects.

This method is inherited from the **CIM\_StorageConfigurationService** class.

## Syntax


```mof
uint32 AttachReplica(
  [out] CIM_ConcreteJob Ref    Job,
  [in]  CIM_ManagedElement Ref SourceElement,
  [in]  CIM_ManagedElement Ref TargetElement,
  [in]  uint16                 CopyType
);
```



## Parameters

<dl> <dt>

*Job* \[out\]
</dt> <dd>

On return, contains a reference to the job, if a job is created and not completed.

</dd> <dt>

*SourceElement* \[in\]
</dt> <dd>

Specifies the source storage object, which can be a [**MSISCSITARGET\_StorageVolume**](msiscsitarget-storagevolume.md) object or other storage object.

</dd> <dt>

*TargetElement* \[in\]
</dt> <dd>

Specifies the replica storage element.

</dd> <dt>

*CopyType* \[in\]
</dt> <dd>

Specifies the type of copy to make.

<dt>

<span id="Async"></span><span id="async"></span><span id="ASYNC"></span>

<span id="Async"></span><span id="async"></span><span id="ASYNC"></span>**Async** (2)


</dt> <dd>

Creates and maintains an asynchronous copy of the source.

</dd> <dt>

<span id="Sync"></span><span id="sync"></span><span id="SYNC"></span>

<span id="Sync"></span><span id="sync"></span><span id="SYNC"></span>**Sync** (3)


</dt> <dd>

Creates and maintains a synchronized copy of the source.

</dd> <dt>

<span id="UnSyncAssoc"></span><span id="unsyncassoc"></span><span id="UNSYNCASSOC"></span>

<span id="UnSyncAssoc"></span><span id="unsyncassoc"></span><span id="UNSYNCASSOC"></span>**UnSyncAssoc** (4)


</dt> <dd>

Creates an unsynchronized copy and maintains an association to the source.

</dd> <dt>

<span id="UnSyncUnAssoc"></span><span id="unsyncunassoc"></span><span id="UNSYNCUNASSOC"></span>

<span id="UnSyncUnAssoc"></span><span id="unsyncunassoc"></span><span id="UNSYNCUNASSOC"></span>**UnSyncUnAssoc** (5)


</dt> <dd>

Creates an unsynchronized and disassociated copy of the source element.

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

**DMTF Reserved** (7 0x0FFF)
</dt> <dt>

**Method Parameters Checked - Job Started** (0x1000)
</dt> <dt>

**Method Reserved** (0x1001 0x7FFF)
</dt> <dt>

**Vendor Specific** (0x8000 0xFFFF)
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

[**MSISCSITARGET\_StorageConfigurationService**](msiscsitarget-storageconfigurationservice.md)
</dt> </dl>

 

 





