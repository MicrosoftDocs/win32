---
title: MCIWNDM_GETTIMEFORMAT message (Vfw.h)
description: The MCIWNDM\_GETTIMEFORMAT message retrieves the current time format of an MCI device in two forms as a numerical value and as a string. You can send this message explicitly or by using the MCIWndGetTimeFormat macro.
ms.assetid: 01844872-5444-4f3b-92a3-64f80b94d3a0
keywords:
- MCIWNDM_GETTIMEFORMAT message Windows Multimedia
topic_type:
- apiref
api_name:
- MCIWNDM_GETTIMEFORMAT
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCIWNDM\_GETTIMEFORMAT message

The **MCIWNDM\_GETTIMEFORMAT** message retrieves the current time format of an MCI device in two forms: as a numerical value and as a string. You can send this message explicitly or by using the [**MCIWndGetTimeFormat**](/windows/desktop/api/Vfw/nf-vfw-mciwndgettimeformat) macro.


```C++
MCIWNDM_GETTIMEFORMAT 
wParam = (WPARAM) (UINT) len; 
lParam = (LPARAM) (LPSTR) lp; 
```



## Parameters

<dl> <dt>

<span id="len"></span><span id="LEN"></span>*len*
</dt> <dd>

Size, in bytes, of the buffer.

</dd> <dt>

<span id="lp"></span><span id="LP"></span>*lp*
</dt> <dd>

Pointer to a buffer to contain the null-terminated string form of the time format.

</dd> </dl>

## Return Value

Returns an integer corresponding to the MCI constant defining the time format.

## Remarks

If the time format string is longer than the return buffer, MCIWnd truncates the string.

An MCI device can support one or more of the following time formats.



| Time format                      | MCI constant               |
|----------------------------------|----------------------------|
| Bytes                            | MCI\_FORMAT\_BYTES         |
| Frames                           | MCI\_FORMAT\_FRAMES        |
| Hours, minutes, seconds          | MCI\_FORMAT\_HMS           |
| Milliseconds                     | MCI\_FORMAT\_MILLISECONDS  |
| Minutes, seconds, frames         | MCI\_FORMAT\_MSF           |
| Samples                          | MCI\_FORMAT\_SAMPLES       |
| SMPTE 24                         | MCI\_FORMAT\_SMPTE\_24     |
| SMPTE 25                         | MCI\_FORMAT\_SMPTE\_25     |
| SMPTE 30 drop                    | MCI\_FORMAT\_SMPTE\_30DROP |
| SMPTE 30 (non-drop)              | MCI\_FORMAT\_SMPTE\_30     |
| Tracks, minutes, seconds, frames | MCI\_FORMAT\_TMSF          |



 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[**MCIWndGetTimeFormat**](/windows/desktop/api/Vfw/nf-vfw-mciwndgettimeformat)
</dt> </dl>

 

 





