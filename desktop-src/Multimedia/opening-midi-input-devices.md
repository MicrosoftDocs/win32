---
title: Opening MIDI Input Devices
description: Opening MIDI Input Devices
ms.assetid: fd6ebd0c-6985-49d3-8015-a636d4c70ff3
keywords:
- Musical Instrument Digital Interface (MIDI),input devices
- MIDI (Musical Instrument Digital Interface),input devices
- recording MIDI audio,input devices
- MIDI input devices
- Musical Instrument Digital Interface (MIDI),opening input devices
- MIDI (Musical Instrument Digital Interface),opening input devices
- recording MIDI audio,opening input devices
- opening MIDI input devices
ms.topic: article
ms.date: 05/31/2018
---

# Opening MIDI Input Devices

To open a MIDI input device for recording, use the [**midiInOpen**](/windows/win32/api/mmeapi/nf-mmeapi-midiinopen) function. This function opens the device associated with the specified device identifier and returns a handle of the open device by writing the handle to a specified memory location.

If you use the MIDI\_IO\_STATUS flag with **midiInOpen**, the system uses the [**MIM\_MOREDATA**](mim-moredata.md) message to alert your application's callback function when it is not processing MIDI data fast enough to keep up with the input device driver. (The [**MM\_MIM\_MOREDATA**](mm-mim-moredata.md) message does the same job with window callbacks. However, for performance reasons, most applications will use callback functions instead of window callbacks.) If your application processes MIDI data in a separate thread, boosting the thread's priority can have a significant impact on the application's ability to keep up with the data flow.

## Related topics

<dl> <dt>

[Recording MIDI Audio](recording-midi-audio.md)
</dt> </dl>

 

 