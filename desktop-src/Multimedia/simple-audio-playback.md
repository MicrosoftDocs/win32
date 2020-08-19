---
title: Simple Audio Playback
description: Simple Audio Playback
ms.assetid: 51a0244d-123d-4efe-92e9-972e914cef78
keywords:
- multimedia audio,waveform
- audio,waveform
- waveform audio,simple playback
- MessageBeep function
- sndPlaySound function
- PlaySound function,simple playback
- multimedia audio,PlaySound function
- audio,PlaySound function
- waveform audio,PlaySound function
ms.topic: article
ms.date: 05/31/2018
---

# Simple Audio Playback

You can use the following functions to play waveform audio in your application in a single function call.



| Function                                                      | Description                                                                                                         |
|---------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| [MessageBeep](/windows/win32/api/winuser/nf-winuser-messagebeep) | Plays the sound that corresponds to a specified system-alert level.                                                 |
| [**sndPlaySound**](/previous-versions//dd798676(v=vs.85))                          | Plays the sound that corresponds to the system sound entered in the registry or the contents of the specified file. |
| [**PlaySound**](/previous-versions//dd743680(v=vs.85))                                | Provides all the functionality of [**sndPlaySound**](/previous-versions//dd798676(v=vs.85)) and can directly access resources.           |



 

The **MessageBeep** function is a standard part of the Win32 API; because its capabilities are very limited and it is documented elsewhere, it is not discussed here.

The functions listed support the following sources of waveform audio:

-   Waveform-audio files associated with system-alert levels
-   Waveform-audio files specified by entries in the registry
-   In-memory WAVE resources
-   Waveform-audio files specified by name

The [**sndPlaySound**](/previous-versions//dd798676(v=vs.85)) and [**PlaySound**](/previous-versions//dd743680(v=vs.85)) functions load an entire waveform-audio file into memory and, in effect, limit the size of the file they can play. Use **sndPlaySound** and **PlaySound** to play waveform-audio files that are small — up to about 100K. These two functions also require the sound data to be in a format that is playable by one of the installed waveform-audio drivers, including the wave mapper.

For larger sound files, use the Media Control Interface (MCI) services. For more information, see [MCI](mci.md).

 

 