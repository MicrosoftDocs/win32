---
title: Summary of Maps and MIDI Messages
description: Summary of Maps and MIDI Messages
ms.assetid: cd0ec7b0-2ba1-4e75-b85c-f5b95ac9dfeb
keywords:
- Musical Instrument Digital Interface (MIDI),MIDI Mapper
- MIDI (Musical Instrument Digital Interface),MIDI Mapper
- MIDI Mapper,channel map
- MIDI Mapper,patch maps
- MIDI Mapper,key maps
- channel map
- patch maps
- key maps
ms.topic: article
ms.date: 05/31/2018
---

# Summary of Maps and MIDI Messages

Following are the status bytes for MIDI messages and the map types that affect each message.



| MIDI status | Description               | Map types                |
|-------------|---------------------------|--------------------------|
| 0x80-0x8F   | Note off                  | Channel maps, key maps   |
| 0x90-0x9F   | Note on                   | Channel maps, key maps   |
| 0xA0-0xAF   | Polyphonic-key aftertouch | Channel maps, key maps   |
| 0xB0-0xBF   | Control change            | Channel maps, patch maps |
| 0xC0-0xCF   | Program change            | Channel maps, patch maps |
| 0xD0-0xDF   | Channel aftertouch        | Channel maps             |
| 0xE0-0xEF   | Pitch-bend change         | Channel maps             |
| 0xF0-0xFF   | System                    | Not mapped               |



 

-   The high-order four bits represent the status value. The low-order four bits represent the channel information.
-   Patch maps affect only controller 7 (main volume).
-   System messages are sent to all devices listed in a channel map.

 

 




