---
Description: The WPD\_POWER\_SOURCES enumeration type describes the power source that a device is using.
ms.assetid: feebf213-052d-4315-84db-2109cab5f179
title: WPD\_POWER\_SOURCES enumeration
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
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



|                   |                                                                                             |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**Structures and Enumeration Types**](structures-and-enumeration-types.md)
</dt> </dl>

 

 




