---
title: AttachReplica method of the CIM\_StorageConfigurationService class
description: Create (or start a job to create) a StorageSynchronized relationship between two existing storage objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1b0ea123-6a97-4d55-9ada-3cf2d0103809
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AttachReplica method iSCSI Software Target API
- AttachReplica method iSCSI Software Target API , CIM_StorageConfigurationService class
- CIM_StorageConfigurationService class iSCSI Software Target API , AttachReplica method
topic_type:
- apiref
api_name:
- CIM_StorageConfigurationService.AttachReplica
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AttachReplica method of the CIM\_StorageConfigurationService class

Create (or start a job to create) a StorageSynchronized relationship between two existing storage objects. Note that using the input parameter, CopyType, this function can be used to to create an ongoing association between the source and replica. If 0 is returned, the function completed successfully and no ConcreteJob instance is created. If 0x1000 is returned, a ConcreteJob is started, a reference to which is returned in the Job output parameter. A return value of 1 indicates the method is not supported. All other values indicate some type of error condition.

## Syntax


```mof
uint32 AttachReplica(
  [out] CIM_ConcreteJob    REF Job,
  [in]  CIM_ManagedElement REF SourceElement,
  [in]  CIM_ManagedElement REF TargetElement,
  [in]  uint16                 CopyType
);
```



## Parameters

<dl> <dt>

*Job* \[out\]
</dt> <dd>

Reference to the job (may be null if the task completed).

</dd> <dt>

*SourceElement* \[in\]
</dt> <dd>

The source storage object which may be a StorageVolume or other storage object.

</dd> <dt>

*TargetElement* \[in\]
</dt> <dd>

Reference to the target storage element (i.e., the replica).

</dd> <dt>

*CopyType* \[in\]
</dt> <dd>

CopyType describes the type of Synchronized relationship that will be created. Values are:

Async: Create and maintain an asynchronous copy of the source.

Sync: Create and maintain a synchronized copy of the source.

UnSyncAssoc: Create an unsynchronized copy and maintain an association to the source.

UnSyncUnAssoc: Create unassociated copy of the source element.

<dt>

<span id="Async"></span><span id="async"></span><span id="ASYNC"></span>

**Async** (2)


</dt> <dd></dd> <dt>

<span id="Sync"></span><span id="sync"></span><span id="SYNC"></span>

**Sync** (3)


</dt> <dd></dd> <dt>

<span id="UnSyncAssoc"></span><span id="unsyncassoc"></span><span id="UNSYNCASSOC"></span>

**UnSyncAssoc** (4)


</dt> <dd></dd> <dt>

<span id="UnSyncUnAssoc"></span><span id="unsyncunassoc"></span><span id="UNSYNCUNASSOC"></span>

**UnSyncUnAssoc** (5)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>6 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl> </dd> </dl>

## Return value

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

**DMTF Reserved** (7 4095)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Method Reserved** (4097 32767)
</dt> <dt>

**Vendor Specific** (32768 65535)
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

[**CIM\_StorageConfigurationService**](cim-storageconfigurationservice.md)
</dt> </dl>

 

 





