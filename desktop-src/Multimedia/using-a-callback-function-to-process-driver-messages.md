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
ms.date: 05/31/2018
---

# Using a Callback Function to Process Driver Messages

You can write your own callback function to process messages sent by the device driver. To use a callback function, specify the CALLBACK\_FUNCTION flag in the *fdwOpen* parameter and the address of the callback in the *dwCallback* parameter of the [**waveInOpen**](/windows/win32/api/mmeapi/nf-mmeapi-waveinopen) or [**waveOutOpen**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutopen) function.

Messages sent to a callback function are similar to messages sent to a window, except they have two **DWORD** parameters instead of a **UINT** and a **DWORD** parameter. For details on these messages, see [Playing Waveform-Audio Files](playing-waveform-audio-files.md).

To pass instance data from an application to a callback function, use one of the following techniques:

-   Pass the instance data using the *dwInstance* parameter of the function that opens the device driver.
-   Pass the instance data using the **dwUser** member of the [**WAVEHDR**](/windows/win32/api/mmeapi/ns-mmeapi-wavehdr) structure that identifies an audio data block being sent to a device driver.

If you need more than 32 bits of instance data, pass a pointer to a structure containing the additional information.

 

 