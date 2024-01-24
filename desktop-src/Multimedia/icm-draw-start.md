---
title: ICM_DRAW_START message (Vfw.h)
description: The ICM\_DRAW\_START message notifies a rendering driver to start its internal clock for the timing of drawing frames. You can send this message explicitly or by using the ICDrawStart macro.
ms.assetid: d49e0d97-5a29-46f7-82d7-e3d4b4f7666f
keywords:
- ICM_DRAW_START message Windows Multimedia
topic_type:
- apiref
api_name:
- ICM_DRAW_START
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# ICM\_DRAW\_START message

The **ICM\_DRAW\_START** message notifies a rendering driver to start its internal clock for the timing of drawing frames. You can send this message explicitly or by using the [**ICDrawStart**](/windows/desktop/api/Vfw/nf-vfw-icdrawstart) macro.


```C++
ICM_DRAW_START 
wParam = 0; 
lParam = 0; 
```



## Return Value

This message does not return a value.

## Remarks

This message is used by hardware that performs its own asynchronous decompression, timing, and drawing.

When the driver receives this message, it should start rendering data at the rate specified with the [**ICM\_DRAW\_BEGIN**](icm-draw-begin.md) message.

The **ICM\_DRAW\_START** and [**ICM\_DRAW\_STOP**](icm-draw-stop.md) messages do not nest. If your driver receives **ICM\_DRAW\_START** before rendering is stopped with **ICM\_DRAW\_STOP**, it should restart rendering with new parameters.

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

 

 





