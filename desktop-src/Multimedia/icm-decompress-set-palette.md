---
title: ICM_DECOMPRESS_SET_PALETTE message (Vfw.h)
description: The ICM\_DECOMPRESS\_SET\_PALETTE message specifies a palette for a video decompression driver to use if it is decompressing to a format that uses a palette. You can send this message explicitly or by using the ICDecompressSetPalette macro.
ms.assetid: 269d01f9-b7c8-40e4-abdb-24dd0c9cc18d
keywords:
- ICM_DECOMPRESS_SET_PALETTE message Windows Multimedia
topic_type:
- apiref
api_name:
- ICM_DECOMPRESS_SET_PALETTE
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# ICM\_DECOMPRESS\_SET\_PALETTE message

The **ICM\_DECOMPRESS\_SET\_PALETTE** message specifies a palette for a video decompression driver to use if it is decompressing to a format that uses a palette. You can send this message explicitly or by using the [**ICDecompressSetPalette**](/windows/desktop/api/Vfw/nf-vfw-icdecompresssetpalette) macro.


```C++
ICM_DECOMPRESS_SET_PALETTE 
wParam = (DWORD_PTR) (LPVOID) lpbiPalette; 
lParam = 0; 
```



## Parameters

<dl> <dt>

<span id="lpbiPalette"></span><span id="lpbipalette"></span><span id="LPBIPALETTE"></span>*lpbiPalette*
</dt> <dd>

Pointer to a [**BITMAPINFOHEADER**](/windows/desktop/api/wingdi/ns-wingdi-bitmapinfoheader) structure whose color table contains the colors that should be used if possible. You can specify zero to use the default set of output colors.

</dd> </dl>

## Return Value

Returns ICERR\_OK if the decompression driver can precisely decompress images to the suggested palette using the set of colors as they are arranged in the palette. Returns ICERR\_UNSUPPORTED otherwise.

## Remarks

This message should not affect decompression already in progress; rather, colors passed using this message should be returned in response to future [**ICM\_DECOMPRESS\_GET\_FORMAT**](icm-decompress-get-format.md) and [**ICM\_DECOMPRESS\_GET\_PALETTE**](icm-decompress-get-palette.md) messages. Colors are sent back to the decompression driver in a future [**ICM\_DECOMPRESS\_BEGIN**](icm-decompress-begin.md) message.

This message is used primarily when a driver decompresses images to the screen and another application that uses a palette is in the foreground, forcing the decompression driver to adapt to a foreign set of colors.

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

 

