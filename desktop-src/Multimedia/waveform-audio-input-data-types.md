---
title: Waveform-Audio Input Data Types
description: Waveform-Audio Input Data Types
ms.assetid: dfedcb93-edfb-4a25-8445-95d4aee55734
keywords:
- waveform audio,input data types
- waveform-audio interface,input data types
- recording waveform audio,input data types
- HWAVEIN handle
- WAVEFORMATEX structure
- WAVEHDR structure
- WAVEINCAPS structure
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Waveform-Audio Input Data Types

\[The feature associated with this page, [Waveform Audio](/windows/win32/multimedia/waveform-audio), is a legacy feature. It has been superseded by [WASAPI](/windows/win32/coreaudio/wasapi) and [Audio Graphs](/windows/uwp/audio-video-camera/audio-graphs). **WASAPI** and **Audio Graphs** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **WASAPI** and **Audio Graphs** instead of **Waveform Audio**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following data types are defined for waveform-audio input functions.



| Type                                 | Description                                                                                                                                                     |
|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **HWAVEIN**                          | Handle of an open waveform-audio input device.                                                                                                                  |
| [**WAVEFORMATEX**](/windows/win32/api/mmeapi/ns-mmeapi-waveformatex) | Structure that specifies the data formats supported by a particular waveform-audio input device. This structure is also used for waveform-audio output devices. |
| [**WAVEHDR**](/windows/win32/api/mmeapi/ns-mmeapi-wavehdr)           | Structure used as a header for a block of waveform-audio input data. This structure is also used for waveform-audio output devices.                             |
| [**WAVEINCAPS**](/windows/win32/api/mmeapi/ns-mmeapi-waveincaps)     | Structure used to inquire about the capabilities of a particular waveform-audio input device.                                                                   |



 

## Related topics

<dl> <dt>

[Recording Waveform Audio](recording-waveform-audio.md)
</dt> </dl>

 

 