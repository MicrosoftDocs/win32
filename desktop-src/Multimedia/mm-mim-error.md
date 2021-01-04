---
title: MM_MIM_ERROR message (Mmsystem.h)
description: The MM\_MIM\_ERROR message is sent to a window when an invalid MIDI message is received.
ms.assetid: 03760bfc-a4ef-48cd-97a9-1b93b56fc641
keywords:
- MM_MIM_ERROR message Windows Multimedia
topic_type:
- apiref
api_name:
- MM_MIM_ERROR
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MM\_MIM\_ERROR message

The **MM\_MIM\_ERROR** message is sent to a window when an invalid MIDI message is received.


```C++
MM_MIM_ERROR 
wParam = (WPARAM) hInput 
lParam = (LPARAM) (DWORD) lMidiMessage 
```



## Parameters

<dl> <dt>

<span id="hInput"></span><span id="hinput"></span><span id="HINPUT"></span>*hInput*
</dt> <dd>

Handle to the MIDI input device that received the invalid message.

</dd> <dt>

<span id="lMidiMessage"></span><span id="lmidimessage"></span><span id="LMIDIMESSAGE"></span>*lMidiMessage*
</dt> <dd>

Invalid MIDI message. The message is packed into a **DWORD** value with the first byte of the message in the low-order byte.

</dd> </dl>

## Return Value

This message does not return a value.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Mmsystem.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Musical Instrument Digital Interface (MIDI)](musical-instrument-digital-interface--midi.md)
</dt> <dt>

[MIDI Messages](midi-messages.md)
</dt> </dl>

 

 





