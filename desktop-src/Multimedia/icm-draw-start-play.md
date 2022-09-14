---
title: ICM_DRAW_START_PLAY message (Vfw.h)
description: The ICM\_DRAW\_START\_PLAY message provides the start and end times of a play operation to a rendering driver. You can send this message explicitly or by using the ICDrawStartPlay macro.
ms.assetid: 27c4c06e-6510-43dc-a754-fe44144796f5
keywords:
- ICM_DRAW_START_PLAY message Windows Multimedia
topic_type:
- apiref
api_name:
- ICM_DRAW_START_PLAY
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# ICM\_DRAW\_START\_PLAY message

The **ICM\_DRAW\_START\_PLAY** message provides the start and end times of a play operation to a rendering driver. You can send this message explicitly or by using the [**ICDrawStartPlay**](/windows/desktop/api/Vfw/nf-vfw-icdrawstartplay) macro.


```C++
ICM_DRAW_START_PLAY 
wParam = (DWORD_PTR) lFrom; 
lParam = (DWORD_PTR) lTo; 
```



## Parameters

<dl> <dt>

<span id="lFrom"></span><span id="lfrom"></span><span id="LFROM"></span>*lFrom*
</dt> <dd>

Start time.

</dd> <dt>

<span id="lTo"></span><span id="lto"></span><span id="LTO"></span>*lTo*
</dt> <dd>

End time.

</dd> </dl>

## Return Value

This message does not return a value.

## Remarks

This message precedes any frame data sent to the rendering driver.

Units for *lFrom* and *lTo* are specified with the [**ICM\_DRAW\_BEGIN**](icm-draw-begin.md) message. For video data this is normally a frame number. For more information about the playback rate, see the **dwRate** and **dwScale** members of the [**ICDRAWBEGIN**](/windows/desktop/api/Vfw/ns-vfw-icdrawbegin) structure.

If the end time is less than the start time, the playback direction is reversed.

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

 

 





