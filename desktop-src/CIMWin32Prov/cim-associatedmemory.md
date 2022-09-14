---
description: The CIM\_AssociateMemory class associates installed or associated memory, such as cache memory with a logical device.
ms.assetid: b108d0cc-9353-4940-a5f6-34bb93330a62
ms.tgt_platform: multiple
title: CIM_AssociatedMemory class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_AssociatedMemory
- CIM_AssociatedMemory.Dependent
- CIM_AssociatedMemory.Antecedent
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_AssociatedMemory class

The **CIM\_AssociateMemory** class associates installed or associated memory, such as cache memory with a logical device.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[abstract, UUID("{464FFAB0-946F-11d2-AAE2-006008C78BC7}"), AMENDMENT]
class CIM_AssociatedMemory : CIM_Dependency
{
  CIM_LogicalDevice REF Dependent;
  CIM_Memory        REF Antecedent;
};
```

## Members

The **CIM\_AssociatedMemory** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_AssociatedMemory** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Memory**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Antecedent")
</dt> </dl>

A [**CIM\_Memory**](cim-memory.md) that describes the memory installed on or associated with a device.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_LogicalDevice**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Dependent")
</dt> </dl>

A [**CIM\_LogicalDevice**](cim-logicaldevice.md) that describes the logical device.

</dd> </dl>

## Remarks

The **CIM\_AssociatedMemory** class is derived from [**CIM\_Dependency**](cim-dependency.md).

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

 

