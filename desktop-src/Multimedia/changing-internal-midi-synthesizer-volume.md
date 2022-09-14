---
title: Changing Internal MIDI Synthesizer Volume
description: Changing Internal MIDI Synthesizer Volume
ms.assetid: 75ab7ff5-f394-4a79-8dcc-f4eef434a36e
keywords:
- Musical Instrument Digital Interface (MIDI),internal synthesizers
- MIDI (Musical Instrument Digital Interface),internal synthesizers
- playing MIDI files,internal synthesizers
- internal MIDI synthesizers
- Musical Instrument Digital Interface (MIDI),changing volume
- MIDI (Musical Instrument Digital Interface),changing volume
- playing MIDI files,changing volume
- changing MIDI volume
ms.topic: article
ms.date: 05/31/2018
---

# Changing Internal MIDI Synthesizer Volume

Windows provides the following functions to retrieve and set the volume level of internal MIDI synthesizer devices:



| Value                                        | Meaning                                                                       |
|----------------------------------------------|-------------------------------------------------------------------------------|
| [**midiOutGetVolume**](/windows/win32/api/mmeapi/nf-mmeapi-midioutgetvolume) | Retrieves the volume level of the specified internal MIDI synthesizer device. |
| [**midiOutSetVolume**](/windows/win32/api/mmeapi/nf-mmeapi-midioutsetvolume) | Sets the volume level of the specified internal MIDI synthesizer device.      |



 

Not all MIDI output devices support volume changes. Some devices can support individual volume changes on both the left and right channels. For information on how to determine if a particular device supports volume changes, see [Querying MIDI Output Devices](querying-midi-output-devices.md).

Unless your application is designed to be a master volume-control application (provides the user with volume control for all audio devices in a system), you should open an audio device before changing its volume. You should also check the volume level before changing it and restore the volume level to its previous level as soon as possible.

Volume is specified as a doubleword value. The upper 16 bits specify the relative volume of the right channel, and the lower 16 bits specify the relative volume of the left channel.

For devices that do not support individual volume changes on both the left and right channels, the lower 16 bits specify the volume level and the upper 16 bits are ignored. Values for the volume level range from 0x0 (silence) to 0xFFFF (maximum volume) and are interpreted logarithmically. The perceived volume increase is the same when increasing the volume level from 0x5000 to 0x6000 as it is from 0x4000 to 0x5000.

 

 