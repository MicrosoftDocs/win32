---
title: MCIWNDM_NEW message (Vfw.h)
description: The MCIWNDM\_NEW message creates a new file for the current MCI device. You can send this message explicitly or by using the MCIWndNew macro.
ms.assetid: 18b2340d-8303-415a-867f-bd346034db2a
keywords:
- MCIWNDM_NEW message Windows Multimedia
topic_type:
- apiref
api_name:
- MCIWNDM_NEW
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCIWNDM\_NEW message

The **MCIWNDM\_NEW** message creates a new file for the current MCI device. You can send this message explicitly or by using the [**MCIWndNew**](/windows/desktop/api/Vfw/nf-vfw-mciwndnew) macro.


```C++
MCIWNDM_NEW 
wParam = 0; 
lParam = (LPARAM) (LPVOID) lp; 
```



## Parameters

<dl> <dt>

<span id="lp"></span><span id="LP"></span>*lp*
</dt> <dd>

Pointer to a buffer containing the name of the MCI device that will use the file.

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[**MCIWndNew**](/windows/desktop/api/Vfw/nf-vfw-mciwndnew)
</dt> </dl>

 

 





