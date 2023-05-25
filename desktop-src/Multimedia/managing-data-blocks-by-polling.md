---
title: Managing Data Blocks by Polling
description: Managing Data Blocks by Polling
ms.assetid: 0a517f1d-4993-49b8-be86-bc63e5687cba
keywords:
- waveform audio,polling data blocks
- audio data blocks,polling
- polling audio data blocks
- WAVEHDR structure
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Managing Data Blocks by Polling

\[The feature associated with this page, [Waveform Audio](/windows/win32/multimedia/waveform-audio), is a legacy feature. It has been superseded by [WASAPI](/windows/win32/coreaudio/wasapi) and [Audio Graphs](/windows/uwp/audio-video-camera/audio-graphs). **WASAPI** and **Audio Graphs** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **WASAPI** and **Audio Graphs** instead of **Waveform Audio**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

In addition to using a callback function, you can poll the **dwFlags** member of a [**WAVEHDR**](/windows/win32/api/mmeapi/ns-mmeapi-wavehdr) structure to determine when an audio device is finished with a data block. Sometimes it is better to poll **dwFlags** than to wait for another mechanism to receive messages from the drivers. For example, after you call the [**waveOutReset**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutreset) function to release pending data blocks, you can immediately poll to be sure that the data blocks have been released before calling [**waveOutUnprepareHeader**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutunprepareheader) and freeing the memory for the data block.

You can use the WHDR\_DONE flag to test the **dwFlags** member. As soon as the WHDR\_DONE flag is set in the **dwFlags** member of the **WAVEHDR** structure, the driver is finished with the data block.

 

 