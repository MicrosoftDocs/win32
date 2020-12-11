---
title: MCIWNDM_GETSPEED message (Vfw.h)
description: The MCIWNDM\_GETSPEED message retrieves the playback speed of an MCI device. You can send this message explicitly or by using the MCIWndGetSpeed macro.
ms.assetid: d10a8f88-e85e-449b-8655-bb0832031d59
keywords:
- MCIWNDM_GETSPEED message Windows Multimedia
topic_type:
- apiref
api_name:
- MCIWNDM_GETSPEED
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCIWNDM\_GETSPEED message

The **MCIWNDM\_GETSPEED** message retrieves the playback speed of an MCI device. You can send this message explicitly or by using the [**MCIWndGetSpeed**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetspeed) macro.


```C++
MCIWNDM_GETSPEED 
wParam = 0; 
lParam = 0; 
```



## Return Value

Returns the playback speed if successful. The value for normal speed is 1000. Larger values indicate faster speeds, smaller values indicate slower speeds.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[**MCIWndGetSpeed**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetspeed)
</dt> </dl>

 

 





