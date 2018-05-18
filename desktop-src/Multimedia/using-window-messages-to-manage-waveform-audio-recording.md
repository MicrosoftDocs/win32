---
title: Using Window Messages to Manage Waveform-Audio Recording
description: Using Window Messages to Manage Waveform-Audio Recording
ms.assetid: '65637d51-9d30-48db-8681-48332442130e'
keywords: ["waveform audio,managing recording with messages", "waveform-audio interface,managing recording with messages", "recording waveform audio,managing recording with messages", "waveform audio,messages", "waveform-audio interface,messages", "recording waveform audio,messages", "MM_WIM_CLOSE message", "MM_WIM_DATA message", "MM_WIM_OPEN message"]
---

# Using Window Messages to Manage Waveform-Audio Recording

The following messages can be sent to a window procedure function for managing waveform-audio recording.



| Message                                | Description                                                                                                                  |
|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| [**MM\_WIM\_CLOSE**](mm-wim-close.md) | Sent when the device is closed by using the [**waveInClose**](waveinclose.md) function.                                     |
| [**MM\_WIM\_DATA**](mm-wim-data.md)   | Sent when the device driver is finished with a buffer sent by using the [**waveInAddBuffer**](waveinaddbuffer.md) function. |
| [**MM\_WIM\_OPEN**](mm-wim-open.md)   | Sent when the device is opened by using the [**waveInOpen**](waveinopen.md) function.                                       |



 

The *lParam* parameter of [**MM\_WIM\_DATA**](mm-wim-data.md) specifies a pointer to a [**WAVEHDR**](wavehdr.md) structure that identifies the buffer. This buffer might not be completely filled with waveform-audio data; recording can stop before the buffer is filled. Use the **dwBytesRecorded** member of the **WAVEHDR** structure to determine the amount of valid data present in the buffer.

The most useful message is probably [**MM\_WIM\_DATA**](mm-wim-data.md). When your application finishes using the data block sent by the device driver, you can clean up and free the data block. Unless you need to allocate memory or initialize variables, you probably do not need to use the [**MM\_WIM\_OPEN**](mm-wim-open.md) and [**MM\_WIM\_CLOSE**](mm-wim-close.md) messages.

The callback function for waveform-audio input devices is supplied by the application. For information about this callback function, see the [**waveInProc**](waveinproc.md) function.

## Related topics

<dl> <dt>

[Recording Waveform Audio](recording-waveform-audio.md)
</dt> </dl>

 

 




