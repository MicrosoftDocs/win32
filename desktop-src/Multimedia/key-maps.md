---
title: Key Maps
description: Key Maps
ms.assetid: 5d0367b0-bbf1-4a4b-98b2-dbca6f2f8b0c
keywords:
- Musical Instrument Digital Interface (MIDI),MIDI Mapper
- MIDI (Musical Instrument Digital Interface),MIDI Mapper
- MIDI Mapper,key maps
- key maps
ms.topic: article
ms.date: 05/31/2018
---

# Key Maps

Each entry in the patch-map translation table can have an associated key map. Key maps affect note-on, note-off, and polyphonic-key-aftertouch messages. A key map has a translation table with an entry for each of the 128 MIDI key values. For example, if the entry for key value 60 is 72, the MIDI Mapper modifies MIDI note-on messages as shown in the following illustration.

![midi mapper image](images/mmap-a06.gif)

Key maps are useful with synthesizers that have key-based percussion instruments with a particular percussion sound assigned to each key. Key maps are usually assigned to the first patch in the patch maps on the percussion channels (10 and 16).

 

 




