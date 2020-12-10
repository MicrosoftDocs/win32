---
title: MCIWNDM_GETSTART message (Vfw.h)
description: The MCIWNDM\_GETSTART message retrieves the location of the beginning of the content of an MCI device or file. You can send this message explicitly or by using the MCIWndGetStart macro.
ms.assetid: 2350616c-2aac-4ff6-b074-bb785a97cdfb
keywords:
- MCIWNDM_GETSTART message Windows Multimedia
topic_type:
- apiref
api_name:
- MCIWNDM_GETSTART
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCIWNDM\_GETSTART message

The **MCIWNDM\_GETSTART** message retrieves the location of the beginning of the content of an MCI device or file. You can send this message explicitly or by using the [**MCIWndGetStart**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetstart) macro.


```C++
MCIWNDM_GETSTART 
wParam = 0; 
lParam = 0; 
```



## Return Value

Returns the location in the current time format.

## Remarks

Typically, the return value is zero; but some devices use a nonzero starting location. Seeking to this location sets the device to the start of the media.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[**MCIWndGetStart**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetstart)
</dt> </dl>

 

 





