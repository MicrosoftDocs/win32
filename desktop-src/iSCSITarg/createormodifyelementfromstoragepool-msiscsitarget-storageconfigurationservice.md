---
title: CreateOrModifyElementFromStoragePool method of the MSISCSITARGET\_StorageConfigurationService class
description: Starts a job to create or modify a specified element, for example, a MSISCSITARGET\_StorageVolume instance from a MSISCSITARGET\_StoragePool instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9781afcf-95d8-4b04-becd-af5dd2308a0d
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CreateOrModifyElementFromStoragePool method iSCSI Software Target API
- CreateOrModifyElementFromStoragePool method iSCSI Software Target API , MSISCSITARGET_StorageConfigurationService class
- MSISCSITARGET_StorageConfigurationService class iSCSI Software Target API , CreateOrModifyElementFromStoragePool method
topic_type:
- apiref
api_name:
- MSISCSITARGET_StorageConfigurationService.CreateOrModifyElementFromStoragePool
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CreateOrModifyElementFromStoragePool method of the MSISCSITARGET\_StorageConfigurationService class

Starts a job to create or modify a specified element, for example, a [**MSISCSITARGET\_StorageVolume**](msiscsitarget-storagevolume.md) instance from a [**MSISCSITARGET\_StoragePool**](msiscsitarget-storagepool.md) instance.

This method is inherited from the **CIM\_StorageConfigurationService** class.

## Syntax


```mof
uint32 CreateOrModifyElementFromStoragePool(
  [in]      string                 ElementName,
  [in]      uint16                 ElementType,
  [out]     CIM_ConcreteJob    REF Job,
  [in]      CIM_ManagedElement REF Goal,
  [in, out] uint64                 Size,
  [in]      CIM_StoragePool    REF InPool,
  [in, out] CIM_LogicalElement REF TheElement
);
```



## Parameters

<dl> <dt>

*ElementName* \[in\]
</dt> <dd>

Specifies an end-user relevant name for the element to be created. The value is propagated to the **ElementName** property of the created element. If **NULL**, a system-supplied default name is used.

If not **NULL** when modifying an existing element, specifies a new name for the element that is modified.

</dd> <dt>

*ElementType* \[in\]
</dt> <dd>

Specifies the type of element that is being created or modified. When modifying an element that is specified in the *TheElement* parameter, this value must match the type of the specified instance.

The possible values are.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Reserved"></span><span id="reserved"></span><span id="RESERVED"></span>

**Reserved** (1)


</dt> <dd></dd> <dt>

<span id="StorageVolume"></span><span id="storagevolume"></span><span id="STORAGEVOLUME"></span>

**StorageVolume** (2)


</dt> <dd></dd> <dt>

<span id="StorageExtent"></span><span id="storageextent"></span><span id="STORAGEEXTENT"></span>

**StorageExtent** (3)


</dt> <dd></dd> <dt>

<span id="LogicalDisk"></span><span id="logicaldisk"></span><span id="LOGICALDISK"></span>

**LogicalDisk** (4)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>5 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl> </dd> <dt>

*Job* \[out\]
</dt> <dd>

On return, contains a reference to the job, if a job is created and not completed.

</dd> <dt>

*Goal* \[in\]
</dt> <dd>

Specifies the characteristics, qualities of service, and goals for the element to maintain. If **NULL**, the default configuration from the source pool is used. Use a setting or profile instance, such as a [**MSISCSITARGET\_StorageSetting**](msiscsitarget-storagesetting.md) instance that is appropriate for the element to be created.

If not **NULL** when modifying an existing element, specifies a new goal for the modified element.

</dd> <dt>

*Size* \[in, out\]
</dt> <dd>

On input, specifies the wanted size in bytes. If not **NULL** when modifying an existing element, specifies a new size.

On output, indicates the actual size created.

If the requested size cannot be created, no action is performed.

</dd> <dt>

*InPool* \[in\]
</dt> <dd>

Specifies the pool from which to create the element. Must be **NULL** if an existing element is specified in the *TheElement* parameter.

</dd> <dt>

*TheElement* \[in, out\]
</dt> <dd>

On input, specifies an element to modify, or if **NULL**, specifies to create a new element.

On output, contains a reference to the created or modified element.

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

[**MSISCSITARGET\_StorageConfigurationService**](msiscsitarget-storageconfigurationservice.md)
</dt> <dt>

[**MSISCSITARGET\_StoragePool**](msiscsitarget-storagepool.md)
</dt> <dt>

[**MSISCSITARGET\_StorageVolume**](msiscsitarget-storagevolume.md)
</dt> <dt>

[**MSISCSITARGET\_StorageSetting**](msiscsitarget-storagesetting.md)
</dt> </dl>

 

 





