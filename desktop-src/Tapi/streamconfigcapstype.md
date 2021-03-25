---
description: The StreamConfigCapsType enumeration type is used by the TAPI\_STREAM\_CONFIG\_CAPS structure as a switch to indicate whether audio or video streaming is involved.
ms.assetid: c3eec6b2-ce3b-49b1-a0ba-f450d60a1477
title: StreamConfigCapsType enumeration (Ipmsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# StreamConfigCapsType enumeration

\[ This enumeration is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **StreamConfigCapsType** enumeration type is used by the [**TAPI\_STREAM\_CONFIG\_CAPS**](tapi-stream-config-caps.md) structure as a switch to indicate whether audio or video streaming is involved.

## Syntax


```C++
} StreamConfigCapsType;
```



## Constants

<dl> <dt>

<span id="AudioStreamConfigCaps"></span><span id="audiostreamconfigcaps"></span><span id="AUDIOSTREAMCONFIGCAPS"></span>**AudioStreamConfigCaps**
</dt> <dd>

Audio streaming configuration.

</dd> <dt>

<span id="VideoStreamConfigCaps"></span><span id="videostreamconfigcaps"></span><span id="VIDEOSTREAMCONFIGCAPS"></span>**VideoStreamConfigCaps**
</dt> <dd>

Video streaming configuration.

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

 

 




