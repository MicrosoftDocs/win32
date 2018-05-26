---
title: MCIWNDM\_CAN\_WINDOW message
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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MCIWNDM\_CAN\_WINDOW message

The **MCIWNDM\_CAN\_WINDOW** message determines if an MCI device supports window-oriented MCI commands. You can send this message explicitly or by using the [**MCIWndCanWindow**](/windows/win32/Vfw/nf-vfw-mciwndcanwindow?branch=master) macro.


```C++
MCIWNDM_CAN_WINDOW 
wParam = 0; 
lParam = 0; 
```



## Return Value

Returns **TRUE** if the device supports window-oriented MCI commands or **FALSE** otherwise.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[**MCIWndCanWindow**](/windows/win32/Vfw/nf-vfw-mciwndcanwindow?branch=master)
</dt> </dl>

 

 





