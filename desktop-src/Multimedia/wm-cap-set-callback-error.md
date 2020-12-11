---
title: WM_CAP_SET_CALLBACK_ERROR message (Vfw.h)
description: The WM\_CAP\_SET\_CALLBACK\_ERROR message sets an error callback function in the client application. AVICap calls this procedure when errors occur. You can send this message explicitly or by using the capSetCallbackOnError macro.
ms.assetid: 4eb57515-9b5a-466c-bbaa-fdee3bca19db
keywords:
- WM_CAP_SET_CALLBACK_ERROR message Windows Multimedia
topic_type:
- apiref
api_name:
- WM_CAP_SET_CALLBACK_ERROR
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CAP\_SET\_CALLBACK\_ERROR message

The **WM\_CAP\_SET\_CALLBACK\_ERROR** message sets an error callback function in the client application. AVICap calls this procedure when errors occur. You can send this message explicitly or by using the [**capSetCallbackOnError**](/windows/desktop/api/Vfw/nf-vfw-capsetcallbackonerror) macro.


```C++
WM_CAP_SET_CALLBACK_ERROR 
wParam = (WPARAM) 0; 
lParam = (LPARAM) (LPVOID) (fpProc); 
```



## Parameters

<dl> <dt>

<span id="fpProc"></span><span id="fpproc"></span><span id="FPPROC"></span>*fpProc*
</dt> <dd>

Pointer to the error callback function, of type [**capErrorCallback**](/windows/desktop/api/Vfw/nc-vfw-caperrorcallbacka). Specify **NULL** for this parameter to disable a previously installed error callback function.

</dd> </dl>

## Return Value

Returns **TRUE** if successful or **FALSE** if streaming capture or a single-frame capture session is in progress.

## Remarks

Applications can optionally set an error callback function. If set, AVICap calls the error procedure in the following situations:

-   The disk is full.
-   A capture window cannot be connected with a capture driver.
-   A waveform-audio device cannot be opened.
-   The number of frames dropped during capture exceeds the specified percentage.
-   The frames cannot be captured due to vertical synchronization interrupt problems.

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

 

 





