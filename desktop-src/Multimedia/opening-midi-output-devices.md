---
title: Opening MIDI Output Devices
description: Opening MIDI Output Devices
ms.assetid: 0a06611b-c0cd-4884-bc17-761c4aec4418
keywords:
- Musical Instrument Digital Interface (MIDI),output devices
- MIDI (Musical Instrument Digital Interface),output devices
- playing MIDI files,output devices
- MIDI output devices
- Musical Instrument Digital Interface (MIDI),opening output devices
- MIDI (Musical Instrument Digital Interface),opening output devices
- playing MIDI files,opening output devices
- opening MIDI output devices
ms.topic: article
ms.date: 05/31/2018
---

# Opening MIDI Output Devices

To open a MIDI output device for playback, use the [**midiOutOpen**](/windows/win32/api/mmeapi/nf-mmeapi-midioutopen) function. This function opens the device associated with the specified device identifier and returns a handle of the open device by writing the handle to a specified memory location.

One of the parameters of **midiOutOpen** is a doubleword value. This value specifies a window or thread handle, an event handle, or the address of a callback function that is used to monitor the progress of the playback of MIDI system-exclusive data and stream buffers. Monitoring enables the application to determine when to send additional data blocks and when to free data blocks that have been sent. For more information about these methods, see [Managing MIDI Data Blocks](managing-midi-data-blocks.md).

 

 