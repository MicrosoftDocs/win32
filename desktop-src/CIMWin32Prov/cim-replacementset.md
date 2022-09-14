---
description: The CIM\_ReplacementSet class aggregates physical elements that must be replaced together.
ms.assetid: db55ae2d-49b3-4cc9-95ee-1e757f58a427
ms.tgt_platform: multiple
title: CIM_ReplacementSet class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_ReplacementSet
- CIM_ReplacementSet.Description
- CIM_ReplacementSet.Name
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_ReplacementSet class

The **CIM\_ReplacementSet** class aggregates physical elements that must be replaced together. For example, when replacing a memory card, the component memory chips can also be removed and replaced. Or, this association can be used to replace or upgrade a set of memory chips.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{FAF76B6C-798C-11D2-AAD1-006008C78BC7}"), AMENDMENT]
class CIM_ReplacementSet
{
  string Description;
  string Name;
};
```

## Members

The **CIM\_ReplacementSet** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ReplacementSet** class has these properties.

<dl> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Free-form string that specifies information related to this class. The purpose of the set, or information related to how the component elements are replaced, can be included in this property.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](/windows/desktop/WmiSdk/key-qualifier), [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (256)
</dt> </dl>

Free-form string that defines a label for this property. This property is the key for the object.

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



 

