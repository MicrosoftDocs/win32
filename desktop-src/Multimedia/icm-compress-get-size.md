---
title: ICM_COMPRESS_GET_SIZE message (Vfw.h)
description: The ICM\_COMPRESS\_GET\_SIZE message requests that the video compression driver supply the maximum size of one frame of data when compressed into the specified output format. You can send this message explicitly or by using the ICCompressGetSize macro.
ms.assetid: 6910e588-e60f-43b1-8fa6-113c2ec32a53
keywords:
- ICM_COMPRESS_GET_SIZE message Windows Multimedia
topic_type:
- apiref
api_name:
- ICM_COMPRESS_GET_SIZE
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# ICM\_COMPRESS\_GET\_SIZE message

The **ICM\_COMPRESS\_GET\_SIZE** message requests that the video compression driver supply the maximum size of one frame of data when compressed into the specified output format. You can send this message explicitly or by using the [**ICCompressGetSize**](/windows/desktop/api/Vfw/nf-vfw-iccompressgetsize) macro.


```C++
ICM_COMPRESS_GET_SIZE 
wParam = (DWORD_PTR) (LPVOID) lpbiInput; 
lParam = (DWORD_PTR) (LPVOID) lpbiOutput; 
```



## Parameters

<dl> <dt>

<span id="lpbiInput"></span><span id="lpbiinput"></span><span id="LPBIINPUT"></span>*lpbiInput*
</dt> <dd>

Pointer to a [**BITMAPINFO**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfo) structure containing the input format.

</dd> <dt>

<span id="lpbiOutput"></span><span id="lpbioutput"></span><span id="LPBIOUTPUT"></span>*lpbiOutput*
</dt> <dd>

Pointer to a [**BITMAPINFO**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfo) structure containing the output format.

</dd> </dl>

## Return Value

Returns the maximum number of bytes a single compressed frame can occupy.

## Remarks

Typically, applications send this message to determine how large a buffer to allocate for the compressed frame.

The driver should calculate the size of the largest possible frame based on the input and output formats.

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

 

