---
title: MCIWNDM\_SETPALETTE message
description: The MCIWNDM\_SETPALETTE message sends a palette handle to the MCI device associated with the MCIWnd window. You can send this message explicitly or by using the MCIWndSetPalette macro.
ms.assetid: 'd2399cb7-d83c-465c-b02f-e6a016c28ae3'
keywords: ["MCIWNDM_SETPALETTE message Windows Multimedia"]
topic_type:
- apiref
api_name:
- MCIWNDM_SETPALETTE
api_location:
- Vfw.h
api_type:
- HeaderDef
---

# MCIWNDM\_SETPALETTE message

The **MCIWNDM\_SETPALETTE** message sends a palette handle to the MCI device associated with the MCIWnd window. You can send this message explicitly or by using the [**MCIWndSetPalette**](mciwndsetpalette.md) macro.


```C++
MCIWNDM_SETPALETTE 
wParam = (WPARAM) (HPALETTE) hpal; 
lParam = 0; 
```



## Parameters

<dl> <dt>

<span id="hpal"></span><span id="HPAL"></span>*hpal*
</dt> <dd>

Palette handle.

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[**MCIWndSetPalette**](mciwndsetpalette.md)
</dt> </dl>

 

 





