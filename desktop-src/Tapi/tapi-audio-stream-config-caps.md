---
description: The TAPI\_AUDIO\_STREAM\_CONFIG\_CAPS structure is contained by the TAPI\_STREAM\_CONFIG\_CAPS structure when the CapsType member is set to the AudioCap member of the StreamConfigCapsType union.
ms.assetid: 61575839-4604-4c8b-ae4d-fe796c3c5314
title: TAPI_AUDIO_STREAM_CONFIG_CAPS structure (Ipmsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# TAPI\_AUDIO\_STREAM\_CONFIG\_CAPS structure

\[ This structure is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **TAPI\_AUDIO\_STREAM\_CONFIG\_CAPS** structure is contained by the [**TAPI\_STREAM\_CONFIG\_CAPS**](tapi-stream-config-caps.md) structure when the **CapsType** member is set to the **AudioCap** member of the [**StreamConfigCapsType**](streamconfigcapstype.md) union.

## Syntax


```C++
} TAPI_AUDIO_STREAM_CONFIG_CAPS;
```



## Members

<dl> <dt>

**Description**
</dt> <dd>

A friendly description of the audio stream configuration type for display to application users.

</dd> <dt>

**MinimumChannels**
</dt> <dd>

The minimum number of channels associated with the stream.

</dd> <dt>

**MaximumChannels**
</dt> <dd>

The maximum number of channels associated with the stream.

</dd> <dt>

**ChannelsGranularity**
</dt> <dd>

The granularity of the channel count.

</dd> <dt>

**MinimumBitsPerSample**
</dt> <dd>

The minimum number of bits per sample.

</dd> <dt>

**MaximumBitsPerSample**
</dt> <dd>

The maximum number of bits per sample.

</dd> <dt>

**BitsPerSampleGranularity**
</dt> <dd>

The granularity of the bits per sample values.

</dd> <dt>

**MinimumSampleFrequency**
</dt> <dd>

The minimum sampling frequency.

</dd> <dt>

**MaximumSampleFrequency**
</dt> <dd>

The maximum sampling frequency.

</dd> <dt>

**SampleFrequencyGranularity**
</dt> <dd>

The granularity of the sampling frequency values.

</dd> <dt>

**MinimumAvgBytesPerSec**
</dt> <dd>

The minimum average bytes per second.

</dd> <dt>

**MaximumAvgBytesPerSec**
</dt> <dd>

The maximum average bytes per second.

</dd> <dt>

**AvgBytesPerSecGranularity**
</dt> <dd>

The granularity of the bytes per second values.

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

 

 




