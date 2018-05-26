---
title: AttachOrModifyReplica method of the CIM\_StorageConfigurationService class
description: Create (or start a job to create) a StorageSynchronized mirror relationship between two storage elements.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 090de9e8-96d9-4f88-ad2b-503650c149e7
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AttachOrModifyReplica method iSCSI Software Target API
- AttachOrModifyReplica method iSCSI Software Target API , CIM_StorageConfigurationService class
- CIM_StorageConfigurationService class iSCSI Software Target API , AttachOrModifyReplica method
topic_type:
- apiref
api_name:
- CIM_StorageConfigurationService.AttachOrModifyReplica
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AttachOrModifyReplica method of the CIM\_StorageConfigurationService class

Create (or start a job to create) a StorageSynchronized mirror relationship between two storage elements. The target element may be a local or a remote storage element. A remote mirror pair may be scoped by a peer-to-peer connection modeled as a NetworkPipe between peers.

If Job Completed with No Error (0) is returned, the function completed successfully and a ConcreteJob instance is not created.

If Method Parameters Checked - Job Started (0x1000) is returned, a ConcreteJob is started, a reference to which is returned in the Job output parameter.

A return value of Not Supported (1) indicates the method is not supported.

All other values indicate some type of error condition.

## Syntax


```mof
uint32 AttachOrModifyReplica(
  [out] CIM_ConcreteJob    REF Job,
  [in]  CIM_ManagedElement REF SourceElement,
  [in]  CIM_ManagedElement REF TargetElement,
  [in]  uint16                 CopyType,
  [in]  string                 Goal,
  [in]  CIM_NetworkPipe    REF ReplicationPipe
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

The source storage element which may be a StorageVolume, StorageExtent, LogicalFile, FileSystem, CommonDatabase, or any other storage object. For this reason, the type is made very generic.

</dd> <dt>

*TargetElement* \[in\]
</dt> <dd>

Reference to the target storage element (i.e., the replica). The target storage element which may be a StorageVolume, StorageExtent, LogicalFile, FileSystem, CommonDatabase, or any other storage object. For this reason, the type is made very generic.

</dd> <dt>

*CopyType* \[in\]
</dt> <dd>

CopyType describes the type of Synchronized relationship that will be created. Values are: Async: Create and maintain an asynchronous copy of the source. Sync: Create and maintain a synchronized copy of the source. UnSyncAssoc: Create an unsynchronized copy and maintain an association to the source element.

UnSyncUnAssoc: Create an unassociated copy of the source element.

UnSyncAssoc and UnSyncUnAssoc are not supported for remote mirror replicas.

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


</dt> <dd>6 4095</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>4096 65535</dd> </dl> </dd> <dt>

*Goal* \[in\]
</dt> <dd>

The StorageSetting properties to be created or modified for the target element.

</dd> <dt>

*ReplicationPipe* \[in\]
</dt> <dd>

The NetworkPipe element that scopes the remote mirror pair. If the value is null, remote mirrors do not require a pre-established connection.

</dd> </dl>

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

 

 





