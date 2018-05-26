---
title: MCIWNDM\_GETFILENAME message
description: The MCIWNDM\_GETFILENAME message retrieves the filename currently used by an MCI device. You can send this message explicitly or by using the MCIWndGetFileName macro.
ms.assetid: d61b1b6d-0fae-4732-993c-41e08a4e05be
keywords:
- MCIWNDM_GETFILENAME message Windows Multimedia
topic_type:
- apiref
api_name:
- MCIWNDM_GETFILENAME
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

# MCIWNDM\_GETFILENAME message

The **MCIWNDM\_GETFILENAME** message retrieves the filename currently used by an MCI device. You can send this message explicitly or by using the [**MCIWndGetFileName**](/windows/win32/Vfw/nf-vfw-mciwndgetfilename?branch=master) macro.


```C++
MCIWNDM_GETFILENAME 
wParam = (WPARAM) (UINT) len; 
lParam = (LPARAM) (LPVOID) lp; 
```



## Parameters

<dl> <dt>

<span id="len"></span><span id="LEN"></span>*len*
</dt> <dd>

Size, in bytes, of the buffer.

</dd> <dt>

<span id="lp"></span><span id="LP"></span>*lp*
</dt> <dd>

Pointer to an application-defined buffer to return the filename.

</dd> </dl>

## Return Value

Returns zero if successful or 1 otherwise.

## Remarks

If the null-terminated string containing the filename is longer than the buffer, MCIWnd truncates the filename.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[**MCIWndGetFileName**](/windows/win32/Vfw/nf-vfw-mciwndgetfilename?branch=master)
</dt> </dl>

 

 





