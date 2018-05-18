---
title: CreateReplicationBuffer method of the MSISCSITARGET\_StorageConfigurationService class
description: Creates a replication buffer that buffers asynchronous write operations for remote mirror pairs. The buffer is a CIM\_Memory instance with an CIM\_AssociatedMemory association to a hosting system or replication network pipe.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e0b87652-e552-4389-bc31-4cf34a455c55'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CreateReplicationBuffer method iSCSI Software Target API", "CreateReplicationBuffer method iSCSI Software Target API , MSISCSITARGET_StorageConfigurationService class", "MSISCSITARGET_StorageConfigurationService class iSCSI Software Target API , CreateReplicationBuffer method"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_StorageConfigurationService.CreateReplicationBuffer
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
---

# CreateReplicationBuffer method of the MSISCSITARGET\_StorageConfigurationService class

Creates a replication buffer that buffers asynchronous write operations for remote mirror pairs. The buffer is a [**CIM\_Memory**](https://msdn.microsoft.com/library/aa387904) instance with an [**CIM\_AssociatedMemory**](https://msdn.microsoft.com/library/aa387183) association to a hosting system or replication network pipe.

This method is inherited from the **CIM\_StorageConfigurationService** class.

## Syntax


```mof
uint32 CreateReplicationBuffer(
  [out] CIM_ConcreteJob Ref    Job,
  [in]  CIM_ManagedElement Ref Host,
  [in]  CIM_StorageExtent Ref  TargetElement,
  [in]  CIM_StoragePool Ref    TargetPool,
  [out] CIM_Memory Ref         ReplicaBuffer
);
```



## Parameters

<dl> <dt>

*Job* \[out\]
</dt> <dd>

On return contains a reference to the job, if a job is created and not completed.

</dd> <dt>

*Host* \[in\]
</dt> <dd>

Specifies the hosting system or replication pipe that is the parent of the created buffer.

</dd> <dt>

*TargetElement* \[in\]
</dt> <dd>

Specifies a component extent for the buffer element.

</dd> <dt>

*TargetPool* \[in\]
</dt> <dd>

Specifies a container pool for the buffer element.

</dd> <dt>

*ReplicaBuffer* \[out\]
</dt> <dd>

On return, contains a reference to the created replica buffer element.

</dd> </dl>

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

**DMTF Reserved** (7–0x0FFF)
</dt> <dt>

**Method Parameters Checked - Job Started** (0x1000)
</dt> <dt>

**Method Reserved** (0x1001–0x7FFF)
</dt> <dt>

**Vendor Specific** (0x8000–0xFFFF)
</dt> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SmIScsiTargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSISCSITARGET\_StorageConfigurationService**](msiscsitarget-storageconfigurationservice.md)
</dt> </dl>

 

 





