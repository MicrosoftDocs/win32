---
title: GetElementsBasedOnUsage method of the CIM\_StorageConfigurationService class
description: Allows retrieving elements that meet the specified Usage. The criteria can be \ 0034;available only \ 0034;, \ 0034;in use only \ 0034;, or both.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c9e216df-b82b-4147-8a4c-c43d0a5e5f67'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetElementsBasedOnUsage method iSCSI Software Target API", "GetElementsBasedOnUsage method iSCSI Software Target API , CIM_StorageConfigurationService class", "CIM_StorageConfigurationService class iSCSI Software Target API , GetElementsBasedOnUsage method"]
topic_type:
- apiref
api_name:
- CIM_StorageConfigurationService.GetElementsBasedOnUsage
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
---

# GetElementsBasedOnUsage method of the CIM\_StorageConfigurationService class

Allows retrieving elements that meet the specified Usage. The criteria can be "available only", "in use only", or both.

## Syntax


```mof
uint32 GetElementsBasedOnUsage(
  [in]  uint16                       ElementType,
  [in]  uint16                       Usage,
  [in]  uint16                       Criteria,
  [in]  CIM_StoragePool          REF ThePool,
  [out] CIM_ManagedSystemElement REF TheElements[]
);
```



## Parameters

<dl> <dt>

*ElementType* \[in\]
</dt> <dd>

Enumeration indicating the type of elements to get.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="StorageVolume"></span><span id="storagevolume"></span><span id="STORAGEVOLUME"></span>

**StorageVolume** (2)


</dt> <dd></dd> <dt>

<span id="StorageExtent"></span><span id="storageextent"></span><span id="STORAGEEXTENT"></span>

**StorageExtent** (3)


</dt> <dd></dd> <dt>

<span id="StoragePool"></span><span id="storagepool"></span><span id="STORAGEPOOL"></span>

**StoragePool** (4)


</dt> <dd></dd> <dt>

<span id="Logical_Disk"></span><span id="logical_disk"></span><span id="LOGICAL_DISK"></span>

**Logical Disk** (5)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>6–32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–65535</dd> </dl> </dd> <dt>

*Usage* \[in\]
</dt> <dd>

The specific Usage to be retrieved.

</dd> <dt>

*Criteria* \[in\]
</dt> <dd>

Specifies whether to retrieve all elements, available elements only, or the elements that are in use.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="All"></span><span id="all"></span><span id="ALL"></span>

**All** (2)


</dt> <dd></dd> <dt>

<span id="Available_Only"></span><span id="available_only"></span><span id="AVAILABLE_ONLY"></span>

**Available Only** (3)


</dt> <dd></dd> <dt>

<span id="In_Use_Only"></span><span id="in_use_only"></span><span id="IN_USE_ONLY"></span>

**In Use Only** (4)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>5–32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–65535</dd> </dl> </dd> <dt>

*ThePool* \[in\]
</dt> <dd>

Limit the search for the elements that satisfy the criteria to this StoragePool only. If null, all appropriate StoragePools will be considered.

</dd> <dt>

*TheElements* \[out\]
</dt> <dd>

Array of references to storage element instances retrieved.

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

**DMTF Reserved** (6)
</dt> <dt>

**Vendor Specific** (7–32767)
</dt> <dt>

 (32768–65535)
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

 

 





