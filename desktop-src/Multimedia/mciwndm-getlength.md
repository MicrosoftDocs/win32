---
title: MCIWNDM_GETLENGTH message (Vfw.h)
description: The MCIWNDM\_GETLENGTH message retrieves the length of the content or file currently used by an MCI device. You can send this message explicitly or by using the MCIWndGetLength macro.
ms.assetid: bee4d9fc-78eb-4577-98bb-d6c2d9acbb7f
keywords:
- MCIWNDM_GETLENGTH message Windows Multimedia
topic_type:
- apiref
api_name:
- MCIWNDM_GETLENGTH
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCIWNDM\_GETLENGTH message

The **MCIWNDM\_GETLENGTH** message retrieves the length of the content or file currently used by an MCI device. You can send this message explicitly or by using the [**MCIWndGetLength**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetlength) macro.


```C++
MCIWNDM_GETLENGTH 
wParam = 0; 
lParam = 0; 
```



## Return Value

Returns the length. The units for the length depend on the current time format.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[**MCIWndGetLength**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetlength)
</dt> </dl>

 

 





