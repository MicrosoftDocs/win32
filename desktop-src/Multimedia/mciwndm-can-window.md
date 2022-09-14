---
title: MCIWNDM_CAN_WINDOW message (Vfw.h)
description: The MCIWNDM\_CAN\_WINDOW message determines if an MCI device supports window-oriented MCI commands. You can send this message explicitly or by using the MCIWndCanWindow macro.
ms.assetid: bf89c096-1272-441e-9334-2b4215dbc979
keywords:
- MCIWNDM_CAN_WINDOW message Windows Multimedia
topic_type:
- apiref
api_name:
- MCIWNDM_CAN_WINDOW
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCIWNDM\_CAN\_WINDOW message

The **MCIWNDM\_CAN\_WINDOW** message determines if an MCI device supports window-oriented MCI commands. You can send this message explicitly or by using the [**MCIWndCanWindow**](/windows/desktop/api/Vfw/nf-vfw-mciwndcanwindow) macro.


```C++
MCIWNDM_CAN_WINDOW 
wParam = 0; 
lParam = 0; 
```



## Return Value

Returns **TRUE** if the device supports window-oriented MCI commands or **FALSE** otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[**MCIWndCanWindow**](/windows/desktop/api/Vfw/nf-vfw-mciwndcanwindow)
</dt> </dl>

 

 





