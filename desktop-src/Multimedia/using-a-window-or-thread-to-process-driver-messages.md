---
title: Using a Window or Thread to Process Driver Messages
description: Using a Window or Thread to Process Driver Messages
ms.assetid: 7a9eaaa1-d3b0-400e-8fbf-ee5fe59efc32
keywords:
- waveform audio,window callback
- audio data blocks,window callback
- waveform audio,thread callback
- audio data blocks,thread callback
- waveform audio,processing driver messages
- audio data blocks,processing driver messages
- processing driver messages
- waveInOpen function
- waveOutOpen function
ms.topic: article
ms.date: 05/31/2018
---

# Using a Window or Thread to Process Driver Messages

To use a window callback function, specify the CALLBACK\_WINDOW flag in the *fdwOpen* parameter and a window handle in the low-order word of the *dwCallback* parameter of the [**waveInOpen**](/windows/win32/api/mmeapi/nf-mmeapi-waveinopen) or [**waveOutOpen**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutopen) function. Driver messages will be sent to the window procedure for the window identified by the handle in *dwCallback*.

Similarly, to use a thread callback, specify CALLBACK\_THREAD and a thread handle in the call to **waveInOpen** or **waveOutOpen**. In this case, messages are posted to the specified thread instead of to a window.

Messages sent to the window or thread callback are specific to the audio device type used. For more information about these messages, see [Playing Waveform-Audio Files](playing-waveform-audio-files.md).

 

 