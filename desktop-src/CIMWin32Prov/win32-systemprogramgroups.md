---
description: The Win32\_SystemProgramGroups association WMI class relates a computer system and a logical program group.
ms.assetid: cbf810c8-a967-4d60-889c-e47c43b039ea
ms.tgt_platform: multiple
title: Win32_SystemProgramGroups class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_SystemProgramGroups
- Win32_SystemProgramGroups.Element
- Win32_SystemProgramGroups.Setting
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# Win32\_SystemProgramGroups class

The **Win32\_SystemProgramGroups** association [WMI class](../wmisdk/retrieving-a-class.md) relates a computer system and a logical program group.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{8502C505-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_SystemProgramGroups : Win32_SystemSetting
{
  Win32_ComputerSystem      REF Element;
  Win32_LogicalProgramGroup REF Setting;
};
```

## Members

The **Win32\_SystemProgramGroups** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_SystemProgramGroups** class has these properties.

<dl> <dt>

**Element**
</dt> <dd> <dl> <dt>

Data type: **Win32\_ComputerSystem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](../wmisdk/standard-qualifiers.md) ("Element"), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("WMI\|Win32\_ComputerSystem")
</dt> </dl>

Reference to the instance representing the computer system containing the logical program group.

</dd> <dt>

**Setting**
</dt> <dd> <dl> <dt>

Data type: **Win32\_LogicalProgramGroup**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](../wmisdk/standard-qualifiers.md) ("Setting"), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("WMI\|Win32\_LogicalProgramGroup")
</dt> </dl>

Reference to the instance representing the logical program group on the computer system.

</dd> </dl>

## Remarks

The **Win32\_SystemProgramGroups** class is derived from [**Win32\_SystemSetting**](win32-systemsetting.md).

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

[**Win32\_SystemSetting**](win32-systemsetting.md)
</dt> <dt>

[Operating System Classes](./operating-system-classes.md)
</dt> </dl>

 

 
