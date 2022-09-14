---
description: The CIM\_PackageInSlot association represents the relationship between device cards and the chassis in which they are mounted.
ms.assetid: 439f28a8-24fd-4a53-9d42-48fabb58e84a
ms.tgt_platform: multiple
title: CIM_PackageInSlot class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_PackageInSlot
- CIM_PackageInSlot.Dependent
- CIM_PackageInSlot.Antecedent
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_PackageInSlot class

The **CIM\_PackageInSlot** association represents the relationship between device cards and the chassis in which they are mounted.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of its inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{FAF76B89-798C-11D2-AAD1-006008C78BC7}"), AMENDMENT]
class CIM_PackageInSlot : CIM_Dependency
{
  CIM_PhysicalPackage REF Dependent;
  CIM_Slot            REF Antecedent;
};
```

## Members

The **CIM\_PackageInSlot** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_PackageInSlot** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Slot**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Antecedent")
</dt> </dl>

A [**CIM\_Slot**](cim-slot.md) describing the slot into which the physical package is inserted.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_PhysicalPackage**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Dependent"), [**Max**](/windows/desktop/WmiSdk/standard-qualifiers) (1)
</dt> </dl>

A [**CIM\_PhysicalPackage**](cim-physicalpackage.md) describing the package in the slot.

</dd> </dl>

## Remarks

**CIM\_PackageInSlot** is derived from [**CIM\_Dependency**](cim-dependency.md).

WMI does not implement this class.

This documentation is derived from the CIM class descriptions published by the DMTF. Microsoft may have made changes to correct minor errors, conform to Microsoft SDK documentation standards, or provide more information.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> </dl>

 

