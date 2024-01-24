---
title: WM_CAP_SET_CALLBACK_YIELD message (Vfw.h)
description: The WM\_CAP\_SET\_CALLBACK\_YIELD message sets a callback function in the application. AVICap calls this procedure when the capture window yields during streaming capture. You can send this message explicitly or by using the capSetCallbackOnYield macro.
ms.assetid: d978dc3b-4336-46a4-85ae-7d588a63489b
keywords:
- WM_CAP_SET_CALLBACK_YIELD message Windows Multimedia
topic_type:
- apiref
api_name:
- WM_CAP_SET_CALLBACK_YIELD
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CAP\_SET\_CALLBACK\_YIELD message

The **WM\_CAP\_SET\_CALLBACK\_YIELD** message sets a callback function in the application. AVICap calls this procedure when the capture window yields during streaming capture. You can send this message explicitly or by using the [**capSetCallbackOnYield**](/windows/desktop/api/Vfw/nf-vfw-capsetcallbackonyield) macro.


```C++
WM_CAP_SET_CALLBACK_YIELD 
wParam = (WPARAM) 0; 
lParam = (LPARAM) (LPVOID) (fpProc); 
```



## Parameters

<dl> <dt>

<span id="fpProc"></span><span id="fpproc"></span><span id="FPPROC"></span>*fpProc*
</dt> <dd>

Pointer to the yield callback function, of type [**capYieldCallback**](/windows/desktop/api/Vfw/nc-vfw-capyieldcallback). Specify **NULL** for this parameter to disable a previously installed yield callback function.

</dd> </dl>

## Return Value

Returns **TRUE** if successful or **FALSE** if streaming capture or a single-frame capture session is in progress.

## Remarks

Applications can optionally set a yield callback function. The yield callback function is called at least once for each video frame captured during streaming capture. If a yield callback function is installed, it will be called regardless of the state of the **fYield** member of the [**CAPTUREPARMS**](/windows/win32/api/vfw/ns-vfw-captureparms) structure.

If the yield callback function is used, it must be installed before starting the capture session and it must remain enabled for the duration of the session. It can be disabled after streaming capture ends.

Applications typically perform some type of message processing in the callback function consisting of a [PeekMessage](/windows/win32/api/winuser/nf-winuser-peekmessagea), [TranslateMessage](/windows/win32/api/winuser/nf-winuser-translatemessage), [DispatchMessage](/windows/win32/api/winuser/nf-winuser-dispatchmessage) loop, as in the message loop of a [WinMain](/windows/win32/api/winbase/nf-winbase-winmain) function. The yield callback function must also filter and remove messages that can cause reentrancy problems.

An application typically returns **TRUE** in the yield procedure to continue streaming capture. If a yield callback function returns **FALSE**, the capture window stops the capture process.

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

 

