---
description: The CIM\_ParticipatesInSet class identifies physical elements that should be replaced together.
ms.assetid: 417607a3-6682-4745-a5ca-0538a0d4853d
ms.tgt_platform: multiple
title: CIM_ParticipatesInSet class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_ParticipatesInSet
- CIM_ParticipatesInSet.Element
- CIM_ParticipatesInSet.Set
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_ParticipatesInSet class

The **CIM\_ParticipatesInSet** class identifies physical elements that should be replaced together.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of its inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, Association, Aggregation, UUID("{FAF76B6D-798C-11D2-AAD1-006008C78BC7}"), AMENDMENT]
class CIM_ParticipatesInSet
{
  CIM_PhysicalElement REF Element;
  CIM_ReplacementSet  REF Set;
};
```

## Members

The **CIM\_ParticipatesInSet** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ParticipatesInSet** class has these properties.

<dl> <dt>

**Element**
</dt> <dd> <dl> <dt>

Data type: **CIM\_PhysicalElement**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to the physical element that should be replaced with other elements, as a set.

</dd> <dt>

**Set**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ReplacementSet**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Aggregate**](/windows/desktop/WmiSdk/standard-qualifiers)
</dt> </dl>

Reference to the replacement set of elements.

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



 

