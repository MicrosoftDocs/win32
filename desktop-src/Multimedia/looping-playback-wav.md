---
title: Looping Playback (Waveform Audio)
description: Looping Playback (Waveform Audio)
ms.assetid: 8411290b-a3c5-4347-bee3-43c35188f736
keywords:
- waveform audio,looping sounds
- waveform-audio interface,looping sounds
- waveform audio,looping playback
- waveform-audio interface,looping playback
- looping waveform-audio sounds
- looping waveform-audio playback
- waveOutWrite function
- waveOutBreakLoop function
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Looping Playback

\[The feature associated with this page, [Waveform Audio](/windows/win32/multimedia/waveform-audio), is a legacy feature. It has been superseded by [WASAPI](/windows/win32/coreaudio/wasapi) and [Audio Graphs](/windows/uwp/audio-video-camera/audio-graphs). **WASAPI** and **Audio Graphs** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **WASAPI** and **Audio Graphs** instead of **Waveform Audio**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Looping a sound is controlled by the **dwLoops** and **dwFlags** members in the [**WAVEHDR**](/windows/win32/api/mmeapi/ns-mmeapi-wavehdr) structures passed to the device with the [**waveOutWrite**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutwrite) function. Use the **WHDR\_BEGINLOOP** and **WHDR\_ENDLOOP** flags in the **dwFlags** member to specify the beginning and ending data blocks for looping.

To loop a single data block, specify both flags for the same block. To specify the number of loops, use the **dwLoops** member in the [**WAVEHDR**](/windows/win32/api/mmeapi/ns-mmeapi-wavehdr) structure for the first block in the loop.

You can call the [**waveOutBreakLoop**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutbreakloop) function to stop a looping sound.

## Related topics

<dl> <dt>

[Playing Waveform-Audio Files](playing-waveform-audio-files.md)
</dt> </dl>

 

 
