---
title: CreateOrModifyStoragePool method of the MSISCSITARGET\_StorageConfigurationService class
description: Creates or modifies a MSISCSITARGET\_StoragePool instance, or starts a job to do so.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '52ce89d2-6a6d-46b8-8963-6c579e9393a4'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CreateOrModifyStoragePool method iSCSI Software Target API", "CreateOrModifyStoragePool method iSCSI Software Target API , MSISCSITARGET_StorageConfigurationService class", "MSISCSITARGET_StorageConfigurationService class iSCSI Software Target API , CreateOrModifyStoragePool method"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_StorageConfigurationService.CreateOrModifyStoragePool
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
---

# CreateOrModifyStoragePool method of the MSISCSITARGET\_StorageConfigurationService class

Creates or modifies a [**MSISCSITARGET\_StoragePool**](msiscsitarget-storagepool.md) instance, or starts a job to do so. This method can only create or modify a storage pool instance in the same system scope as this [**MSISCSITARGET\_StorageConfigurationService**](msiscsitarget-storageconfigurationservice.md) instance.

This method is inherited from the **CIM\_StorageConfigurationService** class.

## Syntax


```mof
uint32 CreateOrModifyStoragePool(
  [in]      string                 ElementName,
  [out]     CIM_ConcreteJob Ref    Job,
  [in]      CIM_StorageSetting Ref Goal,
  [in, out] uint64                 Size,
  [in]      string                 InPools[],
  [in]      string                 InExtents[],
  [in, out] CIM_StoragePool Ref    Pool
);
```



## Parameters

<dl> <dt>

*ElementName* \[in\]
</dt> <dd>

Specifies an end-user relevant name for the pool to be created. The value is propagated to the **ElementName** property of the created pool. If **NULL**, a system-supplied default name is used.

If not **NULL** when modifying an existing pool, specifies a new name for the modified pool.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

On return, contains a reference to the job, if a job is created and not completed.

</dd> <dt>

*Goal* \[in\]
</dt> <dd>

Specifies the characteristics, qualities of service, and goals for the element to maintain. If **NULL**, the default configuration from the source pool is used.

If not **NULL** when modifying an existing element, specifies a new goal for the modified element.

</dd> <dt>

*Size* \[in, out\]
</dt> <dd>

On input, specifies the wanted size in bytes. If not **NULL** when modifying an existing element, specifies a new size.

On output, indicates the actual size created.

</dd> <dt>

*InPools* \[in\]
</dt> <dd>

Specifies, in the form of string representations, the component [**MSISCSITARGET\_StoragePool**](msiscsitarget-storagepool.md) instances that are used to compose the resulting **MSISCSITARGET\_StoragePool** instance.

</dd> <dt>

*InExtents* \[in\]
</dt> <dd>

Specifies, in the form of string representations, the component **CIM\_StorageExtent** instances that are used to compose the resulting [**MSISCSITARGET\_StoragePool**](msiscsitarget-storagepool.md) instance.

</dd> <dt>

*Pool* \[in, out\]
</dt> <dd>

On input, specifies a [**MSISCSITARGET\_StoragePool**](msiscsitarget-storagepool.md) instance to modify, or if **NULL**, specifies to create a new instance.

On output, contains a reference to the created or modified storage pool.

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

**Size Not Supported** (4097)
</dt> <dt>

**Method Reserved** (4098–32767)
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
</dt> </dl>

 

 





