---
title: Querying MIDI Input Devices
description: Querying MIDI Input Devices
ms.assetid: 2da88418-f9cf-49da-b17f-8a26d357b5ab
keywords:
- Musical Instrument Digital Interface (MIDI),input devices
- MIDI (Musical Instrument Digital Interface),input devices
- recording MIDI audio,input devices
- MIDI input devices
- Musical Instrument Digital Interface (MIDI),querying input devices
- MIDI (Musical Instrument Digital Interface),querying input devices
- recording MIDI audio,querying input devices
- querying MIDI input devices
ms.topic: article
ms.date: 05/31/2018
---

# Querying MIDI Input Devices

Before recording MIDI audio, you should use the [**midiInGetDevCaps**](/windows/win32/api/mmeapi/nf-mmeapi-midiingetdevcaps) function to determine the capabilities of the MIDI input device that is present in the system. This function takes an address of a [**MIDIINCAPS**](/windows/win32/api/mmeapi/ns-mmeapi-midiincaps) structure, which it fills with information about the capabilities of the given device. This information includes the manufacturer and product identifiers, a product name for the device, and the version number of the device driver.

## Related topics

<dl> <dt>

[Recording MIDI Audio](recording-midi-audio.md)
</dt> </dl>

 

 