---
title: Requesting Time Formats
description: Requesting Time Formats
ms.assetid: 3492dfe3-ed54-405a-aa4f-b17abbd1e07f
keywords:
- Musical Instrument Digital Interface (MIDI),time formats
- MIDI (Musical Instrument Digital Interface),time formats
- MIDI services,time formats
ms.topic: article
ms.date: 05/31/2018
---

# Requesting Time Formats

Windows uses the [**MMTIME**](/previous-versions//dd757347(v=vs.85)) structure to represent time in one or more different formats, including milliseconds, samples, SMPTE, and MIDI song pointer formats. The **wType** member specifies the time format.

The [**midiStreamPosition**](/windows/win32/api/mmeapi/nf-mmeapi-midistreamposition) function uses the **MMTIME** structure. Before calling this function, you must set the **wType** member to indicate your requested time format. To see if the requested time format is supported, check **wType** after the call. If the requested time format is not supported, the time is specified in an alternate time format selected by the device driver and the **wType** member is changed to indicate the selected time format.

For more information about the **MMTIME** structure, see [Multimedia Timers](multimedia-timers.md).

## Related topics

<dl> <dt>

[MIDI Services](midi-services.md)
</dt> </dl>

 

 