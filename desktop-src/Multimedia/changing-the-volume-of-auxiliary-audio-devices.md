---
title: Changing the Volume of Auxiliary Audio-Devices
description: Changing the Volume of Auxiliary Audio-Devices
ms.assetid: d7357900-132c-4758-8bc2-a890aead01c3
keywords:
- waveform audio,changing auxiliary audio device volume
- changing auxiliary audio device volume
- auxiliary audio,changing device volume
- auxiliary audio interface
- auxiliary audio devices,changing volume
- auxiliary audio,interface
- auxiliary audio,devices
ms.topic: article
ms.date: 05/31/2018
---

# Changing the Volume of Auxiliary Audio-Devices

Windows provides the following functions to query and set the volume for auxiliary audio devices.



| Function                             | Description                                                                    |
|--------------------------------------|--------------------------------------------------------------------------------|
| [**auxGetVolume**](/windows/win32/api/mmeapi/nf-mmeapi-auxgetvolume) | Retrieves the current volume setting of the specified auxiliary output device. |
| [**auxSetVolume**](/windows/win32/api/mmeapi/nf-mmeapi-auxsetvolume) | Sets the volume of the specified auxiliary output device.                      |



 

Not all auxiliary audio devices support volume changes. Some devices can support individual volume changes on both the left and the right channels.

Volume is specified in a doubleword value, as with the waveform-audio and MIDI volume-control functions. When the audio format is stereo, the upper 16 bits specify the relative volume of the right channel and the lower 16 bits specify the relative volume of the left channel. For devices that do not support left- and right-channel volume control, the lower 16 bits specify the volume level, and the upper 16 bits are ignored.

Volume-level values range from 0x0 (silence) to 0xFFFF (maximum volume) and are interpreted logarithmically. The perceived volume increase is the same when increasing the volume level from 0x5000 to 0x6000 as it is from 0x4000 to 0x5000.

 

 