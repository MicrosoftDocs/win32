---
title: MCIWNDM\_CAN\_SAVE message
description: The MCIWNDM\_CAN\_SAVE message determines if an MCI device can save data. You can send this message explicitly or by using the MCIWndCanSave macro.
ms.assetid: b4e27190-b095-494b-9ed3-10653bea187b
keywords:
- MCIWNDM_CAN_SAVE message Windows Multimedia
topic_type:
- apiref
api_name:
- MCIWNDM_CAN_SAVE
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

# MCIWNDM\_CAN\_SAVE message

The **MCIWNDM\_CAN\_SAVE** message determines if an MCI device can save data. You can send this message explicitly or by using the [**MCIWndCanSave**](/windows/win32/Vfw/nf-vfw-mciwndcansave?branch=master) macro.


```C++
MCIWNDM_CAN_SAVE 
wParam = 0; 
lParam = 0; 
```



## Return Value

Returns **TRUE** if the device supports saving or **FALSE** otherwise.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[**MCIWndCanSave**](/windows/win32/Vfw/nf-vfw-mciwndcansave?branch=master)
</dt> </dl>

 

 





