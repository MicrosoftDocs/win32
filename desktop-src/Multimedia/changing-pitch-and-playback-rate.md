---
title: Changing Pitch and Playback Rate
description: Changing Pitch and Playback Rate
ms.assetid: f0f5249b-ae2a-4f17-80ee-575f9f7963a7
keywords:
- waveform audio,pitch
- waveform-audio interface,pitch
- waveform audio,playback rate
- waveform-audio interface,playback rate
- waveform audio,changing pitch
- waveform-audio interface,changing pitch
- waveform audio,changing playback rate
- waveform-audio interface,changing playback rate
- changing waveform-audio playback rate
- changing waveform-audio pitch
ms.topic: article
ms.date: 05/31/2018
---

# Changing Pitch and Playback Rate

Some waveform-audio output devices can vary the pitch and the playback rate of waveform-audio data. Not all waveform-audio devices support pitch and playback-rate changes. For information about how to determine whether a particular waveform-audio device supports pitch and playback rate changes, see [Devices and Data Types](devices-and-data-types.md).

The differences between changing pitch and playback rate are as follows:

-   Changing the playback rate is performed by the device driver and does not require specialized hardware. The sample rate is not changed, but the driver interpolates by skipping or synthesizing samples. For example, if the playback rate is changed by a factor of two, the driver skips every other sample.
-   Changing the pitch requires specialized hardware. The playback rate and sample rate are not changed.

Windows provides the following functions to query and set waveform-audio pitch and playback rates.



| Function                                                 | Description                                                                 |
|----------------------------------------------------------|-----------------------------------------------------------------------------|
| [**waveOutGetPitch**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutgetpitch)               | Retrieves the pitch for the specified waveform-audio output device.         |
| [**waveOutGetPlaybackRate**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutgetplaybackrate) | Retrieves the playback rate for the specified waveform-audio output device. |
| [**waveOutSetPitch**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutsetpitch)               | Sets the pitch for the specified waveform-audio output device.              |
| [**waveOutSetPlaybackRate**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutsetplaybackrate) | Sets the playback rate for the specified waveform-audio output device.      |



 

The pitch and playback rates are changed by a factor specified with a fixed-point number packed into a doubleword value. The upper 16 bits specify the integer part of the number; the lower 16 bits specify the fractional part. For example, the value 1.5 is represented as 0x00018000L. The value 0.75 is represented as 0x0000C000L. A value of 1.0 (0x00010000) means the pitch or playback rate is unchanged.

 

 