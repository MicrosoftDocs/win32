---
title: MCIWNDM\_GETACTIVETIMER message
description: The MCIWNDM\_GETACTIVETIMER message retrieves the update period used when the MCIWnd window is the active window. You can send this message explicitly or by using the MCIWndGetActiveTimer macro.
ms.assetid: 'f9e6f9ed-75fd-4e45-ad92-79a82d8d572c'
keywords: ["MCIWNDM_GETACTIVETIMER message Windows Multimedia"]
topic_type:
- apiref
api_name:
- MCIWNDM_GETACTIVETIMER
api_location:
- Vfw.h
api_type:
- HeaderDef
---

# MCIWNDM\_GETACTIVETIMER message

The **MCIWNDM\_GETACTIVETIMER** message retrieves the update period used when the MCIWnd window is the active window. You can send this message explicitly or by using the [**MCIWndGetActiveTimer**](mciwndgetactivetimer.md) macro.


```C++
MCIWNDM_GETACTIVETIMER 
wParam = 0; 
lParam = 0L; 
```



## Return Value

Returns the update period in milliseconds. The default is 500 milliseconds.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[**MCIWndGetActiveTimer**](mciwndgetactivetimer.md)
</dt> </dl>

 

 





