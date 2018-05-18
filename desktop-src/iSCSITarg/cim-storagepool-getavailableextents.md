---
title: GetAvailableExtents method of the CIM\_StoragePool class
description: This method can be used to retrieve a list of available Extents that may be used in the creation or modification of a StoragePool, StorageVolume, or LogicalDisk.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '8c7eca4d-48b4-4512-97b8-2e720cb8760d'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetAvailableExtents method iSCSI Software Target API", "GetAvailableExtents method iSCSI Software Target API , CIM_StoragePool class", "CIM_StoragePool class iSCSI Software Target API , GetAvailableExtents method"]
topic_type:
- apiref
api_name:
- CIM_StoragePool.GetAvailableExtents
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
---

# GetAvailableExtents method of the CIM\_StoragePool class

This method can be used to retrieve a list of available Extents that may be used in the creation or modification of a StoragePool, StorageVolume, or LogicalDisk. The GetAvailableExtents method MUST return the Extents from the set of Component Extents of the Pool on which the method is being invoked. The returned Extents are available at the time the method returns. There is no guarantee that the same Extents will be available later. This method MUST return the Extents that are not being used as supporting capacity for any other Pools, Volumes, or LogicalDisks that have been allocated from this Pool. The Extent returned MUST be a component Extent of the Pool or subdivisions of a component Extent, the subdivisions themselves represented as Extents.

## Syntax


```mof
uint32 GetAvailableExtents(
  [in]  CIM_StorageSetting REF Goal,
  [out] CIM_StorageExtent  REF AvailableExtents[]
);
```



## Parameters

<dl> <dt>

*Goal* \[in\]
</dt> <dd>

The StorageSetting (Goal) for which supported extents should be retrieved as available.

If a NULL is passed for the Goal, the method will return all available extents, regardless of the goal. There exists a possibility of error in creating a Pool, Volume, or LogicalDisk retrieved in this manner.

</dd> <dt>

*AvailableExtents* \[out\]
</dt> <dd>

List of references to available StorageExtents, or subclass instances.

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

**DMTF Reserved** (7–4097)
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

[**CIM\_StoragePool**](cim-storagepool.md)
</dt> </dl>

 

 





