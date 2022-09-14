---
title: ICM_DRAW_GETTIME message (Vfw.h)
description: The ICM\_DRAW\_GETTIME message requests a rendering driver that controls the timing of drawing frames to return the current value of its internal clock. You can send this message explicitly or by using the ICDrawGetTime macro.
ms.assetid: 77f0a322-c0bc-4cfe-a3d0-7633cf8d682a
keywords:
- ICM_DRAW_GETTIME message Windows Multimedia
topic_type:
- apiref
api_name:
- ICM_DRAW_GETTIME
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# ICM\_DRAW\_GETTIME message

The **ICM\_DRAW\_GETTIME** message requests a rendering driver that controls the timing of drawing frames to return the current value of its internal clock. You can send this message explicitly or by using the [**ICDrawGetTime**](/windows/desktop/api/Vfw/nf-vfw-icdrawgettime) macro.


```C++
ICM_DRAW_GETTIME 
wParam = (DWORD_PTR) (LPVOID) lplTime; 
lParam = 0; 
```



## Parameters

<dl> <dt>

<span id="lplTime"></span><span id="lpltime"></span><span id="LPLTIME"></span>*lplTime*
</dt> <dd>

Address to contain the current time. The return value should be specified in samples.

</dd> </dl>

## Return Value

Returns ICERR\_OK if successful or an error otherwise.

## Remarks

This message is generally supported by hardware that performs its own asynchronous decompression, timing, and drawing. The message can also be sent if the hardware is being used as the synchronization master.

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

 

 





