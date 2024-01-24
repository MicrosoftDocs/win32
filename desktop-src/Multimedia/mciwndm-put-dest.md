---
title: MCIWNDM_PUT_DEST message (Vfw.h)
description: The MCIWNDM\_PUT\_DEST message redefines the coordinates of the destination rectangle used for zooming or stretching the images of an AVI file during playback. You can send this message explicitly or by using the MCIWndPutDest macro.
ms.assetid: 0b13d473-ef93-41a2-bbb2-09fbf264493e
keywords:
- MCIWNDM_PUT_DEST message Windows Multimedia
topic_type:
- apiref
api_name:
- MCIWNDM_PUT_DEST
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCIWNDM\_PUT\_DEST message

The **MCIWNDM\_PUT\_DEST** message redefines the coordinates of the destination rectangle used for zooming or stretching the images of an AVI file during playback. You can send this message explicitly or by using the [**MCIWndPutDest**](/windows/desktop/api/Vfw/nf-vfw-mciwndputdest) macro.


```C++
MCIWNDM_PUT_DEST 
wParam = 0; 
lParam = (LPARAM) (LPRECT) prc; 
```



## Parameters

<dl> <dt>

<span id="prc"></span><span id="PRC"></span>*prc*
</dt> <dd>

Pointer to a [**RECT**](/windows/win32/api/windef/ns-windef-rect) structure containing the coordinates of the destination rectangle.

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[**MCIWndPutDest**](/windows/desktop/api/Vfw/nf-vfw-mciwndputdest)
</dt> </dl>

 

