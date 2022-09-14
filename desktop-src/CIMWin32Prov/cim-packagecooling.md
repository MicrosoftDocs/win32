---
description: The CIM\_PackageCooling association represents the relationship in which a cooling device is installed in a package, such as a chassis or rack, to assist with the package's cooling.
ms.assetid: 0aaae8e1-6e70-4b26-8e56-dac5657e58c1
ms.tgt_platform: multiple
title: CIM_PackageCooling class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_PackageCooling
- CIM_PackageCooling.Dependent
- CIM_PackageCooling.Antecedent
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_PackageCooling class

The **CIM\_PackageCooling** association represents the relationship in which a cooling device is installed in a package, such as a chassis or rack, to assist with the package's cooling.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{FAF76B8E-798C-11D2-AAD1-006008C78BC7}"), AMENDMENT]
class CIM_PackageCooling : CIM_Dependency
{
  CIM_PhysicalPackage REF Dependent;
  CIM_CoolingDevice   REF Antecedent;
};
```

## Members

The **CIM\_PackageCooling** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_PackageCooling** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_CoolingDevice**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Antecedent")
</dt> </dl>

A [**CIM\_CoolingDevice**](cim-coolingdevice.md) that describes the cooling device for the package.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_PhysicalPackage**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Dependent")
</dt> </dl>

A [**CIM\_PhysicalPackage**](cim-physicalpackage.md) that describes the physical package whose environment is cooled.

</dd> </dl>

## Remarks

**CIM\_PackageCooling** is derived from [**CIM\_Dependency**](cim-dependency.md).

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

 

