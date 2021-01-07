---
description: The WPD\_STREAM\_UNITS enumeration specifies the unit types to be used for IPortableDeviceUnitsStream operations.
ms.assetid: BE668696-7AF3-44AA-891A-9BFF67FB5544
title: WPD_STREAM_UNITS enumeration (PortableDeviceTypes.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WPD_STREAM_UNITS
api_type: 
- HeaderDef
api_location: 
- PortableDeviceTypes.h
---

# WPD\_STREAM\_UNITS enumeration

The **WPD\_STREAM\_UNITS** enumeration specifies the unit types to be used for [**IPortableDeviceUnitsStream**](/windows/desktop/api/PortableDeviceAPI/nn-portabledeviceapi-iportabledeviceunitsstream) operations.

## Syntax


```C++
typedef enum _WPD_STREAM_UNITS { 
  WPD_STREAM_UNITS_BYTES         = 0,
  WPD_STREAM_UNITS_FRAMES        = 1,
  WPD_STREAM_UNITS_ROWS          = 2,
  WPD_STREAM_UNITS_MILLISECONDS  = 3,
  WPD_STREAM_UNITS_MICROSECONDS  = 4
} WPD_STREAM_UNITS;
```



## Constants

<dl> <dt>

<span id="WPD_STREAM_UNITS_BYTES"></span><span id="wpd_stream_units_bytes"></span>**WPD\_STREAM\_UNITS\_BYTES**
</dt> <dd>

The stream units are specified in bytes.

</dd> <dt>

<span id="WPD_STREAM_UNITS_FRAMES"></span><span id="wpd_stream_units_frames"></span>**WPD\_STREAM\_UNITS\_FRAMES**
</dt> <dd>

The stream units are specified in frames.

</dd> <dt>

<span id="WPD_STREAM_UNITS_ROWS"></span><span id="wpd_stream_units_rows"></span>**WPD\_STREAM\_UNITS\_ROWS**
</dt> <dd>

The stream units are specified in rows.

</dd> <dt>

<span id="WPD_STREAM_UNITS_MILLISECONDS"></span><span id="wpd_stream_units_milliseconds"></span>**WPD\_STREAM\_UNITS\_MILLISECONDS**
</dt> <dd>

The stream units are specified in milliseconds.

</dd> <dt>

<span id="WPD_STREAM_UNITS_MICROSECONDS"></span><span id="wpd_stream_units_microseconds"></span>**WPD\_STREAM\_UNITS\_MICROSECONDS**
</dt> <dd>

The stream units are specified in microseconds.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                       |
| Minimum supported server<br/> | None supported<br/>                                                                        |
| Header<br/>                   | <dl> <dt>PortableDeviceTypes.h</dt> </dl> |



## See also

<dl> <dt>

[**IPortableDeviceUnitsStream**](/windows/desktop/api/PortableDeviceAPI/nn-portabledeviceapi-iportabledeviceunitsstream)
</dt> <dt>

[**IPortableDeviceUnitsStream::SeekInUnits**](/windows/desktop/api/PortableDeviceAPI/nf-portabledeviceapi-iportabledeviceunitsstream-seekinunits)
</dt> </dl>

 

 




