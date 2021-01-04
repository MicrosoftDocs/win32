---
title: MIM_ERROR message (Mmsystem.h)
description: The MIM\_ERROR message is sent to a MIDI input callback function when an invalid MIDI message is received.
ms.assetid: ea720da5-1f18-4d0d-ac9d-45cd1c3219d6
keywords:
- MIM_ERROR message Windows Multimedia
topic_type:
- apiref
api_name:
- MIM_ERROR
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MIM\_ERROR message

The **MIM\_ERROR** message is sent to a MIDI input callback function when an invalid MIDI message is received.


```C++
MIM_ERROR 
dwParam1 = dwMidiMessage 
dwParam2 = dwTimestamp 
```



## Parameters

<dl> <dt>

<span id="dwMidiMessage"></span><span id="dwmidimessage"></span><span id="DWMIDIMESSAGE"></span>*dwMidiMessage*
</dt> <dd>

Invalid MIDI message that was received. The message is packed into a doubleword value with the first byte of the message in the low-order byte.

</dd> <dt>

<span id="dwTimestamp"></span><span id="dwtimestamp"></span><span id="DWTIMESTAMP"></span>*dwTimestamp*
</dt> <dd>

Time that the message was received by the input device driver. The time stamp is specified in milliseconds, beginning at zero when the [**midiInStart**](/windows/win32/api/mmeapi/nf-mmeapi-midiinstart) function was called.

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

 

