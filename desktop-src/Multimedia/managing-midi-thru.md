---
title: Managing MIDI Thru
description: Managing MIDI Thru
ms.assetid: ba03a2a1-d998-498d-ad53-027ba2b6e276
keywords:
- Musical Instrument Digital Interface (MIDI),thru driver
- MIDI (Musical Instrument Digital Interface),thru driver
- recording MIDI audio,thru driver
- MIDI thru driver
ms.topic: article
ms.date: 05/31/2018
---

# Managing MIDI Thru

You can connect a MIDI input device directly to a MIDI output device so that when the input device receives an [**MIM\_DATA**](mim-data.md) message, the system sends a message with the same MIDI event data to the output device driver. To connect a MIDI output device to a MIDI input device, use the [**midiConnect**](/windows/win32/api/mmeapi/nf-mmeapi-midiconnect) function.

To achieve the best possible performance with multiple outputs, an application can choose to supply a special form of MIDI output driver, called a *thru driver*. Although the system allows only one MIDI output device to be connected to a MIDI input device, multiple MIDI output devices can be connected to a thru driver. An application on such a system could connect the MIDI input device to this thru device and connect the MIDI thru device to as many MIDI output devices as needed. For more information about thru drivers, see the Windows device-driver documentation.

## Using Messages to Manage MIDI Recording

The following messages can be sent to a window or thread callback procedure for managing MIDI recording.



| Value                                          | Meaning                                                                                                                                |
|------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| [**MM\_MIM\_CLOSE**](mm-mim-close.md)         | Sent when a MIDI input device is closed by using the [**midiInClose**](/windows/win32/api/mmeapi/nf-mmeapi-midiinclose) function.                                      |
| [**MM\_MIM\_DATA**](mm-mim-data.md)           | Sent when a complete MIDI message is received. (This message is used for all MIDI messages except system-exclusive messages.)          |
| [**MM\_MIM\_ERROR**](mm-mim-error.md)         | Sent when an invalid MIDI message is received. (This message is used for all MIDI messages except system-exclusive messages.)          |
| [**MM\_MIM\_LONGDATA**](mm-mim-longdata.md)   | Sent when either a complete MIDI system-exclusive message is received or when a buffer has been filled with system-exclusive data.     |
| [**MM\_MIM\_LONGERROR**](mm-mim-longerror.md) | Sent when an invalid MIDI system-exclusive message is received.                                                                        |
| [**MM\_MIM\_MOREDATA**](mm-mim-moredata.md)   | Sent when an application is not processing [**MIM\_DATA**](mim-data.md) messages fast enough to keep up with the input device driver. |
| [**MM\_MIM\_OPEN**](mm-mim-open.md)           | Sent when a MIDI input device is opened by using the [**midiInOpen**](/windows/win32/api/mmeapi/nf-mmeapi-midiinopen) function.                                        |



 

A *wParam* parameter and an *lParam* parameter are associated with each of these messages. The *wParam* parameter always specifies the handle of an open MIDI device. The *lParam* parameter is unused for the [**MM\_MIM\_CLOSE**](mm-mim-close.md) and [**MM\_MIM\_OPEN**](mm-mim-open.md) messages.

For the [**MM\_MIM\_LONGDATA**](mm-mim-longdata.md) message, *lpMidiHdr* specifies an address of a [**MIDIHDR**](/windows/win32/api/mmeapi/ns-mmeapi-midihdr) structure that identifies the buffer for system-exclusive messages. The buffer may not be completely filled, because the size of the system-exclusive messages is usually not known before being recorded and because buffers whose total size can contain the largest expected message must be allocated. To determine the amount of valid data present in the buffer, use the **dwBytesRecorded** member of the **MIDIHDR** structure.

## Using a Callback Function to Manage MIDI Recording

You can define your own callback function to manage recording for MIDI input devices. The callback function is documented as [**MidiInProc**](/previous-versions//dd798460(v=vs.85)).

The following messages can be sent to the *wMsg* parameter of the **MidiInProc** callback function.



| Value                                   | Meaning                                                                                                                                |
|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| [**MIM\_CLOSE**](mim-close.md)         | Sent when the device is closed by using the [**midiInClose**](/windows/win32/api/mmeapi/nf-mmeapi-midiinclose) function.                                               |
| [**MIM\_DATA**](mim-data.md)           | Sent when a complete MIDI message is received (this message is used for all MIDI messages except system-exclusive messages).           |
| [**MIM\_ERROR**](mim-error.md)         | Sent when an invalid MIDI message is received (this message is used for all MIDI messages except system-exclusive messages).           |
| [**MIM\_LONGDATA**](mim-longdata.md)   | Sent when either a complete MIDI system-exclusive message is received or when a buffer has been filled with system-exclusive data.     |
| [**MIM\_LONGERROR**](mim-longerror.md) | Sent when an invalid MIDI system-exclusive message is received.                                                                        |
| [**MIM\_MOREDATA**](mim-moredata.md)   | Sent when an application is not processing [**MIM\_DATA**](mim-data.md) messages fast enough to keep up with the input device driver. |
| [**MIM\_OPEN**](mim-open.md)           | Sent when the MIDI input device is opened by using the [**midiInOpen**](/windows/win32/api/mmeapi/nf-mmeapi-midiinopen) function.                                      |



 

These messages are similar to those sent to window procedure functions, but the parameters are different. A handle of the open MIDI device is passed as a parameter to the callback function, along with the doubleword of instance data that was passed by using **midiInOpen**.

For the [**MIM\_LONGDATA**](mim-longdata.md) message, *lpMidiHdr* specifies an address of a [**MIDIHDR**](/windows/win32/api/mmeapi/ns-mmeapi-midihdr) structure that identifies the buffer for system-exclusive messages. The buffer might not be completely filled. To determine the amount of valid data present in the buffer, use the **dwBytesRecorded** member of the **MIDIHDR** structure.

After the device driver is finished with a data block, you can clean up and free the data block.

## Related topics

<dl> <dt>

[Recording MIDI Audio](recording-midi-audio.md)
</dt> </dl>

 

 