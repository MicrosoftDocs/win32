---
description: "Learn more about: PKEY_AudioEndpoint_PhysicalSpeakers"
ms.assetid: 20049071-0a14-421e-8bc5-04af9c7117b0
title: PKEY_AudioEndpoint_PhysicalSpeakers (Mmdeviceapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PKEY\_AudioEndpoint\_PhysicalSpeakers

The **PKEY\_AudioEndpoint\_PhysicalSpeakers** property specifies the channel-configuration mask for the audio endpoint device. The mask indicates the physical configuration of a set of speakers and specifies the assignment of channels to speakers. For more information about channel-configuration masks, see [KSPROPERTY_AUDIO_CHANNEL_CONFIG](/windows-hardware/drivers/audio/ksproperty-audio-channel-config).

The **vt** member of the **PROPVARIANT** structure is set to VT\_UI4.

The **uintVal** member of the **PROPVARIANT** structure contains a channel-configuration mask that is cast to type **UINT**.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Mmdeviceapi.h</dt> </dl> |



## See also

<dl> <dt>

[**Audio Endpoint Properties**](audio-endpoint-properties.md)
</dt> <dt>

[Core Audio Properties](core-audio-properties.md)
</dt> </dl>

 

 




