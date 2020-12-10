---
title: ICM_DRAW_SETTIME message (Vfw.h)
description: The ICM\_DRAW\_SETTIME provides synchronization information to a rendering driver that handles the timing of drawing frames.
ms.assetid: 211e8ecc-ef36-4598-aa1d-cb0a06e64f14
keywords:
- ICM_DRAW_SETTIME message Windows Multimedia
topic_type:
- apiref
api_name:
- ICM_DRAW_SETTIME
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# ICM\_DRAW\_SETTIME message

The **ICM\_DRAW\_SETTIME** provides synchronization information to a rendering driver that handles the timing of drawing frames. The synchronization information is the sample number of the frame to draw. You can send this message explicitly or by using the [**ICDrawSetTime**](/windows/desktop/api/Vfw/nf-vfw-icdrawsettime) macro.


```C++
ICM_DRAW_SETTIME 
wParam = (DWORD_PTR) lpTime; 
lParam = 0; 
```



## Parameters

<dl> <dt>

<span id="lpTime"></span><span id="lptime"></span><span id="LPTIME"></span>*lpTime*
</dt> <dd>

Sample number of the frame to render.

</dd> </dl>

## Return Value

Returns ICERR\_OK if successful or an error otherwise.

## Remarks

Typically, the driver compares the specified value with the frame number associated with the time of its internal clock and attempts to synchronize the two if the difference is significant.

Use this message when the hardware performs its own asynchronous decompression, timing, and drawing, and the hardware relies on an external synchronization signal (the hardware is not being used as the synchronization master).

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

 

 





