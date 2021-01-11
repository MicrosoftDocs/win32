---
description: The CIM\_SoftwareElementChecks association class relates a software element with condition or location information that a feature may require.
ms.assetid: ff130fe9-ddb2-4e4f-86d3-53f1d8ed14aa
ms.tgt_platform: multiple
title: CIM_SoftwareElementChecks class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_SoftwareElementChecks
- CIM_SoftwareElementChecks.Check
- CIM_SoftwareElementChecks.Element
- CIM_SoftwareElementChecks.Phase
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_SoftwareElementChecks class

The **CIM\_SoftwareElementChecks** association class relates a software element with condition or location information that a feature may require.

Because software elements in a ready-to-run state cannot transition into another state, the value of the **Phase** property is restricted to in-state for [**CIM\_SoftwareElement**](cim-softwareelement.md) objects in a ready-to-run state.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of its inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[UUID("{24783E8A-DB31-11d2-85FC-0000F8102E5F}"), Association, Aggregation, Abstract, AMENDMENT]
class CIM_SoftwareElementChecks
{
  CIM_Check           REF Check;
  CIM_SoftwareElement REF Element;
  uint16                  Phase;
};
```

## Members

The **CIM\_SoftwareElementChecks** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_SoftwareElementChecks** class has these properties.

<dl> <dt>

**Check**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Check**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Min**](/windows/desktop/WmiSdk/standard-qualifiers) (0), [**Max**](/windows/desktop/WmiSdk/standard-qualifiers) (FALSE), [**Weak**](/windows/desktop/WmiSdk/standard-qualifiers)
</dt> </dl>

Reference to the check.

</dd> <dt>

**Element**
</dt> <dd> <dl> <dt>

Data type: **CIM\_SoftwareElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Min**](/windows/desktop/WmiSdk/standard-qualifiers) (1), [**Max**](/windows/desktop/WmiSdk/standard-qualifiers) (1), [**Aggregate**](/windows/desktop/WmiSdk/standard-qualifiers)
</dt> </dl>

Reference to the element.

</dd> <dt>

**Phase**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the referenced check is an in-state check or a next-state check.

<dt>

<span id="In-State"></span><span id="in-state"></span><span id="IN-STATE"></span>

**In-State** (0)


</dt> <dd></dd> <dt>

<span id="Next-State"></span><span id="next-state"></span><span id="NEXT-STATE"></span>

**Next-State** (1)


</dt> <dd></dd> </dl>

</dd> </dl>

## Remarks

WMI does not implement this class. For WMI classes derived from **CIM\_SoftwareElementChecks**, see [Win32 Classes](win32-provider.md).

This documentation is derived from the CIM class descriptions published by the DMTF. Microsoft may have made changes to correct minor errors, conform to Microsoft SDK documentation standards, or provide more information.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



 

