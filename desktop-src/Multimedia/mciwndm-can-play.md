---
title: MCIWNDM_CAN_PLAY message (Vfw.h)
description: The MCIWNDM\_CAN\_PLAY message determines if an MCI device can play a data file or content of some other kind. You can send this message explicitly or by using the MCIWndCanPlay macro.
ms.assetid: dbb742b0-b8ab-4b80-96da-c4823a4747c9
keywords:
- MCIWNDM_CAN_PLAY message Windows Multimedia
topic_type:
- apiref
api_name:
- MCIWNDM_CAN_PLAY
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCIWNDM\_CAN\_PLAY message

The **MCIWNDM\_CAN\_PLAY** message determines if an MCI device can play a data file or content of some other kind. You can send this message explicitly or by using the [**MCIWndCanPlay**](/windows/desktop/api/Vfw/nf-vfw-mciwndcanplay) macro.


```C++
MCIWNDM_CAN_PLAY 
wParam = 0; 
lParam = 0; 
```



## Return Value

Returns **TRUE** if the device supports playing the data or **FALSE** otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[**MCIWndCanPlay**](/windows/desktop/api/Vfw/nf-vfw-mciwndcanplay)
</dt> </dl>

 

 





