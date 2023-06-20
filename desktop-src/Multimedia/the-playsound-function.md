---
title: The PlaySound Function
description: The PlaySound Function
ms.assetid: ce405a13-c4ab-4c9a-bcfe-8d4427b3d2d8
keywords:
- multimedia audio,PlaySound function
- audio,PlaySound function
- waveform audio,PlaySound function
- PlaySound function,about
- sndPlaySound function
- PlaySound function,compared to sndPlaySound function
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# The PlaySound Function

\[The feature associated with this page, [Waveform Audio](/windows/win32/multimedia/waveform-audio), is a legacy feature. It has been superseded by [WASAPI](/windows/win32/coreaudio/wasapi) and [Audio Graphs](/windows/uwp/audio-video-camera/audio-graphs). **WASAPI** and **Audio Graphs** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **WASAPI** and **Audio Graphs** instead of **Waveform Audio**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You can use the [**PlaySound**](/previous-versions//dd743680(v=vs.85)) function to play waveform audio if the sound fits into available memory. (The [**sndPlaySound**](/previous-versions//dd798676(v=vs.85)) function offers a subset of the capabilities of PlaySound. To maximize the portability of your Win32-based application, use **PlaySound**, not **sndPlaySound**.)

The **PlaySound** function allows you to specify a sound in one of three ways:

-   As a system alert, using the alias stored in the WIN.INI file or the registry
-   As a filename
-   As a resource identifier

The [**PlaySound**](/previous-versions//dd743680(v=vs.85)) function allows you to play a sound in a continuous loop, ending only when you call **PlaySound** again, specifying either **NULL** or the sound identifier of another sound for the *pszSound* parameter.

You can use **PlaySound** to play the sound synchronously or asynchronously, and to control the behavior of the function in other ways when it must share system resources.

For more information about using PlaySound, see the following topics:

-   [Using PlaySound to Play Waveform-Audio Files](using-playsound-to-play-waveform-audio-files.md)
-   [Using PlaySound to Loop Sounds](using-playsound-to-loop-sounds.md)
-   [Using PlaySound to Play System Sounds](using-playsound-to-play-system-sounds.md)

For more examples of how to use **PlaySound** in your Win32-based applications, see [Playing WAVE Resources](playing-wave-resources.md).

 

 