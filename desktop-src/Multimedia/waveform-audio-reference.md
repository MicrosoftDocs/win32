---
title: Waveform Audio Reference
description: This section lists the functions, structures, and messages associated with waveform audio, which are documented under Multimedia Reference. These elements are grouped as follows.
ms.assetid: 723953f7-b38e-4f24-8d54-9849e013011d
keywords:
- Windows multimedia,waveform audio reference
- multimedia,waveform audio reference
- multimedia audio,waveform reference
- audio,waveform reference
- Windows multimedia,waveform audio
- multimedia,waveform audio
- multimedia audio,waveform
- audio,waveform
- waveform audio,reference
- waveform audio reference,about
- reference for wavefore audio,about
- waveform audio reference,auxiliary devices
- reference for wavefore audio,auxiliary devices
- waveform audio reference,playback
- reference for wavefore audio,playback
- waveform audio reference,errors
- reference for wavefore audio,errors
- waveform audio reference,opening
- reference for wavefore audio,opening
- waveform audio reference,closing
- reference for wavefore audio,closing
- waveform audio reference,pitch
- reference for wavefore audio,pitch
- waveform audio reference,volume
- reference for wavefore audio,volume
- waveform audio reference,messages
- reference for wavefore audio,messages
- waveform audio reference,current position
- reference for wavefore audio,current position
- waveform audio reference,recording
- reference for wavefore audio,recording
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Waveform Audio Reference

This section lists the functions, structures, and messages associated with waveform audio, which are documented under [Multimedia Reference](multimedia-reference.md). These elements are grouped as follows.

## Auxiliary Devices

