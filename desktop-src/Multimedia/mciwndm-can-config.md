---
title: MCIWNDM\_CAN\_CONFIG message
description: The MCIWNDM\_CAN\_CONFIG message determines if an MCI device can display a configuration dialog box. You can send this message explicitly or by using the MCIWndCanConfig macro.
ms.assetid: 'f1eb22a8-d0fc-4d2c-a414-392e560cfbed'
keywords: ["MCIWNDM_CAN_CONFIG message Windows Multimedia"]
topic_type:
- apiref
api_name:
- MCIWNDM_CAN_CONFIG
api_location:
- Vfw.h
api_type:
- HeaderDef
---

# MCIWNDM\_CAN\_CONFIG message

The **MCIWNDM\_CAN\_CONFIG** message determines if an MCI device can display a configuration dialog box. You can send this message explicitly or by using the [**MCIWndCanConfig**](mciwndcanconfig.md) macro.


```C++
MCIWNDM_CAN_CONFIG 
wParam = 0; 
lParam = 0; 
```



## Return Value

Returns **TRUE** if the device supports configuration or **FALSE** otherwise.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[**MCIWndCanConfig**](mciwndcanconfig.md)
</dt> </dl>

 

 





