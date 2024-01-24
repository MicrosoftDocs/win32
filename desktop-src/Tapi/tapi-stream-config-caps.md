---
description: The TAPI\_STREAM\_CONFIG\_CAPS structure contains either video or audio stream configuration information.
ms.assetid: 83b39751-b00f-4762-830b-13cafbcb1cfd
title: TAPI_STREAM_CONFIG_CAPS structure (Ipmsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# TAPI\_STREAM\_CONFIG\_CAPS structure

\[ This structure is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **TAPI\_STREAM\_CONFIG\_CAPS** structure contains either video or audio stream configuration information.

## Syntax


```C++
} TAPI_STREAM_CONFIG_CAPS, *PTAPI_STREAM_CONFIG_CAPS;
```



## Members

<dl> <dt>

**CapsType**
</dt> <dd>

Defines whether the union member contains video or audio information.

</dd> <dt>

**VideoCap**
</dt> <dd>

A [**TAPI\_VIDEO\_STREAM\_CONFIG\_CAPS**](tapi-video-stream-config-caps.md) structure containing the video stream capabilities.

</dd> <dt>

**AudioCap**
</dt> <dd>

A [**TAPI\_AUDIO\_STREAM\_CONFIG\_CAPS**](tapi-audio-stream-config-caps.md) structure containing the audio stream capabilities.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------|------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.1<br/>                                                       |
| Header<br/>       | <dl> <dt>Ipmsp.h</dt> </dl> |



## See also

<dl> <dt>

[**ITFormatControl::GetStreamCaps**](itformatcontrol-getstreamcaps.md)
</dt> <dt>

[**StreamConfigCapsType**](streamconfigcapstype.md)
</dt> <dt>

[**TAPI\_VIDEO\_STREAM\_CONFIG\_CAPS**](tapi-video-stream-config-caps.md)
</dt> <dt>

[**TAPI\_AUDIO\_STREAM\_CONFIG\_CAPS**](tapi-audio-stream-config-caps.md)
</dt> </dl>

 

 




