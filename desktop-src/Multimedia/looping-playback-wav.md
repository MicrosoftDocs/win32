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
ms.date: 05/31/2018
---

# Looping Playback

Looping a sound is controlled by the **dwLoops** and **dwFlags** members in the [**WAVEHDR**](/windows/win32/api/mmeapi/ns-mmeapi-wavehdr) structures passed to the device with the [**waveOutWrite**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutwrite) function. Use the **WHDR\_BEGINLOOP** and **WHDR\_ENDLOOP** flags in the **dwFlags** member to specify the beginning and ending data blocks for looping.

To loop a single data block, specify both flags for the same block. To specify the number of loops, use the **dwLoops** member in the [**WAVEHDR**](/windows/win32/api/mmeapi/ns-mmeapi-wavehdr) structure for the first block in the loop.

You can call the [**waveOutBreakLoop**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutbreakloop) function to stop a looping sound.

## Related topics

<dl> <dt>

[Playing Waveform-Audio Files](playing-waveform-audio-files.md)
</dt> </dl>

 

 
