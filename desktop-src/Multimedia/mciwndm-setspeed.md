---
title: MCIWNDM\_SETSPEED message
description: The MCIWNDM\_SETSPEED message sets the playback speed of an MCI device. You can send this message explicitly or by using the MCIWndSetSpeed macro.
ms.assetid: 7658dd25-dc68-4bd1-b995-df06b509be16
keywords:
- MCIWNDM_SETSPEED message Windows Multimedia
topic_type:
- apiref
api_name:
- MCIWNDM_SETSPEED
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

# MCIWNDM\_SETSPEED message

The **MCIWNDM\_SETSPEED** message sets the playback speed of an MCI device. You can send this message explicitly or by using the [**MCIWndSetSpeed**](/windows/win32/Vfw/nf-vfw-mciwndsetspeed?branch=master) macro.


```C++
MCIWNDM_SETSPEED 
wParam = 0; 
lParam = (LPARAM) (UINT) iSpeed; 
```



## Parameters

<dl> <dt>

<span id="iSpeed"></span><span id="ispeed"></span><span id="ISPEED"></span>*iSpeed*
</dt> <dd>

Playback speed. Specify 1000 for normal speed, larger values for faster speeds, and smaller values for slower speeds.

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[**MCIWndSetSpeed**](/windows/win32/Vfw/nf-vfw-mciwndsetspeed?branch=master)
</dt> </dl>

 

 





