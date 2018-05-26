---
Description: The Win32\_DisplayControllerConfiguration WMI class represents the video adapter configuration information of a computer system running Windows.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 36ebd840-5e8c-411a-828d-38972fe956e2
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32\_DisplayControllerConfiguration class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Win32\_DisplayControllerConfiguration class

The **Win32\_DisplayControllerConfiguration** [WMI class](https://msdn.microsoft.com/library/aa393244) represents the video adapter configuration information of a computer system running Windows.

This class is obsolete. In place of this class, you should use the properties in the [**Win32\_VideoController**](win32-videocontroller.md), [**Win32\_DesktopMonitor**](win32-desktopmonitor.md), and [**CIM\_VideoControllerResolution**](cim-videocontrollerresolution.md) classes.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[DEPRECATED, Dynamic, Provider("CIMWin32"), UUID("{8502C4E5-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_DisplayControllerConfiguration : CIM_Setting
{
  string Caption;
  string Description;
  string SettingID;
  uint32 BitsPerPixel;
  uint32 ColorPlanes;
  uint32 DeviceEntriesInAColorTable;
  uint32 DeviceSpecificPens;
  uint32 HorizontalResolution;
  string Name;
  sint32 RefreshRate;
  uint32 ReservedSystemPaletteEntries;
  uint32 SystemPaletteEntries;
  uint32 VerticalResolution;
  string VideoMode;
};
```

## Members

The **Win32\_DisplayControllerConfiguration** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_DisplayControllerConfiguration** class has these properties.

<dl> <dt>

**BitsPerPixel**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/library/aa393651), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("Win32API\|Device Context Functions\|[**GetDeviceCaps**](https://msdn.microsoft.com/library/windows/desktop/dd144877)\|BITSPIXEL")
</dt> </dl>

Either the number of bits used to represent the color in this configuration, or the bits in each pixel.

Example: 8

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
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

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/library/aa393651), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("Win32API\|Device Context Functions\|[**GetDeviceCaps**](https://msdn.microsoft.com/library/windows/desktop/dd144877)\|PLANES")
</dt> </dl>

Current number of color planes used in the display configuration. A color plane is another way to represent pixel colors. Instead of assigning a single RGB value to each pixel, color planes separate the graphic into each of the primary color components (red, green, blue), and stores them in their own planes. This allows for greater color depths on 8-bit and 16-bit video systems. Present graphics systems have the bitwidth large enough to store color depth information, meaning only one color plane is needed.

Example: 1

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

**DeviceEntriesInAColorTable**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/library/aa393651), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("Win32API\|Device Context Functions\|[**GetDeviceCaps**](https://msdn.microsoft.com/library/windows/desktop/dd144877)\|NUMCOLORS")
</dt> </dl>

Number of color indexes in a color table of a display device (if the device has a color depth of no more than 8 bits per pixel). For devices with greater color depths, -1 is returned.

Example: 256

</dd> <dt>

**DeviceSpecificPens**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/library/aa393651), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("Win32API\|Device Context Functions\|[**GetDeviceCaps**](https://msdn.microsoft.com/library/windows/desktop/dd144877)\|NUMPENS")
</dt> </dl>

Current number of device-specific pens. A value of 0xFFFFFFFF means the device does not support pens. Pens are logical properties that can be assigned by the display controller to display devices, and are used to draw lines, borders of polygons, and text.

Example: 3

</dd> <dt>

**HorizontalResolution**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/library/aa393651), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("Win32API\|Device Context Functions\|[**GetDeviceCaps**](https://msdn.microsoft.com/library/windows/desktop/dd144877)\|HORZRES"), [**Units**](https://msdn.microsoft.com/library/aa393650) ("pixels")
</dt> </dl>

Current number of pixels in the horizontal direction (x-axis) of the display.

Example: 1024

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/library/aa393651), [**key**](https://msdn.microsoft.com/library/aa392157), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("WMI")
</dt> </dl>

Name of the adapter used in this configuration.

</dd> <dt>

**RefreshRate**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/library/aa393651), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("Win32API\|Device Context Functions\|[**GetDeviceCaps**](https://msdn.microsoft.com/library/windows/desktop/dd144877)\|HORZRESVREFRESH"), [**Units**](https://msdn.microsoft.com/library/aa393650) ("hertz")
</dt> </dl>

Refresh rate of the video adapter. A value of 0 (zero) or 1 (one) indicates a default rate is being used. A value of -1 indicates that an optimal rate is being used.

Example: 72

</dd> <dt>

**ReservedSystemPaletteEntries**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/library/aa393651), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("Win32API\|Device Context Functions\|[**GetDeviceCaps**](https://msdn.microsoft.com/library/windows/desktop/dd144877)\|NUMRESERVED")
</dt> </dl>

Current number of color index entries reserved for system use. This value is only valid for display settings that use an indexed palette. Indexed palettes are not used for color depths greater than 8 bits per pixel. If the color depth is more than 8 bits per pixel, this value is set to **NULL**.

Example: 20

</dd> <dt>

**SettingID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
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

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/library/aa393651), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("Win32API\|Device Context Functions\|[**GetDeviceCaps**](https://msdn.microsoft.com/library/windows/desktop/dd144877)\|NUMRESERVED")
</dt> </dl>

Current number of color index entries reserved for system use. This value is only valid for display settings that use an indexed palette. Indexed palettes are not used for color depths greater than 8 bits per pixel. If the color depth is more than 8 bits per pixel, this value is set to **NULL**.

Example: 20

</dd> <dt>

**VerticalResolution**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/library/aa393651), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("Win32API\|Device Context Functions\|[**GetDeviceCaps**](https://msdn.microsoft.com/library/windows/desktop/dd144877)\|VERTRES"), [**Units**](https://msdn.microsoft.com/library/aa393650) ("pixels")
</dt> </dl>

Current number of pixels in the vertical direction (y-axis) of the display.

Example: 768

</dd> <dt>

**VideoMode**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/library/aa393651), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("WMI")
</dt> </dl>

User-readable description of the current screen resolution and color setting of the display.

Example: "1024   768 with 256 colors"

</dd> </dl>

## Remarks

The **Win32\_DisplayControllerConfiguration** class is derived from [**CIM\_Setting**](cim-setting.md).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Setting**](cim-setting.md)
</dt> <dt>

[Computer System Hardware Classes](computer-system-hardware-classes.md)
</dt> </dl>

 

 




