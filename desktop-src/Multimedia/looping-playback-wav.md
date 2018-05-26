---
title: Looping Playback
description: Looping Playback
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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Looping Playback

Looping a sound is controlled by the **dwLoops** and **dwFlags** members in the [**WAVEHDR**](wavehdr.md) structures passed to the device with the [**waveOutWrite**](waveoutwrite.md) function. Use the **WHDR\_BEGINLOOP** and **WHDR\_ENDLOOP** flags in the **dwFlags** member to specify the beginning and ending data blocks for looping.

To loop a single data block, specify both flags for the same block. To specify the number of loops, use the **dwLoops** member in the [**WAVEHDR**](wavehdr.md) structure for the first block in the loop.

You can call the [**waveOutBreakLoop**](waveoutbreakloop.md) function to stop a looping sound.

## Related topics

<dl> <dt>

[Playing Waveform-Audio Files](playing-waveform-audio-files.md)
</dt> </dl>

 

 




