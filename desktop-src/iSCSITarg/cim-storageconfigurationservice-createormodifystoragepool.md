---
title: CreateOrModifyStoragePool method of the CIM\_StorageConfigurationService class
description: Starts a job to create (or modify) a StoragePool.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3b47b23e-ea8a-4ef9-ae18-901dcab63df6
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CreateOrModifyStoragePool method iSCSI Software Target API
- CreateOrModifyStoragePool method iSCSI Software Target API , CIM_StorageConfigurationService class
- CIM_StorageConfigurationService class iSCSI Software Target API , CreateOrModifyStoragePool method
topic_type:
- apiref
api_name:
- CIM_StorageConfigurationService.CreateOrModifyStoragePool
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreateOrModifyStoragePool method of the CIM\_StorageConfigurationService class

Starts a job to create (or modify) a StoragePool. The StoragePool will be (or must be) scoped to the same System as this Service. One of the parameters for this method is Size. As an input parameter, Size specifies the desired size of the pool. As an output parameter, it specifies the size achieved. Space is taken from either or both of the specified input StoragePools and StorageExtents (InPools and InExtents). The capability requirements that the Pool must support are defined using the Goal parameter. If the requested pool size cannot be created, no action will be taken, the Return Value will be 4097/0x1001, and the output value of Size will be set to the nearest possible size. If 0 is returned, then the task completed successfully and the use of ConcreteJob was not required. If the task will take some time to complete, a ConcreteJob will be created and its reference returned in the output parameter Job.

## Syntax


```mof
uint32 CreateOrModifyStoragePool(
  [in]      string                 ElementName,
  [out]     CIM_ConcreteJob    REF Job,
  [in]      CIM_StorageSetting REF Goal,
  [in, out] uint64                 Size,
  [in]      string                 InPools[],
  [in]      string                 InExtents[],
  [in, out] CIM_StoragePool    REF Pool
);
```



## Parameters

<dl> <dt>

*ElementName* \[in\]
</dt> <dd>

A end user relevant name for the pool being created. If NULL, then a system supplied default name can be used. The value will be stored in the 'ElementName' property for the created pool. If not NULL, this parameter will supply a new name when modifying an existing pool.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

Reference to the job (may be null if job completed).

</dd> <dt>

*Goal* \[in\]
</dt> <dd>

Reference to an instance of StorageSetting that defines the desired capabilities of the StoragePool. If set to a null value, the default configuration from the source pool will be used. If not NULL, this parameter will supply a new Goal setting when modifying an existing pool.

</dd> <dt>

*Size* \[in, out\]
</dt> <dd>

As an input parameter this specifies the desired pool size in bytes. As an output parameter this specifies the size achieved.

</dd> <dt>

*InPools* \[in\]
</dt> <dd>

Array of strings containing representations of references to CIM\_StoragePool instances, that are used to create the Pool or modify the source pools.

</dd> <dt>

*InExtents* \[in\]
</dt> <dd>

Array of strings containing representations of references to CIM\_StorageExtent instances, that are used to create the Pool or modify the source extents.

</dd> <dt>

*Pool* \[in, out\]
</dt> <dd>

As an input parameter: if null, creates a new StoragePool. If not null, modifies the referenced Pool. When returned, it is a reference to the resulting StoragePool.

</dd> </dl>

## Return value

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
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_StorageConfigurationService**](cim-storageconfigurationservice.md)
</dt> </dl>

 

 





