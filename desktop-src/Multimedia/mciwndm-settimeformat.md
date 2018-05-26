---
title: MCIWNDM\_SETTIMEFORMAT message
description: The MCIWNDM\_SETTIMEFORMAT message sets the time format of an MCI device. You can send this message explicitly or by using the MCIWndSetTimeFormat macro.
ms.assetid: 7de82094-6d35-44fd-88e7-ebd18a558cfd
keywords:
- MCIWNDM_SETTIMEFORMAT message Windows Multimedia
topic_type:
- apiref
api_name:
- MCIWNDM_SETTIMEFORMAT
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

# MCIWNDM\_SETTIMEFORMAT message

The **MCIWNDM\_SETTIMEFORMAT** message sets the time format of an MCI device. You can send this message explicitly or by using the [**MCIWndSetTimeFormat**](/windows/win32/Vfw/nf-vfw-mciwndsettimeformat?branch=master) macro.


```C++
MCIWNDM_SETTIMEFORMAT 
wParam = 0; 
lParam = (LPARAM) (LPSTR) lp; 
```



## Parameters

<dl> <dt>

<span id="lp"></span><span id="LP"></span>*lp*
</dt> <dd>

Pointer to a buffer containing the null-terminated string indicating the time format. Specify "frames" to set the time format to frames, or "ms" to set the time format to milliseconds.

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

An application can specify time formats other than frames or milliseconds as long as the formats are supported by the MCI device. Noncontinuous formats, such as tracks and SMPTE, can cause the trackbar to behave erratically. For these time formats, you might want to turn off the toolbar by using the [**MCIWndChangeStyles**](/windows/win32/Vfw/nf-vfw-mciwndchangestyles?branch=master) macro and specifying the MCIWNDF\_NOPLAYBAR window style.

If you want to set the time format to frames or milliseconds, you can also use the [**MCIWndUseFrames**](/windows/win32/Vfw/nf-vfw-mciwnduseframes?branch=master) or [**MCIWndUseTime**](/windows/win32/Vfw/nf-vfw-mciwndusetime?branch=master) macro. For a list of time formats, see the [**MCIWndGetTimeFormat**](/windows/win32/Vfw/nf-vfw-mciwndgettimeformat?branch=master) macro.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[**MCIWndChangeStyles**](/windows/win32/Vfw/nf-vfw-mciwndchangestyles?branch=master)
</dt> <dt>

[**MCIWndGetTimeFormat**](/windows/win32/Vfw/nf-vfw-mciwndgettimeformat?branch=master)
</dt> <dt>

[**MCIWndSetTimeFormat**](/windows/win32/Vfw/nf-vfw-mciwndsettimeformat?branch=master)
</dt> <dt>

[**MCIWndUseFrames**](/windows/win32/Vfw/nf-vfw-mciwnduseframes?branch=master)
</dt> <dt>

[**MCIWndUseTime**](/windows/win32/Vfw/nf-vfw-mciwndusetime?branch=master)
</dt> </dl>

 

 





