---
title: Using PlaySound to Play System Sounds
description: Using PlaySound to Play System Sounds
ms.assetid: b645c488-8b76-4886-8909-75f0342263db
keywords:
- waveform audio,PlaySound function
- waveform audio,playing system sounds
- waveform audio,sound events
- PlaySound function,playing system sounds
- PlaySound function,sound events
- playing waveform-audio system sounds
- sound events
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Using PlaySound to Play System Sounds

\[The feature associated with this page, [Waveform Audio](/windows/win32/multimedia/waveform-audio), is a legacy feature. It has been superseded by [WASAPI](/windows/win32/coreaudio/wasapi) and [Audio Graphs](/windows/uwp/audio-video-camera/audio-graphs). **WASAPI** and **Audio Graphs** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **WASAPI** and **Audio Graphs** instead of **Waveform Audio**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The [**PlaySound**](/previous-versions//dd743680(v=vs.85)) function will also play sounds referred to by a keyname in the registry. Users can assign their own sounds to system alerts and warnings, or to user actions, such as a mouse button click. Sounds that are associated with system alerts and warnings are called *sound events*.

To play a sound event, call **PlaySound** with the *pszSound* parameter pointing to a string containing the name of the registry entry that identifies the sound. For example, to play the sound associated with the "MouseClick" entry and to wait for the sound to complete before returning, use the following statement:


```C++
PlaySound("MouseClick", NULL, SND_SYNC); 
```



If the specified registry entry or the waveform-audio file it identifies does not exist, or if the file does not fit into the available memory, **PlaySound** plays the default system sound.

The sound events that are predefined by the system can vary with the platform. The following list gives the sound events that are defined for all implementations of the Win32 API:

-   SystemAsterisk
-   SystemExclamation
-   SystemExit
-   SystemHand
-   SystemQuestion
-   SystemStart

If an application registers its own sound events, the user can configure the sound event by using the standard Control Panel interface. The application should register the sound event by using the standard registry functions; for more information, see [Registry](../sysinfo/registry.md). The entries belong at the same position in the registry hierarchy as the rest of the sound events. This position varies with the Win32 implementation. The appropriate data value also varies with the implementation.

The [**sndPlaySound**](/previous-versions//dd798676(v=vs.85)) function always searches the registry for a keyname matching *lpszSound* before attempting to load a file with this name. The [**PlaySound**](/previous-versions//dd743680(v=vs.85)) function accepts flags that specify the location of the sound.

 

 