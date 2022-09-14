---
description: The Win32\_AssociatedProcessorMemory association WMI class relates a processor and its cache memory.
ms.assetid: 23da2a9d-772e-4258-9489-07d47801b2d8
ms.tgt_platform: multiple
title: Win32_AssociatedProcessorMemory class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_AssociatedProcessorMemory
- Win32_AssociatedProcessorMemory.BusSpeed
- Win32_AssociatedProcessorMemory.Dependent
- Win32_AssociatedProcessorMemory.Antecedent
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# Win32\_AssociatedProcessorMemory class

The **Win32\_AssociatedProcessorMemory** association [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) relates a processor and its cache memory.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{074737F0-ACBC-11d2-ABF6-00805F538618}"), AMENDMENT]
class Win32_AssociatedProcessorMemory : CIM_AssociatedProcessorMemory
{
  uint32                BusSpeed;
  Win32_Processor   REF Dependent;
  Win32_CacheMemory REF Antecedent;
};
```

## Members

The **Win32\_AssociatedProcessorMemory** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_AssociatedProcessorMemory** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_CacheMemory**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier), [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Antecedent"), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("WMI\|Win32\_CacheMemory")
</dt> </dl>

A [**Win32\_CacheMemory**](win32-cachememory.md) that describes the cache memory available to the processor.

</dd> <dt>

**BusSpeed**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("megahertz")
</dt> </dl>

Speed of the bus, in megahertz (MHz), between the processor and memory.

This property is inherited from [**CIM\_AssociatedProcessorMemory**](cim-associatedprocessormemory.md).

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_Processor**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier), [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Dependent"), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("WMI\|Win32\_Processor")
</dt> </dl>

A [**Win32\_Processor**](win32-processor.md) that describes the processor that is using the cache memory.

</dd> </dl>

## Remarks

The **Win32\_AssociatedProcessorMemory** class is derived from [**CIM\_AssociatedProcessorMemory**](cim-associatedprocessormemory.md).

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

[**CIM\_AssociatedProcessorMemory**](cim-associatedprocessormemory.md)
</dt> <dt>

[Computer System Hardware Classes](computer-system-hardware-classes.md)
</dt> </dl>

 

