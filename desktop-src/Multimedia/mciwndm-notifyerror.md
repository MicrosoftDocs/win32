---
title: MCIWNDM_NOTIFYERROR message (Vfw.h)
description: The MCIWNDM\_NOTIFYERROR message notifies the parent window of an application that an MCI error occurred.
ms.assetid: 0f54886a-77dc-43cc-be46-2d322c75471a
keywords:
- MCIWNDM_NOTIFYERROR message Windows Multimedia
topic_type:
- apiref
api_name:
- MCIWNDM_NOTIFYERROR
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCIWNDM\_NOTIFYERROR message

The **MCIWNDM\_NOTIFYERROR** message notifies the parent window of an application that an MCI error occurred.


```C++
MCIWNDM_NOTIFYERROR 
wParam = (WPARAM) (HWND) hwnd; 
lParam = (LPARAM) (LONG) errorCode; 
```



## Parameters

<dl> <dt>

<span id="hwnd"></span><span id="HWND"></span>*hwnd*
</dt> <dd>

Handle to the MCIWnd window.

</dd> <dt>

<span id="errorCode"></span><span id="errorcode"></span><span id="ERRORCODE"></span>*errorCode*
</dt> <dd>

Numerical code for the MCI error.

</dd> </dl>

## Remarks

You can enable MCI error notification by specifying the MCIWNDF\_NOTIFYERROR window style.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



 

 





