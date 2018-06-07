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
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Waveform Audio Reference

This section lists the functions, structures, and messages associated with waveform audio, which are documented under [Multimedia Reference](multimedia-reference.md). These elements are grouped as follows.

## Auxiliary Devices

-   [**AUXCAPS**](https://www.bing.com/search?q=**AUXCAPS**)
-   [**auxGetDevCaps**](https://www.bing.com/search?q=**auxGetDevCaps**)
-   [**auxGetNumDevs**](https://www.bing.com/search?q=**auxGetNumDevs**)
-   [**auxGetVolume**](https://www.bing.com/search?q=**auxGetVolume**)
-   [**auxOutMessage**](https://www.bing.com/search?q=**auxOutMessage**)
-   [**auxSetVolume**](https://www.bing.com/search?q=**auxSetVolume**)

## Easy Playback

-   [**PlaySound**](/windows/desktop/api/Mmsystem/)
-   [**sndPlaySound**](/windows/desktop/api/Mmsystem/)

## Errors

-   [**waveInGetErrorText**](https://www.bing.com/search?q=**waveInGetErrorText**)
-   [**waveOutGetErrorText**](https://www.bing.com/search?q=**waveOutGetErrorText**)

## Opening and Closing

-   [**PCMWAVEFORMAT**](https://www.bing.com/search?q=**PCMWAVEFORMAT**)
-   [**MM\_WIM\_CLOSE**](mm-wim-close.md)
-   [**MM\_WIM\_OPEN**](mm-wim-open.md)
-   [**MM\_WOM\_CLOSE**](mm-wom-close.md)
-   [**MM\_WOM\_OPEN**](mm-wom-open.md)
-   [**WAVEFORMAT**](/windows/desktop/api/mmeapi/ns-mmeapi-twaveformatex)
-   [**WAVEFORMATEX**](/windows/desktop/api/Mmreg/)
-   [**waveInClose**](https://www.bing.com/search?q=**waveInClose**)
-   [**waveInProc**](/windows/desktop/api/Mmsystem/)
-   [**waveInOpen**](https://www.bing.com/search?q=**waveInOpen**)
-   [**waveOutClose**](https://www.bing.com/search?q=**waveOutClose**)
-   [**waveOutProc**](/windows/desktop/api/Mmsystem/)
-   [**waveOutOpen**](https://www.bing.com/search?q=**waveOutOpen**)
-   [**WIM\_CLOSE**](wim-close.md)
-   [**WIM\_OPEN**](wim-open.md)
-   [**WOM\_CLOSE**](wom-close.md)
-   [**WOM\_OPEN**](wom-open.md)

## Pitch

-   [**waveOutGetPitch**](https://www.bing.com/search?q=**waveOutGetPitch**)
-   [**waveOutSetPitch**](https://www.bing.com/search?q=**waveOutSetPitch**)

## Playback Rate

-   [**waveOutGetPlaybackRate**](https://www.bing.com/search?q=**waveOutGetPlaybackRate**)
-   [**waveOutSetPlaybackRate**](https://www.bing.com/search?q=**waveOutSetPlaybackRate**)

## Playback Progress

-   [**MM\_WOM\_DONE**](mm-wom-done.md)
-   [**waveOutBreakLoop**](https://www.bing.com/search?q=**waveOutBreakLoop**)
-   [**waveOutPause**](https://www.bing.com/search?q=**waveOutPause**)
-   [**waveOutReset**](https://www.bing.com/search?q=**waveOutReset**)
-   [**waveOutRestart**](https://www.bing.com/search?q=**waveOutRestart**)
-   [**WOM\_DONE**](wom-done.md)

## Playing

-   [**MM\_WOM\_DONE**](mm-wom-done.md)
-   [**WAVEHDR**](https://www.bing.com/search?q=**WAVEHDR**)
-   [**waveOutPrepareHeader**](https://www.bing.com/search?q=**waveOutPrepareHeader**)
-   [**waveOutUnprepareHeader**](https://www.bing.com/search?q=**waveOutUnprepareHeader**)
-   [**waveOutWrite**](https://www.bing.com/search?q=**waveOutWrite**)
-   [**WOM\_DONE**](wom-done.md)

## Querying a Device

-   [**WAVEINCAPS**](https://www.bing.com/search?q=**WAVEINCAPS**)
-   [**waveInGetDevCaps**](https://www.bing.com/search?q=**waveInGetDevCaps**)
-   [**waveInGetNumDevs**](https://www.bing.com/search?q=**waveInGetNumDevs**)
-   [**WAVEOUTCAPS**](https://www.bing.com/search?q=**WAVEOUTCAPS**)
-   [**waveOutGetDevCaps**](https://www.bing.com/search?q=**waveOutGetDevCaps**)
-   [**waveOutGetNumDevs**](https://www.bing.com/search?q=**waveOutGetNumDevs**)

## Recording

-   [**MM\_WIM\_DATA**](mm-wim-data.md)
-   [**waveInAddBuffer**](https://www.bing.com/search?q=**waveInAddBuffer**)
-   [**waveInPrepareHeader**](https://www.bing.com/search?q=**waveInPrepareHeader**)
-   [**waveInReset**](https://www.bing.com/search?q=**waveInReset**)
-   [**waveInStart**](https://www.bing.com/search?q=**waveInStart**)
-   [**waveInStop**](https://www.bing.com/search?q=**waveInStop**)
-   [**waveInUnprepareHeader**](https://www.bing.com/search?q=**waveInUnprepareHeader**)
-   [**WIM\_DATA**](wim-data.md)

## Retrieving Device Identifiers

-   [**waveInGetID**](https://www.bing.com/search?q=**waveInGetID**)
-   [**waveOutGetID**](https://www.bing.com/search?q=**waveOutGetID**)

## Retrieving the Current Position

-   [**waveInGetPosition**](https://www.bing.com/search?q=**waveInGetPosition**)
-   [**waveOutGetPosition**](https://www.bing.com/search?q=**waveOutGetPosition**)

## Sending Custom Messages

-   [**waveInMessage**](https://www.bing.com/search?q=**waveInMessage**)
-   [**waveOutMessage**](https://www.bing.com/search?q=**waveOutMessage**)

## Volume

-   [**waveOutGetVolume**](https://www.bing.com/search?q=**waveOutGetVolume**)
-   [**waveOutSetVolume**](https://www.bing.com/search?q=**waveOutSetVolume**)

## Related topics

<dl> <dt>

[Waveform Audio](waveform-audio.md)
</dt> </dl>

 

 




