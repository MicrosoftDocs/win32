---
title: Media Control Interface (MCI)
description: Media Control Interface (MCI)
ms.assetid: e22f23b5-0fa6-4957-bbbf-b1b3a4c8bd31
keywords:
- Windows multimedia,Media Control Interface (MCI)
- multimedia,Media Control Interface (MCI)
- multimedia audio,Media Control Interface (MCI)
- audio,Media Control Interface (MCI)
- Musical Instrument Digital Interface (MIDI),Media Control Interface (MCI)
- MIDI (Musical Instrument Digital Interface),Media Control Interface (MCI)
- Media Control Interface (MCI),Musical Instrument Digital Interface (MIDI)
- MCI (Media Control Interface),Musical Instrument Digital Interface (MIDI)
- Media Control Interface (MCI),MIDI sequencer
- MCI (Media Control Interface),MIDI sequencer
- MCI MIDI sequencer,about
ms.topic: article
ms.date: 05/31/2018
---

# Media Control Interface (MCI)

The MCI MIDI sequencer is the MCI system component that plays MIDI files. Applications can play MIDI files easily using MCI, but MCI imposes the following restrictions on MIDI capabilities:

-   MCI supports MIDI output only.
-   MCI does not allow close synchronization between MIDI events and other real-time events (such as video).

If you need accurate MIDI synchronization, you must use the stream buffers or the MIDI services. If you need MIDI input capabilities, you must use the MIDI services.

The MCI MIDI sequencer plays standard MIDI files and resource interchange file format (RIFF) MIDI files, known as RMID files. Standard MIDI files conform to the [Standard MIDI Files 1.0](creating-midi-files.md) specification. Because RMID files are standard MIDI files with a RIFF header, information about standard MIDI files also applies to RMID files. For more information about RIFF files, see [Resource Interchange File Format Services](resource-interchange-file-format-services.md).

Although there are currently three kinds of standard MIDI files, the MCI sequencer plays only two of them: Format 0 and Format 1 MIDI files.

For more information about controlling multimedia devices (including sequencers) using MCI commands, see [MCI](mci.md).

 

 




