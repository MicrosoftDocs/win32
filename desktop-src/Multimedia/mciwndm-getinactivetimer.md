---
title: MCIWNDM\_GETINACTIVETIMER message
description: The MCIWNDM\_GETINACTIVETIMER message retrieves the update period used when the MCIWnd window is the inactive window. You can send this message explicitly or by using the MCIWndGetInactiveTimer macro.
ms.assetid: 84e00d2f-2cf8-4b6b-a8cb-7eb320754783
keywords:
- MCIWNDM_GETINACTIVETIMER message Windows Multimedia
topic_type:
- apiref
api_name:
- MCIWNDM_GETINACTIVETIMER
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

# MCIWNDM\_GETINACTIVETIMER message

The **MCIWNDM\_GETINACTIVETIMER** message retrieves the update period used when the MCIWnd window is the inactive window. You can send this message explicitly or by using the [**MCIWndGetInactiveTimer**](/windows/win32/Vfw/nf-vfw-mciwndgetinactivetimer?branch=master) macro.


```C++
MCIWNDM_GETINACTIVETIMER 
wParam = 0; 
lParam = 0; 
```



## Return Value

Returns the update period, in milliseconds. The default value is 2000 milliseconds.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[**MCIWndGetInactiveTimer**](/windows/win32/Vfw/nf-vfw-mciwndgetinactivetimer?branch=master)
</dt> </dl>

 

 





