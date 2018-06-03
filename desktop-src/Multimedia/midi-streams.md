---
title: MIDI Streams
description: MIDI Streams
ms.assetid: 622472d9-2888-407f-bdaa-4943896c0bac
keywords:
- Musical Instrument Digital Interface (MIDI),streams
- MIDI (Musical Instrument Digital Interface),streams
- stream buffers,MIDI streams
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MIDI Streams

MIDI events occur in the context of a stream of MIDI data. Although an application can use several streams to define musical data, the MIDI mapper does not recognize multiple streams. Most applications that use streams use a single MIDI stream.

The following functions work with streams.



| Value                                            | Meaning                                                                 |
|--------------------------------------------------|-------------------------------------------------------------------------|
| [**midiStreamClose**](https://www.bing.com/search?q=**midiStreamClose**)       | Closes a MIDI stream.                                                   |
| [**midiStreamOpen**](https://www.bing.com/search?q=**midiStreamOpen**)         | Opens a MIDI stream and retrieves a handle.                             |
| [**midiStreamOut**](https://www.bing.com/search?q=**midiStreamOut**)           | Plays or queues a stream (buffer) of MIDI data to a MIDI output device. |
| [**midiStreamPause**](https://www.bing.com/search?q=**midiStreamPause**)       | Pauses playback of a specified MIDI stream.                             |
| [**midiStreamPosition**](https://www.bing.com/search?q=**midiStreamPosition**) | Retrieves the current position in a MIDI stream.                        |
| [**midiStreamProperty**](https://www.bing.com/search?q=**midiStreamProperty**) | Sets and retrieves stream properties.                                   |
| [**midiStreamRestart**](https://www.bing.com/search?q=**midiStreamRestart**)   | Restarts playback of a paused MIDI stream.                              |
| [**midiStreamStop**](https://www.bing.com/search?q=**midiStreamStop**)         | Turns off all notes on all MIDI channels for the specified MIDI stream. |



 

 

 




