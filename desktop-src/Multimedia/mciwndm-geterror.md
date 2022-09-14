---
title: MCIWNDM_GETERROR message (Vfw.h)
description: The MCIWNDM\_GETERROR message retrieves the last MCI error encountered. You can send this message explicitly or by using the MCIWndGetError macro.
ms.assetid: f110a9b3-5b05-4bf0-85d1-b49ce7396222
keywords:
- MCIWNDM_GETERROR message Windows Multimedia
topic_type:
- apiref
api_name:
- MCIWNDM_GETERROR
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCIWNDM\_GETERROR message

The **MCIWNDM\_GETERROR** message retrieves the last MCI error encountered. You can send this message explicitly or by using the [**MCIWndGetError**](/windows/desktop/api/Vfw/nf-vfw-mciwndgeterror) macro.


```C++
MCIWNDM_GETERROR 
wParam = (WPARAM) (UINT) len; 
lParam = (LPARAM) (LPVOID) lp; 
```



## Parameters

<dl> <dt>

<span id="len"></span><span id="LEN"></span>*len*
</dt> <dd>

Size, in bytes, of the error buffer.

</dd> <dt>

<span id="lp"></span><span id="LP"></span>*lp*
</dt> <dd>

Pointer to an application-defined buffer used to return the error string.

</dd> </dl>

## Return Value

Returns the integer error value if successful.

## Remarks

If *lp* is a valid pointer, a null-terminated string corresponding to the error is returned in its buffer. If the error string is longer than the buffer, MCIWnd truncates it.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[**MCIWndGetError**](/windows/desktop/api/Vfw/nf-vfw-mciwndgeterror)
</dt> </dl>

 

 





