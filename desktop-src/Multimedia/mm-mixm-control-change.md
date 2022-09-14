---
title: MM_MIXM_CONTROL_CHANGE message (Mmsystem.h)
description: The MM\_MIXM\_CONTROL\_CHANGE message is sent by a mixer device to notify an application that the state of a control associated with an audio line has changed. The application should refresh its display and cached values for the specified control.
ms.assetid: 921c55a7-86c0-43d1-b817-bfbd3c4bb28b
keywords:
- MM_MIXM_CONTROL_CHANGE message Windows Multimedia
topic_type:
- apiref
api_name:
- MM_MIXM_CONTROL_CHANGE
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MM\_MIXM\_CONTROL\_CHANGE message

The **MM\_MIXM\_CONTROL\_CHANGE** message is sent by a mixer device to notify an application that the state of a control associated with an audio line has changed. The application should refresh its display and cached values for the specified control.


```C++
MM_MIXM_CONTROL_CHANGE 
wParam = (WPARAM) hMixer 
lParam = (LPARAM) dwControlID 
```



## Parameters

<dl> <dt>

<span id="hMixer"></span><span id="hmixer"></span><span id="HMIXER"></span>*hMixer*
</dt> <dd>

Handle to the mixer device (**HMIXER**) that sent the notification message.

</dd> <dt>

<span id="dwControlID"></span><span id="dwcontrolid"></span><span id="DWCONTROLID"></span>*dwControlID*
</dt> <dd>

Control identifier for the mixer control that has changed state. This identifier is the same as the**dwControlID** member of the**MIXERCONTROL**structure returned by the**mixerGetLineControls**function.

</dd> </dl>

## Remarks

An application must open a mixer device and specify a callback window to receive the **MM\_MIXM\_CONTROL\_CHANGE** message.

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

 

 





