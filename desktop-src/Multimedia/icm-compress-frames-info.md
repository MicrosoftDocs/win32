---
title: ICM_COMPRESS_FRAMES_INFO message (Vfw.h)
description: The ICM\_COMPRESS\_FRAMES\_INFO message notifies a compression driver to set the parameters for the pending compression.
ms.assetid: d2f6f3b7-dff6-4fef-a642-cb77b00119af
keywords:
- ICM_COMPRESS_FRAMES_INFO message Windows Multimedia
topic_type:
- apiref
api_name:
- ICM_COMPRESS_FRAMES_INFO
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# ICM\_COMPRESS\_FRAMES\_INFO message

The **ICM\_COMPRESS\_FRAMES\_INFO** message notifies a compression driver to set the parameters for the pending compression.


```C++
ICM_COMPRESS_FRAMES_INFO 
wParam = (DWORD) (LPVOID) &icf; 
lParam = sizeof(ICCOMPRESSFRAMES); 
```



## Parameters

<dl> <dt>

<span id="icf"></span><span id="ICF"></span>*icf*
</dt> <dd>

Pointer to an [**ICCOMPRESSFRAMES**](/windows/desktop/api/Vfw/ns-vfw-iccompressframes) structure. The **GetData** and **PutData** members of this structure are not used with this message.

</dd> <dt>

<span id="lParam"></span><span id="lparam"></span><span id="LPARAM"></span>*lParam*
</dt> <dd>

Size, in bytes, of [**ICCOMPRESSFRAMES**](/windows/desktop/api/Vfw/ns-vfw-iccompressframes).

</dd> </dl>

## Return Value

Returns ICERR\_OK if successful or an error otherwise.

## Remarks

A compressor can use this message to determine how much space to allocate for each frame while compressing.

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

 

 





