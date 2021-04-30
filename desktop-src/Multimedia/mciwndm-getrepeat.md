---
title: MCIWNDM_GETREPEAT message (Vfw.h)
description: The MCIWNDM\_GETREPEAT message determines if continuous playback has been activated. You can send this message explicitly or by using the MCIWndGetRepeat macro.
ms.assetid: 6d644117-e705-421f-b45f-9f0e833e6bc8
keywords:
- MCIWNDM_GETREPEAT message Windows Multimedia
topic_type:
- apiref
api_name:
- MCIWNDM_GETREPEAT
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCIWNDM\_GETREPEAT message

The **MCIWNDM\_GETREPEAT** message determines if continuous playback has been activated. You can send this message explicitly or by using the [**MCIWndGetRepeat**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetrepeat) macro.


```C++
MCIWNDM_GETREPEAT 
wParam = 0; 
lParam = 0; 
```



## Return Value

Returns **TRUE** if continuous playback is activated or **FALSE** otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[**MCIWndGetRepeat**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetrepeat)
</dt> </dl>

 

 





