---
title: CreateReplicationBuffer method of the CIM\_StorageConfigurationService class
description: Create (or start a job to create) a replication buffer that buffers asynchronous write operations for remote mirror pairs.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1cddd39b-5378-487e-93c1-d3aa4600f7b7
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CreateReplicationBuffer method iSCSI Software Target API
- CreateReplicationBuffer method iSCSI Software Target API , CIM_StorageConfigurationService class
- CIM_StorageConfigurationService class iSCSI Software Target API , CreateReplicationBuffer method
topic_type:
- apiref
api_name:
- CIM_StorageConfigurationService.CreateReplicationBuffer
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CreateReplicationBuffer method of the CIM\_StorageConfigurationService class

Create (or start a job to create) a replication buffer that buffers asynchronous write operations for remote mirror pairs. The buffer is an instance of CIM\_Memory with an AssociatedMemory association to a hosting system or to a replication network pipe. The buffer element may be created based on a StorageExtent, in a pool or in a manner opaque to a client. If 0 is returned, the function completed successfully and no ConcreteJob instance is created. If 0x1000 is returned, a ConcreteJob is started, a reference to which is returned in the Job output parameter. A return value of 1 indicates the method is not supported. All other values indicate some type of error condition.

If Job Completed with No Error (0) is returned, the function completed successfully and a ConcreteJob instance is not created.

If Method Parameters Checked - Job Started (0x1000) is returned, a ConcreteJob is started, a reference to which is returned in the Job output parameter.

A return value of Not Supported (1) indicates the method is not supported.

All other values indicate some type of error condition.

## Syntax


```mof
uint32 CreateReplicationBuffer(
  [out] CIM_ConcreteJob    REF Job,
  [in]  CIM_ManagedElement REF Host,
  [in]  CIM_StorageExtent  REF TargetElement,
  [in]  CIM_StoragePool    REF TargetPool,
  [out] CIM_Memory         REF ReplicaBuffer
);
```



## Parameters

<dl> <dt>

*Job* \[out\]
</dt> <dd>

Reference to the job (may be null if the task completed).

</dd> <dt>

*Host* \[in\]
</dt> <dd>

The hosting system or replication pipe that will be antecedent to the created buffer.

</dd> <dt>

*TargetElement* \[in\]
</dt> <dd>

Reference to a component extent for the buffer element.

</dd> <dt>

*TargetPool* \[in\]
</dt> <dd>

Reference to a container pool for the buffer element.

</dd> <dt>

*ReplicaBuffer* \[out\]
</dt> <dd>

Reference to the created replica buffer element.

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

 

 





