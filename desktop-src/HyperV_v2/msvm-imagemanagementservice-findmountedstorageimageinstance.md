---
description: Finds an Msvm\_MountedStorageImage object for a given disk image path.
ms.assetid: 498ed285-2b5b-472b-b0ee-649c97b61274
title: FindMountedStorageImageInstance method of the Msvm_ImageManagementService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_ImageManagementService.FindMountedStorageImageInstance
api_type: 
- COM
api_location: 
- vmms.exe
---

# FindMountedStorageImageInstance method of the Msvm\_ImageManagementService class

Finds an [**Msvm\_MountedStorageImage**](msvm-mountedstorageimage.md) object for a given disk image path.

## Syntax


```mof
uint32 FindMountedStorageImageInstance(
  [in]  string                       SelectionCriterion,
  [in]  uint16                       CriterionType,
  [out] Msvm_MountedStorageImage REF Image
);
```



## Parameters

<dl> <dt>

*SelectionCriterion* \[in\]
</dt> <dd>

A fully-qualified path that specifies the location of a disk image file.

</dd> <dt>

*CriterionType* \[in\]
</dt> <dd>

The type of criterion to look for when finding the disk image.

<dt>

<span id="unknown"></span><span id="UNKNOWN"></span>

**unknown** (0)


</dt> <dd></dd> <dt>

<span id="Path"></span><span id="path"></span><span id="PATH"></span>

**Path** (2)


</dt> <dd></dd> </dl> </dd> <dt>

*Image* \[out\]
</dt> <dd>

A reference to the [**Msvm\_MountedStorageImage**](msvm-mountedstorageimage.md) (can be null if the image is not mounted).

</dd> </dl>

## Return value

This method returns one of the following values:

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Failed** (32768)
</dt> <dt>

**Access Denied** (32769)
</dt> <dt>

**Not Supported** (32770)
</dt> <dt>

**Status is unknown** (32771)
</dt> <dt>

**Timeout** (32772)
</dt> <dt>

**Invalid parameter** (32773)
</dt> <dt>

**System is in use** (32774)
</dt> <dt>

**Invalid state for this operation** (32775)
</dt> <dt>

**Incorrect data type** (32776)
</dt> <dt>

**System is not available** (32777)
</dt> <dt>

**Out of memory** (32778)
</dt> <dt>

**File not found** (32779)
</dt> <dt>

**Object not found** (32789)
</dt> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**Msvm\_ImageManagementService**](msvm-imagemanagementservice.md)
</dt> </dl>

 

 




