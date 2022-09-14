---
title: Querying MIDI Devices
description: Querying MIDI Devices
ms.assetid: 0c9882a7-b5cb-41d1-a52e-003112225035
keywords:
- Musical Instrument Digital Interface (MIDI),querying devices
- MIDI (Musical Instrument Digital Interface),querying devices
- MIDI services,querying devices
- querying MIDI devices
ms.topic: article
ms.date: 05/31/2018
---

# Querying MIDI Devices

Before playing or recording MIDI data, you must determine the capabilities of the MIDI hardware present in the system. MIDI capability can vary from one multimedia computer to the next; applications should not make assumptions about the hardware present in a given system.

Windows provides the following functions to determine how many MIDI devices are available for input or output in a given system.



| Value                                          | Meaning                                                            |
|------------------------------------------------|--------------------------------------------------------------------|
| [**midiInGetNumDevs**](/windows/win32/api/mmeapi/nf-mmeapi-midiingetnumdevs)   | Retrieves the number of MIDI input devices present in the system.  |
| [**midiOutGetNumDevs**](/windows/win32/api/mmeapi/nf-mmeapi-midioutgetnumdevs) | Retrieves the number of MIDI output devices present in the system. |



 

Like other audio devices, MIDI devices are identified by a device identifier, which is determined implicitly from the number of devices present in a given system. Device identifiers range from zero to the number of devices present, minus one. For example, if there are two MIDI output devices in a system, valid device identifiers are 0 and 1.

After you determine how many MIDI input or output devices are present in a system, you can inquire about the capabilities of each device. Windows provides the following functions to determine the capabilities of audio devices.



| Value                                          | Meaning                                                                                                                                   |
|------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| [**midiInGetDevCaps**](/windows/win32/api/mmeapi/nf-mmeapi-midiingetdevcaps)   | Retrieves the capabilities of a given MIDI input device and places this information in the [**MIDIINCAPS**](/windows/win32/api/mmeapi/ns-mmeapi-midiincaps) structure.    |
| [**midiOutGetDevCaps**](/windows/win32/api/mmeapi/nf-mmeapi-midioutgetdevcaps) | Retrieves the capabilities of a given MIDI output device and places this information in the [**MIDIOUTCAPS**](/windows/win32/api/mmeapi/ns-mmeapi-midioutcaps) structure. |



 

Each of these functions has a parameter specifying the address of a structure that the function fills with information about the capabilities of a specified device.

## Related topics

<dl> <dt>

[MIDI Services](midi-services.md)
</dt> </dl>

 

 