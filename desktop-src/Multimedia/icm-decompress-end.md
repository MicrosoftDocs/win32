---
title: ICM_DECOMPRESS_END message (Vfw.h)
description: The ICM\_DECOMPRESS\_END message notifies a video decompression driver to end decompression and free resources allocated for decompression. You can send this message explicitly or by using the ICDecompressEnd macro.
ms.assetid: 16ce2424-9606-455f-afbd-84326457538e
keywords:
- ICM_DECOMPRESS_END message Windows Multimedia
topic_type:
- apiref
api_name:
- ICM_DECOMPRESS_END
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# ICM\_DECOMPRESS\_END message

The **ICM\_DECOMPRESS\_END** message notifies a video decompression driver to end decompression and free resources allocated for decompression. You can send this message explicitly or by using the [**ICDecompressEnd**](/windows/desktop/api/Vfw/nf-vfw-icdecompressend) macro.


```C++
ICM_DECOMPRESS_END 
wParam = 0; 
lParam = 0; 
```



## Return Value

Returns ICERR\_OK if successful or an error otherwise.

## Remarks

The driver should free any resources allocated for the [**ICM\_DECOMPRESS\_BEGIN**](icm-decompress-begin.md) message.

[**ICM\_DECOMPRESS\_BEGIN**](icm-decompress-begin.md) and **ICM\_DECOMPRESS\_END** do not nest. If your driver receives **ICM\_DECOMPRESS\_BEGIN** before decompression is stopped with **ICM\_DECOMPRESS\_END**, it should restart decompression with new parameters.

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

 

 





