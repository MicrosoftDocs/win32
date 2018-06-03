---
Description: The Win32\_VideoConfiguration class is not active. It will not return any instances as there is no provider backing it.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8dd15e8a-ff9b-4e75-bae9-8c80548301ab
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32\_VideoConfiguration class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_VideoConfiguration class

The **Win32\_VideoConfiguration** class is not active. It will not return any instances as there is no provider backing it.

The **Win32\_VideoConfiguration** class represents a configuration of a video subsystem. This class has been deprecated in favor of the properties contained in the [**Win32\_VideoController**](win32-videocontroller.md), [**Win32\_DesktopMonitor**](win32-desktopmonitor.md), and [**CIM\_VideoControllerResolution**](cim-videocontrollerresolution.md) classes

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[DEPRECATED, UUID("{8502C4ED-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_VideoConfiguration : CIM_Setting
{
  string   Caption;
  string   Description;
  string   SettingID;
  uint32   ActualColorResolution;
  string   AdapterChipType;
  string   AdapterCompatibility;
  string   AdapterDACType;
  string   AdapterDescription;
  uint32   AdapterRAM;
  string   AdapterType;
  uint32   BitsPerPixel;
  uint32   ColorPlanes;
  uint32   ColorTableEntries;
  uint32   DeviceSpecificPens;
  datetime DriverDate;
  uint32   HorizontalResolution;
  string   InfFilename;
  string   InfSection;
  string   InstalledDisplayDrivers;
  string   MonitorManufacturer;
  string   MonitorType;
  string   Name;
  uint32   PixelsPerXLogicalInch;
  uint32   PixelsPerYLogicalInch;
  uint32   RefreshRate;
  string   ScanMode;
  uint32   ScreenHeight;
  uint32   ScreenWidth;
  uint32   SystemPaletteEntries;
  uint32   VerticalResolution;
};
```

## Members

The **Win32\_VideoConfiguration** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_VideoConfiguration** class has these properties.

<dl> <dt>

**ActualColorResolution**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/windows/desktop/63bdbafc-51f3-4714-8b7e-9d5a61cef45e), [**MappingStrings**](https://msdn.microsoft.com/windows/desktop/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Win32API\|Device Context Functions\|[**GetDeviceCaps**](https://msdn.microsoft.com/windows/desktop/d524c4c7-22af-495d-aecc-b9921e53ca7b)\|COLORRES"), [**Units**](https://msdn.microsoft.com/windows/desktop/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("bits per pixel")
</dt> </dl>

Indicates the current color depth of the video display.

This property has been deprecated in favor of a corresponding property(s) contained in the [**Win32\_VideoController**](win32-videocontroller.md), [**Win32\_DesktopMonitor**](win32-desktopmonitor.md) and//or [**CIM\_VideoControllerResolution**](cim-videocontrollerresolution.md).

</dd> <dt>

**AdapterChipType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/windows/desktop/63bdbafc-51f3-4714-8b7e-9d5a61cef45e), [**MappingStrings**](https://msdn.microsoft.com/windows/desktop/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Win32Registry\|System\\\\CurrentControlSet\\\\Services\\\\Class\\\\Info\|ChipType")
</dt> </dl>

Contains the name of the adapter chip.

Example: s3

This property has been deprecated in favor of a corresponding property(s) contained in the [**Win32\_VideoController**](win32-videocontroller.md), [**Win32\_DesktopMonitor**](win32-desktopmonitor.md) and//or [**CIM\_VideoControllerResolution**](cim-videocontrollerresolution.md).

</dd> <dt>

**AdapterCompatibility**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/windows/desktop/63bdbafc-51f3-4714-8b7e-9d5a61cef45e), [**key**](https://msdn.microsoft.com/windows/desktop/838d295f-e812-4e46-99a4-d2714a0ae8dc), [**MaxLen**](https://msdn.microsoft.com/windows/desktop/671ea769-f68d-4788-96f5-c4f86ab3b00e) (256), [**MappingStrings**](https://msdn.microsoft.com/windows/desktop/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("WMI")
</dt> </dl>

Specifies the name of the manufacturer of the adapter. This name can be used to compare the compatibility of this device with the needs of the computer system.

This property has been deprecated in favor of a corresponding property(s) contained in the [**Win32\_VideoController**](win32-videocontroller.md), [**Win32\_DesktopMonitor**](win32-desktopmonitor.md) and//or [**CIM\_VideoControllerResolution**](cim-videocontrollerresolution.md).

</dd> <dt>

**AdapterDACType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/windows/desktop/63bdbafc-51f3-4714-8b7e-9d5a61cef45e), [**MappingStrings**](https://msdn.microsoft.com/windows/desktop/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Win32Registry\|System\\\\CurrentControlSet\\\\Services\\\\Class\\\\Info\|DACType")
</dt> </dl>

Indicates the name of the digital-to-analog chip (DAC) used in the adapter.

This property has been deprecated in favor of a corresponding property(s) contained in the [**Win32\_VideoController**](win32-videocontroller.md), [**Win32\_DesktopMonitor**](win32-desktopmonitor.md) and//or [**CIM\_VideoControllerResolution**](cim-videocontrollerresolution.md).

</dd> <dt>

**AdapterDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/windows/desktop/63bdbafc-51f3-4714-8b7e-9d5a61cef45e), [**MappingStrings**](https://msdn.microsoft.com/windows/desktop/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("WMI")
</dt> </dl>

Contains a description or descriptive name of the video adapter.

This property has been deprecated in favor of a corresponding property(s) contained in the [**Win32\_VideoController**](win32-videocontroller.md), [**Win32\_DesktopMonitor**](win32-desktopmonitor.md) and//or [**CIM\_VideoControllerResolution**](cim-videocontrollerresolution.md).

</dd> <dt>

**AdapterRAM**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/windows/desktop/63bdbafc-51f3-4714-8b7e-9d5a61cef45e), [**MappingStrings**](https://msdn.microsoft.com/windows/desktop/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Win32Registry\|System\\\\CurrentControlSet\\\\Services\\\\Class\\\\Info\|VideoMemory"), [**Units**](https://msdn.microsoft.com/windows/desktop/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("bytes")
</dt> </dl>

Indicates the memory size of the video adapter.

Example: 16777216

This property has been deprecated in favor of a corresponding property(s) contained in the [**Win32\_VideoController**](win32-videocontroller.md), [**Win32\_DesktopMonitor**](win32-desktopmonitor.md) and//or [**CIM\_VideoControllerResolution**](cim-videocontrollerresolution.md).

</dd> <dt>

**AdapterType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/windows/desktop/63bdbafc-51f3-4714-8b7e-9d5a61cef45e), [**MappingStrings**](https://msdn.microsoft.com/windows/desktop/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Win32Registry\|HARDWARE\\\\Description\\\\System\\\\DisplayController\\\\0\\\\Identifier")
</dt> </dl>

Indicates the type of video adapter.

Character Set: Alphanumeric

This property has been deprecated in favor of a corresponding property(s) contained in the [**Win32\_VideoController**](win32-videocontroller.md), [**Win32\_DesktopMonitor**](win32-desktopmonitor.md) and//or [**CIM\_VideoControllerResolution**](cim-videocontrollerresolution.md).

</dd> <dt>

**BitsPerPixel**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/windows/desktop/63bdbafc-51f3-4714-8b7e-9d5a61cef45e), [**MappingStrings**](https://msdn.microsoft.com/windows/desktop/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Win32API\|Device Context Functions\|[**GetDeviceCaps**](https://msdn.microsoft.com/windows/desktop/d524c4c7-22af-495d-aecc-b9921e53ca7b)\|BITSPIXEL")
</dt> </dl>

Indicates the actual number of bits per pixel representing the display. This may be scaled to the current video setting (represented by the ActualColorResolution property) of the user.

Example: 8

This property has been deprecated in favor of a corresponding property(s) contained in the [**Win32\_VideoController**](win32-videocontroller.md), [**Win32\_DesktopMonitor**](win32-desktopmonitor.md) and//or [**CIM\_VideoControllerResolution**](cim-videocontrollerresolution.md).

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/windows/desktop/671ea769-f68d-4788-96f5-c4f86ab3b00e) (64)
</dt> </dl>

Short textual description of the current object.

This property is inherited from [**CIM\_Setting**](cim-setting.md).

</dd> <dt>

**ColorPlanes**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/windows/desktop/63bdbafc-51f3-4714-8b7e-9d5a61cef45e), [**MappingStrings**](https://msdn.microsoft.com/windows/desktop/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Win32API\|Device Context Functions\|[**GetDeviceCaps**](https://msdn.microsoft.com/windows/desktop/d524c4c7-22af-495d-aecc-b9921e53ca7b)\|PLANES")
</dt> </dl>

Indicates the current number of color planes used in the video display. A color plane is another way to represent pixel colors; instead of assigning a single RGB value to each a pixel, color planes separate the graphic into each of the primary color components (red green blue), and store them in their own planes. This allows for greater color depths on 8 and 16 bit video systems. Present graphics systems have the bitwidth large enough to store color depth information, making only one color plane necessary.

Example: 1

This property has been deprecated in favor of a corresponding property(s) contained in the [**Win32\_VideoController**](win32-videocontroller.md), [**Win32\_DesktopMonitor**](win32-desktopmonitor.md) and//or [**CIM\_VideoControllerResolution**](cim-videocontrollerresolution.md).

</dd> <dt>

**ColorTableEntries**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/windows/desktop/63bdbafc-51f3-4714-8b7e-9d5a61cef45e), [**MappingStrings**](https://msdn.microsoft.com/windows/desktop/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Win32API\|Device Context Functions\|[**GetDeviceCaps**](https://msdn.microsoft.com/windows/desktop/d524c4c7-22af-495d-aecc-b9921e53ca7b)\|NUMCOLORS")
</dt> </dl>

Indicates the number of color indexes in a color table for a video display. This property is used if the device has a color depth of no more than 8 bits per pixel. For devices with greater color depths, -1 is returned.

Example: 256

This property has been deprecated in favor of a corresponding property(s) contained in the [**Win32\_VideoController**](win32-videocontroller.md), [**Win32\_DesktopMonitor**](win32-desktopmonitor.md) and//or [**CIM\_VideoControllerResolution**](cim-videocontrollerresolution.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Textual description of the current object.

This property is inherited from [**CIM\_Setting**](cim-setting.md).

</dd> <dt>

**DeviceSpecificPens**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/windows/desktop/63bdbafc-51f3-4714-8b7e-9d5a61cef45e), [**MappingStrings**](https://msdn.microsoft.com/windows/desktop/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Win32API\|Device Context Functions\|[**GetDeviceCaps**](https://msdn.microsoft.com/windows/desktop/d524c4c7-22af-495d-aecc-b9921e53ca7b)\|NUMPENS")
</dt> </dl>

Indicates the current number of device-specific pens. A value of 0xFFFFFFFF means the device does not support pens. Pens are used to draw lines and theborders of polygonal objects.

Example: 3

This property has been deprecated in favor of a corresponding property(s) contained in the [**Win32\_VideoController**](win32-videocontroller.md), [**Win32\_DesktopMonitor**](win32-desktopmonitor.md) and//or [**CIM\_VideoControllerResolution**](cim-videocontrollerresolution.md).

</dd> <dt>

**DriverDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/windows/desktop/63bdbafc-51f3-4714-8b7e-9d5a61cef45e), [**MappingStrings**](https://msdn.microsoft.com/windows/desktop/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Win32Registry\|System\\\\CurrentControlSet\\\\Services\\\\Class\\\\AdapterDescription\|DriverDate")
</dt> </dl>

Indicates the date and time the current video driver was installed.

This property has been deprecated in favor of a corresponding property(s) contained in the [**Win32\_VideoController**](win32-videocontroller.md), [**Win32\_DesktopMonitor**](win32-desktopmonitor.md) and//or [**CIM\_VideoControllerResolution**](cim-videocontrollerresolution.md).

</dd> <dt>

**HorizontalResolution**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/windows/desktop/63bdbafc-51f3-4714-8b7e-9d5a61cef45e), [**MappingStrings**](https://msdn.microsoft.com/windows/desktop/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Win32API\|Device Context Functions\|[**GetDeviceCaps**](https://msdn.microsoft.com/windows/desktop/d524c4c7-22af-495d-aecc-b9921e53ca7b)\|HORZRES")
</dt> </dl>

Indicates the current number of pixels in the horizontal direction (X axis) of the display.

Example: 1024

This property has been deprecated in favor of a corresponding property(s) contained in the [**Win32\_VideoController**](win32-videocontroller.md), [**Win32\_DesktopMonitor**](win32-desktopmonitor.md) and//or [**CIM\_VideoControllerResolution**](cim-videocontrollerresolution.md).

</dd> <dt>

**InfFilename**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/windows/desktop/63bdbafc-51f3-4714-8b7e-9d5a61cef45e), [**MappingStrings**](https://msdn.microsoft.com/windows/desktop/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Win32Registry\|System\\\\CurrentControlSet\\\\Services\\\\Class\|InfPath")
</dt> </dl>

Specifies the path to the .inf file of the video driver.

Example: C:\\Windows\\System32\\Drivers

This property has been deprecated in favor of a corresponding property(s) contained in the [**Win32\_VideoController**](win32-videocontroller.md), [**Win32\_DesktopMonitor**](win32-desktopmonitor.md) and//or [**CIM\_VideoControllerResolution**](cim-videocontrollerresolution.md).

</dd> <dt>

**InfSection**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/windows/desktop/63bdbafc-51f3-4714-8b7e-9d5a61cef45e), [**MappingStrings**](https://msdn.microsoft.com/windows/desktop/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Win32Registry\|System\\\\CurrentControlSet\\\\Services\\\\Class\|InfSection")
</dt> </dl>

Indicates the section of the .inf file where the Win32 video information resides.

This property has been deprecated in favor of a corresponding property(s) contained in the [**Win32\_VideoController**](win32-videocontroller.md), [**Win32\_DesktopMonitor**](win32-desktopmonitor.md) and//or [**CIM\_VideoControllerResolution**](cim-videocontrollerresolution.md).

</dd> <dt>

**InstalledDisplayDrivers**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/windows/desktop/63bdbafc-51f3-4714-8b7e-9d5a61cef45e), [**MappingStrings**](https://msdn.microsoft.com/windows/desktop/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Win32Registry\|System\\\\CurrentControlSet\\\\Services\\\\Class\\\\Defaule\|drv")
</dt> </dl>

Indicates the name of the installed video driver.

This property has been deprecated in favor of a corresponding property(s) contained in the [**Win32\_VideoController**](win32-videocontroller.md), [**Win32\_DesktopMonitor**](win32-desktopmonitor.md) and//or [**CIM\_VideoControllerResolution**](cim-videocontrollerresolution.md).

</dd> <dt>

**MonitorManufacturer**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/windows/desktop/63bdbafc-51f3-4714-8b7e-9d5a61cef45e), [**MappingStrings**](https://msdn.microsoft.com/windows/desktop/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("WMI")
</dt> </dl>

Indicates the name of the manufacturer of the display device.

Example: NEC

This property has been deprecated in favor of a corresponding property(s) contained in the [**Win32\_VideoController**](win32-videocontroller.md), [**Win32\_DesktopMonitor**](win32-desktopmonitor.md) and//or [**CIM\_VideoControllerResolution**](cim-videocontrollerresolution.md).

</dd> <dt>

**MonitorType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/windows/desktop/63bdbafc-51f3-4714-8b7e-9d5a61cef45e), [**MappingStrings**](https://msdn.microsoft.com/windows/desktop/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Win32Registry\|HARDWARE\\\\Description\\\\System\\\\MonitorPeripheral\\\\0\|Identifier")
</dt> </dl>

Indicates the model name of the display device.

Example: NEC 5FGp

This property has been deprecated in favor of a corresponding property(s) contained in the [**Win32\_VideoController**](win32-videocontroller.md), [**Win32\_DesktopMonitor**](win32-desktopmonitor.md) and//or [**CIM\_VideoControllerResolution**](cim-videocontrollerresolution.md).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/windows/desktop/63bdbafc-51f3-4714-8b7e-9d5a61cef45e), [**key**](https://msdn.microsoft.com/windows/desktop/838d295f-e812-4e46-99a4-d2714a0ae8dc), [**MaxLen**](https://msdn.microsoft.com/windows/desktop/671ea769-f68d-4788-96f5-c4f86ab3b00e) (256), [**MappingStrings**](https://msdn.microsoft.com/windows/desktop/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("WMI")
</dt> </dl>

Contains an identifying name for the video configuration class.

This property has been deprecated in favor of a corresponding property(s) contained in the [**Win32\_VideoController**](win32-videocontroller.md), [**Win32\_DesktopMonitor**](win32-desktopmonitor.md) and//or [**CIM\_VideoControllerResolution**](cim-videocontrollerresolution.md).

</dd> <dt>

**PixelsPerXLogicalInch**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/windows/desktop/63bdbafc-51f3-4714-8b7e-9d5a61cef45e), [**MappingStrings**](https://msdn.microsoft.com/windows/desktop/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Win32API\|Device Context Functions\|[**GetDeviceCaps**](https://msdn.microsoft.com/windows/desktop/d524c4c7-22af-495d-aecc-b9921e53ca7b)\|LOGPIXELSX")
</dt> </dl>

Indicates the number of pixels per logical inch along the X axis (horizontal direction) of the display.

This property has been deprecated in favor of a corresponding property(s) contained in the [**Win32\_VideoController**](win32-videocontroller.md), [**Win32\_DesktopMonitor**](win32-desktopmonitor.md) and//or [**CIM\_VideoControllerResolution**](cim-videocontrollerresolution.md).

</dd> <dt>

**PixelsPerYLogicalInch**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/windows/desktop/63bdbafc-51f3-4714-8b7e-9d5a61cef45e), [**MappingStrings**](https://msdn.microsoft.com/windows/desktop/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Win32API\|Device Context Functions\|[**GetDeviceCaps**](https://msdn.microsoft.com/windows/desktop/d524c4c7-22af-495d-aecc-b9921e53ca7b)\|LOGPIXELSY")
</dt> </dl>

Indicates the number of pixels per logical inch along the Y axis (vertical direction) of the display.

This property has been deprecated in favor of a corresponding property(s) contained in the [**Win32\_VideoController**](win32-videocontroller.md), [**Win32\_DesktopMonitor**](win32-desktopmonitor.md) and//or [**CIM\_VideoControllerResolution**](cim-videocontrollerresolution.md).

</dd> <dt>

**RefreshRate**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/windows/desktop/63bdbafc-51f3-4714-8b7e-9d5a61cef45e), [**MappingStrings**](https://msdn.microsoft.com/windows/desktop/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Win32API\|Device Context Functions\|[**GetDeviceCaps**](https://msdn.microsoft.com/windows/desktop/d524c4c7-22af-495d-aecc-b9921e53ca7b)\|VREFRESH")
</dt> </dl>

Indicates the refresh rate of the video configuration. A value of 0 or 1 indicates a default rate is being used.

Example: 72

This property has been deprecated in favor of a corresponding property(s) contained in the [**Win32\_VideoController**](win32-videocontroller.md), [**Win32\_DesktopMonitor**](win32-desktopmonitor.md) and//or [**CIM\_VideoControllerResolution**](cim-videocontrollerresolution.md).

</dd> <dt>

**ScanMode**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/windows/desktop/63bdbafc-51f3-4714-8b7e-9d5a61cef45e), [**MappingStrings**](https://msdn.microsoft.com/windows/desktop/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Win32Registry\|System\\\\CurrentControlSet\\\\Services\|Device0\|DefaultSettings.Interlaced")
</dt> </dl>

Indicates whether the display device is interlaced.

This property has been deprecated in favor of a corresponding property(s) contained in the [**Win32\_VideoController**](win32-videocontroller.md), [**Win32\_DesktopMonitor**](win32-desktopmonitor.md) and//or [**CIM\_VideoControllerResolution**](cim-videocontrollerresolution.md).

<dt>

<span id="Non_Interlaced"></span><span id="non_interlaced"></span><span id="NON_INTERLACED"></span>

**Non Interlaced** ("Non Interlaced")


</dt> <dd></dd> <dt>

<span id="Interlaced"></span><span id="interlaced"></span><span id="INTERLACED"></span>

**Interlaced** ("Interlaced")


</dt> <dd></dd> </dl>

</dd> <dt>

**ScreenHeight**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/windows/desktop/63bdbafc-51f3-4714-8b7e-9d5a61cef45e), [**MappingStrings**](https://msdn.microsoft.com/windows/desktop/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Win32API\|Device Context Functions\|[**GetDeviceCaps**](https://msdn.microsoft.com/windows/desktop/d524c4c7-22af-495d-aecc-b9921e53ca7b)\|VERTSIZE"), [**Units**](https://msdn.microsoft.com/windows/desktop/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("millimeters")
</dt> </dl>

Specifies the height of the physical screen.

This property has been deprecated in favor of a corresponding property(s) contained in the [**Win32\_VideoController**](win32-videocontroller.md), [**Win32\_DesktopMonitor**](win32-desktopmonitor.md) and//or [**CIM\_VideoControllerResolution**](cim-videocontrollerresolution.md).

</dd> <dt>

**ScreenWidth**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/windows/desktop/63bdbafc-51f3-4714-8b7e-9d5a61cef45e), [**MappingStrings**](https://msdn.microsoft.com/windows/desktop/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Win32API\|Device Context Functions\|[**GetDeviceCaps**](https://msdn.microsoft.com/windows/desktop/d524c4c7-22af-495d-aecc-b9921e53ca7b)\|HORZSIZE"), [**Units**](https://msdn.microsoft.com/windows/desktop/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("millimeters")
</dt> </dl>

Specifies the width of the physical screen.

This property has been deprecated in favor of a corresponding property(s) contained in the [**Win32\_VideoController**](win32-videocontroller.md), [**Win32\_DesktopMonitor**](win32-desktopmonitor.md) and//or [**CIM\_VideoControllerResolution**](cim-videocontrollerresolution.md).

</dd> <dt>

**SettingID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/windows/desktop/671ea769-f68d-4788-96f5-c4f86ab3b00e) (256)
</dt> </dl>

Identifier by which the current object is known.

This property is inherited from [**CIM\_Setting**](cim-setting.md).

</dd> <dt>

**SystemPaletteEntries**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/windows/desktop/63bdbafc-51f3-4714-8b7e-9d5a61cef45e), [**MappingStrings**](https://msdn.microsoft.com/windows/desktop/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Win32API\|Device Context Functions\|[**GetDeviceCaps**](https://msdn.microsoft.com/windows/desktop/d524c4c7-22af-495d-aecc-b9921e53ca7b)\|SIZEPALETTE")
</dt> </dl>

Iindicates the current number of color index entries reserved for system use. This value is only valid for display settings that use an indexed palette . Indexed palettes are not used for color depths greater than 8 bits per pixel. If the color depth is more than 8 bits per pixel, this value is set to **NULL**.

Example: 20

This property has been deprecated in favor of a corresponding property(s) contained in the [**Win32\_VideoController**](win32-videocontroller.md), [**Win32\_DesktopMonitor**](win32-desktopmonitor.md) and//or [**CIM\_VideoControllerResolution**](cim-videocontrollerresolution.md).

</dd> <dt>

**VerticalResolution**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/windows/desktop/63bdbafc-51f3-4714-8b7e-9d5a61cef45e), [**MappingStrings**](https://msdn.microsoft.com/windows/desktop/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Win32API\|Device Context Functions\|[**GetDeviceCaps**](https://msdn.microsoft.com/windows/desktop/d524c4c7-22af-495d-aecc-b9921e53ca7b)\|VERTRES")
</dt> </dl>

Indicates the current number of pixels in the vertical direction (Y axis) of the display.

Example: 768

This property has been deprecated in favor of a corresponding property(s) contained in the [**Win32\_VideoController**](win32-videocontroller.md), [**Win32\_DesktopMonitor**](win32-desktopmonitor.md) and//or [**CIM\_VideoControllerResolution**](cim-videocontrollerresolution.md).

</dd> </dl>

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

[**CIM\_Setting**](cim-setting.md)
</dt> </dl>

 

 




