---
title: MCIWNDM_GET_SOURCE message (Vfw.h)
description: The MCIWNDM\_GET\_SOURCE message retrieves the coordinates of the source rectangle used for cropping the images of an AVI file during playback. You can send this message explicitly or by using the MCIWndGetSource macro.
ms.assetid: d5f25926-5a3d-412e-8248-fbf307583757
keywords:
- MCIWNDM_GET_SOURCE message Windows Multimedia
topic_type:
- apiref
api_name:
- MCIWNDM_GET_SOURCE
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCIWNDM\_GET\_SOURCE message

The **MCIWNDM\_GET\_SOURCE** message retrieves the coordinates of the source rectangle used for cropping the images of an AVI file during playback. You can send this message explicitly or by using the [**MCIWndGetSource**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetsource) macro.


```C++
MCIWNDM_GET_SOURCE 
wParam = 0; 
lParam = (LPARAM) (LPRECT) prc; 
```



## Parameters

<dl> <dt>

<span id="prc"></span><span id="PRC"></span>*prc*
</dt> <dd>

Pointer to a [**RECT**](/windows/win32/api/windef/ns-windef-rect) structure to contain the coordinates of the source rectangle.

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

[**MCIWndGetSource**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetsource)
</dt> </dl>

 

