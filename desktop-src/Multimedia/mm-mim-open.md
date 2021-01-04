---
title: MM_MIM_OPEN message (Mmsystem.h)
description: The MM\_MIM\_OPEN message is sent to a window when a MIDI input device is opened.
ms.assetid: 8dfc24a0-0ab8-4f49-954f-0c0a55fa28bc
keywords:
- MM_MIM_OPEN message Windows Multimedia
topic_type:
- apiref
api_name:
- MM_MIM_OPEN
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MM\_MIM\_OPEN message

The **MM\_MIM\_OPEN** message is sent to a window when a MIDI input device is opened.


```C++
MM_MIM_OPEN 
wParam = (WPARAM) hInput 
lParam = reserved 
```



## Parameters

<dl> <dt>

<span id="hInput"></span><span id="hinput"></span><span id="HINPUT"></span>*hInput*
</dt> <dd>

Handle to the MIDI input device that was opened.

</dd> <dt>

<span id="lParam"></span><span id="lparam"></span><span id="LPARAM"></span>*lParam*
</dt> <dd>

Reserved; do not use.

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

 

 





