---
title: MCIWNDM_GETPALETTE message (Vfw.h)
description: The MCIWNDM\_GETPALETTE message retrieves a handle of the palette used by an MCI device. You can send this message explicitly or by using the MCIWndGetPalette macro.
ms.assetid: f8426344-0fee-4419-9d8a-dcee26cb4c28
keywords:
- MCIWNDM_GETPALETTE message Windows Multimedia
topic_type:
- apiref
api_name:
- MCIWNDM_GETPALETTE
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCIWNDM\_GETPALETTE message

The **MCIWNDM\_GETPALETTE** message retrieves a handle of the palette used by an MCI device. You can send this message explicitly or by using the [**MCIWndGetPalette**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetpalette) macro.


```C++
MCIWNDM_GETPALETTE 
wParam = 0; 
lParam = 0; 
```



## Return Value

Returns the handle of the palette if successful.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[**MCIWndGetPalette**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetpalette)
</dt> </dl>

 

 





