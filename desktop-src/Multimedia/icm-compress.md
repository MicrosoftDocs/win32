---
title: ICM\_COMPRESS message
description: The ICM\_COMPRESS message notifies a video compression driver to compress a frame of data into an application-defined buffer.
ms.assetid: 'd95b943f-458d-4a5e-bab1-e3648d323395'
keywords: ["ICM_COMPRESS message Windows Multimedia"]
topic_type:
- apiref
api_name:
- ICM_COMPRESS
api_location:
- Vfw.h
api_type:
- HeaderDef
---

# ICM\_COMPRESS message

The **ICM\_COMPRESS** message notifies a video compression driver to compress a frame of data into an application-defined buffer.


```C++
ICM_COMPRESS 
wParam = (DWORD) (LPVOID) &amp;icc; 
lParam = sizeof(ICCOMPRESS); 
```



## Parameters

<dl> <dt>

<span id="icc"></span><span id="ICC"></span>*icc*
</dt> <dd>

Pointer to an [**ICCOMPRESS**](iccompress-struct.md) structure. The following members of this structure specify the compression parameters: **lpbiInput**, **lpInput**, **lpbiOutput**, **lpOutput**, **lpbiPrev**, **lpPrev**, **lpckid**, **lpdwFlags**, **dwFrameSize**, and **dwQuality**. The driver should also use the **biSizeImage** member of the [**BITMAPINFOHEADER**](https://msdn.microsoft.com/library/windows/desktop/dd183376) structure associated with **lpbiOutput** of **ICCOMPRESS** to return the size of the compressed frame.

</dd> <dt>

<span id="lParam"></span><span id="lparam"></span><span id="LPARAM"></span>*lParam*
</dt> <dd>

Size, in bytes, of [**ICCOMPRESS**](iccompress-struct.md).

</dd> </dl>

## Return Value

Returns ICERR\_OK if successful or an error otherwise.

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

 

 





