---
title: MOM_DONE message (Mciapi.h)
description: The MOM\_DONE message is sent to a MIDI output callback function when the specified system-exclusive or stream buffer has been played and is being returned to the application.
ms.assetid: '0b9bd0e1-c87d-4f21-912e-5ac9f5c04192'
keywords:
- MOM_DONE message Windows Multimedia
topic_type:
- apiref
api_name:
- MOM_DONE
api_location:
- mciapi.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MOM\_DONE message

The **MOM\_DONE** message is sent to a MIDI output callback function when the specified system-exclusive or stream buffer has been played and is being returned to the application.


```C++
MOM_DONE 
dwParam1 = (DWORD) lpMidiHdr 
dwParam2 = reserved 
```



## Parameters

<dl> <dt>

<span id="lpMidiHdr"></span><span id="lpmidihdr"></span><span id="LPMIDIHDR"></span>*lpMidiHdr*
</dt> <dd>

Pointer to a [**MIDIHDR**](/windows/win32/api/mmeapi/ns-mmeapi-midihdr) structure identifying the buffer.

</dd> <dt>

<span id="dwParam2"></span><span id="dwparam2"></span><span id="DWPARAM2"></span>*dwParam2*
</dt> <dd>

Reserved; do not use.

</dd> </dl>

## Return Value

This message does not return a value.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Mciapi.h</dt> </dl> |



## See also

<dl> <dt>

[MIDI Messages](midi-messages.md)
</dt> </dl>

 

