---
title: Processing MIDI Data from Two MIDI Sources
description: Processing MIDI Data from Two MIDI Sources
ms.assetid: d8b605d9-a12a-4830-8f29-ea700aefb41d
keywords:
- Windows multimedia,processing MIDI data from two sources
- multimedia,processing MIDI data from two sources
- multimedia audio,processing MIDI data from two sources
- audio,processing MIDI data from two sources
- Musical Instrument Digital Interface (MIDI),processing data from two sources
- MIDI (Musical Instrument Digital Interface),processing data from two sources
- processing MIDI data from two sources
ms.topic: article
ms.date: 05/31/2018
---

# Processing MIDI Data from Two MIDI Sources

The MIDI subsystem can route MIDI messages from two data sources to a single MIDI output device for concurrent playback. For example, one source can be background music or a bass line that has been pre-recorded and stored in a file. The second source can be live data from a MIDI instrument, such as a keyboard or guitar.

Both data sources send MIDI data to a single MIDI device that is identified with one handle. Send one data stream by using the [**midiStreamOut**](/windows/win32/api/mmeapi/nf-mmeapi-midistreamout) function and one or more stream buffers. This data stream typically contains prerecorded data that is packed into the buffer.

Send the second data stream (typically from a MIDI instrument) asynchronously by using the [**midiOutShortMsg**](/windows/win32/api/mmeapi/nf-mmeapi-midioutshortmsg) function. The running status of a stream buffer will not be adversely affected by the asynchronous calls made by the second data stream.

Each short message sent with **midiOutShortMsg** must be a complete MIDI message, with a status byte and the appropriate number of data bytes. If the status byte is omitted, **midiOutShortMsg** returns an error. (However, there is no running status with stream output.)

 

 