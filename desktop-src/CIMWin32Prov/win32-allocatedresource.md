---
description: The Win32\_AllocatedResource association WMI class relates a logical device to a system resource. This class is used to discover which resources, such as IRQs or DMA channels, are in use by a specific device.
ms.assetid: cfac1209-1405-4fee-847c-8a61504bfac1
ms.tgt_platform: multiple
title: Win32_AllocatedResource class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_AllocatedResource
- Win32_AllocatedResource.Dependent
- Win32_AllocatedResource.Antecedent
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# Win32\_AllocatedResource class

The **Win32\_AllocatedResource** association [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) relates a logical device to a system resource. This class is used to discover which resources, such as IRQs or DMA channels, are in use by a specific device.

This class is obsolete. In place of this class, you should use the properties in the [**Win32\_PNPAllocatedResource**](win32-pnpallocatedresource.md) class.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[DEPRECATED, Dynamic, Provider("CIMWin32"), UUID("{8502C50D-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_AllocatedResource : CIM_Dependency
{
  CIM_LogicalDevice  REF Dependent;
  CIM_SystemResource REF Antecedent;
};
```

## Members

The **Win32\_AllocatedResource** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_AllocatedResource** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_SystemResource**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](/windows/desktop/WmiSdk/key-qualifier), [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Antecedent"), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("CIM\|CIM\_SystemResource")
</dt> </dl>

A [**CIM\_SystemResource**](cim-systemresource.md) that describes the properties of a system resource available to the logical device.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_LogicalDevice**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](/windows/desktop/WmiSdk/key-qualifier), [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Dependent"), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("CIM\|CIM\_LogicalDevice")
</dt> </dl>

A [**CIM\_LogicalDevice**](cim-logicaldevice.md) that represents the properties of the logical device that is using the system resources assigned to it.

</dd> </dl>

## Remarks

The **Win32\_AllocatedResource** class is derived from [**CIM\_Dependency**](cim-dependency.md).

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
</dt> <dt>

[Computer System Hardware Classes](computer-system-hardware-classes.md)
</dt> </dl>

 

