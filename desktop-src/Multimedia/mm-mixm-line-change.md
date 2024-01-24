---
title: MM_MIXM_LINE_CHANGE message (Mmsystem.h)
description: The MM\_MIXM\_LINE\_CHANGE message is sent by a mixer device to notify an application that the state of an audio line on the specified device has changed. The application should refresh its display and cached values for the specified audio line.
ms.assetid: 68ada0be-9dc5-4edf-b924-ef0d10a1b79a
keywords:
- MM_MIXM_LINE_CHANGE message Windows Multimedia
topic_type:
- apiref
api_name:
- MM_MIXM_LINE_CHANGE
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MM\_MIXM\_LINE\_CHANGE message

The **MM\_MIXM\_LINE\_CHANGE** message is sent by a mixer device to notify an application that the state of an audio line on the specified device has changed. The application should refresh its display and cached values for the specified audio line.


```C++
MM_MIXM_LINE_CHANGE 
wParam = (WPARAM) hMixer 
lParam = (LPARAM) dwLineID 
```



## Parameters

<dl> <dt>

<span id="hMixer"></span><span id="hmixer"></span><span id="HMIXER"></span>*hMixer*
</dt> <dd>

Handle to the mixer device that sent the notification message.

</dd> <dt>

<span id="dwLineID"></span><span id="dwlineid"></span><span id="DWLINEID"></span>*dwLineID*
</dt> <dd>

Line identifier for the audio line that has changed state. This identifier is the same as the**dwLineID** member of the**MIXERLINE**structure returned by the**mixerGetLineInfo**function.

</dd> </dl>

## Remarks

An application must open a mixer device and specify a callback window to receive the **MM\_MIXM\_LINE\_CHANGE** message.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Mmsystem.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Audio Mixers](audio-mixers.md)
</dt> <dt>

[Audio Mixer Messages](audio-mixer-messages.md)
</dt> </dl>

 

 





