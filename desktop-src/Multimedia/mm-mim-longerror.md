---
title: MM_MIM_LONGERROR message (Mmsystem.h)
description: The MM\_MIM\_LONGERROR message is sent to a window when an invalid or incomplete MIDI system-exclusive message is received.
ms.assetid: 2de4c2f8-2ded-4994-934c-6e72c95637b2
keywords:
- MM_MIM_LONGERROR message Windows Multimedia
topic_type:
- apiref
api_name:
- MM_MIM_LONGERROR
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MM\_MIM\_LONGERROR message

The **MM\_MIM\_LONGERROR** message is sent to a window when an invalid or incomplete MIDI system-exclusive message is received.


```C++
MM_MIM_LONGERROR 
wParam = (WPARAM) hInput 
lParam = (LPARAM) lpMidiHdr 
```



## Parameters

<dl> <dt>

<span id="hInput"></span><span id="hinput"></span><span id="HINPUT"></span>*hInput*
</dt> <dd>

Handle to the MIDI input device that received the invalid message.

</dd> <dt>

<span id="lpMidiHdr"></span><span id="lpmidihdr"></span><span id="LPMIDIHDR"></span>*lpMidiHdr*
</dt> <dd>

Pointer to a [**MIDIHDR**](/windows/win32/api/mmeapi/ns-mmeapi-midihdr) structure identifying the buffer containing the invalid message.

</dd> </dl>

## Return Value

This message does not return a value.

## Remarks

The returned buffer might not be full. To determine the number of bytes recorded into the returned buffer, use the **dwBytesRecorded** member of the [**MIDIHDR**](/windows/win32/api/mmeapi/ns-mmeapi-midihdr) structure specified by *lpMidiHdr*.

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

 

