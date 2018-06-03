---
title: DeleteStoragePool method of the CIM\_StorageConfigurationService class
description: Start a job to delete a StoragePool.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 47572019-5b73-459f-a114-ee1f6c5364ef
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DeleteStoragePool method iSCSI Software Target API
- DeleteStoragePool method iSCSI Software Target API , CIM_StorageConfigurationService class
- CIM_StorageConfigurationService class iSCSI Software Target API , DeleteStoragePool method
topic_type:
- apiref
api_name:
- CIM_StorageConfigurationService.DeleteStoragePool
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DeleteStoragePool method of the CIM\_StorageConfigurationService class

Start a job to delete a StoragePool. The freed space is returned source StoragePools (indicated by AllocatedFrom StoragePool) or back to underlying storage extents. If 0 is returned, the function completed successfully, and no ConcreteJob was required. If 4096/0x1000 is returned, a ConcreteJob will be started to delete the StoragePool. A reference to the Job is returned in the Job parameter.

## Syntax


```mof
uint32 DeleteStoragePool(
  [out] CIM_ConcreteJob REF Job,
  [in]  CIM_StoragePool REF Pool
);
```



## Parameters

<dl> <dt>

*Job* \[out\]
</dt> <dd>

Reference to the job (may be null if job completed).

</dd> <dt>

*Pool* \[in\]
</dt> <dd>

Reference to the pool to delete.

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

 

 





