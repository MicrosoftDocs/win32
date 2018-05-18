---
Description: 'The Win32\_COMApplicationSettings association WMI class relates a DCOM application and its configuration settings.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'b08eaff1-b42a-42f3-abf7-3664b6195acd'
ms.prod: 'windows-server-dev'
ms.technology:
- cimwin32
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'Win32\_COMApplicationSettings class'
---

# Win32\_COMApplicationSettings class

The **Win32\_COMApplicationSettings** association [WMI class](https://msdn.microsoft.com/library/aa393244) relates a DCOM application and its configuration settings.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{E5D8A563-F6C0-11d2-B35E-00105A1F8569}"), AMENDMENT]
class Win32_COMApplicationSettings : CIM_ElementSetting
{
  Win32_DCOMApplicationSetting REF Setting;
  Win32_DCOMApplication        REF Element;
};
```

## Members

The **Win32\_COMApplicationSettings** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_COMApplicationSettings** class has these properties.

<dl> <dt>

**Element**
</dt> <dd> <dl> <dt>

Data type: **Win32\_DCOMApplication**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Element"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("WMI\|Win32\_DCOMApplication")
</dt> </dl>

A [**Win32\_DCOMApplication**](win32-dcomapplication.md) that represents the DCOM application where the settings are applied.

</dd> <dt>

**Setting**
</dt> <dd> <dl> <dt>

Data type: **Win32\_DCOMApplicationSetting**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Setting"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("WMI\|Win32\_DCOMApplicationSetting")
</dt> </dl>

A [**Win32\_DCOMApplicationSetting**](win32-dcomapplicationsetting.md) that represents the configuration settings associated with the DCOM application.

</dd> </dl>

## Remarks

The **Win32\_COMApplicationSettings** class is derived from [**CIM\_ElementSetting**](cim-elementsetting.md).

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

[**CIM\_ElementSetting**](cim-elementsetting.md)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/aa392727)
</dt> </dl>

 

 




