---
description: The CIM\_RealizesPExtent association represents the relationship in which physical extents are realized on a physical media. In addition, the starting address of the physical extent on the physical media is specified.
ms.assetid: 9abe1a7d-8463-4d48-8cec-52bf934ad08b
ms.tgt_platform: multiple
title: CIM_RealizesPExtent class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_RealizesPExtent
- CIM_RealizesPExtent.Dependent
- CIM_RealizesPExtent.Antecedent
- CIM_RealizesPExtent.StartingAddress
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_RealizesPExtent class

The **CIM\_RealizesPExtent** association represents the relationship in which physical extents are realized on a physical media. In addition, the starting address of the physical extent on the physical media is specified.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of its inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{FAF76B7F-798C-11D2-AAD1-006008C78BC7}"), AMENDMENT]
class CIM_RealizesPExtent : CIM_Realizes
{
  CIM_PhysicalExtent REF Dependent;
  CIM_PhysicalMedia  REF Antecedent;
  uint64                 StartingAddress;
};
```

## Members

The **CIM\_RealizesPExtent** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_RealizesPExtent** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_PhysicalMedia**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Antecedent"), [**Max**](/windows/desktop/WmiSdk/standard-qualifiers) (1)
</dt> </dl>

A [**CIM\_PhysicalMedia**](cim-physicalmedia.md) that describes the physical media on which the extent is realized.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_PhysicalExtent**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Dependent")
</dt> </dl>

A [**CIM\_PhysicalExtent**](cim-physicalextent.md) that describes the physical extent that is located on the media.

</dd> <dt>

**StartingAddress**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Starting address on the physical media where the physical extent begins. The ending address of the physical extent is determined using the **NumberOfBlocks** and **BlockSize** properties of the [**CIM\_PhysicalExtent**](cim-physicalextent.md) object.

For more information about using **uint64** values in scripts, see [Scripting in WMI](/windows/desktop/WmiSdk/creating-a-wmi-script).

</dd> </dl>

## Remarks

The **CIM\_RealizesPExtent** class is derived from [**CIM\_Realizes**](cim-realizes.md).

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

[**CIM\_Realizes**](cim-realizes.md)
</dt> </dl>

 

