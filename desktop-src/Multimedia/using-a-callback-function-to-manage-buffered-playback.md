---
title: Using a Callback Function to Manage Buffered Playback
description: Using a Callback Function to Manage Buffered Playback
ms.assetid: aaaf9c5f-c9b2-4e55-a4c1-28c99cc03945
keywords:
- Musical Instrument Digital Interface (MIDI),buffered playback
- MIDI (Musical Instrument Digital Interface),buffered playback
- playing MIDI files,buffered playback
- buffered playback
- MOM_CLOSE message
- MOM_DONE message
- MOM_OPEN message
- Musical Instrument Digital Interface (MIDI),sending messages
- MIDI (Musical Instrument Digital Interface),sending messages
- playing MIDI files,sending messages
- sending MIDI messages
- Musical Instrument Digital Interface (MIDI),callback functions
- MIDI (Musical Instrument Digital Interface),callback functions
- playing MIDI files,callback functions
- MidiOutProc callback function
ms.topic: article
ms.date: 05/31/2018
---

# Using a Callback Function to Manage Buffered Playback

You can define your own callback function to manage buffered playback of MIDI output devices. The callback function is documented as [**MidiOutProc**](/previous-versions//dd798478(v=vs.85)).

The following messages can be sent to the *wMsg* parameter of the **MidiOutProc** callback function.



| Value                           | Meaning                                                                                                                                                                  |
|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MOM\_CLOSE**](mom-close.md) | Sent when the device is closed by using the [**midiOutClose**](/windows/win32/api/mmeapi/nf-mmeapi-midioutclose) function.                                                                               |
| [**MOM\_DONE**](mom-done.md)   | Sent when the device driver is finished with a data block sent by using the [**midiOutLongMsg**](/windows/win32/api/mmeapi/nf-mmeapi-midioutlongmsg) or [**midiStreamOut**](/windows/win32/api/mmeapi/nf-mmeapi-midistreamout) function. |
| [**MOM\_OPEN**](mom-open.md)   | Sent when the device is opened by using the [**midiOutOpen**](/windows/win32/api/mmeapi/nf-mmeapi-midioutopen) function.                                                                                 |



 

These messages are similar to those sent to window procedure functions, but the parameters are different. A handle of the open MIDI device is passed as a parameter to the callback function, along with the doubleword of instance data passed by using **midiOutOpen**.

After the driver is finished with a data block, you can clean up and free the data block. Because of the suggested restrictions on callback functions, it is better not to do this from within the callback function.

 

 