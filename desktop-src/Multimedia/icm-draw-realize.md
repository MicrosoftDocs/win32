---
title: ICM_DRAW_REALIZE message (Vfw.h)
description: The ICM\_DRAW\_REALIZE message notifies a rendering driver to realize its drawing palette while drawing. You can send this message explicitly or by using the ICDrawRealize macro.
ms.assetid: 501540cd-41e2-4f80-abf8-2ec2179970a9
keywords:
- ICM_DRAW_REALIZE message Windows Multimedia
topic_type:
- apiref
api_name:
- ICM_DRAW_REALIZE
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# ICM\_DRAW\_REALIZE message

The **ICM\_DRAW\_REALIZE** message notifies a rendering driver to realize its drawing palette while drawing. You can send this message explicitly or by using the [**ICDrawRealize**](/windows/desktop/api/Vfw/nf-vfw-icdrawrealize) macro.


```C++
ICM_DRAW_REALIZE 
wParam = (DWORD_PTR) (UINT_PTR) (HDC) hdc; 
lParam = (DWORD_PTR) (BOOL) fBackground; 
```



## Parameters

<dl> <dt>

<span id="hdc"></span><span id="HDC"></span>*hdc*
</dt> <dd>

Handle to the DC used to realize the palette.

</dd> <dt>

<span id="fBackground"></span><span id="fbackground"></span><span id="FBACKGROUND"></span>*fBackground*
</dt> <dd>

Background flag. Specify **TRUE** to realize the palette as a background task or **FALSE** to realize the palette in the foreground.

</dd> </dl>

## Return Value

Returns ICERR\_OK if the drawing palette is realized or ICERR\_UNSUPPORTED if the palette associated with the decompressed data is realized.

## Remarks

Drivers need to respond to this message only if the drawing palette is different from the decompressed palette.

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

 

 





