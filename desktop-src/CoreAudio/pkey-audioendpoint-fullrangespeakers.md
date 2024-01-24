---
description: The PKEY\_AudioEndpoint\_FullRangeSpeakers property specifies the channel-configuration mask for the full-range speakers that are connected to the audio endpoint device.
ms.assetid: c0a54b3d-84dc-4771-8891-167ce00e2218
title: PKEY_AudioEndpoint_FullRangeSpeakers (Mmdeviceapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PKEY\_AudioEndpoint\_FullRangeSpeakers

The **PKEY\_AudioEndpoint\_FullRangeSpeakers** property specifies the channel-configuration mask for the full-range speakers that are connected to the audio endpoint device. The mask indicates the physical configuration of the full-range speakers and specifies the assignment of channels to those speakers.

The **vt** member of the **PROPVARIANT** structure is set to VT\_UI4.

The **uintVal** member of the **PROPVARIANT** structure contains a channel-configuration mask that is cast to type **UINT**.

A full-range speaker is capable of playing sounds over the full range from bass to treble. Typically, larger speakers are full range but smaller speakers are significantly less capable of playing bass sounds. In Windows Vista, the audio engine uses this property to manage bass levels in the audio output stream that is played by the audio endpoint device.

The channel-configuration mask for this property is in the same format as the channel-configuration mask for the [**PKEY\_AudioEndpoint\_PhysicalSpeakers**](pkey-audioendpoint-physicalspeakers.md) property. For more information about channel-configuration masks, see [KSPROPERTY_AUDIO_CHANNEL_CONFIG](/windows-hardware/drivers/audio/ksproperty-audio-channel-config).

The system obtains the channel-configuration mask for the PKEY\_AudioEndpoint\_FullRangeSpeakers property from the user. The user enters this information through the Windows multimedia control panel, Mmsys.cpl. For more information about Mmsys.cpl, see the Windows DDK documentation.

The channel-configuration mask for the PKEY\_AudioEndpoint\_FullRangeSpeakers property of an audio endpoint device is a subset of the channel-configuration mask for the PKEY\_AudioEndpoint\_PhysicalSpeakers property of the same device.

For example, if an audio endpoint device drives a set of 5.1 surround-sound speakers, then the channel-configuration mask for the PKEY\_AudioEndpoint\_PhysicalSpeakers property is KSAUDIO\_SPEAKER\_5POINT1. This mask indicates the presence of front-left, front-right, front-center, side-left, and side-right speakers—plus a subwoofer. If the front-left and front-right speakers are large enough to produce bass sounds but the smaller front-center and side speakers are not, then the channel-configuration mask for the PKEY\_AudioEndpoint\_FullRangeSpeakers property is KSAUDIO\_SPEAKER\_STEREO, which indicates only the front-left and front-right speakers. Channel-configuration masks KSAUDIO\_SPEAKER\_5POINT1 and KSAUDIO\_SPEAKER\_STEREO are defined in header file Ksmedia.h.

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
</dt> <dt>

[**PKEY\_AudioEndpoint\_PhysicalSpeakers Property**](pkey-audioendpoint-physicalspeakers.md)
</dt> </dl>

 

 




