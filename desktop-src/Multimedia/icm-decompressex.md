---
title: ICM\_DECOMPRESSEX message
description: The ICM\_DECOMPRESSEX message notifies a video compression driver to decompress a frame of data directly to the screen, decompress to an upside-down DIB, or decompress images described with source and destination rectangles.
ms.assetid: 'ed253280-c246-4e86-91f1-ad1e1132d732'
keywords: ["ICM_DECOMPRESSEX message Windows Multimedia"]
topic_type:
- apiref
api_name:
- ICM_DECOMPRESSEX
api_location:
- Vfw.h
api_type:
- HeaderDef
---

# ICM\_DECOMPRESSEX message

The **ICM\_DECOMPRESSEX** message notifies a video compression driver to decompress a frame of data directly to the screen, decompress to an upside-down DIB, or decompress images described with source and destination rectangles.


```C++
ICM_DECOMPRESSEX 
wParam = (DWORD_PTR) (LPVOID) &amp;icdex; 
lParam = sizeof(ICDECOMPRESSEX); 
```



## Parameters

<dl> <dt>

<span id="icdex"></span><span id="ICDEX"></span>*icdex*
</dt> <dd>

Pointer to an [**ICDECOMPRESSEX**](icdecompressex-struct.md) structure.

</dd> <dt>

<span id="lParam"></span><span id="lparam"></span><span id="LPARAM"></span>*lParam*
</dt> <dd>

Size, in bytes, of [**ICDECOMPRESSEX**](icdecompressex-struct.md).

</dd> </dl>

## Return Value

Returns ICERR\_OK if successful or an error otherwise.

## Remarks

This message is similar to [**ICM\_DECOMPRESS**](icm-decompress.md) except that it uses the [**ICDECOMPRESSEX**](icdecompressex-struct.md) structure to define its decompression information.

If you want the driver to decompress data directly to the screen, send the [**ICM\_DRAW**](icm-draw.md) message.

The driver returns an error if this message is received before the [**ICM\_DECOMPRESSEX\_BEGIN**](icm-decompressex-begin.md) message.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[Video Compression Manager](video-compression-manager.md)
</dt> <dt>

[Video Compression Messages](video-compression-messages.md)
</dt> </dl>

 

 





