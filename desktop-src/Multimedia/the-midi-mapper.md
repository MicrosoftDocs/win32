---
title: The MIDI Mapper
description: The MIDI Mapper
ms.assetid: 92cffc67-b4a4-4807-94d2-02fbbdba5abf
keywords:
- Windows multimedia,MIDI Mapper
- multimedia,MIDI Mapper
- multimedia audio,MIDI Mapper
- audio,MIDI Mapper
- Musical Instrument Digital Interface (MIDI),MIDI Mapper
- MIDI (Musical Instrument Digital Interface),MIDI Mapper
- MIDI Mapper,about
- MIDI Mapper,source
- MIDI Mapper,destination
ms.topic: article
ms.date: 05/31/2018
---

# The MIDI Mapper

The MIDI Mapper's standard patch services provide device-independent MIDI file playback for applications. The MIDI Mapper can be used with the MCI MIDI sequencer or with low-level MIDI output services.

Unless stated otherwise, all references to MIDI channel numbers use the logical channel numbers 1 through 16. These logical channel numbers correspond to the physical channel numbers 0 through 15 that are actually part of the MIDI message. All references to MIDI program-change and key values use the physical values 0 through 127. All numbers are decimal unless preceded by "0x" prefix, in which case they are hexadecimal.

In the discussion of the MIDI Mapper, the term *source* refers to the input side of the MIDI Mapper. The term *destination* refers to the output side of the MIDI Mapper. For example, a source channel is the MIDI channel of a message sent to the MIDI Mapper, and a destination channel is the MIDI channel of a message sent from the MIDI Mapper to an output device.

-   [The MIDI Mapper and Windows](the-midi-mapper-and-windows.md)
-   [The MIDI Mapper Architecture](the-midi-mapper-architecture.md)
-   [The Channel Map](the-channel-map.md)
-   [Patch Maps](patch-maps.md)
-   [The Volume Scalar](the-volume-scalar.md)
-   [Key Maps](key-maps.md)
-   [Summary of Maps and MIDI Messages](summary-of-maps-and-midi-messages.md)

 

 




