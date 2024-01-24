---
title: Stopping, Pausing, and Restarting Playback
description: Stopping, Pausing, and Restarting Playback
ms.assetid: 39751342-63bc-4e68-bf9e-38665db8a05c
keywords:
- waveform audio,stopping playback
- waveform-audio interface,stopping playback
- playing waveform-audio files,stopping playback
- waveform audio,pausing playback
- waveform-audio interface,pausing playback
- playing waveform-audio files,pausing playback
- waveform audio,restarting playback
- waveform-audio interface,restarting playback
- playing waveform-audio files,restarting playback
- waveOutPause function
- waveOutReset function
- waveOutRestart function
- stopping waveform-audio playback
- pausing waveform-audio playback
- restarting waveform-audio playback
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Stopping, Pausing, and Restarting Playback

\[The feature associated with this page, [Waveform Audio](/windows/win32/multimedia/waveform-audio), is a legacy feature. It has been superseded by [WASAPI](/windows/win32/coreaudio/wasapi) and [Audio Graphs](/windows/uwp/audio-video-camera/audio-graphs). **WASAPI** and **Audio Graphs** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **WASAPI** and **Audio Graphs** instead of **Waveform Audio**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You can stop or pause playback while waveform audio is playing. After playback has been paused, you can restart it. Windows provides the following functions for controlling waveform-audio playback.



| Function                                 | Description                                                                                 |
|------------------------------------------|---------------------------------------------------------------------------------------------|
| [**waveOutPause**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutpause)     | Pauses playback on a waveform-audio output device.                                          |
| [**waveOutReset**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutreset)     | Stops playback on a waveform-audio output device and marks all pending data blocks as done. |
| [**waveOutRestart**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutrestart) | Resumes playback on a paused waveform-audio output device.                                  |



 

Pausing a waveform-audio device by using [**waveOutPause**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutpause) might not be instantaneous; the driver may finish playing the current block before pausing playback.

Generally, as soon as the first waveform-audio data block is sent by using the [**waveOutWrite**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutwrite) function, the waveform-audio device begins playing. If you do not want the sound to start playing immediately, call **waveOutPause** before calling **waveOutWrite**. Then, when you want to begin playing waveform-audio data, call [**waveOutRestart**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutrestart).

You cannot use **waveOutRestart** to restart a device that has been stopped with [**waveOutReset**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutreset); you must use **waveOutWrite** to send the first data block to resume playback on the device.

 

 