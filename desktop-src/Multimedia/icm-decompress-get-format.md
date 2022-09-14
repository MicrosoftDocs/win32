---
title: ICM_DECOMPRESS_GET_FORMAT message (Vfw.h)
description: The ICM\_DECOMPRESS\_GET\_FORMAT message requests the output format of the decompressed data from a video decompression driver. You can send this message explicitly or by using the ICDecompressGetFormat macro.
ms.assetid: 51753f47-758b-4d3e-9a53-9db284da2473
keywords:
- ICM_DECOMPRESS_GET_FORMAT message Windows Multimedia
topic_type:
- apiref
api_name:
- ICM_DECOMPRESS_GET_FORMAT
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# ICM\_DECOMPRESS\_GET\_FORMAT message

The **ICM\_DECOMPRESS\_GET\_FORMAT** message requests the output format of the decompressed data from a video decompression driver. You can send this message explicitly or by using the [**ICDecompressGetFormat**](/windows/desktop/api/Vfw/nf-vfw-icdecompressgetformat) macro.


```C++
ICM_DECOMPRESS_GET_FORMAT 
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

Pointer to a [**BITMAPINFO**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfo) structure to contain the output format. You can specify zero to request only the size of the output format, as in the [**ICDecompressGetFormatSize**](/windows/desktop/api/Vfw/nf-vfw-icdecompressgetformatsize) macro.

</dd> </dl>

## Return Value

If *lpbiOutput* is zero, returns the size of the structure.

If *lpbiOutput* is nonzero, returns ICERR\_OK if successful or an error otherwise.

## Remarks

If *lpbiOutput* is nonzero, the driver should fill the [**BITMAPINFO**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfo) structure with the default output format corresponding to the input format specified for *lpbiInput*. If the compressor can produce several formats, the default format should be the one that preserves the greatest amount of information.

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

 

