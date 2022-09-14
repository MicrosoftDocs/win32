---
title: WIM_DATA message (Mmsystem.h)
description: The WIM\_DATA message is sent to the given waveform-audio input callback function when waveform-audio data is present in the input buffer and the buffer is being returned to the application.
ms.assetid: '94cc02b8-61c4-44b9-9f8e-041fe989c1a6'
keywords:
- WIM_DATA message Windows Multimedia
topic_type:
- apiref
api_name:
- WIM_DATA
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WIM\_DATA message

The **WIM\_DATA** message is sent to the given waveform-audio input callback function when waveform-audio data is present in the input buffer and the buffer is being returned to the application. The message can be sent when the buffer is full or after the [**waveInReset**](/windows/win32/api/mmeapi/nf-mmeapi-waveinreset) function is called.


```C++
WIM_DATA 
dwParam1 = (DWORD) lpwvhdr 
dwParam2 = reserved 
```



## Parameters

<dl> <dt>

<span id="dwParam1"></span><span id="dwparam1"></span><span id="DWPARAM1"></span>*dwParam1*
</dt> <dd>

Pointer to a [**WAVEHDR**](/windows/win32/api/mmeapi/ns-mmeapi-wavehdr) structure that identifies the buffer containing the data.

</dd> <dt>

<span id="dwParam2"></span><span id="dwparam2"></span><span id="DWPARAM2"></span>*dwParam2*
</dt> <dd>

Reserved; must be zero.

</dd> </dl>

## Return Value

This message does not return a value.

## Remarks

The returned buffer might not be full. Use the **dwBytesRecorded** member of the [**WAVEHDR**](/windows/win32/api/mmeapi/ns-mmeapi-wavehdr) structure specified by *lpwvhdr* to determine the number of bytes recorded into the returned buffer.

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

 

