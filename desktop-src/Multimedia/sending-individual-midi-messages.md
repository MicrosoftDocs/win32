---
title: Sending Individual MIDI Messages
description: Sending Individual MIDI Messages
ms.assetid: 9e5b7194-d6d0-40a6-b8c1-ea9442f34bd8
keywords:
- Musical Instrument Digital Interface (MIDI),sending messages
- MIDI (Musical Instrument Digital Interface),sending messages
- playing MIDI files,sending messages
- sending MIDI messages
- Musical Instrument Digital Interface (MIDI),individual messages
- MIDI (Musical Instrument Digital Interface),individual messages
- playing MIDI files,individual messages
- individual MIDI messages
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Sending Individual MIDI Messages

You can work with individual MIDI messages by using the following functions.



| Value                                      | Meaning                                                                                                                                                                             |
|--------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**midiOutLongMsg**](https://msdn.microsoft.com/en-us/library/Dd798474(v=VS.85).aspx)   | Sends a buffer of MIDI data to the specified MIDI output device. Use this function to send system-exclusive messages to a MIDI device.                                              |
| [**midiOutReset**](https://msdn.microsoft.com/en-us/library/Dd798479(v=VS.85).aspx)       | Turns off all notes on all channels for a specified MIDI output device. Any pending system-exclusive buffers and stream buffers are marked as done and returned to the application. |
| [**midiOutShortMsg**](https://msdn.microsoft.com/en-us/library/Dd798481(v=VS.85).aspx) | Sends a MIDI message to a specified MIDI output device.                                                                                                                             |



 

To send any MIDI message (except for system-exclusive messages), use [**midiOutShortMsg**](https://msdn.microsoft.com/en-us/library/Dd798481(v=VS.85).aspx).

 

 




