---
title: WM\_CAP\_SET\_AUDIOFORMAT message
description: The WM\_CAP\_SET\_AUDIOFORMAT message sets the audio format to use when performing streaming or step capture. You can send this message explicitly or by using the capSetAudioFormat macro.
ms.assetid: 8bffa401-3d36-43bb-9f69-988ebc69b860
keywords:
- WM_CAP_SET_AUDIOFORMAT message Windows Multimedia
topic_type:
- apiref
api_name:
- WM_CAP_SET_AUDIOFORMAT
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WM\_CAP\_SET\_AUDIOFORMAT message

The **WM\_CAP\_SET\_AUDIOFORMAT** message sets the audio format to use when performing streaming or step capture. You can send this message explicitly or by using the [**capSetAudioFormat**](/windows/win32/Vfw/nf-vfw-capsetaudioformat?branch=master) macro.


```C++
WM_CAP_SET_AUDIOFORMAT 
wParam = (WPARAM) (wSize); 
lParam = (LPARAM) (LPVOID) (LPWAVEFORMATEX) (psAudioFormat); 
```



## Parameters

<dl> <dt>

<span id="wSize"></span><span id="wsize"></span><span id="WSIZE"></span>*wSize*
</dt> <dd>

Size, in bytes, of the structure referenced by **s**.

</dd> <dt>

<span id="psAudioFormat"></span><span id="psaudioformat"></span><span id="PSAUDIOFORMAT"></span>*psAudioFormat*
</dt> <dd>

Pointer to a [**WAVEFORMATEX**](/windows/win32/Mmreg/?branch=master) or [**PCMWAVEFORMAT**](pcmwaveformat.md) structure that defines the audio format.

</dd> </dl>

## Return Value

Returns **TRUE** if successful or **FALSE** otherwise.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[Video Capture](video-capture.md)
</dt> <dt>

[Video Capture Messages](video-capture-messages.md)
</dt> </dl>

 

 





