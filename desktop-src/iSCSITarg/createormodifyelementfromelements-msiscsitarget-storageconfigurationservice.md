---
title: CreateOrModifyElementFromElements method of the MSISCSITARGET\_StorageConfigurationService class
description: Creates or modifies a specified storage element by using specified CIM\_StorageExtent instances.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '85d1d7ba-a9c9-4667-8389-c77a1365987a'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CreateOrModifyElementFromElements method iSCSI Software Target API", "CreateOrModifyElementFromElements method iSCSI Software Target API , MSISCSITARGET_StorageConfigurationService class", "MSISCSITARGET_StorageConfigurationService class iSCSI Software Target API , CreateOrModifyElementFromElements method"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_StorageConfigurationService.CreateOrModifyElementFromElements
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
---

# CreateOrModifyElementFromElements method of the MSISCSITARGET\_StorageConfigurationService class

Creates or modifies a specified storage element by using specified [**CIM\_StorageExtent**](https://msdn.microsoft.com/library/aa388496) instances. You can use the [**MSISCSITARGET\_StoragePool**](msiscsitarget-storagepool.md).**GetAvailableExtents** method to get a list of valid extent instances.

This method is inherited from the **CIM\_StorageConfigurationService** class.

## Syntax


```mof
uint32 CreateOrModifyElementFromElements(
  [in]      string                 ElementName,
  [in]      uint16                 ElementType,
  [out]     CIM_ConcreteJob Ref    Job,
  [in]      CIM_ManagedElement Ref Goal,
  [in, out] uint64                 Size,
  [in]      CIM_StorageExtent Ref  InElements[],
  [in, out] CIM_LogicalElement Ref TheElement
);
```



## Parameters

<dl> <dt>

*ElementName* \[in\]
</dt> <dd>

Specifies an end-user relevant name for the element that is being created. This value is propagated to the **ElementName** property of the created element.

If **NULL**, a system-supplied default name is used. If not **NULL**, when modifying an existing element, this value replaces the **ElementName** of the existing element.

</dd> <dt>

*ElementType* \[in\]
</dt> <dd>

Specifies the type of element to be created or modified.

The element returned in the *TheElement* parameter must be of the type that is specified here or a subtype of it.

Required.

The possible values are.

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


</dt> <dd>6–0x7FFF</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>0x8000–0xFFFF</dd> </dl> </dd> <dt>

*Job* \[out\]
</dt> <dd>

On return, contains a reference to the job, if a job is created and not completed.

</dd> <dt>

*Goal* \[in\]
</dt> <dd>

Specifies the characteristics, qualities of service, and goals for the element to maintain. If **NULL**, the default configuration from the source pool is used.

If not **NULL**, when an existing element is modified, specifies a new goal for the modified element.

</dd> <dt>

*Size* \[in, out\]
</dt> <dd>

On input, specifies the wanted size in bytes. If **NULL**, the size is the maximum size that can be created from the extent instances that are specified in the *InElements* parameter.

If not **NULL**, when an existing element is modified, specifies a new size.

On output, indicates the actual size of the resulting element.

If the requested size cannot be created, no action is performed.

</dd> <dt>

*InElements* \[in\]
</dt> <dd>

Specifies the storage element instances that are used to create or modify the resulting element.

If the size of the individual extent instances that are specified is less than the requested *Size* parameter, then the space is drawn from the extent instances in the order that is specified.

Required.

</dd> <dt>

*TheElement* \[in, out\]
</dt> <dd>

On input, optionally specifies an element to modify. If an existing element is specified, it must match the *ElementType* parameter. It must be an instance of the same class or a subclass of it.

If **NULL**, this method creates a new element.

On output, contains a reference to the resulting element, which can be a vendor-specific subclass of the type that is specified in the *ElementType* parameter.

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
</dt> <dt>

[**MSISCSITARGET\_StoragePool**](msiscsitarget-storagepool.md)
</dt> <dt>

[**CIM\_StorageExtent**](https://msdn.microsoft.com/library/aa388496)
</dt> </dl>

 

 





