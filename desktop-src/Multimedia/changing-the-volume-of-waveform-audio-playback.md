---
title: Changing the Volume of Waveform-Audio Playback
description: Changing the Volume of Waveform-Audio Playback
ms.assetid: 814daa35-7905-47a2-ab08-29f20493af1e
keywords:
- waveform audio,changing playback volume
- waveform-audio interface,changing playback volume
- waveform audio,playback volume
- waveform-audio interface,playback volume
- changing waveform-audio playback volume
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Changing the Volume of Waveform-Audio Playback

\[The feature associated with this page, [Waveform Audio](/windows/win32/multimedia/waveform-audio), is a legacy feature. It has been superseded by [WASAPI](/windows/win32/coreaudio/wasapi) and [Audio Graphs](/windows/uwp/audio-video-camera/audio-graphs). **WASAPI** and **Audio Graphs** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **WASAPI** and **Audio Graphs** instead of **Waveform Audio**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Windows provides the following functions to query and set the volume level of waveform-audio output devices.



| Function                                     | Description                                                                       |
|----------------------------------------------|-----------------------------------------------------------------------------------|
| [**waveOutGetVolume**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutgetvolume) | Retrieves the current volume level of the specified waveform-audio output device. |
| [**waveOutSetVolume**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutsetvolume) | Sets the volume level of the specified waveform-audio output device.              |



 

Not all waveform-audio devices support volume changes. Some devices support individual volume control on both the left and right channels. For information about how to determine the volume-control capabilities of waveform-audio devices, see [Devices and Data Types](devices-and-data-types.md).

Some applications allow the user to control the volume for all audio devices in a system. (Many applications of this type use the audio mixer services; for more information, see [Audio Mixers](audio-mixers.md).) Unless your application is capable of this kind of master volume control, you should open an audio device before changing its volume. You should also query the volume level before changing it and restore the volume level to its previous level as soon as possible.

Volume is specified in a doubleword value. When the audio format is stereo, the upper 16 bits specify the relative volume of the right channel and the lower 16 bits specify the relative volume of the left channel. For devices that do not support left- and right-channel volume control, the lower 16 bits specify the volume level, and the upper 16 bits are ignored.

Volume-level values range from 0x0 (silence) to 0xFFFF (maximum volume) and are interpreted logarithmically. The perceived volume increase is the same when increasing the volume level from 0x5000 to 0x6000 as it is from 0x4000 to 0x5000.

 

 