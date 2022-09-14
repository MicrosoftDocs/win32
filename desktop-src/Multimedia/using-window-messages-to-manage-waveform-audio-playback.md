---
title: Using Window Messages to Manage Waveform-Audio Playback
description: Using Window Messages to Manage Waveform-Audio Playback
ms.assetid: 217968fd-4bb3-405d-a371-c129e29637ab
keywords:
- waveform audio,managing playback with messages
- waveform-audio interface,managing playback with messages
- playing waveform-audio files,managing playback with messages
- waveform audio,messages
- waveform-audio interface,messages
- playing waveform-audio files,messages
- MM_WOM_CLOSE message
- MM_WOM_DONE message
- MM_WOM_OPEN message
ms.topic: article
ms.date: 05/31/2018
---

# Using Window Messages to Manage Waveform-Audio Playback

The following messages can be sent to a window procedure function for managing waveform-audio playback.



| Message                                | Description                                                                                                                |
|----------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [**MM\_WOM\_CLOSE**](mm-wom-close.md) | Sent when the device is closed by using the [**waveOutClose**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutclose) function.                                 |
| [**MM\_WOM\_DONE**](mm-wom-done.md)   | Sent when the device driver is finished with a data block sent by using the [**waveOutWrite**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutwrite) function. |
| [**MM\_WOM\_OPEN**](mm-wom-open.md)   | Sent when the device is opened by using the [**waveOutOpen**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutopen) function.                                   |



 

A *wParam* and *lParam* parameter is associated with each of these messages. The *wParam* parameter always specifies a handle of the open waveform-audio device. For the [**MM\_WOM\_DONE**](mm-wom-done.md) message, *lParam* specifies a pointer to a [**WAVEHDR**](/windows/win32/api/mmeapi/ns-mmeapi-wavehdr) structure that identifies the completed data block. The *lParam* parameter is unused for the [**MM\_WOM\_CLOSE**](mm-wom-close.md) and [**MM\_WOM\_OPEN**](mm-wom-open.md) messages.

The most useful message is probably MM\_WOM\_DONE. When this message signals that playback of a data block is complete, you can clean up and free the data block. Unless you need to allocate memory or initialize variables, you probably do not need to process the MM\_WOM\_OPEN and MM\_WOM\_CLOSE messages.

The callback function for waveform-audio output devices is supplied by the application. For information about this callback function, see the [**waveOutProc**](/previous-versions//dd743869(v=vs.85)) function.

 

 