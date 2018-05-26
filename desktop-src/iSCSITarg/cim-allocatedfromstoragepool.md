---
title: CIM\_AllocatedFromStoragePool class
description: AllocatedFromStoragePool is an association describing how LogicalElements are allocated from underlying StoragePools. These elements typically would be subclasses of StorageExtents or StoragePools.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 579c749c-b29f-4903-892f-e2524ec3144a
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_AllocatedFromStoragePool class iSCSI Software Target API
- CIM_AllocatedFromStoragePool class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- CIM_AllocatedFromStoragePool
- CIM_AllocatedFromStoragePool.Antecedent
- CIM_AllocatedFromStoragePool.Dependent
- CIM_AllocatedFromStoragePool.SpaceConsumed
- CIM_AllocatedFromStoragePool.SpaceLimit
- CIM_AllocatedFromStoragePool.SpaceLimitWarningThreshold
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_AllocatedFromStoragePool class

AllocatedFromStoragePool is an association describing how LogicalElements are allocated from underlying StoragePools. These elements typically would be subclasses of StorageExtents or StoragePools.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Abstract, Version("2.15.0"), UMLPackagePath("CIM::Device::StorageServices")]
class CIM_AllocatedFromStoragePool : CIM_ElementAllocatedFromPool
{
  CIM_StoragePool    REF Antecedent;
  CIM_LogicalElement REF Dependent;
  uint64                 SpaceConsumed;
  uint64                 SpaceLimit = 0;
  uint16                 SpaceLimitWarningThreshold;
};
```

## Members

The **CIM\_AllocatedFromStoragePool** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_AllocatedFromStoragePool** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_StoragePool**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

The StoragePool.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_LogicalElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

The subsidiary element.

</dd> <dt>

**SpaceConsumed**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650), **Punit** ("byte"), [**Units**](https://msdn.microsoft.com/library/aa393650) ("Bytes"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StoragePool.TotalManagedSpace", "CIM\_StoragePool.RemainingManagedSpace")
</dt> </dl>

Space consumed from this Pool, in bytes. This value MUST be maintained so that, relative to the Antecedent StoragePool, it is possible to compute TotalManagedSpace as StoragePool.RemainingManagedSpace plus the sum of SpaceConsumed from all of the AllocatedFromStoragePool references from the antecedent StoragePool.

</dd> <dt>

**SpaceLimit**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729), **Punit** ("byte"), [**Units**](https://msdn.microsoft.com/library/aa393650) ("Bytes"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_AllocatedFromStoragePool.SpaceConsumed")
</dt> </dl>

SpaceLimit is the consumption limit for the allocated storage element from the associated StoragePool. If SpaceLimt is greater than zero, the assumption is that the storage element can grow, (for instance an element representing the storage for a delta replica)

If SpaceLimit is greater than zero, SpaceConsumed shall not exceed the value of SpaceLimit.

If SpaceLimit = 0 (the default) then no limits are asserted on SpaceConsumed.

</dd> <dt>

**SpaceLimitWarningThreshold**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729), **Punit** ("percent"), [**Units**](https://msdn.microsoft.com/library/aa393650) ("Percentage"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (0), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) (100), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_AllocatedFromStoragePool.SpaceConsumed")
</dt> </dl>

If the associated storage element may dynamically consume an increasing amount of space and a space limit is enforced on the element, then a non-zero warning threshold percentage indicates when a warning indication should be generated based on SpaceConsumed &gt;= (SpaceLimit\*SpaceLimitWarningThreshold)/100.

</dd> </dl>

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

[**CIM\_ElementAllocatedFromPool**](cim-elementallocatedfrompool.md)
</dt> </dl>

 

 





