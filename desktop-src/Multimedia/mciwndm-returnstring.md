---
title: MCIWNDM_RETURNSTRING message (Vfw.h)
description: The MCIWNDM\_RETURNSTRING message retrieves the reply to the most recent MCI string command sent to an MCI device.
ms.assetid: 36a5222c-a63c-4b8c-ad0c-a00477e95b96
keywords:
- MCIWNDM_RETURNSTRING message Windows Multimedia
topic_type:
- apiref
api_name:
- MCIWNDM_RETURNSTRING
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCIWNDM\_RETURNSTRING message

The **MCIWNDM\_RETURNSTRING** message retrieves the reply to the most recent MCI string command sent to an MCI device. Information in the reply is supplied as a null-terminated string. You can send this message explicitly or by using the [**MCIWndReturnString**](/windows/desktop/api/Vfw/nf-vfw-mciwndreturnstring) macro.


```C++
MCIWNDM_RETURNSTRING 
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

Pointer to an application-defined buffer to contain the null-terminated string.

</dd> </dl>

## Return Value

Returns an integer corresponding to the MCI string.

## Remarks

If the null-terminated string is longer than the buffer, the string is truncated.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[**MCIWndReturnString**](/windows/desktop/api/Vfw/nf-vfw-mciwndreturnstring)
</dt> </dl>

 

 





