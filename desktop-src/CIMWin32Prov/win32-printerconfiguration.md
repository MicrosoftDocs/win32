---
description: The Win32\_PrinterConfiguration WMI class represents the configuration for a printer device. This includes capabilities such as resolution, color, fonts, and orientation.
ms.assetid: b6649da0-ecb0-4ed1-979c-5005837eb474
ms.tgt_platform: multiple
title: Win32_PrinterConfiguration class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_PrinterConfiguration
- Win32_PrinterConfiguration.Caption
- Win32_PrinterConfiguration.Description
- Win32_PrinterConfiguration.SettingID
- Win32_PrinterConfiguration.BitsPerPel
- Win32_PrinterConfiguration.Collate
- Win32_PrinterConfiguration.Color
- Win32_PrinterConfiguration.Copies
- Win32_PrinterConfiguration.DeviceName
- Win32_PrinterConfiguration.DisplayFlags
- Win32_PrinterConfiguration.DisplayFrequency
- Win32_PrinterConfiguration.DitherType
- Win32_PrinterConfiguration.DriverVersion
- Win32_PrinterConfiguration.Duplex
- Win32_PrinterConfiguration.FormName
- Win32_PrinterConfiguration.HorizontalResolution
- Win32_PrinterConfiguration.ICMIntent
- Win32_PrinterConfiguration.ICMMethod
- Win32_PrinterConfiguration.LogPixels
- Win32_PrinterConfiguration.MediaType
- Win32_PrinterConfiguration.Name
- Win32_PrinterConfiguration.Orientation
- Win32_PrinterConfiguration.PaperLength
- Win32_PrinterConfiguration.PaperSize
- Win32_PrinterConfiguration.PaperWidth
- Win32_PrinterConfiguration.PelsHeight
- Win32_PrinterConfiguration.PelsWidth
- Win32_PrinterConfiguration.PrintQuality
- Win32_PrinterConfiguration.Scale
- Win32_PrinterConfiguration.SpecificationVersion
- Win32_PrinterConfiguration.TTOption
- Win32_PrinterConfiguration.VerticalResolution
- Win32_PrinterConfiguration.XResolution
- Win32_PrinterConfiguration.YResolution
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# Win32\_PrinterConfiguration class

