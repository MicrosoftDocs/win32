---
description: The Win32\_PhysicalMemoryLocation association WMI class relates an array of physical memory and its physical memory.
ms.assetid: 40252428-77ca-4dfb-8048-c05096a114d8
ms.tgt_platform: multiple
title: Win32_PhysicalMemoryLocation class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_PhysicalMemoryLocation
- Win32_PhysicalMemoryLocation.LocationWithinContainer
- Win32_PhysicalMemoryLocation.PartComponent
- Win32_PhysicalMemoryLocation.GroupComponent
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# Win32\_PhysicalMemoryLocation class

The **Win32\_PhysicalMemoryLocation** association [WMI class](../wmisdk/retrieving-a-class.md) relates an array of physical memory and its physical memory.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{B24EF562-BBBE-11d2-ABFB-00805F538618}"), AMENDMENT]
class Win32_PhysicalMemoryLocation : CIM_PackagedComponent
{
  string                        LocationWithinContainer;
  Win32_PhysicalMemory      REF PartComponent;
  Win32_PhysicalMemoryArray REF GroupComponent;
};
```

## Members

The **Win32\_PhysicalMemoryLocation** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_PhysicalMemoryLocation** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_PhysicalMemoryArray**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](../wmisdk/key-qualifier.md), [**Override**](../wmisdk/standard-qualifiers.md) ("GroupComponent"), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("WMI\|Win32\_PhysicalMemoryArray")
</dt> </dl>

A [**Win32\_PhysicalMemoryArray**](win32-physicalmemoryarray.md) that represents the physical memory array that contains the physical memory.

</dd> <dt>

**LocationWithinContainer**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Free-form string that represents the positioning of the physical element within the physical package. Information relative to stationary elements in the container (for example, "second drive bay from the top"), angles, altitudes, and other data can be recorded in this property. This string could supplement or be used in place of instantiating the [**CIM\_Location**](cim-location.md) object.

This property is inherited from [**CIM\_Container**](cim-container.md).

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_PhysicalMemory**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](../wmisdk/key-qualifier.md), [**Override**](../wmisdk/standard-qualifiers.md) ("PartComponent"), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("WMI\|Win32\_PhysicalMemory")
</dt> </dl>

A [**Win32\_PhysicalMemory**](win32-physicalmemory.md) that represents the physical memory contained in the physical memory array.

</dd> </dl>

## Remarks

The **Win32\_PhysicalMemoryLocation** class is derived from [**CIM\_PackagedComponent**](cim-packagedcomponent.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_PackagedComponent**](cim-packagedcomponent.md)
</dt> <dt>

[Computer System Hardware Classes](computer-system-hardware-classes.md)
</dt> </dl>

 

 
