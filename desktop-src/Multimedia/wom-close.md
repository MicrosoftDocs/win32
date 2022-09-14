---
title: WOM_CLOSE message (Mmsystem.h)
description: The WOM\_CLOSE message is sent to a waveform-audio output callback function when a waveform-audio output device is closed. The device handle is no longer valid after this message has been sent.
ms.assetid: 'ac20216a-6a60-4e62-8241-3ca6f33567f1'
keywords:
- WOM_CLOSE message Windows Multimedia
topic_type:
- apiref
api_name:
- WOM_CLOSE
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WOM\_CLOSE message

The **WOM\_CLOSE** message is sent to a waveform-audio output callback function when a waveform-audio output device is closed. The device handle is no longer valid after this message has been sent.


```C++
WOM_CLOSE 
dwParam1 = reserved 
dwParam2 = reserved 
```



## Parameters

<dl> <dt>

<span id="dwParam1"></span><span id="dwparam1"></span><span id="DWPARAM1"></span>*dwParam1*
</dt> <dd>

Reserved; must be zero.

</dd> <dt>

<span id="dwParam2"></span><span id="dwparam2"></span><span id="DWPARAM2"></span>*dwParam2*
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

 

 





