---
title: MIDI Streams
description: MIDI Streams
ms.assetid: '622472d9-2888-407f-bdaa-4943896c0bac'
keywords: ["Musical Instrument Digital Interface (MIDI),streams", "MIDI (Musical Instrument Digital Interface),streams", "stream buffers,MIDI streams"]
---

# MIDI Streams

MIDI events occur in the context of a stream of MIDI data. Although an application can use several streams to define musical data, the MIDI mapper does not recognize multiple streams. Most applications that use streams use a single MIDI stream.

The following functions work with streams.



| Value                                            | Meaning                                                                 |
|--------------------------------------------------|-------------------------------------------------------------------------|
| [**midiStreamClose**](midistreamclose.md)       | Closes a MIDI stream.                                                   |
| [**midiStreamOpen**](midistreamopen.md)         | Opens a MIDI stream and retrieves a handle.                             |
| [**midiStreamOut**](midistreamout.md)           | Plays or queues a stream (buffer) of MIDI data to a MIDI output device. |
| [**midiStreamPause**](midistreampause.md)       | Pauses playback of a specified MIDI stream.                             |
| [**midiStreamPosition**](midistreamposition.md) | Retrieves the current position in a MIDI stream.                        |
| [**midiStreamProperty**](midistreamproperty.md) | Sets and retrieves stream properties.                                   |
| [**midiStreamRestart**](midistreamrestart.md)   | Restarts playback of a paused MIDI stream.                              |
| [**midiStreamStop**](midistreamstop.md)         | Turns off all notes on all MIDI channels for the specified MIDI stream. |



 

 

 




