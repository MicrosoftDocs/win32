---
title: Resetting MIDI Output
description: Resetting MIDI Output
ms.assetid: 281a7cfa-f274-4c7a-b63a-c0573b9f1169
keywords:
- Musical Instrument Digital Interface (MIDI),resetting output devices
- MIDI (Musical Instrument Digital Interface),resetting output devices
- playing MIDI files,resetting output devices
- resetting output devices
- Musical Instrument Digital Interface (MIDI),output devices
- MIDI (Musical Instrument Digital Interface),output devices
- playing MIDI files,output devices
- MIDI output devices
- EOX (end-of-exclusive)
- end-of-exclusive (EOX)
ms.topic: article
ms.date: 05/31/2018
---

# Resetting MIDI Output

The [**midiOutReset**](/windows/win32/api/mmeapi/nf-mmeapi-midioutreset) function turns off all notes on all MIDI channels for a specified MIDI device. Then, the function marks any pending system-exclusive buffers as done and returns them to the application. This function can be useful in an application that uses MIDI output to provide the user with the ability to reset MIDI output.

> [!Note]  
> Terminating a system-exclusive message without sending an EOX (end-of-exclusive) byte can cause problems for the receiving device. The **midiOutReset** function does not send an EOX byte when it terminates a system-exclusive message, because applications are responsible for doing this.

 

 

 