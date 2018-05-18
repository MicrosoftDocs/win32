---
title: MCIWNDM\_GETDEVICEID message
description: The MCIWNDM\_GETDEVICEID message retrieves the identifier of the currently open MCI device to use with the mciSendCommand function. You can send this message explicitly or by using the MCIWndGetDeviceID macro.
ms.assetid: '188f15fa-579a-438e-a812-9a2b684127c0'
keywords: ["MCIWNDM_GETDEVICEID message Windows Multimedia"]
topic_type:
- apiref
api_name:
- MCIWNDM_GETDEVICEID
api_location:
- Vfw.h
api_type:
- HeaderDef
---

# MCIWNDM\_GETDEVICEID message

The **MCIWNDM\_GETDEVICEID** message retrieves the identifier of the currently open MCI device to use with the [**mciSendCommand**](mcisendcommand.md) function. You can send this message explicitly or by using the [**MCIWndGetDeviceID**](mciwndgetdeviceid.md) macro.


```C++
MCIWNDM_GETDEVICEID 
wParam = 0; 
lParam = 0; 
```



## Return Value

Returns the device identifier.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[**mciSendCommand**](mcisendcommand.md)
</dt> <dt>

[**MCIWndGetDeviceID**](mciwndgetdeviceid.md)
</dt> </dl>

 

 





