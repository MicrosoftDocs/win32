---
title: Using Window Messages to Manage Waveform-Audio Recording
description: Using Window Messages to Manage Waveform-Audio Recording
ms.assetid: 65637d51-9d30-48db-8681-48332442130e
keywords:
- waveform audio,managing recording with messages
- waveform-audio interface,managing recording with messages
- recording waveform audio,managing recording with messages
- waveform audio,messages
- waveform-audio interface,messages
- recording waveform audio,messages
- MM_WIM_CLOSE message
- MM_WIM_DATA message
- MM_WIM_OPEN message
ms.topic: article
ms.date: 05/31/2018
---

# Using Window Messages to Manage Waveform-Audio Recording

The following messages can be sent to a window procedure function for managing waveform-audio recording.



| Message                                | Description                                                                                                                  |
|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| [**MM\_WIM\_CLOSE**](mm-wim-close.md) | Sent when the device is closed by using the [**waveInClose**](/windows/win32/api/mmeapi/nf-mmeapi-waveinclose) function.                                     |
| [**MM\_WIM\_DATA**](mm-wim-data.md)   | Sent when the device driver is finished with a buffer sent by using the [**waveInAddBuffer**](/windows/win32/api/mmeapi/nf-mmeapi-waveinaddbuffer) function. |
| [**MM\_WIM\_OPEN**](mm-wim-open.md)   | Sent when the device is opened by using the [**waveInOpen**](/windows/win32/api/mmeapi/nf-mmeapi-waveinopen) function.                                       |



 

The *lParam* parameter of [**MM\_WIM\_DATA**](mm-wim-data.md) specifies a pointer to a [**WAVEHDR**](/windows/win32/api/mmeapi/ns-mmeapi-wavehdr) structure that identifies the buffer. This buffer might not be completely filled with waveform-audio data; recording can stop before the buffer is filled. Use the **dwBytesRecorded** member of the **WAVEHDR** structure to determine the amount of valid data present in the buffer.

The most useful message is probably [**MM\_WIM\_DATA**](mm-wim-data.md). When your application finishes using the data block sent by the device driver, you can clean up and free the data block. Unless you need to allocate memory or initialize variables, you probably do not need to use the [**MM\_WIM\_OPEN**](mm-wim-open.md) and [**MM\_WIM\_CLOSE**](mm-wim-close.md) messages.

The callback function for waveform-audio input devices is supplied by the application. For information about this callback function, see the [**waveInProc**](/previous-versions//dd743849(v=vs.85)) function.

## Related topics

<dl> <dt>

[Recording Waveform Audio](recording-waveform-audio.md)
</dt> </dl>

 

 