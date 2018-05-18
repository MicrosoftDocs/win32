---
Description: 'The Win32\_SystemDesktop association WMI class relates a computer system and its desktop configuration.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '2b024660-d707-4463-8207-73df74bfa7d6'
ms.prod: 'windows-server-dev'
ms.technology:
- cimwin32
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'Win32\_SystemDesktop class'
---

# Win32\_SystemDesktop class

The **Win32\_SystemDesktop** association [WMI class](wmi.retrieving_a_class) relates a computer system and its desktop configuration.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{8502C506-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_SystemDesktop : Win32_SystemSetting
{
  Win32_ComputerSystem REF Element;
  Win32_Desktop        REF Setting;
};
```

## Members

The **Win32\_SystemDesktop** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_SystemDesktop** class has these properties.

<dl> <dt>

**Element**
</dt> <dd> <dl> <dt>

Data type: **Win32\_ComputerSystem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](wmi.standard_qualifiers) ("Element"), [**MappingStrings**](wmi.standard_qualifiers) ("WMI\|Win32\_ComputerSystem")
</dt> </dl>

Reference to the instance representing the computer system where the desktop configuration exists.

</dd> <dt>

**Setting**
</dt> <dd> <dl> <dt>

Data type: **Win32\_Desktop**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](wmi.standard_qualifiers) ("Setting"), [**MappingStrings**](wmi.standard_qualifiers) ("WMI\|Win32\_Desktop")
</dt> </dl>

Reference to the instance representing the configuration existing on the computer system.

</dd> </dl>

## Remarks

The **Win32\_SystemDesktop** class is derived from [**Win32\_SystemSetting**](win32-systemsetting.md).

## Requirements



|                                     |                                                                                         |
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

[Operating System Classes](wmi.operating_system_classes)
</dt> </dl>

 

 




