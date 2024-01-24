---
title: MCIWNDM_GETALIAS message (Vfw.h)
description: The MCIWNDM\_GETALIAS message retrieves the alias used to open an MCI device or file with the mciSendString function. You can send this message explicitly or by using the MCIWndGetAlias macro.
ms.assetid: 37131b89-275c-4ab6-9278-0e08c42471bd
keywords:
- MCIWNDM_GETALIAS message Windows Multimedia
topic_type:
- apiref
api_name:
- MCIWNDM_GETALIAS
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCIWNDM\_GETALIAS message

The **MCIWNDM\_GETALIAS** message retrieves the alias used to open an MCI device or file with the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function. You can send this message explicitly or by using the [**MCIWndGetAlias**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetalias) macro.


```C++
MCIWNDM_GETALIAS 
wParam = 0; 
lParam = 0; 
```



## Return Value

Returns the device alias.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[**mciSendString**](/previous-versions//dd757161(v=vs.85))
</dt> <dt>

[**MCIWndGetAlias**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetalias)
</dt> </dl>

 

