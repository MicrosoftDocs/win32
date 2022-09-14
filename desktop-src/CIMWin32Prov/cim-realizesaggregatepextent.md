---
description: The CIM\_RealizesAggregatePExtent association represents the relationship in which the CIM\_AggregatePExtent class is realized on a physical media.
ms.assetid: 420dde1d-daa8-4cd3-b3fd-c2aefdc1e217
ms.tgt_platform: multiple
title: CIM_RealizesAggregatePExtent class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_RealizesAggregatePExtent
- CIM_RealizesAggregatePExtent.Dependent
- CIM_RealizesAggregatePExtent.Antecedent
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_RealizesAggregatePExtent class

The **CIM\_RealizesAggregatePExtent** association represents the relationship in which the [**CIM\_AggregatePExtent**](cim-aggregatepextent.md) class is realized on a physical media.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of its inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{FAF76B81-798C-11D2-AAD1-006008C78BC7}"), AMENDMENT]
class CIM_RealizesAggregatePExtent : CIM_Realizes
{
  CIM_AggregatePExtent REF Dependent;
  CIM_PhysicalMedia    REF Antecedent;
};
```

## Members

The **CIM\_RealizesAggregatePExtent** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_RealizesAggregatePExtent** class has these properties.

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

Data type: **CIM\_AggregatePExtent**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Dependent")
</dt> </dl>

The [**CIM\_AggregatePExtent**](cim-aggregatepextent.md) that is located on the media.

</dd> </dl>

## Remarks

The **CIM\_RealizesAggregatePExtent** class is derived from [**CIM\_Realizes**](cim-realizes.md).

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

 

