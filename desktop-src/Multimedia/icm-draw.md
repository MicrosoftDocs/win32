---
title: ICM_DRAW message (Vfw.h)
description: The ICM\_DRAW message notifies a rendering driver to decompress a frame of data and draw it to the screen.
ms.assetid: eceb42c6-d91a-45b7-98dc-e0944df3e558
keywords:
- ICM_DRAW message Windows Multimedia
topic_type:
- apiref
api_name:
- ICM_DRAW
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# ICM\_DRAW message

The **ICM\_DRAW** message notifies a rendering driver to decompress a frame of data and draw it to the screen.


```C++
ICM_DRAW 
wParam = (DWORD) (LPVOID) &icdraw; 
lParam = sizeof(ICDRAW); 
```



## Parameters

<dl> <dt>

<span id="wParam"></span><span id="wparam"></span><span id="WPARAM"></span>*wParam*
</dt> <dd>

Pointer to an [**ICDRAW**](/windows/desktop/api/Vfw/ns-vfw-icdraw) structure.

</dd> <dt>

<span id="lParam"></span><span id="lparam"></span><span id="LPARAM"></span>*lParam*
</dt> <dd>

Size, in bytes, of [**ICDRAW**](/windows/desktop/api/Vfw/ns-vfw-icdraw).

</dd> </dl>

## Return Value

Returns ICERR\_OK if successful or an error otherwise.

## Remarks

If the ICDRAW\_UPDATE flag is set in the **dwFlags** member of [**ICDRAW**](/windows/desktop/api/Vfw/ns-vfw-icdraw), the area of the screen used for drawing is invalid and needs to be updated. The extent of updating depends on the contents of the **lpData** member.

If **lpData** is **NULL**, the driver should update the entire destination rectangle with the current image. If the driver maintains a copy of the image in an off-screen buffer, it can fail this message. If **lpData** is not **NULL**, the driver should draw the data and make sure the entire destination is updated.

If the ICDRAW\_HURRYUP flag is set in **dwFlags**, the calling application wants the driver to proceed as quickly as possible, possibly not even updating the screen.

If the ICDRAW\_PREROLL flag is set in **dwFlags**, this video frame is preliminary information and should not be displayed if possible. For example, if play is to start from frame 10, and frame 0 is the nearest previous key frame, frames 0 through 9 will have ICDRAW\_PREROLL set.

If you want the driver to decompress data into a buffer, send the [**ICM\_DECOMPRESS**](icm-decompress.md) message.

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

 

 





