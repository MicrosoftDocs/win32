---
description: References the compatibility info for a virtual machine (VM) (when run on a VM computer system) or a host (when run on a host computer system).
ms.assetid: A3DB75BF-91C8-444E-B273-25DF8A5BFA7B
title: Msvm_CompatibilityVector class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_CompatibilityVector
- Msvm_CompatibilityVector.VectorId
- Msvm_CompatibilityVector.CompareOperation
- Msvm_CompatibilityVector.CompatibilityInfo
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_CompatibilityVector class

References the compatibility info for a virtual machine (VM) (when run on a VM computer system) or a host (when run on a host computer system).

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_CompatibilityVector
{
  uint32 VectorId;
  uint32 CompareOperation;
  uint64 CompatibilityInfo;
};
```

## Members

The **Msvm\_CompatibilityVector** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_CompatibilityVector** class has these properties.

<dl> <dt>

**CompareOperation**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Identifies the comparison operation that will return true if and only if two vectors are compatible. The VM's data is on the left hand side of the comparison, and the host's data is on the right hand side.

<dt>

<span id="Equal"></span><span id="equal"></span><span id="EQUAL"></span>

**Equal** (0)


</dt> <dd></dd> <dt>

<span id="Superset"></span><span id="superset"></span><span id="SUPERSET"></span>

**Superset** (1)


</dt> <dd></dd> <dt>

<span id="Subset"></span><span id="subset"></span><span id="SUBSET"></span>

**Subset** (2)


</dt> <dd></dd> <dt>

<span id="Disjoint"></span><span id="disjoint"></span><span id="DISJOINT"></span>

**Disjoint** (3)


</dt> <dd></dd> <dt>

<span id="GreaterThan"></span><span id="greaterthan"></span><span id="GREATERTHAN"></span>

**GreaterThan** (4)


</dt> <dd></dd> <dt>

<span id="GreaterThanOrEqual"></span><span id="greaterthanorequal"></span><span id="GREATERTHANOREQUAL"></span>

**GreaterThanOrEqual** (5)


</dt> <dd></dd> <dt>

<span id="LessThan"></span><span id="lessthan"></span><span id="LESSTHAN"></span>

**LessThan** (6)


</dt> <dd></dd> <dt>

<span id="LessThanOrEqual"></span><span id="lessthanorequal"></span><span id="LESSTHANOREQUAL"></span>

**LessThanOrEqual** (7)


</dt> <dd></dd> <dt>

<span id="Multiple"></span><span id="multiple"></span><span id="MULTIPLE"></span>

**Multiple** (8)


</dt> <dd></dd> <dt>

<span id="Divisible"></span><span id="divisible"></span><span id="DIVISIBLE"></span>

**Divisible** (9)


</dt> <dd></dd> </dl>

</dd> <dt>

**CompatibilityInfo**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The actual compatibility attribute data that is used for comparison.

</dd> <dt>

**VectorId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Identifies a compatibility vector that represents a specific attribute. This property is used to match corresponding vectors between a host and a VM.

</dd> </dl>

## Remarks

The [**GetSystemCompatibilityVectors**](getsystemcompatibilityvectors-msvm-virtualsystemmigrationservice.md) method of the [**Msvm\_VirtualSystemMigrationService**](msvm-virtualsystemmigrationservice.md) class returns an array of **Msvm\_CompatibilityVector** instances for the host (if run on the host) or a VM (if run on the VM). Each **Msvm\_CompatibilityVector** entry in the list describes a compatibility attribute vector. For a VM to be compatible with a host, all of its compatibility attributes must be compatible with the host s attributes.

Each **Msvm\_CompatibilityVector** entry has these properties:

<dl> <dt>

**VectorId**
</dt> <dd>

Uniquely identifies the compatibility vector. This is used to match the vectors to compare between a host and a VM.

</dd> <dt>

**CompareOperation**
</dt> <dd>

Identifies the comparison operation that determines whether the vectors are compatible.

</dd> <dt>

**CompatibilityInfo**
</dt> <dd>

Contains the actual compatibility attribute; This is effectively the attribute payload (e.g. processor feature mask, cache line flush size, etc.)

</dd> </dl>

The set of operations defined for **CompareOperation** just involve basic integer comparison and bitwise logic. This enables the actual contents of **CompatibilityInfo** to remain opaque. The set of operations include:



| CompareOperation | Description                                      | Pseudocode Comparison                |
|------------------|--------------------------------------------------|--------------------------------------|
| VmCcEqual        | VmAttr must equal HostAttr                       | If (VmAttr == HostAttr)              |
| VmCcSuperSet     | VmAttr must be a superset of HostAttr            | If ((VmAttr & HostAttr) == HostAttr) |
| VmCcSubSet       | VmAttr must be a subset of HostAttr              | If ((VmAttr & HostAttr) == VmAttr)   |
| VmCcDisjointSet  | VmAttr must be a disjoint set from HostAttr      | If ((VmAttr & HostAttr) == 0)        |
| VmCcGreater      | VmAttr must be greater than HostAttr             | If (VmAttr > HostAttr)            |
| VmCcGreaterEqual | VmAttr must be greater than or equal to HostAttr | If (VmAttr >= HostAttr)           |
| VmCcLess         | VmAttr must be less than HostAttr                | If (VmAttr < HostAttr)            |
| VmCcLessEqual    | VmAttr must be less than or equal to HostAttr    | If (VmAttr <= HostAttr)           |
| VmCcMultiple     | VmAttr must be a multiple of HostAttr            | If ((VmAttr % HostAttr) == 0)        |
| VmCcDivisor      | VmAttr must be a divisor of HostAttr             | If ((HostAttr % VmAttr) == 0)        |



 

SCVMM needs to do these steps to determine whether a VM is compatible with a host.

**To determine whether a VM is compatible with a host**

1.  Iterate through all of the **Msvm\_CompatibilityVector** elements for the VM.
2.  For each **Msvm\_CompatibilityVector** element, use the compatibility operation specified in **CompareOperation** to compare the VM s hardware compatibility vector with the corresponding compatibility vector for the host.
3.  If the all of the **Msvm\_CompatibilityVector** elements from the VM are deemed compatible, the VM is compatible with the host (from a processor feature perspective).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                                 |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**GetSystemCompatibilityVectors**](getsystemcompatibilityvectors-msvm-virtualsystemmigrationservice.md)
</dt> <dt>

[**Msvm\_VirtualSystemMigrationService**](msvm-virtualsystemmigrationservice.md)
</dt> </dl>

 

 




