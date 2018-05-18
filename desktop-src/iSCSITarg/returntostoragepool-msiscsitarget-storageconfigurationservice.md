---
title: ReturnToStoragePool method of the MSISCSITARGET\_StorageConfigurationService class
description: Starts a job to delete an element that was previously created from a MSISCSITARGET\_StoragePool instance and returns the freed space to the storage pool.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '8b880b01-49c4-43a8-a00a-1e10f420ca89'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["ReturnToStoragePool method iSCSI Software Target API", "ReturnToStoragePool method iSCSI Software Target API , MSISCSITARGET_StorageConfigurationService class", "MSISCSITARGET_StorageConfigurationService class iSCSI Software Target API , ReturnToStoragePool method"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_StorageConfigurationService.ReturnToStoragePool
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
---

# ReturnToStoragePool method of the MSISCSITARGET\_StorageConfigurationService class

Starts a job to delete an element that was previously created from a [**MSISCSITARGET\_StoragePool**](msiscsitarget-storagepool.md) instance and returns the freed space to the storage pool.

This method overrides the method inherited from the **CIM\_StorageConfigurationService** class.

## Syntax


```mof
uint32 ReturnToStoragePool(
  [out] CIM_ConcreteJob    REF Job,
  [in]  CIM_LogicalElement REF TheElement
);
```



## Parameters

<dl> <dt>

*Job* \[out\]
</dt> <dd>

On return, contains a reference to the job, if a job is created and not completed.

</dd> <dt>

*TheElement* \[in\]
</dt> <dd>

Specifies the element to return to the [**MSISCSITARGET\_StoragePool**](msiscsitarget-storagepool.md) instance.

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
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSISCSITARGET\_StorageConfigurationService**](msiscsitarget-storageconfigurationservice.md)
</dt> <dt>

[**MSISCSITARGET\_StoragePool**](msiscsitarget-storagepool.md)
</dt> </dl>

 

 





