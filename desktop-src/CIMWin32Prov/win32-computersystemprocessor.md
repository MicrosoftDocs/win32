---
description: The Win32\_ComputerSystemProcessor association WMI class relates a computer system and a processor running on that system.
ms.assetid: e630ebea-19bf-43c7-a8a0-7acfda3a752b
ms.tgt_platform: multiple
title: Win32_ComputerSystemProcessor class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_ComputerSystemProcessor
- Win32_ComputerSystemProcessor.PartComponent
- Win32_ComputerSystemProcessor.GroupComponent
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# Win32\_ComputerSystemProcessor class

The **Win32\_ComputerSystemProcessor** association [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) relates a computer system and a processor running on that system.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{719A6839-C124-11d2-85E8-0000F8102E5F}"), AMENDMENT]
class Win32_ComputerSystemProcessor : Win32_SystemDevices
{
  Win32_Processor      REF PartComponent;
  Win32_ComputerSystem REF GroupComponent;
};
```

## Members

The **Win32\_ComputerSystemProcessor** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_ComputerSystemProcessor** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_ComputerSystem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("GroupComponent"), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("WMI\|Win32\_ComputerSystem")
</dt> </dl>

A **Win32\_ComputerSystem** that describes the properties of the computer system on which the processor is running.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_Processor**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("PartComponent"), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("WMI\|Win32\_Processor")
</dt> </dl>

A [**Win32\_Processor**](win32-processor.md) that describes the properties of a processor which is running the computer system.

</dd> </dl>

## Remarks

The **Win32\_ComputerSystemProcessor** class is derived from [**Win32\_SystemDevices**](win32-systemdevices.md).

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

[**Win32\_SystemDevices**](win32-systemdevices.md)
</dt> <dt>

[Operating System Classes](/previous-versions//aa392727(v=vs.85))
</dt> </dl>

 

