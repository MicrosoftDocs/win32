---
title: MCIWNDM_PUT_SOURCE message (Vfw.h)
description: The MCIWNDM\_PUT\_SOURCE message redefines the coordinates of the source rectangle used for cropping the images of an AVI file during playback. You can send this message explicitly or by using the MCIWndPutSource macro.
ms.assetid: cff95139-0302-4db3-bf2e-559e75257e85
keywords:
- MCIWNDM_PUT_SOURCE message Windows Multimedia
topic_type:
- apiref
api_name:
- MCIWNDM_PUT_SOURCE
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCIWNDM\_PUT\_SOURCE message

The **MCIWNDM\_PUT\_SOURCE** message redefines the coordinates of the source rectangle used for cropping the images of an AVI file during playback. You can send this message explicitly or by using the [**MCIWndPutSource**](/windows/desktop/api/Vfw/nf-vfw-mciwndputsource) macro.


```C++
MCIWNDM_PUT_SOURCE 
wParam = 0; 
lParam = (LPARAM) (LPRECT) prc; 
```



## Parameters

<dl> <dt>

<span id="prc"></span><span id="PRC"></span>*prc*
</dt> <dd>

Pointer to a [RECT](/previous-versions//ms536136(v=vs.85)) structure containing the coordinates of the source rectangle.

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



 

