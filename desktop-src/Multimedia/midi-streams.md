---
title: MIDI Streams
description: MIDI Streams
ms.assetid: 622472d9-2888-407f-bdaa-4943896c0bac
keywords:
- Musical Instrument Digital Interface (MIDI),streams
- MIDI (Musical Instrument Digital Interface),streams
- stream buffers,MIDI streams
ms.topic: article
ms.date: 05/31/2018
---

# MIDI Streams

MIDI events occur in the context of a stream of MIDI data. Although an application can use several streams to define musical data, the MIDI mapper does not recognize multiple streams. Most applications that use streams use a single MIDI stream.

The following functions work with streams.



| Value                                            | Meaning                                                                 |
|--------------------------------------------------|-------------------------------------------------------------------------|
| [**midiStreamClose**](/windows/win32/api/mmeapi/nf-mmeapi-midistreamclose)       | Closes a MIDI stream.                                                   |
| [**midiStreamOpen**](/windows/win32/api/mmeapi/nf-mmeapi-midistreamopen)         | Opens a MIDI stream and retrieves a handle.                             |
| [**midiStreamOut**](/windows/win32/api/mmeapi/nf-mmeapi-midistreamout)           | Plays or queues a stream (buffer) of MIDI data to a MIDI output device. |
| [**midiStreamPause**](/windows/win32/api/mmeapi/nf-mmeapi-midistreampause)       | Pauses playback of a specified MIDI stream.                             |
| [**midiStreamPosition**](/windows/win32/api/mmeapi/nf-mmeapi-midistreamposition) | Retrieves the current position in a MIDI stream.                        |
| [**midiStreamProperty**](/windows/win32/api/mmeapi/nf-mmeapi-midistreamproperty) | Sets and retrieves stream properties.                                   |
| [**midiStreamRestart**](/windows/win32/api/mmeapi/nf-mmeapi-midistreamrestart)   | Restarts playback of a paused MIDI stream.                              |
| [**midiStreamStop**](/windows/win32/api/mmeapi/nf-mmeapi-midistreamstop)         | Turns off all notes on all MIDI channels for the specified MIDI stream. |



 

 

 