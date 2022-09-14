---
title: MCIWNDM_NOTIFYMODE message (Vfw.h)
description: The MCIWNDM\_NOTIFYMODE message notifies the parent window of an application that the operating mode of the MCI device has changed.
ms.assetid: 08adfa8b-4d88-4953-acd8-8a4728f9e1b6
keywords:
- MCIWNDM_NOTIFYMODE message Windows Multimedia
topic_type:
- apiref
api_name:
- MCIWNDM_NOTIFYMODE
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCIWNDM\_NOTIFYMODE message

The **MCIWNDM\_NOTIFYMODE** message notifies the parent window of an application that the operating mode of the MCI device has changed.


```C++
MCIWNDM_NOTIFYMODE 
wParam = (WPARAM) (HWND) hwnd; 
lParam = (LPARAM) (LONG) mode; 
```



## Parameters

<dl> <dt>

<span id="hwnd"></span><span id="HWND"></span>*hwnd*
</dt> <dd>

Handle to the MCIWnd window.

</dd> <dt>

<span id="mode"></span><span id="MODE"></span>*mode*
</dt> <dd>

Integer corresponding to the MCI mode.

</dd> </dl>

## Remarks

You can enable notification of mode changes of an MCI device by specifying the MCIWNDF\_NOTIFYMODE window style.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



 

 





