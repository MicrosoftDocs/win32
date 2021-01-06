---
description: The CIM\_ElementCapacity class associates a CIM\_PhysicalCapacity object with one or more physical elements. It associates a description of the minimum and maximum hardware requirements (or capabilities) to the physical elements being described.
ms.assetid: 368c31e8-d56b-4b90-ba3f-20d9b0de8730
ms.tgt_platform: multiple
title: CIM_ElementCapacity class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_ElementCapacity
- CIM_ElementCapacity.Capacity
- CIM_ElementCapacity.Element
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_ElementCapacity class

The **CIM\_ElementCapacity** class associates a [**CIM\_PhysicalCapacity**](cim-physicalcapacity.md) object with one or more physical elements. It associates a description of the minimum and maximum hardware requirements (or capabilities) to the physical elements being described.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, Association, UUID("{FAF76B6A-798C-11D2-AAD1-006008C78BC7}"), AMENDMENT]
class CIM_ElementCapacity
{
  CIM_PhysicalCapacity REF Capacity;
  CIM_PhysicalElement  REF Element;
};
```

## Members

The **CIM\_ElementCapacity** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ElementCapacity** class has these properties.

<dl> <dt>

**Capacity**
</dt> <dd> <dl> <dt>

Data type: **CIM\_PhysicalCapacity**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to the [**CIM\_PhysicalCapacity**](cim-physicalcapacity.md) class that describes the minimum and maximum requirements and the ability to support different types of hardware for a physical element.

</dd> <dt>

**Element**
</dt> <dd> <dl> <dt>

Data type: **CIM\_PhysicalElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Min**](/windows/desktop/WmiSdk/standard-qualifiers) (1)
</dt> </dl>

Reference to the physical element being described.

</dd> </dl>

## Remarks

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



 

