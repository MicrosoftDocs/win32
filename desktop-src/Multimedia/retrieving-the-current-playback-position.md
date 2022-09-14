---
title: Retrieving the Current Playback Position
description: Retrieving the Current Playback Position
ms.assetid: a08fe5da-8945-486f-9413-877c7d13d5de
keywords:
- waveform audio,current playback position
- waveform-audio interface,current playback position
- playing waveform-audio files,current playback position
- waveOutGetPosition function
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving the Current Playback Position

You can monitor the current playback position within the file while waveform audio is playing by using the [**waveOutGetPosition**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutgetposition) function.

For waveform-audio devices, samples are the preferred time format in which to represent the current position. Thus, the current position of a waveform-audio device is specified as the number of samples for one channel from the beginning of the waveform-audio file. To query the current position of a waveform-audio device, set the **wType** member of the [**MMTIME**](/previous-versions//dd757347(v=vs.85)) structure to TIME\_SAMPLES and pass this structure to **waveOutGetPosition**.

The **MMTIME** structure can represent time in one or more different formats, including milliseconds, samples, SMPTE (Society of Motion Picture and Television Engineers), and MIDI song pointer formats. The **wType** member specifies the format used to represent time. Before calling a function that uses the **MMTIME** structure, you must set **wType** to indicate your requested time format. Be sure to check **wType** after the call to see whether the requested time format is supported. If the requested time format is not supported, the device driver specifies the time in an alternate time format and changes the **wType** member to the selected time format.

For more information about the **MMTIME** structure, see [Multimedia Timers](multimedia-timers.md).

 

 