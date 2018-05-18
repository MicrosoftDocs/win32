---
title: CreateOrModifyElementFromStoragePool method of the CIM\_StorageConfigurationService class
description: Start a job to create (or modify) a specified element (for example a StorageVolume or StorageExtent) from a StoragePool.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '684b22b1-f7f0-418b-8787-5ea84afe0aed'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CreateOrModifyElementFromStoragePool method iSCSI Software Target API", "CreateOrModifyElementFromStoragePool method iSCSI Software Target API , CIM_StorageConfigurationService class", "CIM_StorageConfigurationService class iSCSI Software Target API , CreateOrModifyElementFromStoragePool method"]
topic_type:
- apiref
api_name:
- CIM_StorageConfigurationService.CreateOrModifyElementFromStoragePool
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
---

# CreateOrModifyElementFromStoragePool method of the CIM\_StorageConfigurationService class

Start a job to create (or modify) a specified element (for example a StorageVolume or StorageExtent) from a StoragePool. One of the parameters for this method is Size. As an input parameter, Size specifies the desired size of the element. As an output parameter, it specifies the size achieved. Space is taken from the input StoragePool. The desired settings for the element are specified by the Goal parameter. If the requested size cannot be created, no action will be taken, and the Return Value will be 4097/0x1001. Also, the output value of Size is set to the nearest possible size. If 0 is returned, the function completed successfully and no ConcreteJob instance was required. If 4096/0x1000 is returned, a ConcreteJob will be started to create the element. The Job's reference will be returned in the output parameter Job.

## Syntax


```mof
uint32 CreateOrModifyElementFromStoragePool(
  [in]      string                 ElementName,
  [in]      uint16                 ElementType,
  [out]     CIM_ConcreteJob    REF Job,
  [in]      CIM_ManagedElement REF Goal,
  [in, out] uint64                 Size,
  [in]      CIM_StoragePool    REF InPool,
  [in, out] CIM_LogicalElement REF TheElement
);
```



## Parameters

<dl> <dt>

*ElementName* \[in\]
</dt> <dd>

A end user relevant name for the element being created. If NULL, then a system supplied default name can be used. The value will be stored in the 'ElementName' property for the created element. If not NULL, this parameter will supply a new name when modifying an existing element.

</dd> <dt>

*ElementType* \[in\]
</dt> <dd>

Enumeration indicating the type of element being created or modified. If the input parameter TheElement is specified when the operation is a 'modify', this type value must match the type of that instance.

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


</dt> <dd>5–32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–65535</dd> </dl> </dd> <dt>

*Job* \[out\]
</dt> <dd>

Reference to the job (may be null if job completed).

</dd> <dt>

*Goal* \[in\]
</dt> <dd>

The requirements for the element to maintain. If set to a null value, the default configuration from the source pool will be used. This parameter should be a reference to a Setting or Profile appropriate to the element being created. If not NULL, this parameter will supply a new Goal when modifying an existing element.

</dd> <dt>

*Size* \[in, out\]
</dt> <dd>

As an input parameter Size specifies the desired size. If not NULL, this parameter will supply a new size when modifying an existing element. As an output parameter Size specifies the size achieved.

</dd> <dt>

*InPool* \[in\]
</dt> <dd>

The Pool from which to create the element. This parameter must be set to null if the input parameter TheElement is specified (in the case of a 'modify' operation).

</dd> <dt>

*TheElement* \[in, out\]
</dt> <dd>

As an input parameter: if null, creates a new element. If not null, then the method modifies the specified element. As an output parameter, it is a reference to the resulting element.

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
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_StorageConfigurationService**](cim-storageconfigurationservice.md)
</dt> </dl>

 

 





