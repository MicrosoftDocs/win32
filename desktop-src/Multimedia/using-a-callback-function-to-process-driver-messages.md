---
title: Using a Callback Function to Process Driver Messages
description: Using a Callback Function to Process Driver Messages
ms.assetid: 7fef400f-5040-4d33-9a2f-bb12aa9369e0
keywords:
- waveform audio,callback functions
- audio data blocks,callback functions
- waveform audio,processing driver messages
- audio data blocks,processing driver messages
- processing driver messages
- waveInOpen function
- waveOutOpen function
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Using a Callback Function to Process Driver Messages

\[The feature associated with this page, [Waveform Audio](/windows/win32/multimedia/waveform-audio), is a legacy feature. It has been superseded by [WASAPI](/windows/win32/coreaudio/wasapi) and [Audio Graphs](/windows/uwp/audio-video-camera/audio-graphs). **WASAPI** and **Audio Graphs** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **WASAPI** and **Audio Graphs** instead of **Waveform Audio**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You can write your own callback function to process messages sent by the device driver. To use a callback function, specify the CALLBACK\_FUNCTION flag in the *fdwOpen* parameter and the address of the callback in the *dwCallback* parameter of the [**waveInOpen**](/windows/win32/api/mmeapi/nf-mmeapi-waveinopen) or [**waveOutOpen**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutopen) function.

Messages sent to a callback function are similar to messages sent to a window, except they have two **DWORD** parameters instead of a **UINT** and a **DWORD** parameter. For details on these messages, see [Playing Waveform-Audio Files](playing-waveform-audio-files.md).

To pass instance data from an application to a callback function, use one of the following techniques:

-   Pass the instance data using the *dwInstance* parameter of the function that opens the device driver.
-   Pass the instance data using the **dwUser** member of the [**WAVEHDR**](/windows/win32/api/mmeapi/ns-mmeapi-wavehdr) structure that identifies an audio data block being sent to a device driver.

If you need more than 32 bits of instance data, pass a pointer to a structure containing the additional information.

 

 