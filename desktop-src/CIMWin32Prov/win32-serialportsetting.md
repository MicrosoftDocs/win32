---
Description: 'The Win32\_SerialPortSetting association WMI class relates a serial port and its configuration settings.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '57856207-abe5-4d93-9a34-acfe30ccd80c'
ms.prod: 'windows-server-dev'
ms.technology:
- cimwin32
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'Win32\_SerialPortSetting class'
---

# Win32\_SerialPortSetting class

The **Win32\_SerialPortSetting** association [WMI class](wmi.retrieving_a_class) relates a serial port and its configuration settings.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{8502C4FE-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_SerialPortSetting : Win32_DeviceSettings
{
  Win32_SerialPortConfiguration REF Setting;
  Win32_SerialPort              REF Element;
};
```

## Members

The **Win32\_SerialPortSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_SerialPortSetting** class has these properties.

<dl> <dt>

**Element**
</dt> <dd> <dl> <dt>

Data type: **Win32\_SerialPort**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](wmi.standard_qualifiers) ("Element"), [**MappingStrings**](wmi.standard_qualifiers) ("WMI\|Win32\_SerialPort")
</dt> </dl>

A [**Win32\_SerialPort**](win32-serialport.md) that contains the properties of a serial port on the computer system.

</dd> <dt>

**Setting**
</dt> <dd> <dl> <dt>

Data type: **Win32\_SerialPortConfiguration**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](wmi.standard_qualifiers) ("Setting"), [**MappingStrings**](wmi.standard_qualifiers) ("WMI\|Win32\_SerialPortConfiguration")
</dt> </dl>

A [**Win32\_SerialPortConfiguration**](win32-serialportconfiguration.md) that contains the configuration setting for the serial port.

</dd> </dl>

## Remarks

The **Win32\_SerialPortSetting** class is derived from [**Win32\_DeviceSettings**](win32-devicesettings.md).

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

[**Win32\_DeviceSettings**](win32-devicesettings.md)
</dt> <dt>

[Computer System Hardware Classes](computer-system-hardware-classes.md)
</dt> </dl>

 

 




