---
title: MCIWNDM_CAN_RECORD message (Vfw.h)
description: The MCIWNDM\_CAN\_RECORD message determines if an MCI device supports recording. You can send this message explicitly or by using the MCIWndCanRecord macro.
ms.assetid: b5a789fa-6a88-487d-a374-8f4798ee5a62
keywords:
- MCIWNDM_CAN_RECORD message Windows Multimedia
topic_type:
- apiref
api_name:
- MCIWNDM_CAN_RECORD
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCIWNDM\_CAN\_RECORD message

The **MCIWNDM\_CAN\_RECORD** message determines if an MCI device supports recording. You can send this message explicitly or by using the [**MCIWndCanRecord**](/windows/desktop/api/Vfw/nf-vfw-mciwndcanrecord) macro.


```C++
MCIWNDM_CAN_RECORD 
wParam = 0; 
lParam = 0; 
```



## Return Value

Returns **TRUE** if the device supports recording or **FALSE** otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[**MCIWndCanRecord**](/windows/desktop/api/Vfw/nf-vfw-mciwndcanrecord)
</dt> </dl>

 

 





