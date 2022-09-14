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
ms.topic: article
ms.date: 05/31/2018
---

# Waveform Audio Reference

This section lists the functions, structures, and messages associated with waveform audio, which are documented under [Multimedia Reference](multimedia-reference.md). These elements are grouped as follows.

## Auxiliary Devices

-   [**AUXCAPS**](/windows/win32/api/mmeapi/ns-mmeapi-auxcaps)
-   [**auxGetDevCaps**](/windows/win32/api/mmeapi/nf-mmeapi-auxgetdevcaps)
-   [**auxGetNumDevs**](/windows/win32/api/mmeapi/nf-mmeapi-auxgetnumdevs)
-   [**auxGetVolume**](/windows/win32/api/mmeapi/nf-mmeapi-auxgetvolume)
-   [**auxOutMessage**](/windows/win32/api/mmeapi/nf-mmeapi-auxoutmessage)
-   [**auxSetVolume**](/windows/win32/api/mmeapi/nf-mmeapi-auxsetvolume)

## Easy Playback

-   [**PlaySound**](/previous-versions//dd743680(v=vs.85))
-   [**sndPlaySound**](/previous-versions//dd798676(v=vs.85))

## Errors

-   [**waveInGetErrorText**](/windows/win32/api/mmeapi/nf-mmeapi-waveingeterrortext)
-   [**waveOutGetErrorText**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutgeterrortext)

## Opening and Closing

-   [**PCMWAVEFORMAT**](/windows/win32/api/mmreg/ns-mmreg-pcmwaveformat)
-   [**MM\_WIM\_CLOSE**](mm-wim-close.md)
-   [**MM\_WIM\_OPEN**](mm-wim-open.md)
-   [**MM\_WOM\_CLOSE**](mm-wom-close.md)
-   [**MM\_WOM\_OPEN**](mm-wom-open.md)
-   [**WAVEFORMAT**](/windows/win32/api/mmreg/ns-mmreg-waveformat)
-   [**WAVEFORMATEX**](/windows/win32/api/mmeapi/ns-mmeapi-waveformatex)
-   [**waveInClose**](/windows/win32/api/mmeapi/nf-mmeapi-waveinclose)
-   [**waveInProc**](/previous-versions//dd743849(v=vs.85))
-   [**waveInOpen**](/windows/win32/api/mmeapi/nf-mmeapi-waveinopen)
-   [**waveOutClose**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutclose)
-   [**waveOutProc**](/previous-versions//dd743869(v=vs.85))
-   [**waveOutOpen**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutopen)
-   [**WIM\_CLOSE**](wim-close.md)
-   [**WIM\_OPEN**](wim-open.md)
-   [**WOM\_CLOSE**](wom-close.md)
-   [**WOM\_OPEN**](wom-open.md)

## Pitch

-   [**waveOutGetPitch**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutgetpitch)
-   [**waveOutSetPitch**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutsetpitch)

## Playback Rate

-   [**waveOutGetPlaybackRate**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutgetplaybackrate)
-   [**waveOutSetPlaybackRate**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutsetplaybackrate)

## Playback Progress

-   [**MM\_WOM\_DONE**](mm-wom-done.md)
-   [**waveOutBreakLoop**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutbreakloop)
-   [**waveOutPause**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutpause)
-   [**waveOutReset**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutreset)
-   [**waveOutRestart**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutrestart)
-   [**WOM\_DONE**](wom-done.md)

## Playing

-   [**MM\_WOM\_DONE**](mm-wom-done.md)
-   [**WAVEHDR**](/windows/win32/api/mmeapi/ns-mmeapi-wavehdr)
-   [**waveOutPrepareHeader**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutprepareheader)
-   [**waveOutUnprepareHeader**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutunprepareheader)
-   [**waveOutWrite**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutwrite)
-   [**WOM\_DONE**](wom-done.md)

## Querying a Device

-   [**WAVEINCAPS**](/windows/win32/api/mmeapi/ns-mmeapi-waveincaps)
-   [**waveInGetDevCaps**](/windows/win32/api/mmeapi/nf-mmeapi-waveingetdevcaps)
-   [**waveInGetNumDevs**](/windows/win32/api/mmeapi/nf-mmeapi-waveingetnumdevs)
-   [**WAVEOUTCAPS**](/windows/win32/api/mmeapi/ns-mmeapi-waveoutcaps)
-   [**waveOutGetDevCaps**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutgetdevcaps)
-   [**waveOutGetNumDevs**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutgetnumdevs)

## Recording

-   [**MM\_WIM\_DATA**](mm-wim-data.md)
-   [**waveInAddBuffer**](/windows/win32/api/mmeapi/nf-mmeapi-waveinaddbuffer)
-   [**waveInPrepareHeader**](/windows/win32/api/mmeapi/nf-mmeapi-waveinprepareheader)
-   [**waveInReset**](/windows/win32/api/mmeapi/nf-mmeapi-waveinreset)
-   [**waveInStart**](/windows/win32/api/mmeapi/nf-mmeapi-waveinstart)
-   [**waveInStop**](/windows/win32/api/mmeapi/nf-mmeapi-waveinstop)
-   [**waveInUnprepareHeader**](/windows/win32/api/mmeapi/nf-mmeapi-waveinunprepareheader)
-   [**WIM\_DATA**](wim-data.md)

## Retrieving Device Identifiers

-   [**waveInGetID**](/windows/win32/api/mmeapi/nf-mmeapi-waveingetid)
-   [**waveOutGetID**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutgetid)

## Retrieving the Current Position

-   [**waveInGetPosition**](/windows/win32/api/mmeapi/nf-mmeapi-waveingetposition)
-   [**waveOutGetPosition**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutgetposition)

## Sending Custom Messages

-   [**waveInMessage**](/windows/win32/api/mmeapi/nf-mmeapi-waveinmessage)
-   [**waveOutMessage**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutmessage)

## Volume

-   [**waveOutGetVolume**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutgetvolume)
-   [**waveOutSetVolume**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutsetvolume)

## Related topics

<dl> <dt>

[Waveform Audio](waveform-audio.md)
</dt> </dl>

 

 