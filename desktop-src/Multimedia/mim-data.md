---
title: MIM_DATA message
description: The MIM\_DATA message is sent to a MIDI input callback function when a MIDI message is received by a MIDI input device.
ms.assetid: 966aab84-420a-42ce-9989-da5910ced9c0
keywords:
- MIM_DATA message Windows Multimedia
topic_type:
- apiref
api_name:
- MIM_DATA
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MIM\_DATA message

The **MIM\_DATA** message is sent to a MIDI input callback function when a MIDI message is received by a MIDI input device.


```C++
MIM_DATA 
dwParam1 = dwMidiMessage 
dwParam2 = dwTimestamp 
```



## Parameters

<dl> <dt>

<span id="dwMidiMessage"></span><span id="dwmidimessage"></span><span id="DWMIDIMESSAGE"></span>*dwMidiMessage*
</dt> <dd>

MIDI message that was received. The message is packed into a doubleword value as follows:



|           |                 |                                                     |
|-----------|-----------------|-----------------------------------------------------|
| High word | High-order byte | Not used.                                           |
|           | Low-order byte  | Contains a second byte of MIDI data (when needed).  |
| Low word  | High-order byte | Contains the first byte of MIDI data (when needed). |
|           | Low-order byte  | Contains the MIDI status.                           |



 

The two MIDI data bytes are optional, depending on the MIDI status byte.

</dd> <dt>

<span id="dwTimestamp"></span><span id="dwtimestamp"></span><span id="DWTIMESTAMP"></span>*dwTimestamp*
</dt> <dd>

Time that the message was received by the input device driver. The time stamp is specified in milliseconds, beginning at zero when the [**midiInStart**](https://msdn.microsoft.com/en-us/library/Dd798462(v=VS.85).aspx) function was called.

</dd> </dl>

## Return Value

This message does not return a value.

## Remarks

MIDI messages received from a MIDI input port have running status disabled; each message is expanded to include the MIDI status byte.

This message is not sent when a MIDI system-exclusive message is received.

## Requirements



|                                     |                                                                                                           |
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

 

 





