---
title: MCIWNDM_CAN_EJECT message (Vfw.h)
description: The MCIWNDM\_CAN\_EJECT message determines if an MCI device can eject its media. You can send this message explicitly or by using the MCIWndCanEject macro.
ms.assetid: e9bd33c4-0ad8-4c0a-8b75-52011b58904d
keywords:
- MCIWNDM_CAN_EJECT message Windows Multimedia
topic_type:
- apiref
api_name:
- MCIWNDM_CAN_EJECT
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCIWNDM\_CAN\_EJECT message

The **MCIWNDM\_CAN\_EJECT** message determines if an MCI device can eject its media. You can send this message explicitly or by using the [**MCIWndCanEject**](/windows/desktop/api/Vfw/nf-vfw-mciwndcaneject) macro.


```C++
MCIWNDM_CAN_EJECT 
wParam = 0; 
lParam = 0; 
```



## Return Value

Returns **TRUE** if the device can eject its media or **FALSE** otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[**MCIWndCanEject**](/windows/desktop/api/Vfw/nf-vfw-mciwndcaneject)
</dt> </dl>

 

 





