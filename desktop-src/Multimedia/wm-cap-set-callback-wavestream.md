---
title: WM_CAP_SET_CALLBACK_WAVESTREAM message (Vfw.h)
description: The WM\_CAP\_SET\_CALLBACK\_WAVESTREAM message sets a callback function in the application.
ms.assetid: f2554cbb-73de-4f76-b785-6c18c82c2992
keywords:
- WM_CAP_SET_CALLBACK_WAVESTREAM message Windows Multimedia
topic_type:
- apiref
api_name:
- WM_CAP_SET_CALLBACK_WAVESTREAM
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CAP\_SET\_CALLBACK\_WAVESTREAM message

The **WM\_CAP\_SET\_CALLBACK\_WAVESTREAM** message sets a callback function in the application. AVICap calls this procedure during streaming capture when a new audio buffer becomes available. You can send this message explicitly or by using the [**capSetCallbackOnWaveStream**](/windows/desktop/api/Vfw/nf-vfw-capsetcallbackonwavestream) macro.


```C++
WM_CAP_SET_CALLBACK_WAVESTREAM 
wParam = (WPARAM) 0; 
lParam = (LPARAM) (LPVOID) (fpProc); 
```



## Parameters

<dl> <dt>

<span id="fpProc"></span><span id="fpproc"></span><span id="FPPROC"></span>*fpProc*
</dt> <dd>

Pointer to the wave stream callback function, of type [**capWaveStreamCallback**](/windows/desktop/api/Vfw/nc-vfw-capwavecallback). Specify **NULL** for this parameter to disable a previously installed wave stream callback function.

</dd> </dl>

## Return Value

Returns **TRUE** if successful or **FALSE** if streaming capture or a single-frame capture session is in progress.

## Remarks

The capture window calls the procedure before writing the audio buffer to disk. This allows applications to modify the audio buffer if desired.

If a wave stream callback function is used, it must be installed before starting the capture session and it must remain enabled for the duration of the session. It can be disabled after streaming capture ends.

## Requirements



| Requirement | Value |
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

 

 





