---
description: The WPD\_POWER\_SOURCES enumeration type describes the power source that a device is using.
ms.assetid: feebf213-052d-4315-84db-2109cab5f179
title: WPD_POWER_SOURCES enumeration (PortableDevice.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WPD_POWER_SOURCES
api_type: 
- HeaderDef
api_location: 
- PortableDevice.h
---

# WPD\_POWER\_SOURCES enumeration

The **WPD\_POWER\_SOURCES** enumeration type describes the power source that a device is using.

## Syntax


```C++
typedef enum WPD_POWER_SOURCES { 
  WPD_POWER_SOURCE_BATTERY   = 0,
  WPD_POWER_SOURCE_EXTERNAL  = 1
} ;
```



## Constants

<dl> <dt>

<span id="WPD_POWER_SOURCE_BATTERY"></span><span id="wpd_power_source_battery"></span>**WPD\_POWER\_SOURCE\_BATTERY**
</dt> <dd>

The device power source is a battery.

</dd> <dt>

<span id="WPD_POWER_SOURCE_EXTERNAL"></span><span id="wpd_power_source_external"></span>**WPD\_POWER\_SOURCE\_EXTERNAL**
</dt> <dd>

The device uses an external power source.

</dd> </dl>

## Remarks

This enumeration is used by the [WPD\_DEVICE\_POWER\_SOURCE](device-properties.md) property.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**Structures and Enumeration Types**](structures-and-enumeration-types.md)
</dt> </dl>

 

 




