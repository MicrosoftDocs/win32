---
description: Represents a CRT desktop monitor.
ms.assetid: 26a06320-9fd9-434e-87c8-486e9ca4945c
title: CIM_DesktopMonitor class (Hyper-V management)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_DesktopMonitor
- CIM_DesktopMonitor.DisplayType
- CIM_DesktopMonitor.Bandwidth
- CIM_DesktopMonitor.ScreenHeight
- CIM_DesktopMonitor.ScreenWidth
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# CIM_DesktopMonitor class (Hyper-V management)

Represents a CRT desktop monitor.

## Syntax

``` syntax
[Abstract, Version("2.6.0"), UMLPackagePath("CIM::Device::UserDevices")]
class CIM_DesktopMonitor : CIM_Display
{
  uint16 DisplayType;
  uint32 Bandwidth;
  uint32 ScreenHeight;
  uint32 ScreenWidth;
};
```

## Members

The **CIM\_DesktopMonitor** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_DesktopMonitor** class has these properties.

<dl> <dt>

**Bandwidth**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("MegaHertz"), **PUnit** ("hertz \* 10^6")
</dt> </dl>

The bandwidth of the display, in MHertz. "0" indicates unknown.

</dd> <dt>

**DisplayType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type of display type of the CRT monitor. For example, multiscan color, or monochrome.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Multiscan_Color"></span><span id="multiscan_color"></span><span id="MULTISCAN_COLOR"></span>

**Multiscan Color** (2)


</dt> <dd></dd> <dt>

<span id="Multiscan_Monochrome"></span><span id="multiscan_monochrome"></span><span id="MULTISCAN_MONOCHROME"></span>

**Multiscan Monochrome** (3)


</dt> <dd></dd> <dt>

<span id="Fixed_Frequency_Color"></span><span id="fixed_frequency_color"></span><span id="FIXED_FREQUENCY_COLOR"></span>

**Fixed Frequency Color** (4)


</dt> <dd></dd> <dt>

<span id="Fixed_Frequency_Monochrome"></span><span id="fixed_frequency_monochrome"></span><span id="FIXED_FREQUENCY_MONOCHROME"></span>

**Fixed Frequency Monochrome** (5)


</dt> <dd></dd> </dl>

</dd> <dt>

**ScreenHeight**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The logical height of the display, in screen coordinates.

</dd> <dt>

**ScreenWidth**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The logical width of the display, in screen coordinates.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                                  |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                       |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_Display**](cim-display.md)
</dt> </dl>

 

