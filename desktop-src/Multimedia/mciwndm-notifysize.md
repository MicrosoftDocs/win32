---
title: MCIWNDM_NOTIFYSIZE message (Vfw.h)
description: The MCIWNDM\_NOTIFYSIZE message notifies the parent window of an application that the window size has changed.
ms.assetid: 76e1f663-bfc6-4d3c-9486-c8c7f79e4265
keywords:
- MCIWNDM_NOTIFYSIZE message Windows Multimedia
topic_type:
- apiref
api_name:
- MCIWNDM_NOTIFYSIZE
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCIWNDM\_NOTIFYSIZE message

The **MCIWNDM\_NOTIFYSIZE** message notifies the parent window of an application that the window size has changed.


```C++
MCIWNDM_NOTIFYSIZE 
wParam = (WPARAM) (HWND) hwnd; 
lParam = 0; 
```



## Parameters

<dl> <dt>

<span id="hwnd"></span><span id="HWND"></span>*hwnd*
</dt> <dd>

Handle to the MCIWnd window.

</dd> </dl>

## Remarks

You can enable notification of changes in the size of an MCIWnd window by specifying the MCIWNDF\_NOTIFYSIZE window style.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



 

 





