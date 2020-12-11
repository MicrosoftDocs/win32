---
title: MCIWNDM_GETMODE message (Vfw.h)
description: The MCIWNDM\_GETMODE message retrieves the current operating mode of an MCI device. MCI devices have several operating modes, which are designated by constants. You can send this message explicitly or by using the MCIWndGetMode macro.
ms.assetid: cc327281-434e-4047-9e15-c04a10953f47
keywords:
- MCIWNDM_GETMODE message Windows Multimedia
topic_type:
- apiref
api_name:
- MCIWNDM_GETMODE
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCIWNDM\_GETMODE message

The **MCIWNDM\_GETMODE** message retrieves the current operating mode of an MCI device. MCI devices have several operating modes, which are designated by constants. You can send this message explicitly or by using the [**MCIWndGetMode**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetmode) macro.


```C++
MCIWNDM_GETMODE 
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

Pointer to the application-defined buffer used to return the mode.

</dd> </dl>

## Return Value

Returns an integer corresponding to the MCI constant defining the mode.

## Remarks

If the null-terminated string describing the mode is longer than the buffer, it is truncated.

Not all devices can operate in every mode. For example, the MCIAVI device is a playback device; it doesn't support the recording mode. The following modes can be retrieved by using **MCIWNDM\_GETMODE**.



| Operating mode | MCI constant          |
|----------------|-----------------------|
| not ready      | MCI\_MODE\_NOT\_READY |
| open           | MCI\_MODE\_OPEN       |
| paused         | MCI\_MODE\_PAUSE      |
| playing        | MCI\_MODE\_PLAY       |
| recording      | MCI\_MODE\_RECORD     |
| seeking        | MCI\_MODE\_SEEK       |
| stopped        | MCI\_MODE\_STOP       |



 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[**MCIWndGetMode**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetmode)
</dt> </dl>

 

 





