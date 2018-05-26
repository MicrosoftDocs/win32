---
title: Stream Buffers
description: Stream Buffers
ms.assetid: f9e77637-098c-4ee8-bca9-a05ecce0c569
keywords:
- Windows multimedia,stream buffers
- multimedia,stream buffers
- multimedia audio,stream buffers
- audio,stream buffers
- Musical Instrument Digital Interface (MIDI),stream buffers
- MIDI (Musical Instrument Digital Interface),stream buffers
- stream buffers,about
- MIDIHDR structure
- MIDIEVENT structure
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Stream Buffers

Applications can use stream buffers to send streams of MIDI events to a device. Each stream buffer is a block of memory pointed to by a [**MIDIHDR**](midihdr.md) structure. This block of memory contains data for one or more MIDI events, each of which is defined by a [**MIDIEVENT**](midievent.md) structure. An application controls the buffer by calling the stream-manipulation functions, such as [**midiStreamOpen**](midistreamopen.md), [**midiStreamOut**](midistreamout.md), and [**midiStreamClose**](midistreamclose.md).

-   [Stream Buffer Format](stream-buffer-format.md)
-   [Timing Information](timing-information.md)
-   [MIDI Event Types](midi-event-types.md)
-   [MIDI Streams](midi-streams.md)

 

 




