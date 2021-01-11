---
description: The Win32\_SystemProcesses association WMI class relates a computer system and a process running on that system.
ms.assetid: 0d8c3ec6-265e-4486-8e94-f5acd2845cf5
ms.tgt_platform: multiple
title: Win32_SystemProcesses class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_SystemProcesses
- Win32_SystemProcesses.GroupComponent
- Win32_SystemProcesses.PartComponent
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# Win32\_SystemProcesses class

The **Win32\_SystemProcesses** association [WMI class](../wmisdk/retrieving-a-class.md) relates a computer system and a process running on that system.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{8502C4F3-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_SystemProcesses : CIM_SystemComponent
{
  Win32_ComputerSystem REF GroupComponent;
  Win32_Process        REF PartComponent;
};
```

## Members

The **Win32\_SystemProcesses** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_SystemProcesses** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_ComputerSystem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](../wmisdk/key-qualifier.md), [**Override**](../wmisdk/standard-qualifiers.md) ("GroupComponent"), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("WMI\|Win32\_ComputerSystem")
</dt> </dl>

Reference to the instance representing the computer system upon which the process is running.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_Process**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](../wmisdk/key-qualifier.md), [**Override**](../wmisdk/standard-qualifiers.md) ("PartComponent"), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("WMI\|Win32\_Process")
</dt> </dl>

Reference to the instance representing the process running on the computer system.

</dd> </dl>

## Remarks

The **Win32\_SystemProcesses** class is derived from [**CIM\_SystemComponent**](cim-systemcomponent.md).

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

[Operating System Classes](./operating-system-classes.md)
</dt> </dl>

 

 
