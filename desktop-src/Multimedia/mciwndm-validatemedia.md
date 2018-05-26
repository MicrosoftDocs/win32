---
title: MCIWNDM\_VALIDATEMEDIA message
description: The MCIWNDM\_VALIDATEMEDIA message updates the starting and ending locations of the content, the current position in the content, and the trackbar according to the current time format.
ms.assetid: 98ac6227-fc90-4276-8e26-2bd005e35dc6
keywords:
- MCIWNDM_VALIDATEMEDIA message Windows Multimedia
topic_type:
- apiref
api_name:
- MCIWNDM_VALIDATEMEDIA
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

# MCIWNDM\_VALIDATEMEDIA message

The **MCIWNDM\_VALIDATEMEDIA** message updates the starting and ending locations of the content, the current position in the content, and the trackbar according to the current time format. You can send this message explicitly or by using the [**MCIWndValidateMedia**](/windows/win32/Vfw/nf-vfw-mciwndvalidatemedia?branch=master) macro.


```C++
MCIWNDM_VALIDATEMEDIA 
wParam = 0; 
lParam = 0; 
```



## Return Value

This message does not return a value.

## Remarks

Typically, you should not need to use this macro; however, if your application changes the time format of a device without using MCIWnd; the starting and ending locations of the content, as well as the trackbar, continue to use the old format. You can use this macro to update these values.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[**MCIWndValidateMedia**](/windows/win32/Vfw/nf-vfw-mciwndvalidatemedia?branch=master)
</dt> </dl>

 

 





