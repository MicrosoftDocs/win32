---
title: Stream Buffers
description: Stream Buffers
ms.assetid: 'd73209a3-4b9d-4405-9e62-8ecfb94c0bd5'
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
ms.topic: article
ms.date: 05/31/2018
---

# Stream Buffers

Applications can use stream buffers to send streams of MIDI events to a device. Each stream buffer is a block of memory pointed to by a [**MIDIHDR**](/windows/win32/api/mmeapi/ns-mmeapi-midihdr) structure. This block of memory contains data for one or more MIDI events, each of which is defined by a [**MIDIEVENT**](/windows/win32/api/mmeapi/ns-mmeapi-midievent) structure. An application controls the buffer by calling the stream-manipulation functions, such as [**midiStreamOpen**](/windows/win32/api/mmeapi/nf-mmeapi-midistreamopen), [**midiStreamOut**](/windows/win32/api/mmeapi/nf-mmeapi-midistreamout), and [**midiStreamClose**](/windows/win32/api/mmeapi/nf-mmeapi-midistreamclose).

-   [Stream Buffer Format](stream-buffer-format.md)
-   [Timing Information](timing-information.md)
-   [MIDI Event Types](midi-event-types.md)
-   [MIDI Streams](midi-streams.md)

 

 