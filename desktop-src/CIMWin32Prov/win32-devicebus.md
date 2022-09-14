---
description: The Win32\_DeviceBus association WMI class relates a system bus and a logical device using the bus. This class is used to discover which devices are on which bus.
ms.assetid: 2d7d83a5-c058-40c0-aab3-7700f4067a16
ms.tgt_platform: multiple
title: Win32_DeviceBus class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_DeviceBus
- Win32_DeviceBus.Dependent
- Win32_DeviceBus.Antecedent
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# Win32\_DeviceBus class

The **Win32\_DeviceBus** association [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) relates a system bus and a logical device using the bus. This class is used to discover which devices are on which bus.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{8502C50F-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_DeviceBus : CIM_Dependency
{
  CIM_LogicalDevice REF Dependent;
  Win32_Bus         REF Antecedent;
};
```

## Members

The **Win32\_DeviceBus** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_DeviceBus** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_Bus**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](/windows/desktop/WmiSdk/key-qualifier), [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Antecedent"), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("WMI\|Win32\_Bus")
</dt> </dl>

A [**Win32\_Bus**](win32-bus.md) that describes the properties of the system bus that is used by the logical device.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_LogicalDevice**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](/windows/desktop/WmiSdk/key-qualifier), [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Dependent"), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("CIM\|CIM\_LogicalDevice")
</dt> </dl>

A [**CIM\_LogicalDevice**](cim-logicaldevice.md) that describes the properties of the logical device that is using the system bus.

</dd> </dl>

## Remarks

The **Win32\_DeviceBus** class is derived from [**CIM\_Dependency**](cim-dependency.md).

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

 

