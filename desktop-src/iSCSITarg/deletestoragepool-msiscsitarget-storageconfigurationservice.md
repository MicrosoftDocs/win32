---
title: DeleteStoragePool method of the MSISCSITARGET\_StorageConfigurationService class
description: Deletes or starts a job to delete a MSISCSITARGET\_StoragePool instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '082d3513-611e-490e-bd8f-36f0e4e7cf12'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DeleteStoragePool method iSCSI Software Target API", "DeleteStoragePool method iSCSI Software Target API , MSISCSITARGET_StorageConfigurationService class", "MSISCSITARGET_StorageConfigurationService class iSCSI Software Target API , DeleteStoragePool method"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_StorageConfigurationService.DeleteStoragePool
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
---

# DeleteStoragePool method of the MSISCSITARGET\_StorageConfigurationService class

Deletes or starts a job to delete a [**MSISCSITARGET\_StoragePool**](msiscsitarget-storagepool.md) instance. The freed space is returned to the source storage pools, which are indicated by [**MSISCSITARGET\_AllocatedFromStoragePool**](msiscsitarget-allocatedfromstoragepool.md) associations, or returned back to underlying storage extent instances.

This method is inherited from the **CIM\_StorageConfigurationService** class.

## Syntax


```mof
uint32 DeleteStoragePool(
  [out] CIM_ConcreteJob Ref Job,
  [in]  CIM_StoragePool Ref Pool
);
```



## Parameters

<dl> <dt>

*Job* \[out\]
</dt> <dd>

On return, contains a reference to the job, if a job is created and not completed.

</dd> <dt>

*Pool* \[in\]
</dt> <dd>

Specifies the pool to delete.

</dd> </dl>

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

**DMTF Reserved** (7–4095)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Method Reserved** (4097–32767)
</dt> <dt>

**Vendor Specific** (32768–65535)
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
</dt> <dt>

[**MSISCSITARGET\_StoragePool**](msiscsitarget-storagepool.md)
</dt> </dl>

 

 





