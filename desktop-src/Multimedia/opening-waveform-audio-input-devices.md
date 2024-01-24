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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Opening Waveform-Audio Input Devices

\[The feature associated with this page, [Waveform Audio](/windows/win32/multimedia/waveform-audio), is a legacy feature. It has been superseded by [WASAPI](/windows/win32/coreaudio/wasapi) and [Audio Graphs](/windows/uwp/audio-video-camera/audio-graphs). **WASAPI** and **Audio Graphs** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **WASAPI** and **Audio Graphs** instead of **Waveform Audio**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Use the [**waveInOpen**](/windows/win32/api/mmeapi/nf-mmeapi-waveinopen) function to open a waveform-audio input device for recording. This function opens the device associated with the specified device identifier and returns a handle of the open device by writing the handle of a specified memory location.

Some multimedia computers have multiple waveform-audio input devices. Unless you know you want to open a specific waveform-audio input device in a system, you should use the WAVE\_MAPPER constant for the device identifier when you open a device. The [**waveInOpen**](/windows/win32/api/mmeapi/nf-mmeapi-waveinopen) function will choose the device in the system best able to record in the specified data format.

## Related topics

<dl> <dt>

[Recording Waveform Audio](recording-waveform-audio.md)
</dt> </dl>

 

 