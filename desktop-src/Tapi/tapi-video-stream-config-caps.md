---
description: The TAPI\_VIDEO\_STREAM\_CONFIG\_CAPS structure is contained by the TAPI\_STREAM\_CONFIG\_CAPS structure when the CapsType member is set to the VideoCap member of the StreamConfigCapsType union.
ms.assetid: 8812755a-50e8-4d8e-ab67-7a3a4b2a4a67
title: TAPI_VIDEO_STREAM_CONFIG_CAPS structure (Ipmsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# TAPI\_VIDEO\_STREAM\_CONFIG\_CAPS structure

\[ This structure is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **TAPI\_VIDEO\_STREAM\_CONFIG\_CAPS** structure is contained by the [**TAPI\_STREAM\_CONFIG\_CAPS**](tapi-stream-config-caps.md) structure when the **CapsType** member is set to the **VideoCap** member of the [**StreamConfigCapsType**](streamconfigcapstype.md) union.

## Syntax


```C++
} TAPI_VIDEO_STREAM_CONFIG_CAPS;
```



## Members

<dl> <dt>

**Description**
</dt> <dd>

A friendly description of the audio stream configuration type for display to application users.

</dd> <dt>

**VideoStandard**
</dt> <dd>

Video standard being used.

</dd> <dt>

**InputSize**
</dt> <dd>

Input size of frame.

</dd> <dt>

**MinCroppingSize**
</dt> <dd>

Minimum cropping size.

</dd> <dt>

**MaxCroppingSize**
</dt> <dd>

Maximum cropping size.

</dd> <dt>

**CropGranularityX**
</dt> <dd>

Granularity of cropping allowed along the x-axis.

</dd> <dt>

**CropGranularityY**
</dt> <dd>

Granularity of cropping allowed along the y-axis.

</dd> <dt>

**CropAlignX**
</dt> <dd>

Alignment of x-axis cropping.

</dd> <dt>

**CropAlignY**
</dt> <dd>

Alignment of y-axis cropping.

</dd> <dt>

**MinOutputSize**
</dt> <dd>

Minimum resultant size of video window.

</dd> <dt>

**MaxOutputSize**
</dt> <dd>

Maximum resultant size of video window.

</dd> <dt>

**OutputGranularityX**
</dt> <dd>

Granularity of output size along the x-axis.

</dd> <dt>

**OutputGranularityY**
</dt> <dd>

Granularity of output size along the y-axis.

</dd> <dt>

**StretchTapsX**
</dt> <dd>

Stretch along the x-axis.

</dd> <dt>

**StretchTapsY**
</dt> <dd>

Stretch along the y-axis.

</dd> <dt>

**ShrinkTapsX**
</dt> <dd>

Shrink along the x-axis.

</dd> <dt>

**ShrinkTapsY**
</dt> <dd>

Shrink along the y-axis.

</dd> <dt>

**MinFrameInterval**
</dt> <dd>

Minimum video frame interval.

</dd> <dt>

**MaxFrameInterval**
</dt> <dd>

Maximum video frame interval.

</dd> <dt>

**MinBitsPerSecond**
</dt> <dd>

Minimum bits per second.

</dd> <dt>

**MaxBitsPerSecond**
</dt> <dd>

Maximum bits per second.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------|------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.1<br/>                                                       |
| Header<br/>       | <dl> <dt>Ipmsp.h</dt> </dl> |



## See also

<dl> <dt>

[**TAPI\_STREAM\_CONFIG\_CAPS**](tapi-stream-config-caps.md)
</dt> </dl>

 

 




