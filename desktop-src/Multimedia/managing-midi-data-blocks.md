---
title: Managing MIDI Data Blocks
description: Managing MIDI Data Blocks
ms.assetid: f29fbc08-ef67-489c-aedf-5a2bc65233f7
keywords:
- Musical Instrument Digital Interface (MIDI),managing data blocks
- MIDI (Musical Instrument Digital Interface),managing data blocks
- MIDI services,managing data blocks
- managing MIDI data blocks
- Musical Instrument Digital Interface (MIDI),processing driver messages
- MIDI (Musical Instrument Digital Interface),processing driver messages
- MIDI services,processing driver messages
- processing driver messages
- Musical Instrument Digital Interface (MIDI),data blocks
- MIDI (Musical Instrument Digital Interface),data blocks
- MIDI services,data blocks
ms.topic: article
ms.date: 05/31/2018
---

# Managing MIDI Data Blocks

Applications that use data blocks for passing system-exclusive messages (using the [**midiOutLongMsg**](/windows/win32/api/mmeapi/nf-mmeapi-midioutlongmsg) and [**midiInAddBuffer**](/windows/win32/api/mmeapi/nf-mmeapi-midiinaddbuffer) functions) and stream buffers (using the [**midiStreamOut**](/windows/win32/api/mmeapi/nf-mmeapi-midistreamout) function) must continually supply the device driver with data blocks until playback or recording is complete.

Even if a single data block is used, an application must be able to determine when a device driver is finished with the data block so it can free the memory associated with the data block and header structure. Three methods can be used to determine when a device driver is finished with a data block:

-   Specify a callback function to receive a message sent by the driver when it is finished with a data block. To get time-stamped MIDI input data, you must use a callback function.
-   Use an event callback (for output only).
-   Use a window or thread callback to receive a message sent by the driver when it is finished with a data block.

If an application does not get a data block to the device driver when it is needed, an audible gap in playback or a loss of incoming recorded information can occur. At a minimum, an application should use a double-buffering scheme to stay at least one data block ahead of the device driver.

## Using a Callback Function to Process Driver Messages

You can write your own callback function to process messages sent by the device driver. To use a callback function, specify the CALLBACK\_FUNCTION flag in the *dwFlags* parameter and the address of the callback function in the *dwCallback* parameter of the [**midiInOpen**](/windows/win32/api/mmeapi/nf-mmeapi-midiinopen) or [**midiOutOpen**](/windows/win32/api/mmeapi/nf-mmeapi-midioutopen) function.

Messages sent to a callback function are similar to messages sent to a window, except they have two doubleword parameters instead of an unsigned integer parameter and a doubleword parameter. For more information about these messages, see [Sending System-Exclusive Messages](sending-system-exclusive-messages.md) and [Managing MIDI Recording](managing-midi-recording.md).

Use one of the following techniques to pass instance data from an application to a callback function:

-   Use the *dwCallbackInstance* parameter of the function that opens the device driver.
-   Use the **dwUser** member of the [**MIDIHDR**](/windows/win32/api/mmeapi/ns-mmeapi-midihdr) structure that identifies a data block being sent to a MIDI device driver.

If you need more than 32 bits of instance data, pass an address of a structure containing the additional information.

## Using an Event Callback to Process Driver Messages

To use an event callback, use the [CreateEvent](/windows/win32/api/synchapi/nf-synchapi-createeventa) function to retrieve the handle of an event and specify CALLBACK\_EVENT in the call to the [**midiOutOpen**](/windows/win32/api/mmeapi/nf-mmeapi-midioutopen) function.

An event callback is set by anything that might cause a function callback. Unlike callback functions and window or thread callbacks, event callbacks do not receive specific close, done, or open notifications. Therefore, an application may have to check the status of the process it is waiting for after the event occurs.

For more information about event callbacks, see [Using an Event Callback to Manage Buffered Playback](using-an-callback-to-manage-buffered-playback.md).

## Using a Window or Thread Callback to Process Driver Messages

To use a window callback, specify the CALLBACK\_WINDOW flag in the *dwFlags* parameter and a window handle in the low-order word of the *dwCallback* parameter of the [**midiInOpen**](/windows/win32/api/mmeapi/nf-mmeapi-midiinopen) or [**midiOutOpen**](/windows/win32/api/mmeapi/nf-mmeapi-midioutopen) function. Driver messages will be sent to the window procedure function for the window identified by the handle in *dwCallback*.

Similarly, to use a thread callback, specify the CALLBACK\_THREAD flag and a thread identifier in the call to **midiInOpen** or **midiOutOpen**. In this case, messages will be posted to the specified thread instead of to a window.

Messages sent to a window or thread callback are specific to the MIDI device used. For more information about these messages, see [Sending System-Exclusive Messages](sending-system-exclusive-messages.md) and [Managing MIDI Recording](managing-midi-recording.md).

## Related topics

<dl> <dt>

[MIDI Services](midi-services.md)
</dt> </dl>

 

 