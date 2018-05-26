---
title: MCIWNDM\_GETDEVICEID message
description: The MCIWNDM\_GETDEVICEID message retrieves the identifier of the currently open MCI device to use with the mciSendCommand function. You can send this message explicitly or by using the MCIWndGetDeviceID macro.
ms.assetid: 188f15fa-579a-438e-a812-9a2b684127c0
keywords:
- MCIWNDM_GETDEVICEID message Windows Multimedia
topic_type:
- apiref
api_name:
- MCIWNDM_GETDEVICEID
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

# MCIWNDM\_GETDEVICEID message

The **MCIWNDM\_GETDEVICEID** message retrieves the identifier of the currently open MCI device to use with the [**mciSendCommand**](/windows/win32/Mmsystem/?branch=master) function. You can send this message explicitly or by using the [**MCIWndGetDeviceID**](/windows/win32/Vfw/nf-vfw-mciwndgetdeviceid?branch=master) macro.


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
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[**mciSendCommand**](/windows/win32/Mmsystem/?branch=master)
</dt> <dt>

[**MCIWndGetDeviceID**](/windows/win32/Vfw/nf-vfw-mciwndgetdeviceid?branch=master)
</dt> </dl>

 

 





