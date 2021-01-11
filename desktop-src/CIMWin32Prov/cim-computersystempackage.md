---
description: The CIM\_ComputerSystemPackage class represents an association that explicitly defines the relationship between unitary computer systems and one or more physical packages.
ms.assetid: a91bf09d-0768-4d2a-a0e5-16237b2e6ddc
ms.tgt_platform: multiple
title: CIM_ComputerSystemPackage class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_ComputerSystemPackage
- CIM_ComputerSystemPackage.Dependent
- CIM_ComputerSystemPackage.Antecedent
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_ComputerSystemPackage class

The **CIM\_ComputerSystemPackage** class represents an association that explicitly defines the relationship between unitary computer systems and one or more physical packages. The association is similar to the way that logical devices are realized by physical elements.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{FAF76B8D-798C-11D2-AAD1-006008C78BC7}"), AMENDMENT]
class CIM_ComputerSystemPackage : CIM_Dependency
{
  CIM_UnitaryComputerSystem REF Dependent;
  CIM_PhysicalPackage       REF Antecedent;
};
```

## Members

The **CIM\_ComputerSystemPackage** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ComputerSystemPackage** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_PhysicalPackage**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Antecedent")
</dt> </dl>

A [**CIM\_PhysicalPackage**](cim-physicalpackage.md) that describes the physical package(s) that realize a unitary computer system.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_UnitaryComputerSystem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Dependent")
</dt> </dl>

A [**CIM\_UnitaryComputerSystem**](cim-unitarycomputersystem.md) that describes the unitary computer system.

</dd> </dl>

## Remarks

The **CIM\_ComputerSystemPackage** class is derived from [**CIM\_Dependency**](cim-dependency.md).

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

 

