---
title: Allocating and Preparing MIDI Data Blocks
description: Allocating and Preparing MIDI Data Blocks
ms.assetid: b3a70441-e8f9-4886-bf22-426ebd74d045
keywords:
- Musical Instrument Digital Interface (MIDI),allocating data blocks
- MIDI (Musical Instrument Digital Interface),allocating data blocks
- MIDI services,allocating data blocks
- allocating MIDI data blocks
- Musical Instrument Digital Interface (MIDI),preparing data blocks
- MIDI (Musical Instrument Digital Interface),preparing data blocks
- MIDI services,preparing data blocks
- preparing MIDI data blocks
- Musical Instrument Digital Interface (MIDI),data blocks
- MIDI (Musical Instrument Digital Interface),data blocks
- MIDI services,data blocks
ms.topic: article
ms.date: 05/31/2018
---

# Allocating and Preparing MIDI Data Blocks

The [**midiOutLongMsg**](/windows/win32/api/mmeapi/nf-mmeapi-midioutlongmsg), [**midiInAddBuffer**](/windows/win32/api/mmeapi/nf-mmeapi-midiinaddbuffer), and [**midiStreamOut**](/windows/win32/api/mmeapi/nf-mmeapi-midistreamout) functions require that applications to allocate data blocks to pass to the device drivers for playback or recording purposes. Each of these functions uses a [**MIDIHDR**](/windows/win32/api/mmeapi/ns-mmeapi-midihdr) structure to describe its data block.

Before you use one of these functions to pass a data block to a device driver, you must allocate memory for the buffer and the header structure that describes the data block.

Windows provides the following functions for preparing and cleaning up MIDI data blocks.



| Value                                                    | Meaning                                                |
|----------------------------------------------------------|--------------------------------------------------------|
| [**midiInPrepareHeader**](/windows/win32/api/mmeapi/nf-mmeapi-midiinprepareheader)       | Prepares a MIDI input data block.                      |
| [**midiInUnprepareHeader**](/windows/win32/api/mmeapi/nf-mmeapi-midiinunprepareheader)   | Cleans up the preparation of a MIDI input data block.  |
| [**midiOutPrepareHeader**](/windows/win32/api/mmeapi/nf-mmeapi-midioutprepareheader)     | Prepares a MIDI output data block.                     |
| [**midiOutUnprepareHeader**](/windows/win32/api/mmeapi/nf-mmeapi-midioutunprepareheader) | Cleans up the preparation of a MIDI output data block. |



 

Before you pass a MIDI data block to a device driver, you must prepare the buffer by passing it to the [**midiInPrepareHeader**](/windows/win32/api/mmeapi/nf-mmeapi-midiinprepareheader) or [**midiOutPrepareHeader**](/windows/win32/api/mmeapi/nf-mmeapi-midioutprepareheader) function. When the device driver is finished with the buffer and returns it, you must clean up this preparation by passing the buffer to the [**midiInUnprepareHeader**](/windows/win32/api/mmeapi/nf-mmeapi-midiinunprepareheader) or [**midiOutUnprepareHeader**](/windows/win32/api/mmeapi/nf-mmeapi-midioutunprepareheader) function before any allocated memory can be freed.

## Related topics

<dl> <dt>

[MIDI Services](midi-services.md)
</dt> </dl>

 

 