The **Win32\_PrinterConfiguration** [WMI class](../wmisdk/retrieving-a-class.md) represents the configuration for a printer device. This includes capabilities such as resolution, color, fonts, and orientation.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class Win32_PrinterConfiguration : CIM_Setting
{
  string  Caption;
  string  Description;
  string  SettingID;
  uint32  BitsPerPel;
  boolean Collate;
  uint32  Color;
  uint32  Copies;
  string  DeviceName;
  uint32  DisplayFlags;
  uint32  DisplayFrequency;
  uint32  DitherType;
  uint32  DriverVersion;
  boolean Duplex;
  string  FormName;
  uint32  HorizontalResolution;
  uint32  ICMIntent;
  uint32  ICMMethod;
  uint32  LogPixels;
  uint32  MediaType;
  string  Name;
  uint32  Orientation;
  uint32  PaperLength;
  string  PaperSize;
  uint32  PaperWidth;
  uint32  PelsHeight;
  uint32  PelsWidth;
  uint32  PrintQuality;
  uint32  Scale;
  uint32  SpecificationVersion;
  uint32  TTOption;
  uint32  VerticalResolution;
  uint32  XResolution;
  uint32  YResolution;
};
```

## Members

The **Win32\_PrinterConfiguration** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_PrinterConfiguration** class has these properties.

<dl> <dt>

**BitsPerPel**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](../wmisdk/standard-wmi-qualifiers.md)
</dt> </dl>

Number of bits used to represent the color in this configuration (the bits per pixel). This property is obsolete. Instead, use properties in the [**Win32\_VideoController**](win32-videocontroller.md), [**Win32\_DesktopMonitor**](win32-desktopmonitor.md), or [**CIM\_VideoControllerResolution**](cim-videocontrollerresolution.md) classes to determine how color is represented.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](../wmisdk/standard-qualifiers.md) (64)
</dt> </dl>

Short textual description of the current object.

This property is inherited from [**CIM\_Setting**](cim-setting.md).

</dd> <dt>

**Collate**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the pages that are printed should be collated. To collate is to print out the entire document before printing the next copy, as opposed to printing out each page of the document the required number of times.

This property is ignored unless the printer driver indicates support for collation.

</dd> <dt>

**Color**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Color of the document. Some color printers have the capability to print using true black instead of a combination of cyan, magenta, and yellow (CMY). This usually creates darker and sharper text for documents. This option is only useful for color printers that support true black printing.

<dt>

<span id="1"></span>

<span id="1"></span>**1**


</dt> <dd>

Monochrome (true black)

</dd> <dt>

<span id="2"></span>

<span id="2"></span>**2**


</dt> <dd>

Color

</dd> </dl>

</dd> <dt>

**Copies**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of copies to be printed. The printer driver must support printing multi-page copies.

Example: 2

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

**DeviceName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Friendly name of the printer. This name is unique to the type of printer and may be truncated because of the limitations of the string from which it is derived.

Example: "PCL/HP LaserJet"

</dd> <dt>

**DisplayFlags**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the display device is color or monochrome and whether the type of scanning is noninterlaced or interlaced. This property is obsolete. Instead, use display properties such as the **DisplayType** property of the **Win32\_DesktopMonitor** class.

</dd> <dt>

**DisplayFrequency**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Displays the vertical refresh rate. The refresh rate for a monitor is the number of times the screen is redrawn per second (frequency). This property is obsolete. Instead, use properties in the [**Win32\_VideoController**](win32-videocontroller.md), [**Win32\_DesktopMonitor**](win32-desktopmonitor.md), or [**CIM\_VideoControllerResolution**](cim-videocontrollerresolution.md) class.

</dd> <dt>

**DitherType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Dither type of the printer. This property can assume predefined values of 1 to 5, or driver-defined values from 6 to 256. Line art dithering is a special dithering method that produces well defined borders between black, white, and gray scalings. It is not suitable for images that include continuous graduations in intensity and hue, such as scanned photographs.

<dt>

<span id="1"></span>

<span id="1"></span>**1**


</dt> <dd>

No Dithering

</dd> <dt>

<span id="2"></span>

<span id="2"></span>**2**


</dt> <dd>

Coarse Brush

</dd> <dt>

<span id="3"></span>

<span id="3"></span>**3**


</dt> <dd>

Fine Brush

</dd> <dt>

<span id="4"></span>

<span id="4"></span>**4**


</dt> <dd>

Line Art

</dd> <dt>

<span id="5"></span>

<span id="5"></span>**5**


</dt> <dd>

Grayscale

</dd> </dl>

</dd> <dt>

**DriverVersion**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Version number of the Windows-based printer driver. The version numbers are created and maintained by the driver manufacturer.

</dd> <dt>

**Duplex**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, printing is done on both sides. If **FALSE**, printing is done on only one side of the media.

</dd> <dt>

**FormName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Not supported.

</dd> <dt>

**HorizontalResolution**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](../wmisdk/standard-qualifiers.md) (dots per inch)
</dt> </dl>

Print resolution in dots per inch along the x-axis (width) of the print job (similar to the obsolete **XResolution** property). This value is only set when the **PrintQuality** property of this class is positive.

</dd> <dt>

**ICMIntent**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specific value of one of the three possible color matching methods (called intents) that should be used by default. ICM applications establish intents by using the ICM functions. This property can assume predefined values of 1 to 3, or driver-defined values from 4 to 256. Non-ICM applications can use this value to determine how the printer handles color printing jobs.

<dt>

<span id="1"></span>

<span id="1"></span>**1**


</dt> <dd>

Saturation

</dd> <dt>

<span id="2"></span>

<span id="2"></span>**2**


</dt> <dd>

Contrast

</dd> <dt>

<span id="3"></span>

<span id="3"></span>**3**


</dt> <dd>

Exact Color

</dd> </dl>

</dd> <dt>

**ICMMethod**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

How ICM is handled. For a non-ICM application, this property determines if ICM is enabled or disabled. For ICM applications, the system examines this property to determine which part of the computer system handles ICM support.

<dt>

<span id="1"></span>

<span id="1"></span>**1**


</dt> <dd>

Disabled

</dd> <dt>

<span id="2"></span>

<span id="2"></span>**2**


</dt> <dd>

Windows

</dd> <dt>

<span id="3"></span>

<span id="3"></span>**3**


</dt> <dd>

Device Driver

</dd> <dt>

<span id="4"></span>

<span id="4"></span>**4**


</dt> <dd>

Device

</dd> </dl>

</dd> <dt>

**LogPixels**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](../wmisdk/standard-wmi-qualifiers.md)
</dt> </dl>

Number of pixels per logical inch. This obsolete property is valid only with devices that work with pixels, which excludes devices such as printers. There is no replacement value that applies to printers.

</dd> <dt>

**MediaType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Type of media on which the printer prints. The property can be set to a predefined value or a driver-defined value greater than or equal to 256.

<dt>

<span id="1"></span>

<span id="1"></span>**1**


</dt> <dd>

Standard

</dd> <dt>

<span id="2"></span>

<span id="2"></span>**2**


</dt> <dd>

Transparency

</dd> <dt>

<span id="3"></span>

<span id="3"></span>**3**


</dt> <dd>

Glossy

</dd> </dl>

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](../wmisdk/standard-qualifiers.md), [**MaxLen**](../wmisdk/standard-qualifiers.md) (256)
</dt> </dl>

Name of the printer with which this configuration is associated. This value matches the **Name** property of the associated [**Win32\_Printer**](win32-printer.md) instance.

</dd> <dt>

**Orientation**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Printing orientation of the paper.

<dt>

<span id="1"></span>

<span id="1"></span>**1**


</dt> <dd>

Portrait

</dd> <dt>

<span id="2"></span>

<span id="2"></span>**2**


</dt> <dd>

Landscape

</dd> </dl>

</dd> <dt>

**PaperLength**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](../wmisdk/standard-qualifiers.md) (Tenths of a millimeter)
</dt> </dl>

Length of the paper. To determine the size of the paper in inches, divide this value by 254.

Example: 2794

</dd> <dt>

**PaperSize**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Size of the paper. The possible sizes are found in the **PaperSizesSupported** property of the associated [**Win32\_Printer**](win32-printer.md) class.

Example: "A4 or Letter".

</dd> <dt>

**PaperWidth**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](../wmisdk/standard-qualifiers.md) (Tenths of a millimeter)
</dt> </dl>

Width of the paper. To determine the size of the paper in inches, divide this value by 254.

Example: 2159

</dd> <dt>

**PelsHeight**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](../wmisdk/standard-wmi-qualifiers.md)
</dt> </dl>

This property is not supported.

</dd> <dt>

**PelsWidth**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](../wmisdk/standard-wmi-qualifiers.md)
</dt> </dl>

This property is not supported.

</dd> <dt>

**PrintQuality**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

One of four quality levels of the print job. If a positive value is specified, the quality is measured in dots per inch.

<dt>

<span id="-1"></span>

<span id="-1"></span>**-1**


</dt> <dd>

Draft

</dd> <dt>

<span id="-2"></span>

<span id="-2"></span>**-2**


</dt> <dd>

Low

</dd> <dt>

<span id="-3"></span>

<span id="-3"></span>**-3**


</dt> <dd>

Medium

</dd> <dt>

<span id="-4"></span>

<span id="-4"></span>**-4**


</dt> <dd>

High

</dd> </dl>

</dd> <dt>

**Scale**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](../wmisdk/standard-qualifiers.md) (Percent)
</dt> </dl>

Factor by which the printed output is to be scaled. For example, a scale of 75 reduces the print output to 3/4 its original height and width.

</dd> <dt>

**SettingID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](../wmisdk/standard-qualifiers.md) (256)
</dt> </dl>

Identifier by which the current object is known.

This property is inherited from [**CIM\_Setting**](cim-setting.md).

</dd> <dt>

**SpecificationVersion**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Version number of the initialization data for the device associated with the Windows-based printer.

</dd> <dt>

**TTOption**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates how TrueType fonts should be printed.

<dt>

<span id="Bitmap"></span><span id="bitmap"></span><span id="BITMAP"></span>

<span id="Bitmap"></span><span id="bitmap"></span><span id="BITMAP"></span>**Bitmap** (1)


</dt> <dd>

Prints TrueType fonts as graphics. This is the default action for dot-matrix printers.

</dd> <dt>

<span id="Download"></span><span id="download"></span><span id="DOWNLOAD"></span>

<span id="Download"></span><span id="download"></span><span id="DOWNLOAD"></span>**Download** (2)


</dt> <dd>

Downloads TrueType fonts as soft fonts. This is the default action for printers that use the Printer Control Language (PCL).

</dd> <dt>

<span id="Substitute"></span><span id="substitute"></span><span id="SUBSTITUTE"></span>

<span id="Substitute"></span><span id="substitute"></span><span id="SUBSTITUTE"></span>**Substitute** (3)


</dt> <dd>

Substitutes device fonts for TrueType fonts. This is the default action for PostScript printers.

</dd> </dl>

</dd> <dt>

**VerticalResolution**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](../wmisdk/standard-qualifiers.md) (dots per inch)
</dt> </dl>

Print resolution along the y-axis (height) of the print job (similar to the obsolete **YResolution** property). This value is only set when the **PrintQuality** property of this class is positive.

</dd> <dt>

**XResolution**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](../wmisdk/standard-wmi-qualifiers.md)
</dt> </dl>

This property is obsolete. Use the **HorizontalResolution** property instead.

</dd> <dt>

**YResolution**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](../wmisdk/standard-wmi-qualifiers.md)
</dt> </dl>

This property is obsolete. Use the **VerticalResolution** property instead.

</dd> </dl>

## Remarks

The **Win32\_PrinterConfiguration** class is derived from [**CIM\_Setting**](cim-setting.md).

**Overview**

Before you can determine how to best distribute and use your printing resources, you must have a detailed knowledge of those resources. For example, Department A might have only three printers compared with five printers in Department B. However, if the printers in Department A can print 20 pages per minute and the printers in Department B can print only 5 pages per minute, users in Department A actually have more printing capacity. Without knowing the detailed capabilities of these printers, you might erroneously conclude that Department A is short on printing capacity and thus purchase additional printers that end up going unused.

WMI includes two classes, [**Win32\_Printer**](win32-printer.md) and **Win32\_PrinterConfiguration**, which can be used to return detailed information about all the printers installed on a computer.

## Examples

The following code sample retrieves printer information.


```VB
strComputer = "."
Set objWMIService = GetObject("winmgmts:" _
 & "{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")
