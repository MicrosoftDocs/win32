---
title: MCIWNDM_GETPOSITION message (Vfw.h)
description: The MCIWNDM\_GETPOSITION message retrieves the numerical value of the current position within the content of the MCI device.
ms.assetid: 6dc5d3bd-8515-4514-a2a5-c1bee07f7acf
keywords:
- MCIWNDM_GETPOSITION message Windows Multimedia
topic_type:
- apiref
api_name:
- MCIWNDM_GETPOSITION
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCIWNDM\_GETPOSITION message

The **MCIWNDM\_GETPOSITION** message retrieves the numerical value of the current position within the content of the MCI device. This macro also provides the current position in string form in an application-defined buffer. You can send this message explicitly or by using the [**MCIWndGetPosition**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetposition) or [**MCIWndGetPositionString**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetpositionstring) macro.


```C++
MCIWNDM_GETPOSITION 
wParam = (WPARAM) (UINT) len; 
lParam = (LPARAM) (LPTSTR) lp; 
```



## Parameters

<dl> <dt>

<span id="len"></span><span id="LEN"></span>*len*
</dt> <dd>

Size, in bytes, of the buffer. If the null-terminated string is longer than the buffer, it is truncated. Use zero to inhibit retrieval of the position as a string.

</dd> <dt>

<span id="lp"></span><span id="LP"></span>*lp*
</dt> <dd>

Pointer to an application-defined buffer used to return the position. Use zero to inhibit retrieval of the position as a string. If the device supports tracks, the string position information is returned in the form TT:MM:SS:FF where TT corresponds to tracks, MM and SS correspond to minutes and seconds, and FF corresponds to frames.

</dd> </dl>

## Return Value

Returns an integer corresponding to the current position. The units for the position value depend on the current time format.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[**MCIWndGetPosition**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetposition)
</dt> <dt>

[**MCIWndGetPositionString**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetpositionstring)
</dt> </dl>

 

 





