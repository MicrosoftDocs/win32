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
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Allocating and Preparing MIDI Data Blocks

The [**midiOutLongMsg**](https://www.bing.com/search?q=**midiOutLongMsg**), [**midiInAddBuffer**](https://www.bing.com/search?q=**midiInAddBuffer**), and [**midiStreamOut**](https://www.bing.com/search?q=**midiStreamOut**) functions require that applications to allocate data blocks to pass to the device drivers for playback or recording purposes. Each of these functions uses a [**MIDIHDR**](https://www.bing.com/search?q=**MIDIHDR**) structure to describe its data block.

Before you use one of these functions to pass a data block to a device driver, you must allocate memory for the buffer and the header structure that describes the data block.

Windows provides the following functions for preparing and cleaning up MIDI data blocks.



| Value                                                    | Meaning                                                |
|----------------------------------------------------------|--------------------------------------------------------|
| [**midiInPrepareHeader**](https://www.bing.com/search?q=**midiInPrepareHeader**)       | Prepares a MIDI input data block.                      |
| [**midiInUnprepareHeader**](https://www.bing.com/search?q=**midiInUnprepareHeader**)   | Cleans up the preparation of a MIDI input data block.  |
| [**midiOutPrepareHeader**](https://www.bing.com/search?q=**midiOutPrepareHeader**)     | Prepares a MIDI output data block.                     |
| [**midiOutUnprepareHeader**](https://www.bing.com/search?q=**midiOutUnprepareHeader**) | Cleans up the preparation of a MIDI output data block. |



 

Before you pass a MIDI data block to a device driver, you must prepare the buffer by passing it to the [**midiInPrepareHeader**](https://www.bing.com/search?q=**midiInPrepareHeader**) or [**midiOutPrepareHeader**](https://www.bing.com/search?q=**midiOutPrepareHeader**) function. When the device driver is finished with the buffer and returns it, you must clean up this preparation by passing the buffer to the [**midiInUnprepareHeader**](https://www.bing.com/search?q=**midiInUnprepareHeader**) or [**midiOutUnprepareHeader**](https://www.bing.com/search?q=**midiOutUnprepareHeader**) function before any allocated memory can be freed.

## Related topics

<dl> <dt>

[MIDI Services](midi-services.md)
</dt> </dl>

 

 




