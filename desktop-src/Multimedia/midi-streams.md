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
| [**midiStreamClose**](https://msdn.microsoft.com/library/Dd798485(v=VS.85).aspx)       | Closes a MIDI stream.                                                   |
| [**midiStreamOpen**](https://msdn.microsoft.com/library/Dd798486(v=VS.85).aspx)         | Opens a MIDI stream and retrieves a handle.                             |
| [**midiStreamOut**](https://msdn.microsoft.com/library/Dd798487(v=VS.85).aspx)           | Plays or queues a stream (buffer) of MIDI data to a MIDI output device. |
| [**midiStreamPause**](https://msdn.microsoft.com/library/Dd798488(v=VS.85).aspx)       | Pauses playback of a specified MIDI stream.                             |
| [**midiStreamPosition**](https://msdn.microsoft.com/library/Dd798489(v=VS.85).aspx) | Retrieves the current position in a MIDI stream.                        |
| [**midiStreamProperty**](https://msdn.microsoft.com/library/Dd798490(v=VS.85).aspx) | Sets and retrieves stream properties.                                   |
| [**midiStreamRestart**](https://msdn.microsoft.com/library/Dd798491(v=VS.85).aspx)   | Restarts playback of a paused MIDI stream.                              |
| [**midiStreamStop**](https://msdn.microsoft.com/library/Dd798492(v=VS.85).aspx)         | Turns off all notes on all MIDI channels for the specified MIDI stream. |



 

 

 




