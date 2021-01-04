---
title: MM_WOM_OPEN message (Mmsystem.h)
description: The MM\_WOM\_OPEN message is sent to a window when the given waveform-audio output device is opened.
ms.assetid: 1b0366de-61cd-4203-9173-ababaefdb153
keywords:
- MM_WOM_OPEN message Windows Multimedia
topic_type:
- apiref
api_name:
- MM_WOM_OPEN
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MM\_WOM\_OPEN message

The **MM\_WOM\_OPEN** message is sent to a window when the given waveform-audio output device is opened.


```C++
MM_WOM_OPEN 
wParam = (WPARAM) hOutputDev 
lParam = reserved 
```



## Parameters

<dl> <dt>

<span id="hOutputDev"></span><span id="houtputdev"></span><span id="HOUTPUTDEV"></span>*hOutputDev*
</dt> <dd>

Handle to the device that was opened.

</dd> <dt>

<span id="lParam"></span><span id="lparam"></span><span id="LPARAM"></span>*lParam*
</dt> <dd>

Reserved; must be zero.

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

[Waveform Audio](waveform-audio.md)
</dt> <dt>

[Waveform Messages](waveform-messages.md)
</dt> </dl>

 

 





