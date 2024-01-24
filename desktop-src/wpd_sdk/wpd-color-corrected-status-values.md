---
description: The WPD\_COLOR\_CORRECTED\_STATUS\_VALUES enumeration type describes the color correction status of an image or video file.
ms.assetid: af129a1b-7760-4339-adf7-3f3c17cebde2
title: WPD_COLOR_CORRECTED_STATUS_VALUES enumeration (PortableDevice.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WPD_COLOR_CORRECTED_STATUS_VALUES
api_type: 
- HeaderDef
api_location: 
- PortableDevice.h
---

# WPD\_COLOR\_CORRECTED\_STATUS\_VALUES enumeration

The **WPD\_COLOR\_CORRECTED\_STATUS\_VALUES** enumeration type describes the color correction status of an image or video file.

## Syntax


```C++
typedef enum WPD_COLOR_CORRECTED_STATUS_VALUES { 
  WPD_COLOR_CORRECTED_STATUS_NOT_CORRECTED            = 0,
  WPD_COLOR_CORRECTED_STATUS_CORRECTED                = 1,
  WPD_COLOR_CORRECTED_STATUS_SHOULD_NOT_BE_CORRECTED  = 2
} ;
```



## Constants

<dl> <dt>

<span id="WPD_COLOR_CORRECTED_STATUS_NOT_CORRECTED"></span><span id="wpd_color_corrected_status_not_corrected"></span>**WPD\_COLOR\_CORRECTED\_STATUS\_NOT\_CORRECTED**
</dt> <dd>

The image has not been color corrected.

</dd> <dt>

<span id="WPD_COLOR_CORRECTED_STATUS_CORRECTED"></span><span id="wpd_color_corrected_status_corrected"></span>**WPD\_COLOR\_CORRECTED\_STATUS\_CORRECTED**
</dt> <dd>

The image has been color corrected.

</dd> <dt>

<span id="WPD_COLOR_CORRECTED_STATUS_SHOULD_NOT_BE_CORRECTED"></span><span id="wpd_color_corrected_status_should_not_be_corrected"></span>**WPD\_COLOR\_CORRECTED\_STATUS\_SHOULD\_NOT\_BE\_CORRECTED**
</dt> <dd>

The image has not been, and should not be, color corrected.

</dd> </dl>

## Remarks

Indicates the color corrected status of an image. This enumeration is used by the [WPD\_IMAGE\_COLOR\_CORRECTED\_STATUS](image-properties.md) property.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**Structures and Enumeration Types**](structures-and-enumeration-types.md)
</dt> </dl>

 

 




