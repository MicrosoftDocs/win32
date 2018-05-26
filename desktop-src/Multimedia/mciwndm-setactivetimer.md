---
title: MCIWNDM\_SETACTIVETIMER message
description: The MCIWNDM\_SETACTIVETIMER message sets the update period used by MCIWnd to update the trackbar in the MCIWnd window, update position information displayed in the window title bar, and send notification messages to the parent window when the MCIWnd window is active. You can send this message explicitly or by using the MCIWndSetActiveTimer macro.
ms.assetid: a30c0091-d9bb-44a3-a7b0-d1be30adcd9c
keywords:
- MCIWNDM_SETACTIVETIMER message Windows Multimedia
topic_type:
- apiref
api_name:
- MCIWNDM_SETACTIVETIMER
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

# MCIWNDM\_SETACTIVETIMER message

The **MCIWNDM\_SETACTIVETIMER** message sets the update period used by MCIWnd to update the trackbar in the MCIWnd window, update position information displayed in the window title bar, and send notification messages to the parent window when the MCIWnd window is active. You can send this message explicitly or by using the [**MCIWndSetActiveTimer**](/windows/win32/Vfw/nf-vfw-mciwndsetactivetimer?branch=master) macro.


```C++
MCIWNDM_SETACTIVETIMER 
wParam = (WPARAM) (UINT) active; 
lParam = 0L; 
```



## Parameters

<dl> <dt>

<span id="active"></span><span id="ACTIVE"></span>*active*
</dt> <dd>

Update period, in milliseconds. The default is 500 milliseconds.

</dd> </dl>

## Return Value

This message does not return a value.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[**MCIWndSetActiveTimer**](/windows/win32/Vfw/nf-vfw-mciwndsetactivetimer?branch=master)
</dt> </dl>

 

 





