---
description: The WPD\_FOCUS\_MODES enumeration type describes the focus mode used by a still image capture device.
ms.assetid: 3b092391-e4c1-4586-8df4-b58a1dcccc81
title: WPD_FOCUS_MODES enumeration (PortableDevice.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WPD_FOCUS_MODES
api_type: 
- HeaderDef
api_location: 
- PortableDevice.h
---

# WPD\_FOCUS\_MODES enumeration

The **WPD\_FOCUS\_MODES** enumeration type describes the focus mode used by a still image capture device.

## Syntax


```C++
typedef enum WPD_FOCUS_MODES { 
  WPD_FOCUS_UNDEFINED        = 0,
  WPD_FOCUS_MANUAL           = 1,
  WPD_FOCUS_AUTOMATIC        = 2,
  WPD_FOCUS_AUTOMATIC_MACRO  = 3
} ;
```



## Constants

<dl> <dt>

<span id="WPD_FOCUS_UNDEFINED"></span><span id="wpd_focus_undefined"></span>**WPD\_FOCUS\_UNDEFINED**
</dt> <dd>

The focus mode has not been specified.

</dd> <dt>

<span id="WPD_FOCUS_MANUAL"></span><span id="wpd_focus_manual"></span>**WPD\_FOCUS\_MANUAL**
</dt> <dd>

Specifies manual focus.

</dd> <dt>

<span id="WPD_FOCUS_AUTOMATIC"></span><span id="wpd_focus_automatic"></span>**WPD\_FOCUS\_AUTOMATIC**
</dt> <dd>

Specifies automatic focus, controlled by the device.

</dd> <dt>

<span id="WPD_FOCUS_AUTOMATIC_MACRO"></span><span id="wpd_focus_automatic_macro"></span>**WPD\_FOCUS\_AUTOMATIC\_MACRO**
</dt> <dd>

Specifies that the device should automatically switch between macro and normal focus, as required.

</dd> </dl>

## Remarks

This enumeration is used by the [WPD\_STILL\_IMAGE\_FOCUS\_MODE](still-image-properties.md) property.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**Structures and Enumeration Types**](structures-and-enumeration-types.md)
</dt> </dl>

 

 




