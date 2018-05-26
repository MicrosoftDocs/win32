---
title: ICM\_COMPRESS\_END message
description: The ICM\_COMPRESS\_END message notifies a video compression driver to end compression and free resources allocated for compression. You can send this message explicitly or by using the ICCompressEnd macro.
ms.assetid: 5d4b5962-c4f0-44eb-a3a9-36026f167a5a
keywords:
- ICM_COMPRESS_END message Windows Multimedia
topic_type:
- apiref
api_name:
- ICM_COMPRESS_END
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ICM\_COMPRESS\_END message

The **ICM\_COMPRESS\_END** message notifies a video compression driver to end compression and free resources allocated for compression. You can send this message explicitly or by using the [**ICCompressEnd**](/windows/win32/Vfw/nf-vfw-iccompressend?branch=master) macro.


```C++
ICM_COMPRESS_END 
wParam = 0; 
lParam = 0; 
```



## Return Value

Returns ICERR\_OK if successful or an error otherwise.

## Remarks

VCM saves the settings of the most recent [**ICM\_COMPRESS\_BEGIN**](icm-compress-begin.md) message. **ICM\_COMPRESS\_BEGIN** and **ICM\_COMPRESS\_END** do not nest. If your driver receives **ICM\_COMPRESS\_BEGIN** before compression is stopped with **ICM\_COMPRESS\_END**, it should restart compression with new parameters.

## Requirements



|                                     |                                                                                  |
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

 

 





