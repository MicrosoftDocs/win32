---
title: MM_MIM_DATA message (Mmsystem.h)
description: The MM\_MIM\_DATA message is sent to a window when a complete MIDI message is received by a MIDI input device.
ms.assetid: 9c580e48-78f3-4914-bdea-393823fb8482
keywords:
- MM_MIM_DATA message Windows Multimedia
topic_type:
- apiref
api_name:
- MM_MIM_DATA
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MM\_MIM\_DATA message

The **MM\_MIM\_DATA** message is sent to a window when a complete MIDI message is received by a MIDI input device.


```C++
MM_MIM_DATA 
wParam = (WPARAM) hInput 
lParam = (LPARAM) (DWORD) lMidiMessage 
```



## Parameters

<dl> <dt>

<span id="hInput"></span><span id="hinput"></span><span id="HINPUT"></span>*hInput*
</dt> <dd>

Handle to the MIDI input device that received the MIDI message.

</dd> <dt>

<span id="lMidiMessage"></span><span id="lmidimessage"></span><span id="LMIDIMESSAGE"></span>*lMidiMessage*
</dt> <dd>

MIDI message that was received. The message is packed into a doubleword value as follows:



| Requirement | Value | Description |
|-----------|-----------------|-----------------------------------------------------|
| High word | High-order byte | Not used.                                           |
|           | Low-order byte  | Contains a second byte of MIDI data (when needed).  |
| Low word  | High-order byte | Contains the first byte of MIDI data (when needed). |
|           | Low-order byte  | Contains the MIDI status.                           |



 

The two MIDI data bytes are optional, depending on the MIDI status byte.

</dd> </dl>

## Return Value

This message does not return a value.

## Remarks

MIDI messages received from a MIDI input port have running status disabled; each message is expanded to include the MIDI status byte.

This message is not sent when a MIDI system-exclusive message is received. No time stamp is available with this message. For time-stamped input data, you must use the messages that are sent to callback functions.

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

 

 





