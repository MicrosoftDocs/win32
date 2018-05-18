---
title: ICM\_DECOMPRESSEX\_QUERY message
description: The ICM\_DECOMPRESSEX\_QUERY message queries a video compression driver to determine if it supports a specific input format or if it can decompress a specific input format to a specific output format.
ms.assetid: '7778a52d-2ed8-495c-8656-c6beb1863499'
keywords: ["ICM_DECOMPRESSEX_QUERY message Windows Multimedia"]
topic_type:
- apiref
api_name:
- ICM_DECOMPRESSEX_QUERY
api_location:
- Vfw.h
api_type:
- HeaderDef
---

# ICM\_DECOMPRESSEX\_QUERY message

The **ICM\_DECOMPRESSEX\_QUERY** message queries a video compression driver to determine if it supports a specific input format or if it can decompress a specific input format to a specific output format.


```C++
ICM_DECOMPRESSEX_QUERY 
wParam = (DWORD_PTR) (LPVOID) &amp;icdex; 
lParam = sizeof(ICDECOMPRESSEX); 
```



## Parameters

<dl> <dt>

<span id="icdex"></span><span id="ICDEX"></span>*icdex*
</dt> <dd>

Pointer to a [**ICDECOMPRESSEX**](icdecompressex-struct.md) structure containing the input format.

</dd> <dt>

<span id="lParam"></span><span id="lparam"></span><span id="LPARAM"></span>*lParam*
</dt> <dd>

Size, in bytes, of [**ICDECOMPRESSEX**](icdecompressex-struct.md).

</dd> </dl>

## Return Value

Returns ICERR\_OK if the specified decompression is supported or ICERR\_BADFORMAT otherwise.

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

 

 





