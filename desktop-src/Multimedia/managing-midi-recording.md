---
title: Managing MIDI Recording
description: Managing MIDI Recording
ms.assetid: '48b2d815-72cf-4c96-8d93-247d2426b8f2'
keywords: ["Musical Instrument Digital Interface (MIDI),recording", "MIDI (Musical Instrument Digital Interface),recording", "recording MIDI audio,managing", "MIDI recording"]
---

# Managing MIDI Recording

After you open a MIDI device, you can begin recording MIDI data. Windows provides the following functions for managing MIDI recording.



| Value                                      | Meaning                                                                                           |
|--------------------------------------------|---------------------------------------------------------------------------------------------------|
| [**midiInAddBuffer**](midiinaddbuffer.md) | Sends a buffer to the device driver so it can be filled with recorded system-exclusive MIDI data. |
| [**midiInReset**](midiinreset.md)         | Stops MIDI recording and marks all pending buffers as done.                                       |
| [**midiInStart**](midiinstart.md)         | Starts MIDI recording and resets the time stamp to zero.                                          |
| [**midiInStop**](midiinstop.md)           | Stops MIDI recording.                                                                             |



 

To send buffers to the device driver for recording system-exclusive messages, use [**midiInAddBuffer**](midiinaddbuffer.md). The application is notified as the buffers are filled with system-exclusive recorded data. For more information about the notification techniques, see [Managing MIDI Data Blocks](managing-midi-data-blocks.md).

The [**midiInStart**](midiinstart.md) function begins the recording process. When recording system-exclusive messages, send at least one buffer to the driver before starting recording. To stop recording, use [**midiInStop**](midiinstop.md). Before closing the device by using the [**midiInClose**](midiinclose.md) function, mark any pending data blocks as being done by calling [**midiInReset**](midiinreset.md).

Applications that require time-stamped data use a callback function to receive MIDI data. If your timing requirements are not strict, you can use a window or thread callback. However, you cannot use an event callback to receive MIDI data.

To record system-exclusive messages with applications that do not use stream buffers, you must supply the device driver with buffers. These buffers are specified by using a [**MIDIHDR**](midihdr.md) structure.

## Related topics

<dl> <dt>

[Recording MIDI Audio](recording-midi-audio.md)
</dt> </dl>

 

 




