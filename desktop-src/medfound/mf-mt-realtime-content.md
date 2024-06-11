---
description: Specifies the real time media type.
title: MF_MT_REALTIME_CONTENT attribute (Mfapi.h)
ms.topic: reference
ms.date: 06/07/2024
---

# MF\_MT\_REALTIME\_CONTENT attribute

Specifies the real time media content type for low-latency rendering.

## Data type

**UINT32**

## Remarks

This attribute will enable the adaptive low-latency rendering feature.  It will minimize the latency to all of the monitors that the video is currently displayed on, while ensuring high quality output. A media source should set this attribute on its output video stream.



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 version 1607<br/>                                       |
| Minimum supported server<br/> | Windows Server version 1607<br/>                            |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> </dl>

 

 
