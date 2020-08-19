---
title: Opening and Closing Device Drivers
description: Opening and Closing Device Drivers
ms.assetid: 441bc0ec-41c9-4595-92f9-4c2304b10f16
keywords:
- Musical Instrument Digital Interface (MIDI),opening devices
- MIDI (Musical Instrument Digital Interface),opening devices
- MIDI services,opening devices
- opening MIDI devices
- Musical Instrument Digital Interface (MIDI),closing devices
- MIDI (Musical Instrument Digital Interface),closing devices
- MIDI services,closing devices
- closing MIDI devices
ms.topic: article
ms.date: 05/31/2018
---

# Opening and Closing Device Drivers

You must open a MIDI device before using it, and you should close the device as soon as you finish using it. Windows provides the following functions to open and close different types of MIDI devices.



| Value                                | Meaning                                            |
|--------------------------------------|----------------------------------------------------|
| [**midiInClose**](/windows/win32/api/mmeapi/nf-mmeapi-midiinclose)   | Closes a specified MIDI input device.              |
| [**midiInOpen**](/windows/win32/api/mmeapi/nf-mmeapi-midiinopen)     | Opens a specified MIDI input device for recording. |
| [**midiOutClose**](/windows/win32/api/mmeapi/nf-mmeapi-midioutclose) | Closes a specified MIDI output device.             |
| [**midiOutOpen**](/windows/win32/api/mmeapi/nf-mmeapi-midioutopen)   | Opens a MIDI output device for playback.           |



 

Each function that opens a MIDI device takes as parameters a device identifier, an address of a memory location, and some parameters unique to MIDI devices. The memory location is filled with a device handle, which is used to identify the open audio device in calls to other audio functions.

Many MIDI functions can accept either a device handle or a device identifier. Although you can use a device handle wherever you would use a device identifier, you cannot always use a device identifier when a handle is called for.

> [!Note]  
> MIDI devices are not necessarily sharable, so a particular device may not be available when a user requests it. If this happens, the application should notify the user and allow the user to try to open the device again.

 

## Related topics

<dl> <dt>

[MIDI Services](midi-services.md)
</dt> </dl>

 

 