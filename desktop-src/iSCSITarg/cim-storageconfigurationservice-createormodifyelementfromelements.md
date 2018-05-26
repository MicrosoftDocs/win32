---
title: CreateOrModifyElementFromElements method of the CIM\_StorageConfigurationService class
description: Start a job to create (or modify) a specified storage element from specified input StorageExtents.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b26eefc1-21f0-49e7-bc82-9c7b5c16cab9
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CreateOrModifyElementFromElements method iSCSI Software Target API
- CreateOrModifyElementFromElements method iSCSI Software Target API , CIM_StorageConfigurationService class
- CIM_StorageConfigurationService class iSCSI Software Target API , CreateOrModifyElementFromElements method
topic_type:
- apiref
api_name:
- CIM_StorageConfigurationService.CreateOrModifyElementFromElements
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CreateOrModifyElementFromElements method of the CIM\_StorageConfigurationService class

Start a job to create (or modify) a specified storage element from specified input StorageExtents. The created or modified storage element can be a StorageExtent, StorageVolume, LogicalDisk, or StoragePool. An input list of InElements must be specified. The GetAvailableExtents method can be used to get a list of valid extents that can be used to achieve a desired goal. Validity of the extents is determined by the implementation. As an input parameter, Size specifies the desired size of the element. As an output parameter, it specifies the size achieved. Space is taken from the input InElements. The desired Settings for the element are specified by the Goal parameter. If the size of Extents passed is less than the size requested, then the capacity is drawn from the extents in the order, left to right, that the Extents were specified. The partial consumption of an Extent is represented by an Extent for the capacity used and an Extent for the capacity not used. If the Size is NULL, then a configuration using all Extents passed will be attempted. If the requested size cannot be created, no action will be taken, and the Return Value will be 4097/0x1001. Also, the output value of Size is set to the nearest possible size. If 0 is returned, the function completed successfully and no ConcreteJob instance was required. If 4096/0x1000 is returned, a ConcreteJob will be started to create the element. The Job's reference will be returned in the output parameter Job.

## Syntax


```mof
uint32 CreateOrModifyElementFromElements(
  [in]      string                 ElementName,
  [in]      uint16                 ElementType,
  [out]     CIM_ConcreteJob    REF Job,
  [in]      CIM_ManagedElement REF Goal,
  [in, out] uint64                 Size,
  [in]      CIM_StorageExtent  REF InElements[],
  [in, out] CIM_LogicalElement REF TheElement
);
```



## Parameters

<dl> <dt>

*ElementName* \[in\]
</dt> <dd>

A end user relevant name for the element being created. If NULL, then a system-supplied default name can be used. The value will be stored in the 'ElementName' property for the created element. If not NULL, this parameter will supply a new name when modifying an existing element.

</dd> <dt>

*ElementType* \[in\]
</dt> <dd>

Enumeration indicating the type of element being created or modified. If the input parameter TheElement is specified when the operation is a 'modify', this type value must match the type of that instance. The actual CIM class of the created TheElement can be vendor-specific, but it must be a derived class of the appropriate CIM class -- i.e., CIM\_StorageVolume, CIM\_StorageExtent, CIM\_LogicalDisk, or CIM\_StoragePool.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Reserved"></span><span id="reserved"></span><span id="RESERVED"></span>

**Reserved** (1)


</dt> <dd></dd> <dt>

<span id="Storage_Volume"></span><span id="storage_volume"></span><span id="STORAGE_VOLUME"></span>

**Storage Volume** (2)


</dt> <dd></dd> <dt>

<span id="Storage_Extent"></span><span id="storage_extent"></span><span id="STORAGE_EXTENT"></span>

**Storage Extent** (3)


</dt> <dd></dd> <dt>

<span id="Storage_Pool"></span><span id="storage_pool"></span><span id="STORAGE_POOL"></span>

**Storage Pool** (4)


</dt> <dd></dd> <dt>

<span id="Logical_Disk"></span><span id="logical_disk"></span><span id="LOGICAL_DISK"></span>

**Logical Disk** (5)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>6 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl> </dd> <dt>

*Job* \[out\]
</dt> <dd>

Reference to the job (may be null if job completed).

</dd> <dt>

*Goal* \[in\]
</dt> <dd>

The requirements for the element to maintain. If set to a null value, the default configuration associated with the Service will be used. This parameter should be a reference to a Setting, SettingData, or Profile appropriate to the element being created. If not NULL, this parameter will supply a new Goal when modifying an existing element.

</dd> <dt>

*Size* \[in, out\]
</dt> <dd>

As an input parameter Size specifies the desired size. If not NULL, this parameter will supply a new size when modifying an existing element. As an output parameter Size specifies the size achieved.

</dd> <dt>

*InElements* \[in\]
</dt> <dd>

Array of references to storage element instances that are used to create or modify TheElement.

</dd> <dt>

*TheElement* \[in, out\]
</dt> <dd>

As an input parameter: if null, creates a new element. If not null, then the method modifies the specified element. As an output parameter, it is a reference to the resulting element.

</dd> </dl>

## Return value

<dl> <dt>

**Completed with No Error** (0)
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

 

 





