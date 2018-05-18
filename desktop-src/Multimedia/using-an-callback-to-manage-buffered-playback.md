---
title: Using an Event Callback to Manage Buffered Playback
description: Using an Event Callback to Manage Buffered Playback
ms.assetid: '3b60daea-574d-430b-b14e-1fefceb69dfb'
keywords: ["Musical Instrument Digital Interface (MIDI),buffered playback", "MIDI (Musical Instrument Digital Interface),buffered playback", "playing MIDI files,buffered playback", "buffered playback", "CreateEvent function", "Musical Instrument Digital Interface (MIDI),event callback", "MIDI (Musical Instrument Digital Interface),event callback", "playing MIDI files,event callback", "event callback"]
---

# Using an Event Callback to Manage Buffered Playback

To use an event callback, use the [CreateEvent](http://go.microsoft.com/fwlink/p/?linkid=17091) function to retrieve the handle of an event. In a call to the [**midiOutOpen**](midioutopen.md) function, specify CALLBACK\_EVENT for the *dwFlags* parameter. After using the [**midiOutPrepareHeader**](midioutprepareheader.md) function but before sending MIDI events to the device, create a nonsignaled event by calling the [ResetEvent](http://go.microsoft.com/fwlink/p/?linkid=17120) function, specifying the event handle retrieved by **CreateEvent**. Then, inside a loop that checks whether the MHDR\_DONE bit is set in the **dwFlags** member of the [**MIDIHDR**](midihdr.md) structure, use the [WaitForSingleObject](http://go.microsoft.com/fwlink/p/?linkid=17121) function, specifying the event handle and a time-out value of INFINITE as parameters.

An event callback is set by anything that might cause a function callback.

Because event callbacks do not receive specific close, done, or open notifications, an application may need to check the status of the process it is waiting for after the event occurs. It is possible that a number of tasks could be completed by the time **WaitForSingleObject** returns.

 

 




