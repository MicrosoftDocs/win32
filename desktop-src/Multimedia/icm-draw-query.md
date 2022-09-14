---
title: ICM_DRAW_QUERY message (Vfw.h)
description: The ICM\_DRAW\_QUERY message queries a rendering driver to determine if it can render data in a specific format. You can send this message explicitly or by using the ICDrawQuery macro.
ms.assetid: b829a04b-c1be-47c6-96e9-a6dc6f802811
keywords:
- ICM_DRAW_QUERY message Windows Multimedia
topic_type:
- apiref
api_name:
- ICM_DRAW_QUERY
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# ICM\_DRAW\_QUERY message

The **ICM\_DRAW\_QUERY** message queries a rendering driver to determine if it can render data in a specific format. You can send this message explicitly or by using the [**ICDrawQuery**](/windows/desktop/api/Vfw/nf-vfw-icdrawquery) macro.


```C++
ICM_DRAW_QUERY 
wParam = (DWORD_PTR) (LPVOID) lpbiInput; 
lParam = 0; 
```



## Parameters

<dl> <dt>

<span id="lpbiInput"></span><span id="lpbiinput"></span><span id="LPBIINPUT"></span>*lpbiInput*
</dt> <dd>

Pointer to a [**BITMAPINFO**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfo) structure containing the input format.

</dd> </dl>

## Return Value

Returns ICERR\_OK if the driver can render data in the specified format or ICERR\_BADFORMAT otherwise.

## Remarks

This message differs from the [**ICM\_DRAW\_BEGIN**](icm-draw-begin.md) message in that it queries the driver in a general sense. **ICM\_DRAW\_BEGIN** determines if the driver can draw the data using the specified format under specific conditions, such as stretching the image.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[Video Compression Manager](video-compression-manager.md)
</dt> <dt>

[Video Compression Messages](video-compression-messages.md)
</dt> </dl>

 

