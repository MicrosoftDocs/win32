---
description: The WPD\_FOCUS\_METERING\_MODES enumeration type describes how a device should decide what part of a frame to use to set focus.
ms.assetid: 0e68d0e8-2ce3-4994-99c2-2ff2293d8a20
title: WPD_FOCUS_METERING_MODES enumeration (PortableDevice.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WPD_FOCUS_METERING_MODES
api_type: 
- HeaderDef
api_location: 
- PortableDevice.h
---

# WPD\_FOCUS\_METERING\_MODES enumeration

The **WPD\_FOCUS\_METERING\_MODES** enumeration type describes how a device should decide what part of a frame to use to set focus.

## Syntax


```C++
typedef enum WPD_FOCUS_METERING_MODES { 
  WPD_FOCUS_METERING_MODE_UNDEFINED    = 0,
  WPD_FOCUS_METERING_MODE_CENTER_SPOT  = 1,
  WPD_FOCUS_METERING_MODE_MULTI_SPOT   = 2
} ;
```



## Constants

<dl> <dt>

<span id="WPD_FOCUS_METERING_MODE_UNDEFINED"></span><span id="wpd_focus_metering_mode_undefined"></span>**WPD\_FOCUS\_METERING\_MODE\_UNDEFINED**
</dt> <dd>

Indicates that no focusing mode has been specified.

</dd> <dt>

<span id="WPD_FOCUS_METERING_MODE_CENTER_SPOT"></span><span id="wpd_focus_metering_mode_center_spot"></span>**WPD\_FOCUS\_METERING\_MODE\_CENTER\_SPOT**
</dt> <dd>

Focuses on the center of the framed area.

</dd> <dt>

<span id="WPD_FOCUS_METERING_MODE_MULTI_SPOT"></span><span id="wpd_focus_metering_mode_multi_spot"></span>**WPD\_FOCUS\_METERING\_MODE\_MULTI\_SPOT**
</dt> <dd>

Determine focus by analyzing multiple parts of the framed area.

</dd> </dl>

## Remarks

This enumeration is specified by the [WPD\_STILL\_IMAGE\_FOCUS\_METERING\_MODE](still-image-properties.md) property.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**Structures and Enumeration Types**](structures-and-enumeration-types.md)
</dt> </dl>

 

 




