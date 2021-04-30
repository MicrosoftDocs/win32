---
title: MCIWNDM_GETVOLUME message (Vfw.h)
description: The MCIWNDM\_GETVOLUME message retrieves the current volume setting of an MCI device. You can send this message explicitly or by using the MCIWndGetVolume macro.
ms.assetid: 3f1de023-4da8-4899-accc-409701d6e921
keywords:
- MCIWNDM_GETVOLUME message Windows Multimedia
topic_type:
- apiref
api_name:
- MCIWNDM_GETVOLUME
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCIWNDM\_GETVOLUME message

The **MCIWNDM\_GETVOLUME** message retrieves the current volume setting of an MCI device. You can send this message explicitly or by using the [**MCIWndGetVolume**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetvolume) macro.


```C++
MCIWNDM_GETVOLUME 
wParam = 0; 
lParam = 0; 
```



## Return Value

Returns the current volume setting. The default value is 1000. Higher values indicate louder volumes, lower values indicate quieter volumes.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[**MCIWndGetVolume**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetvolume)
</dt> </dl>

 

 





