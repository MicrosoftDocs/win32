---
title: Using a Window or Thread to Manage Buffered Playback
description: Using a Window or Thread to Manage Buffered Playback
ms.assetid: 3c8145a8-e56a-449d-ad45-2ae016f79697
keywords:
- Musical Instrument Digital Interface (MIDI),buffered playback
- MIDI (Musical Instrument Digital Interface),buffered playback
- playing MIDI files,buffered playback
- buffered playback
- MM_MOM_CLOSE message
- MM_MOM_DONE message
- MM_MOM_OPEN message
- Musical Instrument Digital Interface (MIDI),sending messages
- MIDI (Musical Instrument Digital Interface),sending messages
- playing MIDI files,sending messages
- sending MIDI messages
ms.topic: article
ms.date: 05/31/2018
---

# Using a Window or Thread to Manage Buffered Playback

The following messages can be sent to a window or thread for managing playback of MIDI system-exclusive messages or stream buffers.



| Value                                  | Meaning                                                                                                                                                                  |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MM\_MOM\_CLOSE**](mm-mom-close.md) | Sent when the device is closed by using the [**midiOutClose**](/windows/win32/api/mmeapi/nf-mmeapi-midioutclose) function.                                                                               |
| [**MM\_MOM\_DONE**](mm-mom-done.md)   | Sent when the device driver is finished with a data block sent by using the [**midiOutLongMsg**](/windows/win32/api/mmeapi/nf-mmeapi-midioutlongmsg) or [**midiStreamOut**](/windows/win32/api/mmeapi/nf-mmeapi-midistreamout) function. |
| [**MM\_MOM\_OPEN**](mm-mom-open.md)   | Sent when the device is opened by using the [**midiOutOpen**](/windows/win32/api/mmeapi/nf-mmeapi-midioutopen) function.                                                                                 |



 

A *wParam* parameter and an *lParam* parameter are associated with each of these messages. The *wParam* parameter always specifies the handle of an open MIDI device. For [**MM\_MOM\_DONE**](mm-mom-done.md), *lParam* specifies an address of a [**MIDIHDR**](/windows/win32/api/mmeapi/ns-mmeapi-midihdr) structure identifying the completed data block. The *lParam* parameter is unused for [**MM\_MOM\_CLOSE**](mm-mom-close.md) and [**MM\_MOM\_OPEN**](mm-mom-open.md).

The most useful message is probably MM\_MOM\_DONE. Unless you need to allocate memory or initialize variables, you probably do not need to process MM\_MOM\_OPEN and MM\_MOM\_CLOSE. When playback of a data block is complete, you can clean up and free the data block.

 

 