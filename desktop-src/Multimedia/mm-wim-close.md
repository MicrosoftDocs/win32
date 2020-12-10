---
title: MM_WIM_CLOSE message (Mmsystem.h)
description: The MM\_WIM\_CLOSE message is sent to a window when a waveform-audio input device is closed. The device handle is no longer valid after this message has been sent.
ms.assetid: 4ea35b66-6bfa-41f0-9d52-a8cf2b0a69dd
keywords:
- MM_WIM_CLOSE message Windows Multimedia
topic_type:
- apiref
api_name:
- MM_WIM_CLOSE
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MM\_WIM\_CLOSE message

The **MM\_WIM\_CLOSE** message is sent to a window when a waveform-audio input device is closed. The device handle is no longer valid after this message has been sent.


```C++
MM_WIM_CLOSE 
wParam = (WPARAM) hInputDev 
lParam = reserved 
```



## Parameters

<dl> <dt>

<span id="hInputDev"></span><span id="hinputdev"></span><span id="HINPUTDEV"></span>*hInputDev*
</dt> <dd>

Handle to the waveform-audio input device that was closed.

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

 

 





