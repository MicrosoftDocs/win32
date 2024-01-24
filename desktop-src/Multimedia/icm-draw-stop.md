---
title: ICM_DRAW_STOP message (Vfw.h)
description: The ICM\_DRAW\_STOP message notifies a rendering driver to stop its internal clock for the timing of drawing frames. You can send this message explicitly or by using the ICDrawStop macro.
ms.assetid: 9ffda595-e3d6-48f0-9487-69f7e95979c2
keywords:
- ICM_DRAW_STOP message Windows Multimedia
topic_type:
- apiref
api_name:
- ICM_DRAW_STOP
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# ICM\_DRAW\_STOP message

The **ICM\_DRAW\_STOP** message notifies a rendering driver to stop its internal clock for the timing of drawing frames. You can send this message explicitly or by using the [**ICDrawStop**](/windows/desktop/api/Vfw/nf-vfw-icdrawstop) macro.


```C++
ICM_DRAW_STOP 
wParam = 0; 
lParam = 0; 
```



## Return Value

This message does not return a value.

## Remarks

This message is used by hardware that performs its own asynchronous decompression, timing, and drawing.

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

 

 





