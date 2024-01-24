---
title: WM_CAP_SET_CALLBACK_STATUS message (Vfw.h)
description: The WM\_CAP\_SET\_CALLBACK\_STATUS message sets a status callback function in the application. AVICap calls this procedure whenever the capture window status changes. You can send this message explicitly or by using the capSetCallbackOnStatus macro.
ms.assetid: 451ba9f9-7bfb-4c57-af6c-d5f691f39618
keywords:
- WM_CAP_SET_CALLBACK_STATUS message Windows Multimedia
topic_type:
- apiref
api_name:
- WM_CAP_SET_CALLBACK_STATUS
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CAP\_SET\_CALLBACK\_STATUS message

The **WM\_CAP\_SET\_CALLBACK\_STATUS** message sets a status callback function in the application. AVICap calls this procedure whenever the capture window status changes. You can send this message explicitly or by using the [**capSetCallbackOnStatus**](/windows/desktop/api/Vfw/nf-vfw-capsetcallbackonstatus) macro.


```C++
WM_CAP_SET_CALLBACK_STATUS 
wParam = (WPARAM) 0; 
lParam = (LPARAM) (LPVOID) (fpProc); 
```



## Parameters

<dl> <dt>

<span id="fpProc"></span><span id="fpproc"></span><span id="FPPROC"></span>*fpProc*
</dt> <dd>

Pointer to the status callback function, of type [**capStatusCallback**](/windows/desktop/api/Vfw/nc-vfw-capstatuscallbacka). Specify **NULL** for this parameter to disable a previously installed status callback function.

</dd> </dl>

## Return Value

Returns **TRUE** if successful or **FALSE** if streaming capture or a single-frame capture session is in progress.

## Remarks

Applications can optionally set a status callback function. If set, AVICap calls this procedure in the following situations:

-   A capture session is completed.
-   A capture driver successfully connected to a capture window.
-   An optimal palette is created.
-   The number of captured frames is reported.

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

 

 





