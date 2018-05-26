---
title: MCIWNDM\_GETSTYLES message
description: The MCIWNDM\_GETSTYLES message retrieves the flags specifying the current MCIWnd window styles used by a window. You can send this message explicitly or by using the MCIWndGetStyles macro.
ms.assetid: cd34ba05-47cb-488e-a6c6-4ec1c0d25de8
keywords:
- MCIWNDM_GETSTYLES message Windows Multimedia
topic_type:
- apiref
api_name:
- MCIWNDM_GETSTYLES
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

# MCIWNDM\_GETSTYLES message

The **MCIWNDM\_GETSTYLES** message retrieves the flags specifying the current MCIWnd window styles used by a window. You can send this message explicitly or by using the [**MCIWndGetStyles**](/windows/win32/Vfw/nf-vfw-mciwndgetstyles?branch=master) macro.


```C++
MCIWNDM_GETSTYLES 
wParam = 0; 
lParam = 0; 
```



## Return Value

Returns a value representing the current styles of the MCIWnd window. The return value is the bitwise OR operator of the MCIWnd window styles (MCIWNDF flags).

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[**MCIWndGetStyles**](/windows/win32/Vfw/nf-vfw-mciwndgetstyles?branch=master)
</dt> </dl>

 

 





