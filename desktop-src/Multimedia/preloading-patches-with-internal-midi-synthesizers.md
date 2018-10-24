---
title: Preloading Patches with Internal MIDI Synthesizers
description: Preloading Patches with Internal MIDI Synthesizers
ms.assetid: c200aa91-ab91-48e8-b3b5-8e7f36e511be
keywords:
- Musical Instrument Digital Interface (MIDI),internal synthesizers
- MIDI (Musical Instrument Digital Interface),internal synthesizers
- playing MIDI files,internal synthesizers
- internal MIDI synthesizers
- Musical Instrument Digital Interface (MIDI),preloading patches
- MIDI (Musical Instrument Digital Interface),preloading patches
- playing MIDI files,preloading patches
- preloading MIDI patches
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Preloading Patches with Internal MIDI Synthesizers

Some internal MIDI synthesizer devices cannot keep all of their patches loaded simultaneously. These devices must preload their patch data.

Windows provides the following functions to request that a synthesizer preload and cache specified patches.



| Value                                                      | Meaning                                                                                                     |
|------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| [**midiOutCachePatches**](https://msdn.microsoft.com/en-us/library/Dd798466(v=VS.85).aspx)         | Requests that an internal MIDI synthesizer device preload and cache specified melodic patches.              |
| [**midiOutCacheDrumPatches**](https://msdn.microsoft.com/en-us/library/Dd798465(v=VS.85).aspx) | Requests that an internal MIDI synthesizer device preload and cache specified key-based percussion patches. |



 

For information on how to determine if a particular device supports preloading patches, see [Querying MIDI Output Devices](querying-midi-output-devices.md).

 

 




