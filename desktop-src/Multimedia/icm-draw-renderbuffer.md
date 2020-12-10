---
title: ICM_DRAW_RENDERBUFFER message (Vfw.h)
description: The ICM\_DRAW\_RENDERBUFFER message notifies a rendering driver to draw the frames that have been passed to it. You can send this message explicitly or by using the ICDrawRenderBuffer macro.
ms.assetid: b21be12c-b8a5-49ea-b6b3-d2eb0077a8e9
keywords:
- ICM_DRAW_RENDERBUFFER message Windows Multimedia
topic_type:
- apiref
api_name:
- ICM_DRAW_RENDERBUFFER
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# ICM\_DRAW\_RENDERBUFFER message

The **ICM\_DRAW\_RENDERBUFFER** message notifies a rendering driver to draw the frames that have been passed to it. You can send this message explicitly or by using the [**ICDrawRenderBuffer**](/windows/desktop/api/Vfw/nf-vfw-icdrawrenderbuffer) macro.


```C++
ICM_DRAW_RENDERBUFFER 
wParam = 0; 
lParam = 0; 
```



## Return Value

This message does not return a value.

## Remarks

Use this message with hardware that performs its own asynchronous decompression, timing, and drawing.

This message is typically used to perform a seek operation when the driver must be specifically instructed to display each video frame passed to it rather than playing a sequence of video frames.

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

 

 





