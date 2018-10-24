---
title: MIDI Input Data Types
description: MIDI Input Data Types
ms.assetid: c67f149e-60b8-4f9e-8e3c-a88cd579d29f
keywords:
- Musical Instrument Digital Interface (MIDI),input data types
- MIDI (Musical Instrument Digital Interface),input data types
- recording MIDI audio,input data types
- MIDI input data types
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MIDI Input Data Types

Windows defines the following data types for the MIDI input functions.



| Value                            | Meaning                                                                                                                                                                                     |
|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **HMIDIIN**                      | Handle of a MIDI input device.                                                                                                                                                              |
| [**MIDIHDR**](https://msdn.microsoft.com/en-us/library/Dd798449(v=VS.85).aspx)       | Header for a stream buffer or a block of MIDI system-exclusive data. For input applications, this structure records only system-exclusive data (streaming is not supported for MIDI input). |
| [**MIDIINCAPS**](https://msdn.microsoft.com/en-us/library/Dd798451(v=VS.85).aspx) | Structure used to inquire about the capabilities of a MIDI input device.                                                                                                                    |



 

## Related topics

<dl> <dt>

[Recording MIDI Audio](recording-midi-audio.md)
</dt> </dl>

 

 




