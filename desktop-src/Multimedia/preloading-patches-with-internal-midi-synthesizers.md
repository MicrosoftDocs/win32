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
ms.topic: article
ms.date: 05/31/2018
---

# Preloading Patches with Internal MIDI Synthesizers

Some internal MIDI synthesizer devices cannot keep all of their patches loaded simultaneously. These devices must preload their patch data.

Windows provides the following functions to request that a synthesizer preload and cache specified patches.



| Value                                                      | Meaning                                                                                                     |
|------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| [**midiOutCachePatches**](/windows/win32/api/mmeapi/nf-mmeapi-midioutcachepatches)         | Requests that an internal MIDI synthesizer device preload and cache specified melodic patches.              |
| [**midiOutCacheDrumPatches**](/windows/win32/api/mmeapi/nf-mmeapi-midioutcachedrumpatches) | Requests that an internal MIDI synthesizer device preload and cache specified key-based percussion patches. |



 

For information on how to determine if a particular device supports preloading patches, see [Querying MIDI Output Devices](querying-midi-output-devices.md).

 

 