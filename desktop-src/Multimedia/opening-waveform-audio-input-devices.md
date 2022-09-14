---
title: Opening Waveform-Audio Input Devices
description: Opening Waveform-Audio Input Devices
ms.assetid: 46cdbce6-2433-433a-abd2-39e4146aa2e9
keywords:
- waveform audio,opening input devices
- waveform-audio interface,opening input devices
- recording waveform audio,opening input devices
- opening waveform-audio input devices
- waveInOpen function
ms.topic: article
ms.date: 05/31/2018
---

# Opening Waveform-Audio Input Devices

Use the [**waveInOpen**](/windows/win32/api/mmeapi/nf-mmeapi-waveinopen) function to open a waveform-audio input device for recording. This function opens the device associated with the specified device identifier and returns a handle of the open device by writing the handle of a specified memory location.

Some multimedia computers have multiple waveform-audio input devices. Unless you know you want to open a specific waveform-audio input device in a system, you should use the WAVE\_MAPPER constant for the device identifier when you open a device. The [**waveInOpen**](/windows/win32/api/mmeapi/nf-mmeapi-waveinopen) function will choose the device in the system best able to record in the specified data format.

## Related topics

<dl> <dt>

[Recording Waveform Audio](recording-waveform-audio.md)
</dt> </dl>

 

 