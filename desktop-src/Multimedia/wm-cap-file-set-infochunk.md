---
title: WM\_CAP\_FILE\_SET\_INFOCHUNK message
description: The WM\_CAP\_FILE\_SET\_INFOCHUNK message sets and clears information chunks.
ms.assetid: '67d11a05-a2b4-45d2-ba66-83a198745303'
keywords: ["WM_CAP_FILE_SET_INFOCHUNK message Windows Multimedia"]
topic_type:
- apiref
api_name:
- WM_CAP_FILE_SET_INFOCHUNK
api_location:
- Vfw.h
api_type:
- HeaderDef
---

# WM\_CAP\_FILE\_SET\_INFOCHUNK message

The **WM\_CAP\_FILE\_SET\_INFOCHUNK** message sets and clears information chunks. Information chunks can be inserted in an AVI file during capture to embed text strings or custom data. You can send this message explicitly or by using the [**capFileSetInfoChunk**](capfilesetinfochunk.md) macro.


```C++
WM_CAP_FILE_SET_INFOCHUNK 
wParam = (WPARAM)0; 
lParam = (LPARAM) (LPCAPINFOCHUNK) (lpInfoChunk); 
```



## Parameters

<dl> <dt>

<span id="lpInfoChunk"></span><span id="lpinfochunk"></span><span id="LPINFOCHUNK"></span>*lpInfoChunk*
</dt> <dd>

Pointer to a [**CAPINFOCHUNK**](capinfochunk.md) structure defining the information chunk to be created or deleted.

</dd> </dl>

## Return Value

Returns **TRUE** if successful or **FALSE** otherwise.

If an error occurs and an error callback function is set using the [**WM\_CAP\_SET\_CALLBACK\_ERROR**](wm-cap-set-callback-error.md) message, the error callback function is called.

## Remarks

Multiple registered information chunks can be added to an AVI file. After an information chunk is set, it continues to be added to subsequent capture files until either the entry is cleared or all information chunk entries are cleared. To clear a single entry, specify the information chunk in the **fccInfoID** member and **NULL** in the **lpData** member of the [**CAPINFOCHUNK**](capinfochunk.md) structure. To clear all entries, specify **NULL** in **fccInfoID**.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[Video Capture](video-capture.md)
</dt> <dt>

[Video Capture Messages](video-capture-messages.md)
</dt> </dl>

 

 





