---
title: Managing Waveform-Audio Recording
description: Managing Waveform-Audio Recording
ms.assetid: a44f7c33-54d6-4ba7-bc57-b63c8b205392
keywords:
- waveform audio,recording
- waveform-audio interface,recording
- recording waveform audio,about
- WAVEHDR structure
- waveInAddBuffer function
ms.topic: article
ms.date: 05/31/2018
---

# Managing Waveform-Audio Recording

After you open a waveform-audio input device, you can begin recording waveform-audio data. Waveform-audio data is recorded into application-supplied buffers specified by a [**WAVEHDR**](/windows/win32/api/mmeapi/ns-mmeapi-wavehdr) structure. These data blocks must be prepared before they are used; for more information, see [Audio Data Blocks](audio-data-blocks.md).

Windows provides the following functions to manage waveform-audio recording.



| Function                                   | Description                                                                                |
|--------------------------------------------|--------------------------------------------------------------------------------------------|
| [**waveInAddBuffer**](/windows/win32/api/mmeapi/nf-mmeapi-waveinaddbuffer) | Sends a buffer to the device driver so it can be filled with recorded waveform-audio data. |
| [**waveInReset**](/windows/win32/api/mmeapi/nf-mmeapi-waveinreset)         | Stops waveform-audio recording and marks all pending buffers as done.                      |
| [**waveInStart**](/windows/win32/api/mmeapi/nf-mmeapi-waveinstart)         | Starts waveform-audio recording.                                                           |
| [**waveInStop**](/windows/win32/api/mmeapi/nf-mmeapi-waveinstop)           | Stops waveform-audio recording.                                                            |



 

Use the [**waveInAddBuffer**](/windows/win32/api/mmeapi/nf-mmeapi-waveinaddbuffer) function to send buffers to the device driver. As the buffers are filled with recorded waveform-audio data, the application is notified with a window message, callback message, thread message, or event, depending on the flag specified when the device was opened.

Before you begin recording by using [**waveInStart**](/windows/win32/api/mmeapi/nf-mmeapi-waveinstart), you should send at least one buffer to the driver, or incoming data could be lost.

Before closing the device using [**waveInClose**](/windows/win32/api/mmeapi/nf-mmeapi-waveinclose), call [**waveInReset**](/windows/win32/api/mmeapi/nf-mmeapi-waveinreset) to mark any pending data blocks as being done.

## Related topics

<dl> <dt>

[Recording Waveform Audio](recording-waveform-audio.md)
</dt> </dl>

 

 