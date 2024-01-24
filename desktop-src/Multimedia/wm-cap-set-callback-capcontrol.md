---
title: WM_CAP_SET_CALLBACK_CAPCONTROL message (Vfw.h)
description: The WM\_CAP\_SET\_CALLBACK\_CAPCONTROL message sets a callback function in the application giving it precise recording control. You can send this message explicitly or by using the capSetCallbackOnCapControl macro.
ms.assetid: 1e93ed7b-8205-45fe-bdcf-efe3f709f728
keywords:
- WM_CAP_SET_CALLBACK_CAPCONTROL message Windows Multimedia
topic_type:
- apiref
api_name:
- WM_CAP_SET_CALLBACK_CAPCONTROL
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CAP\_SET\_CALLBACK\_CAPCONTROL message

The **WM\_CAP\_SET\_CALLBACK\_CAPCONTROL** message sets a callback function in the application giving it precise recording control. You can send this message explicitly or by using the [**capSetCallbackOnCapControl**](/windows/desktop/api/Vfw/nf-vfw-capsetcallbackoncapcontrol) macro.


```C++
WM_CAP_SET_CALLBACK_CAPCONTROL 
wParam = (WPARAM) 0; 
lParam = (LPARAM) (LPVOID) (fpProc); 
```



## Parameters

<dl> <dt>

<span id="fpProc"></span><span id="fpproc"></span><span id="FPPROC"></span>*fpProc*
</dt> <dd>

Pointer to the callback function, of type [**capControlCallback**](/windows/desktop/api/Vfw/nc-vfw-capcontrolcallback). Specify **NULL** for this parameter to disable a previously installed callback function.

</dd> </dl>

## Return Value

Returns **TRUE** if successful or **FALSE** if a streaming capture or a single-frame capture session is in progress.

## Remarks

A single callback function is used to give the application precise control over the moments that streaming capture begins and completes. The capture window first calls the procedure with *nState* set to CONTROLCALLBACK\_PREROLL after all buffers have been allocated and all other capture preparations have finished. This gives the application the ability to preroll video sources, returning from the callback function at the exact moment recording is to begin. A return value of **TRUE** from the callback function continues capture, and a return value of **FALSE** aborts capture. After capture begins, this callback function will be called frequently with *nState* set to CONTROLCALLBACK\_CAPTURING to allow the application to end capture by returning **FALSE**.

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

 

 





