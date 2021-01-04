---
title: ICM_DRAW_STOP_PLAY message (Vfw.h)
description: The ICM\_DRAW\_STOP\_PLAY message notifies a rendering driver when a play operation is complete. You can send this message explicitly or by using the ICDrawStopPlay macro.
ms.assetid: cfe2ee98-80d0-4554-bcbd-9873769da674
keywords:
- ICM_DRAW_STOP_PLAY message Windows Multimedia
topic_type:
- apiref
api_name:
- ICM_DRAW_STOP_PLAY
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# ICM\_DRAW\_STOP\_PLAY message

The **ICM\_DRAW\_STOP\_PLAY** message notifies a rendering driver when a play operation is complete. You can send this message explicitly or by using the [**ICDrawStopPlay**](/windows/desktop/api/Vfw/nf-vfw-icdrawstopplay) macro.


```C++
ICM_DRAW_STOP_PLAY 
wParam = 0; 
lParam = 0; 
```



## Return Value

This message does not return a value.

## Remarks

Use this message when the play operation is complete. Use the [**ICM\_DRAW\_STOP**](icm-draw-stop.md) message to end timing.

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

 

 