Set colInstalledPrinters = objWMIService.ExecQuery _
 ("SELECT * FROM Win32_PrinterConfiguration")
For Each objPrinter in colInstalledPrinters
 Wscript.Echo "Name: " & objPrinter.Name
 Wscript.Echo "Collate: " & objPrinter.Collate
 Wscript.Echo "Copies: " & objPrinter.Copies
 Wscript.Echo "Driver Version: " & objPrinter.DriverVersion
 Wscript.Echo "Duplex: " & objPrinter.Duplex
 Wscript.Echo "Horizontal Resolution: " & _
 objPrinter.HorizontalResolution
 If objPrinter.Orientation = 1 Then
 strOrientation = "Portrait"
 Else
 strOrientation = "Landscape"
 End If
 Wscript.Echo "Orientation : " & strOrientation
 Wscript.Echo "Paper Length: " & objPrinter.PaperLength / 254
 Wscript.Echo "Paper Width: " & objPrinter.PaperWidth / 254
 Wscript.Echo "Print Quality: " & objPrinter.PrintQuality
 Wscript.Echo "Scale: " & objPrinter.Scale
 Wscript.Echo "Specification Version: " & _
 objPrinter.SpecificationVersion
 If objPrinter.TTOption = 1 Then
 strTTOption = "Print TrueType fonts as graphics."
 ElseIf objPrinter.TTOption = 2 Then
 strTTOption = "Download TrueType fonts as soft fonts."
 Else
 strTTOption = "Substitute device fonts for TrueType fonts."
 End If
 Wscript.Echo "True Type Option: " & strTTOption
 Wscript.Echo "Vertical Resolution: " & objPrinter.VerticalResolution
Next
```



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

[**CIM\_Setting**](./cim-setting.md)
</dt> <dt>

[Computer System Hardware Classes](computer-system-hardware-classes.md)
</dt> </dl>

 

 
