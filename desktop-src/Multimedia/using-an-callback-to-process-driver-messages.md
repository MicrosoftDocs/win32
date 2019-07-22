---
title: Using an Event Callback to Process Driver Messages
description: Using an Event Callback to Process Driver Messages
ms.assetid: 5b17ff93-ed00-46ee-828c-baf716c9257c
keywords:
- waveform audio,event callback
- audio data blocks,event callback
- waveform audio,processing driver messages
- audio data blocks,processing driver messages
- processing driver messages
- CreateEvent function
ms.topic: article
ms.date: 05/31/2018
---

# Using an Event Callback to Process Driver Messages

To use an event callback, use the [**CreateEvent**](https://docs.microsoft.com/windows/desktop/api/synchapi/nf-synchapi-createeventa) function to create a manual-reset event. In the call to the [**waveOutOpen**](https://msdn.microsoft.com/en-us/library/Dd743866(v=VS.85).aspx) function, specify **CALLBACK\_EVENT** for the *fdwOpen* parameter. After you call the [**waveOutPrepareHeader**](https://msdn.microsoft.com/en-us/library/Dd743868(v=VS.85).aspx) function, but before sending waveform-audio data to the device, put the event into a nonsignaled state by calling the [**ResetEvent**](https://docs.microsoft.com/windows/desktop/api/synchapi/nf-synchapi-resetevent) function. Then, inside a loop that checks whether the **WHDR\_DONE** flag is set in the **dwFlags** member of the [**WAVEHDR**](https://msdn.microsoft.com/en-us/library/Dd743837(v=VS.85).aspx) structure, call the [WaitForSingleObject](https://go.microsoft.com/fwlink/p/?linkid=17121) function, specifying as parameters the event handle and a time-out value.

Because event callbacks do not receive specific close, done, or open notifications, an application might have to check the status of the process it is waiting for after the event occurs. It is possible that a number of tasks could have been completed by the time [**WaitForSingleObject**](https://docs.microsoft.com/windows/desktop/api/synchapi/nf-synchapi-waitforsingleobject) returns.

## Related topics

<dl> <dt>

[Audio Data Blocks](audio-data-blocks.md)
</dt> </dl>

 

 