-   [**AUXCAPS**](https://msdn.microsoft.com/en-us/library/Dd756711(v=VS.85).aspx)
-   [**auxGetDevCaps**](https://msdn.microsoft.com/en-us/library/Dd756712(v=VS.85).aspx)
-   [**auxGetNumDevs**](https://msdn.microsoft.com/en-us/library/Dd756713(v=VS.85).aspx)
-   [**auxGetVolume**](https://msdn.microsoft.com/en-us/library/Dd756714(v=VS.85).aspx)
-   [**auxOutMessage**](https://msdn.microsoft.com/en-us/library/Dd756716(v=VS.85).aspx)
-   [**auxSetVolume**](https://msdn.microsoft.com/en-us/library/Dd756717(v=VS.85).aspx)

## Easy Playback

-   [**PlaySound**](https://msdn.microsoft.com/en-us/library/Dd743680(v=VS.85).aspx)
-   [**sndPlaySound**](https://msdn.microsoft.com/en-us/library/Dd798676(v=VS.85).aspx)

## Errors

-   [**waveInGetErrorText**](https://msdn.microsoft.com/en-us/library/Dd743842(v=VS.85).aspx)
-   [**waveOutGetErrorText**](https://msdn.microsoft.com/en-us/library/Dd743858(v=VS.85).aspx)

## Opening and Closing

-   [**PCMWAVEFORMAT**](https://msdn.microsoft.com/en-us/library/Dd743663(v=VS.85).aspx)
-   [**MM\_WIM\_CLOSE**](mm-wim-close.md)
-   [**MM\_WIM\_OPEN**](mm-wim-open.md)
-   [**MM\_WOM\_CLOSE**](mm-wom-close.md)
-   [**MM\_WOM\_OPEN**](mm-wom-open.md)
-   [**WAVEFORMAT**](/windows/desktop/api/mmeapi/ns-mmeapi-twaveformatex)
-   [**WAVEFORMATEX**](https://msdn.microsoft.com/en-us/library/Dd757713(v=VS.85).aspx)
-   [**waveInClose**](https://msdn.microsoft.com/en-us/library/Dd743840(v=VS.85).aspx)
-   [**waveInProc**](https://msdn.microsoft.com/en-us/library/Dd743849(v=VS.85).aspx)
-   [**waveInOpen**](https://msdn.microsoft.com/en-us/library/Dd743847(v=VS.85).aspx)
-   [**waveOutClose**](https://msdn.microsoft.com/en-us/library/Dd743856(v=VS.85).aspx)
-   [**waveOutProc**](https://msdn.microsoft.com/en-us/library/Dd743869(v=VS.85).aspx)
-   [**waveOutOpen**](https://msdn.microsoft.com/en-us/library/Dd743866(v=VS.85).aspx)
-   [**WIM\_CLOSE**](wim-close.md)
-   [**WIM\_OPEN**](wim-open.md)
-   [**WOM\_CLOSE**](wom-close.md)
-   [**WOM\_OPEN**](wom-open.md)

## Pitch

-   [**waveOutGetPitch**](https://msdn.microsoft.com/en-us/library/Dd743861(v=VS.85).aspx)
-   [**waveOutSetPitch**](https://msdn.microsoft.com/en-us/library/Dd743872(v=VS.85).aspx)

## Playback Rate

-   [**waveOutGetPlaybackRate**](https://msdn.microsoft.com/en-us/library/Dd743862(v=VS.85).aspx)
-   [**waveOutSetPlaybackRate**](https://msdn.microsoft.com/en-us/library/Dd743873(v=VS.85).aspx)

## Playback Progress

-   [**MM\_WOM\_DONE**](mm-wom-done.md)
-   [**waveOutBreakLoop**](https://msdn.microsoft.com/en-us/library/Dd743854(v=VS.85).aspx)
-   [**waveOutPause**](https://msdn.microsoft.com/en-us/library/Dd743867(v=VS.85).aspx)
-   [**waveOutReset**](https://msdn.microsoft.com/en-us/library/Dd743870(v=VS.85).aspx)
-   [**waveOutRestart**](https://msdn.microsoft.com/en-us/library/Dd743871(v=VS.85).aspx)
-   [**WOM\_DONE**](wom-done.md)

## Playing

-   [**MM\_WOM\_DONE**](mm-wom-done.md)
-   [**WAVEHDR**](https://msdn.microsoft.com/en-us/library/Dd743837(v=VS.85).aspx)
-   [**waveOutPrepareHeader**](https://msdn.microsoft.com/en-us/library/Dd743868(v=VS.85).aspx)
-   [**waveOutUnprepareHeader**](https://msdn.microsoft.com/en-us/library/Dd743875(v=VS.85).aspx)
-   [**waveOutWrite**](https://msdn.microsoft.com/en-us/library/Dd743876(v=VS.85).aspx)
-   [**WOM\_DONE**](wom-done.md)

## Querying a Device

-   [**WAVEINCAPS**](https://msdn.microsoft.com/en-us/library/Dd743839(v=VS.85).aspx)
-   [**waveInGetDevCaps**](https://msdn.microsoft.com/en-us/library/Dd743841(v=VS.85).aspx)
-   [**waveInGetNumDevs**](https://msdn.microsoft.com/en-us/library/Dd743844(v=VS.85).aspx)
-   [**WAVEOUTCAPS**](https://msdn.microsoft.com/en-us/library/Dd743855(v=VS.85).aspx)
-   [**waveOutGetDevCaps**](https://msdn.microsoft.com/en-us/library/Dd743857(v=VS.85).aspx)
-   [**waveOutGetNumDevs**](https://msdn.microsoft.com/en-us/library/Dd743860(v=VS.85).aspx)

## Recording

-   [**MM\_WIM\_DATA**](mm-wim-data.md)
-   [**waveInAddBuffer**](https://msdn.microsoft.com/en-us/library/Dd743838(v=VS.85).aspx)
-   [**waveInPrepareHeader**](https://msdn.microsoft.com/en-us/library/Dd743848(v=VS.85).aspx)
-   [**waveInReset**](https://msdn.microsoft.com/en-us/library/Dd743850(v=VS.85).aspx)
-   [**waveInStart**](https://msdn.microsoft.com/en-us/library/Dd743851(v=VS.85).aspx)
-   [**waveInStop**](https://msdn.microsoft.com/en-us/library/Dd743852(v=VS.85).aspx)
-   [**waveInUnprepareHeader**](https://msdn.microsoft.com/en-us/library/Dd743853(v=VS.85).aspx)
-   [**WIM\_DATA**](wim-data.md)

## Retrieving Device Identifiers

-   [**waveInGetID**](https://msdn.microsoft.com/en-us/library/Dd743843(v=VS.85).aspx)
-   [**waveOutGetID**](https://msdn.microsoft.com/en-us/library/Dd743859(v=VS.85).aspx)

## Retrieving the Current Position

-   [**waveInGetPosition**](https://msdn.microsoft.com/en-us/library/Dd743845(v=VS.85).aspx)
-   [**waveOutGetPosition**](https://msdn.microsoft.com/en-us/library/Dd743863(v=VS.85).aspx)

## Sending Custom Messages

-   [**waveInMessage**](https://msdn.microsoft.com/en-us/library/Dd743846(v=VS.85).aspx)
-   [**waveOutMessage**](https://msdn.microsoft.com/en-us/library/Dd743865(v=VS.85).aspx)

## Volume

-   [**waveOutGetVolume**](https://msdn.microsoft.com/en-us/library/Dd743864(v=VS.85).aspx)
-   [**waveOutSetVolume**](https://msdn.microsoft.com/en-us/library/Dd743874(v=VS.85).aspx)

## Related topics

<dl> <dt>

[Waveform Audio](waveform-audio.md)
</dt> </dl>

 

 




