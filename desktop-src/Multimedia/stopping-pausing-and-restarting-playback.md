---
title: Stopping, Pausing, and Restarting Playback
description: Stopping, Pausing, and Restarting Playback
ms.assetid: '39751342-63bc-4e68-bf9e-38665db8a05c'
keywords: ["waveform audio,stopping playback", "waveform-audio interface,stopping playback", "playing waveform-audio files,stopping playback", "waveform audio,pausing playback", "waveform-audio interface,pausing playback", "playing waveform-audio files,pausing playback", "waveform audio,restarting playback", "waveform-audio interface,restarting playback", "playing waveform-audio files,restarting playback", "waveOutPause function", "waveOutReset function", "waveOutRestart function", "stopping waveform-audio playback", "pausing waveform-audio playback", "restarting waveform-audio playback"]
---

# Stopping, Pausing, and Restarting Playback

You can stop or pause playback while waveform audio is playing. After playback has been paused, you can restart it. Windows provides the following functions for controlling waveform-audio playback.



| Function                                 | Description                                                                                 |
|------------------------------------------|---------------------------------------------------------------------------------------------|
| [**waveOutPause**](waveoutpause.md)     | Pauses playback on a waveform-audio output device.                                          |
| [**waveOutReset**](waveoutreset.md)     | Stops playback on a waveform-audio output device and marks all pending data blocks as done. |
| [**waveOutRestart**](waveoutrestart.md) | Resumes playback on a paused waveform-audio output device.                                  |



 

Pausing a waveform-audio device by using [**waveOutPause**](waveoutpause.md) might not be instantaneous; the driver may finish playing the current block before pausing playback.

Generally, as soon as the first waveform-audio data block is sent by using the [**waveOutWrite**](waveoutwrite.md) function, the waveform-audio device begins playing. If you do not want the sound to start playing immediately, call **waveOutPause** before calling **waveOutWrite**. Then, when you want to begin playing waveform-audio data, call [**waveOutRestart**](waveoutrestart.md).

You cannot use **waveOutRestart** to restart a device that has been stopped with [**waveOutReset**](waveoutreset.md); you must use **waveOutWrite** to send the first data block to resume playback on the device.

 

 




