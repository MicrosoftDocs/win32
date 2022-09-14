---
title: Receiving Time-Stamped MIDI Messages
description: Receiving Time-Stamped MIDI Messages
ms.assetid: a91c85fe-f9c4-4cf6-b0bb-49aa8ed45644
keywords:
- Musical Instrument Digital Interface (MIDI),time-stamped messages
- MIDI (Musical Instrument Digital Interface),time-stamped messages
- recording MIDI audio,time-stamped messages
- time-stamped MIDI messages
ms.topic: article
ms.date: 05/31/2018
---

# Receiving Time-Stamped MIDI Messages

Because of the delay between when the device driver receives a MIDI message and the time the application receives the message, MIDI input device drivers time stamp the MIDI message with the time that the message was received. MIDI time stamps, which are defined as the time the first byte of the message was received, are specified in milliseconds. The [**midiInStart**](/windows/win32/api/mmeapi/nf-mmeapi-midiinstart) function resets the time stamps for a device to zero.

As stated previously, to receive time stamps with MIDI input, you must use a callback function. The *dwParam2* parameter of the callback function specifies the time stamp for data associated with the [**MIM\_DATA**](mim-data.md) and [**MIM\_LONGDATA**](mim-longdata.md) messages.

## Related topics

<dl> <dt>

[Recording MIDI Audio](recording-midi-audio.md)
</dt> </dl>

 

 