---
title: MSISCSITARGET\_AllocatedFromStoragePool class
description: Represents an association between an instance of the CIM\_LogicalElement class that represents an allocated resource with the MSISCSITARGET\_StoragePool instance from which it was allocated.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 17fa1eed-f121-4eb4-8a39-71eb0e35fb53
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSISCSITARGET_AllocatedFromStoragePool class iSCSI Software Target API
- MSISCSITARGET_AllocatedFromStoragePool class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- MSISCSITARGET_AllocatedFromStoragePool
- MSISCSITARGET_AllocatedFromStoragePool.Antecedent
- MSISCSITARGET_AllocatedFromStoragePool.Dependent
- MSISCSITARGET_AllocatedFromStoragePool.SpaceConsumed
- MSISCSITARGET_AllocatedFromStoragePool.SpaceLimit
- MSISCSITARGET_AllocatedFromStoragePool.SpaceLimitWarningThreshold
api_location:
- WTWmiProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSISCSITARGET\_AllocatedFromStoragePool class

Represents an association between an instance of the [**CIM\_LogicalElement**](https://msdn.microsoft.com/library/aa387892) class that represents an allocated resource with the [**MSISCSITARGET\_StoragePool**](msiscsitarget-storagepool.md) instance from which it was allocated. These elements typically are subclasses of the [**CIM\_StorageExtent**](https://msdn.microsoft.com/library/aa388496) or [**MSISCSITARGET\_StorageVolume**](msiscsitarget-storagevolume.md) classes.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MSiSCSITargetProv"), Association, Version("1.0.0")]
class MSISCSITARGET_AllocatedFromStoragePool : CIM_AllocatedFromStoragePool
{
  CIM_StoragePool    REF Antecedent;
  CIM_LogicalElement REF Dependent;
  uint64                 SpaceConsumed;
  uint64                 SpaceLimit = 0;
  uint16                 SpaceLimitWarningThreshold;
};
```

## Members

The **MSISCSITARGET\_AllocatedFromStoragePool** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSISCSITARGET\_AllocatedFromStoragePool** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_StoragePool**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The StoragePool.

This property is inherited from [**CIM\_AllocatedFromStoragePool**](cim-allocatedfromstoragepool.md).

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_LogicalElement**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The subsidiary element.

This property is inherited from [**CIM\_AllocatedFromStoragePool**](cim-allocatedfromstoragepool.md).

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

This property is inherited from [**CIM\_AllocatedFromStoragePool**](cim-allocatedfromstoragepool.md).

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

This property is inherited from [**CIM\_AllocatedFromStoragePool**](cim-allocatedfromstoragepool.md).

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

This property is inherited from [**CIM\_AllocatedFromStoragePool**](cim-allocatedfromstoragepool.md).

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                            |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                 |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WTWmiProv.dll</dt> </dl>     |



## See also

<dl> <dt>

[**CIM\_AllocatedFromStoragePool**](cim-allocatedfromstoragepool.md)
</dt> <dt>

[iSCSI Target Server Reference](https://msdn.microsoft.com/library/hh830439)
</dt> <dt>

[**MSISCSITARGET\_StoragePool**](msiscsitarget-storagepool.md)
</dt> </dl>

 

 





