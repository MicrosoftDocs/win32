---
title: Querying MIDI Output Devices
description: Querying MIDI Output Devices
ms.assetid: c6a33a4e-c61a-4e06-805e-5128a97f5199
keywords:
- Musical Instrument Digital Interface (MIDI),output devices
- MIDI (Musical Instrument Digital Interface),output devices
- playing MIDI files,output devices
- MIDI output devices
- Musical Instrument Digital Interface (MIDI),querying output devices
- MIDI (Musical Instrument Digital Interface),querying output devices
- playing MIDI files,querying output devices
- querying MIDI output devices
ms.topic: article
ms.date: 05/31/2018
---

# Querying MIDI Output Devices

Before playing a MIDI file, you should use the [**midiOutGetDevCaps**](/windows/win32/api/mmeapi/nf-mmeapi-midioutgetdevcaps) function to determine the capabilities of the MIDI output device that is present in the system. This function takes an address of a [**MIDIOUTCAPS**](/windows/win32/api/mmeapi/ns-mmeapi-midioutcaps) structure, which it fills with information about the capabilities of the given device. This information includes the manufacturer and product identifiers, a product name for the device, and the version number of the device driver (specified in the **wMid**, **wPid**, **szPname**, and **vDriverVersion** members, respectively).

MIDI output devices can be either internal synthesizers or external MIDI output ports. The **wTechnology** member of the **MIDIOUTCAPS** structure specifies the technology of the device.

If the device is an internal synthesizer, additional device information is available in the **wVoices**, **wNotes**, and **wChannelMask** members. The **wVoices** member specifies the number of voices that the device supports. Each voice can have a different sound or timbre. Voices are organized into MIDI channels. The **wNotes** member specifies the *polyphony* of the device — that is, the maximum number of notes that can be played simultaneously. The **wChannelMask** member is a bit representation of the MIDI channels that the device responds to. For example, if the device responds to the first eight MIDI channels, **wChannelMask** is 0x00FF. If the device is an external output port, **wVoices** and **wNotes** are unused, and **wChannelMask** is set to 0xFFFF.

The **dwSupport** member of the **MIDIOUTCAPS** structure indicates whether the device driver supports volume changes, patch caching, and streaming. Volume changes are supported only by internal synthesizer devices. External MIDI output ports do not support volume changes. For information about changing volume, see [Changing Internal MIDI Synthesizer Volume](changing-internal-midi-synthesizer-volume.md).

 

 