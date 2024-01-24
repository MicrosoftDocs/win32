---
title: About Waveform Audio
description: About Waveform Audio
ms.assetid: 2d886488-bdab-4422-b89e-15140d86fe48
keywords:
- Windows multimedia,waveform audio
- multimedia,waveform audio
- multimedia audio,waveform
- audio,waveform
- waveform audio,about
- multimedia audio,PlaySound function
- audio,PlaySound function
- waveform audio,PlaySound function
- PlaySound function,about
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# About Waveform Audio

\[The feature associated with this page, [Waveform Audio](/windows/win32/multimedia/waveform-audio), is a legacy feature. It has been superseded by [WASAPI](/windows/win32/coreaudio/wasapi) and [Audio Graphs](/windows/uwp/audio-video-camera/audio-graphs). **WASAPI** and **Audio Graphs** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **WASAPI** and **Audio Graphs** instead of **Waveform Audio**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

There are several methods for adding sound to your application using waveform audio. The simplest method documented here is that of using the [**PlaySound**](/previous-versions//dd743680(v=vs.85)) function. Most of the other waveform-audio API elements are relatively low-level.

For more information, see the following topics:

-   [Simple Audio Playback](simple-audio-playback.md)
-   [Waveform-Audio Interface](waveform-audio-interface.md)
-   [Auxiliary Audio Interface](auxiliary-audio-interface.md)
-   [Audio Data Blocks](audio-data-blocks.md)
-   [Handling Errors with Audio Functions](handling-errors-with-audio-functions.md)

In addition to the APIs discussed here, the Media Control Interface can be used to play waveform audio as well as other media such as MIDI sounds and video. For more information, see [MCI](mci.md).

 

 