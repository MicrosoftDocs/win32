---
title: MCIWNDM_GETDEVICE message (Vfw.h)
description: The MCIWNDM\_GETDEVICE message retrieves the name of the currently open MCI device. You can send this message explicitly or by using the MCIWndGetDevice macro.
ms.assetid: e69a73a6-a927-4536-98c7-ee7d5b16668a
keywords:
- MCIWNDM_GETDEVICE message Windows Multimedia
topic_type:
- apiref
api_name:
- MCIWNDM_GETDEVICE
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCIWNDM\_GETDEVICE message

The **MCIWNDM\_GETDEVICE** message retrieves the name of the currently open MCI device. You can send this message explicitly or by using the [**MCIWndGetDevice**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetdevice) macro.


```C++
MCIWNDM_GETDEVICE 
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

Pointer to an application-defined buffer to return the device name.

</dd> </dl>

## Return Value

Returns zero if successful or a nonzero value otherwise.

## Remarks

If the null-terminated string containing the device name is longer than the buffer, MCIWnd truncates it.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



 

 





