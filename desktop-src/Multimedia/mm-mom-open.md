---
title: MM_MOM_OPEN message (Mmsystem.h)
description: The MM\_MOM\_OPEN message is sent to a window when a MIDI output device is opened.
ms.assetid: 1374a07c-02fa-4b43-82df-cbd96302aec5
keywords:
- MM_MOM_OPEN message Windows Multimedia
topic_type:
- apiref
api_name:
- MM_MOM_OPEN
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MM\_MOM\_OPEN message

The **MM\_MOM\_OPEN** message is sent to a window when a MIDI output device is opened.


```C++
MM_MOM_OPEN 
wParam = (WPARAM) hOutput 
lParam = reserved 
```



## Parameters

<dl> <dt>

<span id="hOutput"></span><span id="houtput"></span><span id="HOUTPUT"></span>*hOutput*
</dt> <dd>

Handle to the MIDI output device.

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

[MIDI Messages](midi-messages.md)
</dt> </dl>

 

 





