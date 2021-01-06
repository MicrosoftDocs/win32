---
description: The CIM\_PSExtentBasedOnPExtent class associates protected space extents that are based on a physical extent.
ms.assetid: 4b89319c-022c-4ff4-91ec-70c435a5888a
ms.tgt_platform: multiple
title: CIM_PSExtentBasedOnPExtent class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_PSExtentBasedOnPExtent
- CIM_PSExtentBasedOnPExtent.EndingAddress
- CIM_PSExtentBasedOnPExtent.StartingAddress
- CIM_PSExtentBasedOnPExtent.Dependent
- CIM_PSExtentBasedOnPExtent.Antecedent
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_PSExtentBasedOnPExtent class

The **CIM\_PSExtentBasedOnPExtent** class associates protected space extents that are based on a physical extent.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of its inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{451FE14C-E3D3-11d2-8601-0000F8102E5F}"), AMENDMENT]
class CIM_PSExtentBasedOnPExtent : CIM_BasedOn
{
  uint64                       EndingAddress;
  uint64                       StartingAddress;
  CIM_ProtectedSpaceExtent REF Dependent;
  CIM_PhysicalExtent       REF Antecedent;
};
```

## Members

The **CIM\_PSExtentBasedOnPExtent** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_PSExtentBasedOnPExtent** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_PhysicalExtent**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Max**](/windows/desktop/WmiSdk/standard-qualifiers) (1), [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Antecedent")
</dt> </dl>

A [**CIM\_PhysicalExtent**](cim-physicalextent.md) that describes the physical extent.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ProtectedSpaceExtent**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Dependent")
</dt> </dl>

A [**CIM\_ProtectedSpaceExtent**](cim-protectedspaceextent.md) that describes the protected space extent which is built on the physical extent.

</dd> <dt>

**EndingAddress**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the end of the high-level extent in lower-level storage. This property is useful when mapping non-contiguous extents into a higher-level grouping.

For more information about using **uint64** values in scripts, see [Scripting in WMI](/windows/desktop/WmiSdk/creating-a-wmi-script).

This property is inherited from [**CIM\_BasedOn**](cim-basedon.md).

</dd> <dt>

**StartingAddress**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the beginning of the high-level extent in lower-level storage.

For more information about using **uint64** values in scripts, see [Scripting in WMI](/windows/desktop/WmiSdk/creating-a-wmi-script).

This property is inherited from [**CIM\_BasedOn**](cim-basedon.md).

</dd> </dl>

## Remarks

The **CIM\_PSExtentBasedOnPExtent** class is derived from [**CIM\_BasedOn**](cim-basedon.md).

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

[**CIM\_BasedOn**](cim-basedon.md)
</dt> </dl>

 

