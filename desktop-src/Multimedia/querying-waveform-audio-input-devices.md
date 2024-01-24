---
title: Querying Waveform-Audio Input Devices
description: Querying Waveform-Audio Input Devices
ms.assetid: 573b33bc-f445-496e-a0e6-0194d30bb668
keywords:
- waveform audio,querying input devices
- waveform-audio interface,querying input devices
- recording waveform audio,querying input devices
- querying waveform-audio input devices
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Querying Waveform-Audio Input Devices

\[The feature associated with this page, [Waveform Audio](/windows/win32/multimedia/waveform-audio), is a legacy feature. It has been superseded by [WASAPI](/windows/win32/coreaudio/wasapi) and [Audio Graphs](/windows/uwp/audio-video-camera/audio-graphs). **WASAPI** and **Audio Graphs** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **WASAPI** and **Audio Graphs** instead of **Waveform Audio**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Before recording waveform audio, you should call the [**waveInGetDevCaps**](/windows/win32/api/mmeapi/nf-mmeapi-waveingetdevcaps) function to determine the waveform-audio input capabilities of the system. This function fills a [**WAVEINCAPS**](/windows/win32/api/mmeapi/ns-mmeapi-waveincaps) structure with information about the capabilities of a specified device. This information includes the manufacturer and product identifiers, a product name for the device, and the version number of the device driver. In addition, the **WAVEINCAPS** structure provides information about the standard waveform-audio formats that the device supports.

## Related topics

<dl> <dt>

[Recording Waveform Audio](recording-waveform-audio.md)
</dt> </dl>

 

 