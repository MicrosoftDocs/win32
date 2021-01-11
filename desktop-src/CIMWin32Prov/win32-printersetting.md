---
description: The Win32\_PrinterSetting association WMI class relates a printer and its configuration settings.
ms.assetid: 5d0f0724-0583-449b-a6da-336e7c8e526e
ms.tgt_platform: multiple
title: Win32_PrinterSetting class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_PrinterSetting
- Win32_PrinterSetting.Setting
- Win32_PrinterSetting.Element
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# Win32\_PrinterSetting class

The **Win32\_PrinterSetting** association [WMI class](../wmisdk/retrieving-a-class.md) relates a printer and its configuration settings.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class Win32_PrinterSetting : Win32_DeviceSettings
{
  CIM_Setting       REF Setting;
  CIM_LogicalDevice REF Element;
};
```

## Members

The **Win32\_PrinterSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_PrinterSetting** class has these properties.

<dl> <dt>

**Element**
</dt> <dd> <dl> <dt>

Data type: **CIM\_LogicalDevice**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](../wmisdk/key-qualifier.md), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("CIM\|CIM\_LogicalDevice")
</dt> </dl>

A [**CIM\_LogicalDevice**](cim-logicaldevice.md) that represents properties of the logical device on which the settings can be applied.

This property is inherited from [**Win32\_DeviceSettings**](win32-devicesettings.md).

</dd> <dt>

**Setting**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Setting**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](../wmisdk/key-qualifier.md), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("CIM\|CIM\_Setting")
</dt> </dl>

A [**CIM\_Setting**](cim-setting.md) that represents settings that can be applied to the logical device.

This property is inherited from [**Win32\_DeviceSettings**](win32-devicesettings.md).

</dd> </dl>

## Remarks

The **Win32\_PrinterSetting** class is derived from [**Win32\_DeviceSettings**](win32-devicesettings.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                        |
| MOF<br/>                      | <dl> <dt>Win32\_Printer.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl>       |



## See also

<dl> <dt>

[**Win32\_DeviceSettings**](win32-devicesettings.md)
</dt> <dt>

[Computer System Hardware Classes](computer-system-hardware-classes.md)
</dt> </dl>

 

 
