---
description: SystemConfig_Video class - This class is the event type class for video configuration events.
ms.assetid: ddb5924b-70d9-4693-bf68-0536c3c3fa8d
title: SystemConfig_Video class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SystemConfig_Video
- SystemConfig_Video.MemorySize
- SystemConfig_Video.XResolution
- SystemConfig_Video.YResolution
- SystemConfig_Video.BitsPerPixel
- SystemConfig_Video.VRefresh
- SystemConfig_Video.ChipType
- SystemConfig_Video.DACType
- SystemConfig_Video.AdapterString
- SystemConfig_Video.BiosString
- SystemConfig_Video.DeviceId
- SystemConfig_Video.StateFlags
api_type: 
- NA
api_location: 
---

# SystemConfig\_Video class

This class is the event type class for video configuration events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType(14), EventTypeName("Video")]
class SystemConfig_Video : SystemConfig
{
  uint32 MemorySize;
  uint32 XResolution;
  uint32 YResolution;
  uint32 BitsPerPixel;
  uint32 VRefresh;
  char16 ChipType[];
  char16 DACType[];
  char16 AdapterString[];
  char16 BiosString[];
  char16 DeviceId[];
  uint32 StateFlags;
};
```

## Members

The **SystemConfig\_Video** class has these types of members:

-   [Properties](#properties)

### Properties

The **SystemConfig\_Video** class has these properties.

<dl> <dt>

**AdapterString**
</dt> <dd> <dl> <dt>

Data type: **char16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (8), **Max** (256), **Format("s")**
</dt> </dl>

Name or description of the adapter.

</dd> <dt>

**BiosString**
</dt> <dd> <dl> <dt>

Data type: **char16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (9), **Max** (256), **Format("s")**
</dt> </dl>

BIOS name of the adapter.

</dd> <dt>

**BitsPerPixel**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (4)
</dt> </dl>

Number of bits used to display each pixel.

</dd> <dt>

**ChipType**
</dt> <dd> <dl> <dt>

Data type: **char16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (6), **Max** (256), **Format("s")**
</dt> </dl>

Chip name of the adapter.

</dd> <dt>

**DACType**
</dt> <dd> <dl> <dt>

Data type: **char16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (7), **Max** (256), **Format("s")**
</dt> </dl>

Digital-to-analog converter (DAC) chip name of the adapter.

</dd> <dt>

**DeviceId**
</dt> <dd> <dl> <dt>

Data type: **char16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (10), **Max** (256), **Format("s")**
</dt> </dl>

Address or other identifying information to uniquely name the logical device.

</dd> <dt>

**MemorySize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (1)
</dt> </dl>

Maximum amount of memory supported, in bytes.

</dd> <dt>

**StateFlags**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (11), **Format("x")**
</dt> </dl>

Device state flags. It can be any reasonable combination of the following.



| Value                                                                                                                                                                                                                                                                                        | Meaning                                                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="DISPLAY_DEVICE_ATTACHED_TO_DESKTOP"></span><span id="display_device_attached_to_desktop"></span><dl> <dt>**DISPLAY\_DEVICE\_ATTACHED\_TO\_DESKTOP**</dt> <dt>1 (0x1)</dt> </dl> | The device is part of the desktop.<br/>                                                                                                                                                                                |
| <span id="DISPLAY_DEVICE_MIRRORING_DRIVER"></span><span id="display_device_mirroring_driver"></span><dl> <dt>**DISPLAY\_DEVICE\_MIRRORING\_DRIVER**</dt> <dt>8 (0x8)</dt> </dl>           | Represents a pseudo device used to mirror application drawing for connecting to a remote computer or other purposes. An invisible pseudo monitor is associated with this device. For example, NetMeeting uses it.<br/> |
| <span id="DISPLAY_DEVICE_MODESPRUNED"></span><span id="display_device_modespruned"></span><dl> <dt>**DISPLAY\_DEVICE\_MODESPRUNED**</dt> <dt>134217728 (0x8000000)</dt> </dl>             | The device has more display modes than its output devices support.<br/>                                                                                                                                                |
| <span id="DISPLAY_DEVICE_PRIMARY_DEVICE"></span><span id="display_device_primary_device"></span><dl> <dt>**DISPLAY\_DEVICE\_PRIMARY\_DEVICE**</dt> <dt>4 (0x4)</dt> </dl>                 | The primary desktop is on the device. For a system with a single display card, this is always set. For a system with multiple display cards, only one device can have this set.<br/>                                   |
| <span id="DISPLAY_DEVICE_REMOVABLE"></span><span id="display_device_removable"></span><dl> <dt>**DISPLAY\_DEVICE\_REMOVABLE**</dt> <dt>32 (0x20)</dt> </dl>                               | The device is removable; it cannot be the primary display.<br/>                                                                                                                                                        |
| <span id="DISPLAY_DEVICE_VGA_COMPATIBLE"></span><span id="display_device_vga_compatible"></span><dl> <dt>**DISPLAY\_DEVICE\_VGA\_COMPATIBLE**</dt> <dt>16 (0x10)</dt> </dl>               | The device is VGA compatible.<br/>                                                                                                                                                                                     |



 

</dd> <dt>

**VRefresh**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (5)
</dt> </dl>

Current refresh rate, in hertz.

</dd> <dt>

**XResolution**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (2)
</dt> </dl>

Current number of horizontal pixels.

</dd> <dt>

**YResolution**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (3)
</dt> </dl>

Current number of vertical pixels.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**SystemConfig**](systemconfig.md)
</dt> </dl>

 

 




