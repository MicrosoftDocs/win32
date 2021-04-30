---
title: MCIWNDM_NOTIFYMEDIA message (Vfw.h)
description: The MCIWNDM\_NOTIFYMEDIA message notifies the parent window of an application that the media has changed.
ms.assetid: cc31502d-09a9-4580-9ff8-9c2be51c8e35
keywords:
- MCIWNDM_NOTIFYMEDIA message Windows Multimedia
topic_type:
- apiref
api_name:
- MCIWNDM_NOTIFYMEDIA
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCIWNDM\_NOTIFYMEDIA message

The **MCIWNDM\_NOTIFYMEDIA** message notifies the parent window of an application that the media has changed.


```C++
MCIWNDM_NOTIFYMEDIA 
wParam = (WPARAM) (HWND) hwnd; 
lParam = (LPARAM) (LPSTR) lp; 
```



## Parameters

<dl> <dt>

<span id="hwnd"></span><span id="HWND"></span>*hwnd*
</dt> <dd>

Handle to the MCIWnd window.

</dd> <dt>

<span id="lp"></span><span id="LP"></span>*lp*
</dt> <dd>

Pointer to a null-terminated string containing the new filename. If the media is closing, it specifies a null string.

</dd> </dl>

## Remarks

You can enable notification of media changes by specifying the MCIWNDF\_NOTIFYMEDIA window style.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



 

 





