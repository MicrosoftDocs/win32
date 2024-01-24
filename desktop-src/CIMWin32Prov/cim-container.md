---
description: The CIM\_Container class represents an association between a contained and a containing physical element. A containing object must be a physical package.
ms.assetid: 9b119163-3c56-44e2-ba66-d8add3c375fa
ms.tgt_platform: multiple
title: CIM_Container class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_Container
- CIM_Container.PartComponent
- CIM_Container.GroupComponent
- CIM_Container.LocationWithinContainer
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_Container class

The **CIM\_Container** class represents an association between a contained and a containing physical element. A containing object must be a physical package.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{FAF76B6F-798C-11D2-AAD1-006008C78BC7}"), AMENDMENT]
class CIM_Container : CIM_Component
{
  CIM_PhysicalElement REF PartComponent;
  CIM_PhysicalPackage REF GroupComponent;
  string                  LocationWithinContainer;
};
```

## Members

The **CIM\_Container** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_Container** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_PhysicalPackage**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("GroupComponent"), [**Max**](/windows/desktop/WmiSdk/standard-qualifiers) (1)
</dt> </dl>

A [**CIM\_PhysicalPackage**](cim-physicalpackage.md) that represents the physical package that contains other physical elements, including other packages.

</dd> <dt>

**LocationWithinContainer**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Free-form string that represents the positioning of the physical element within the physical package. Information relative to stationary elements in the container (for example, "second drive bay from the top"), angles, altitudes, and other data can be recorded in this property. This string could supplement or be used in place of instantiating the [**CIM\_Location**](cim-location.md) object.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_PhysicalElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("PartComponent")
</dt> </dl>

A [**CIM\_PhysicalElement**](cim-physicalelement.md) that describes the physical element which is contained in the package.

</dd> </dl>

## Remarks

WMI does not implement this class. For more information about classes derived from **CIM\_Container**, see [Win32 Classes](win32-provider.md).

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

[**CIM\_Component**](cim-component.md)
</dt> </dl>

 

