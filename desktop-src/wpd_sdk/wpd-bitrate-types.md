---
description: The WPD\_BITRATE\_TYPES enumeration type describes an audio files compression type.
ms.assetid: 9905b189-00c5-469b-ae48-10c79b9ac903
title: WPD_BITRATE_TYPES enumeration (PortableDevice.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WPD_BITRATE_TYPES
api_type: 
- HeaderDef
api_location: 
- PortableDevice.h
---

# WPD\_BITRATE\_TYPES enumeration

The **WPD\_BITRATE\_TYPES** enumeration type describes an audio file's compression type.

## Syntax


```C++
typedef enum WPD_BITRATE_TYPES { 
  WPD_BITRATE_TYPE_UNUSED    = 0,
  WPD_BITRATE_TYPE_DISCRETE  = 1,
  WPD_BITRATE_TYPE_VARIABLE  = 2,
  WPD_BITRATE_TYPE_FREE      = 3
} ;
```



## Constants

<dl> <dt>

<span id="WPD_BITRATE_TYPE_UNUSED"></span><span id="wpd_bitrate_type_unused"></span>**WPD\_BITRATE\_TYPE\_UNUSED**
</dt> <dd>

This value has not been specified.

</dd> <dt>

<span id="WPD_BITRATE_TYPE_DISCRETE"></span><span id="wpd_bitrate_type_discrete"></span>**WPD\_BITRATE\_TYPE\_DISCRETE**
</dt> <dd>

Constant bit rate compression.

</dd> <dt>

<span id="WPD_BITRATE_TYPE_VARIABLE"></span><span id="wpd_bitrate_type_variable"></span>**WPD\_BITRATE\_TYPE\_VARIABLE**
</dt> <dd>

Variable bit rate compression.

</dd> <dt>

<span id="WPD_BITRATE_TYPE_FREE"></span><span id="wpd_bitrate_type_free"></span>**WPD\_BITRATE\_TYPE\_FREE**
</dt> <dd>

Free format bit rate. This is a constant bit rate that is lower than the maximum allowed bit rate.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**Structures and Enumeration Types**](structures-and-enumeration-types.md)
</dt> </dl>

 

 




