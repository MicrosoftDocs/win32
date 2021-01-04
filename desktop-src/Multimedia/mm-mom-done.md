---
title: MM_MOM_DONE message (Mmsystem.h)
description: The MM\_MOM\_DONE message is sent to a window when the specified MIDI system-exclusive or stream buffer has been played and is being returned to the application.
ms.assetid: 4651d5b4-3c98-4fa7-b761-dafb30e0d31e
keywords:
- MM_MOM_DONE message Windows Multimedia
topic_type:
- apiref
api_name:
- MM_MOM_DONE
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MM\_MOM\_DONE message

The **MM\_MOM\_DONE** message is sent to a window when the specified MIDI system-exclusive or stream buffer has been played and is being returned to the application.


```C++
MM_MOM_DONE 
wParam = (WPARAM) hOutput 
lParam = (LPARAM) lpMidiHdr 
```



## Parameters

<dl> <dt>

<span id="hOutput"></span><span id="houtput"></span><span id="HOUTPUT"></span>*hOutput*
</dt> <dd>

Handle to the MIDI output device that played the buffer.

</dd> <dt>

<span id="lpMidiHdr"></span><span id="lpmidihdr"></span><span id="LPMIDIHDR"></span>*lpMidiHdr*
</dt> <dd>

Pointer to a [**MIDIHDR**](/windows/win32/api/mmeapi/ns-mmeapi-midihdr) structure identifying the buffer.

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

[MIDI Messages](midi-messages.md)
</dt> </dl>

 

