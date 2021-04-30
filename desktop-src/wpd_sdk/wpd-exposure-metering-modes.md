---
description: The WPD\_EXPOSURE\_METERING\_MODES enumeration type describes the metering mode to use when estimating exposure for still image capture by a device.
ms.assetid: 5e92013c-600d-4128-ab59-1cfa8953db67
title: WPD_EXPOSURE_METERING_MODES enumeration (PortableDevice.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WPD_EXPOSURE_METERING_MODES
api_type: 
- HeaderDef
api_location: 
- PortableDevice.h
---

# WPD\_EXPOSURE\_METERING\_MODES enumeration

The **WPD\_EXPOSURE\_METERING\_MODES** enumeration type describes the metering mode to use when estimating exposure for still image capture by a device.

## Syntax


```C++
typedef enum WPD_EXPOSURE_METERING_MODES { 
  WPD_EXPOSURE_METERING_MODE_UNDEFINED                = 0,
  WPD_EXPOSURE_METERING_MODE_AVERAGE                  = 1,
  WPD_EXPOSURE_METERING_MODE_CENTER_WEIGHTED_AVERAGE  = 2,
  WPD_EXPOSURE_METERING_MODE_MULTI_SPOT               = 3,
  WPD_EXPOSURE_METERING_MODE_CENTER_SPOT              = 4
} ;
```



## Constants

<dl> <dt>

<span id="WPD_EXPOSURE_METERING_MODE_UNDEFINED"></span><span id="wpd_exposure_metering_mode_undefined"></span>**WPD\_EXPOSURE\_METERING\_MODE\_UNDEFINED**
</dt> <dd>

The metering mode is undefined.

</dd> <dt>

<span id="WPD_EXPOSURE_METERING_MODE_AVERAGE"></span><span id="wpd_exposure_metering_mode_average"></span>**WPD\_EXPOSURE\_METERING\_MODE\_AVERAGE**
</dt> <dd>

Use averaged exposure across the full image.

</dd> <dt>

<span id="WPD_EXPOSURE_METERING_MODE_CENTER_WEIGHTED_AVERAGE"></span><span id="wpd_exposure_metering_mode_center_weighted_average"></span>**WPD\_EXPOSURE\_METERING\_MODE\_CENTER\_WEIGHTED\_AVERAGE**
</dt> <dd>

Use an averaged exposure, with the center of the image given more weight.

</dd> <dt>

<span id="WPD_EXPOSURE_METERING_MODE_MULTI_SPOT"></span><span id="wpd_exposure_metering_mode_multi_spot"></span>**WPD\_EXPOSURE\_METERING\_MODE\_MULTI\_SPOT**
</dt> <dd>

Use a multi-spot averaging technique.

</dd> <dt>

<span id="WPD_EXPOSURE_METERING_MODE_CENTER_SPOT"></span><span id="wpd_exposure_metering_mode_center_spot"></span>**WPD\_EXPOSURE\_METERING\_MODE\_CENTER\_SPOT**
</dt> <dd>

Use a center-spot averaging technique.

</dd> </dl>

## Remarks

Indicates the metering mode of the device. This enumeration is used by the [WPD\_STILL\_IMAGE\_EXPOSURE\_METERING\_MODE](still-image-properties.md) property.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**Structures and Enumeration Types**](structures-and-enumeration-types.md)
</dt> </dl>

 

 




