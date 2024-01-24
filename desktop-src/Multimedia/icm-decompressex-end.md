---
title: ICM_DECOMPRESSEX_END message (Vfw.h)
description: The ICM\_DECOMPRESSEX\_END message notifies a video decompression driver to end decompression and free resources allocated for decompression. You can send this message explicitly or by using the ICDecompressExEnd macro.
ms.assetid: 7ed63a4e-bb17-43a3-b593-25c4a51be942
keywords:
- ICM_DECOMPRESSEX_END message Windows Multimedia
topic_type:
- apiref
api_name:
- ICM_DECOMPRESSEX_END
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# ICM\_DECOMPRESSEX\_END message

The **ICM\_DECOMPRESSEX\_END** message notifies a video decompression driver to end decompression and free resources allocated for decompression. You can send this message explicitly or by using the [**ICDecompressExEnd**](/windows/desktop/api/Vfw/nf-vfw-icdecompressexend) macro.


```C++
ICM_DECOMPRESSEX_END 
wParam = 0; 
lParam = 0; 
```



## Return Value

Returns ICERR\_OK if successful or an error otherwise.

## Remarks

The driver frees any resources allocated for the [**ICM\_DECOMPRESSEX\_BEGIN**](icm-decompressex-begin.md) message.

[**ICM\_DECOMPRESSEX\_BEGIN**](icm-decompressex-begin.md) and **ICM\_DECOMPRESSEX\_END** do not nest. If your driver receives **ICM\_DECOMPRESSEX\_BEGIN** before decompression is stopped with **ICM\_DECOMPRESSEX\_END**, it should restart decompression with new parameters.

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

 

 





