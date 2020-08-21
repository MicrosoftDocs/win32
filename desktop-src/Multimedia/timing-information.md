---
title: Timing Information
description: Timing Information
ms.assetid: ff9d6fb2-1387-49ce-a4de-1b2f67353628
keywords:
- Musical Instrument Digital Interface (MIDI),timing information
- MIDI (Musical Instrument Digital Interface),timing information
- stream buffers,timing information
- MIDIEVENT structure
- stream buffers,SMPTE format
- stream buffers,quarter note time
- stream buffers,ticks
- SMPTE format
- quarter note time
- ticks
ms.topic: article
ms.date: 05/31/2018
---

# Timing Information

Timing information for a MIDI event is stored in the **dwDeltaTime** member of the [**MIDIEVENT**](/windows/win32/api/mmeapi/ns-mmeapi-midievent) structure. Time is given in ticks, as defined in the *Standard MIDI Files 1.0* specification. The length of a tick is defined by the time format and possibly the tempo associated with the stream. For more information about streams, see [MIDI Streams](midi-streams.md).

A tick is expressed either as microseconds per quarter note or as ticks of SMPTE (Society of Motion Picture and Television Engineers) time. Applications that send MIDI messages individually or use unprocessed MIDI messages use quarter note time and tempo information to determine the duration of a tick. Applications that preprocess MIDI messages can store the elapsed time as a count of the SMPTE units being used.

Quarter note time is indicated with a zero in the high-word bit (bit 15) of the time-division word. The remainder of the word contains the ticks per quarter note. A tempo associated with a stream of MIDI data is kept in units (microseconds per quarter note) consistent with the *Standard MIDI Files 1.0* specification. For example, a quarter note in 4/4 time that uses a tempo of 500,000 microseconds per quarter note plays at the rate of 120 beats per minute.

SMPTE time division formats completely specify the length of a tick without the need for tempo information. In using SMPTE time formats, MIDI sequences can be synchronized with other SMPTE events, such as video or striped audio. SMPTE time is indicated with a 1 in the high-order bit (bit 15) of the time-division word. The rest of the most-significant byte specifies the SMPTE format in use as negative values. The supported SMPTE formats and their corresponding values (in parentheses) are 24 (-24), 25 (-25), 30 (-30), and 30 drop (-29). The low byte of the time-division word specifies the number of ticks per SMPTE frame.

 

 