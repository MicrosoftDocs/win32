---
title: WIM\_CLOSE message
description: The WIM\_CLOSE message is sent to the given waveform-audio input callback function when a waveform-audio input device is closed. The device handle is no longer valid after this message has been sent.
ms.assetid: '4ea35b66-6bfa-41f0-9d52-a8cf2b0a69dd'
keywords: ["WIM_CLOSE message Windows Multimedia"]
topic_type:
- apiref
api_name:
- WIM_CLOSE
api_location:
- Mmsystem.h
api_type:
- HeaderDef
---

# WIM\_CLOSE message

The **WIM\_CLOSE** message is sent to the given waveform-audio input callback function when a waveform-audio input device is closed. The device handle is no longer valid after this message has been sent.


```C++
WIM_CLOSE 
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



|                                     |                                                                                                           |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Mmsystem.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Waveform Audio](waveform-audio.md)
</dt> <dt>

[Waveform Messages](waveform-messages.md)
</dt> </dl>

 

 





