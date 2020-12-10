---
title: ICM_DECOMPRESS_QUERY message (Vfw.h)
description: The ICM\_DECOMPRESS\_QUERY message queries a video decompression driver to determine if it supports a specific input format or if it can decompress a specific input format to a specific output format.
ms.assetid: 622dd1de-3f7a-4841-913c-282c2ad766f4
keywords:
- ICM_DECOMPRESS_QUERY message Windows Multimedia
topic_type:
- apiref
api_name:
- ICM_DECOMPRESS_QUERY
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# ICM\_DECOMPRESS\_QUERY message

The **ICM\_DECOMPRESS\_QUERY** message queries a video decompression driver to determine if it supports a specific input format or if it can decompress a specific input format to a specific output format. You can send this message explicitly or by using the [**ICDecompressQuery**](/windows/desktop/api/Vfw/nf-vfw-icdecompressquery) macro.


```C++
ICM_DECOMPRESS_QUERY 
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

Pointer to a [**BITMAPINFO**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfo) structure containing the output format. You can specify zero for this parameter to indicate any output format is acceptable.

</dd> </dl>

## Return Value

Returns ICERR\_OK if the specified decompression is supported or ICERR\_BADFORMAT otherwise.

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

 

