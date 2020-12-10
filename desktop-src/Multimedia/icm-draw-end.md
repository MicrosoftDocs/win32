---
title: ICM_DRAW_END message (Vfw.h)
description: The ICM\_DRAW\_END message notifies a rendering driver to decompress the current image to the screen and to release resources allocated for decompression and drawing. You can send this message explicitly or by using the ICDrawEnd macro.
ms.assetid: 03910752-6122-4a5a-84ff-2cecf66cf439
keywords:
- ICM_DRAW_END message Windows Multimedia
topic_type:
- apiref
api_name:
- ICM_DRAW_END
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# ICM\_DRAW\_END message

The **ICM\_DRAW\_END** message notifies a rendering driver to decompress the current image to the screen and to release resources allocated for decompression and drawing. You can send this message explicitly or by using the [**ICDrawEnd**](/windows/desktop/api/Vfw/nf-vfw-icdrawend) macro.


```C++
ICM_DRAW_END 
wParam = 0; 
lParam = 0; 
```



## Return Value

Returns ICERR\_OK if successful or an error otherwise.

## Remarks

The [**ICM\_DRAW\_BEGIN**](icm-draw-begin.md) and **ICM\_DRAW\_END** messages do not nest. If your driver receives **ICM\_DRAW\_BEGIN** before decompression is stopped with **ICM\_DRAW\_END**, it should restart decompression with new parameters.

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

 

 





