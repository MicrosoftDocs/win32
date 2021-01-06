---
description: The Win32\_SystemBIOS association WMI class relates a computer system (including data such as startup properties, time zones, boot configurations, or administrative passwords), and a system BIOS (services, languages, and system management properties).
ms.assetid: 92747b1b-ef28-40ab-868a-6755aee8c723
ms.tgt_platform: multiple
title: Win32_SystemBIOS class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_SystemBIOS
- Win32_SystemBIOS.PartComponent
- Win32_SystemBIOS.GroupComponent
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# Win32\_SystemBIOS class

The **Win32\_SystemBIOS** association [WMI class](../wmisdk/retrieving-a-class.md) relates a computer system (including data such as startup properties, time zones, boot configurations, or administrative passwords), and a system BIOS (services, languages, and system management properties).

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{8502C4EE-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_SystemBIOS : CIM_SystemComponent
{
  Win32_BIOS           REF PartComponent;
  Win32_ComputerSystem REF GroupComponent;
};
```

## Members

The **Win32\_SystemBIOS** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_SystemBIOS** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_ComputerSystem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](../wmisdk/key-qualifier.md), [**Override**](../wmisdk/standard-qualifiers.md) ("GroupComponent"), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("WMI\|Win32\_ComputerSystem")
</dt> </dl>

The [**Win32\_ComputerSystem**](win32-computersystemprocessor.md) containing the BIOS of the association.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_BIOS**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](../wmisdk/key-qualifier.md), [**Override**](../wmisdk/standard-qualifiers.md) ("PartComponent"), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("WMI\|Win32\_BIOS")
</dt> </dl>

A [**Win32\_BIOS**](win32-bios.md) contained in the computer system of this association.

</dd> </dl>

## Remarks

The **Win32\_SystemBIOS** class is derived from [**CIM\_SystemComponent**](cim-systemcomponent.md).

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

[**CIM\_SystemComponent**](cim-systemcomponent.md)
</dt> <dt>

[Computer System Hardware Classes](computer-system-hardware-classes.md)
</dt> </dl>

 

 
