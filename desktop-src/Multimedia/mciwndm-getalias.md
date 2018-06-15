---
title: MCIWNDM\_GETALIAS message
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
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MCIWNDM\_GETALIAS message

The **MCIWNDM\_GETALIAS** message retrieves the alias used to open an MCI device or file with the [**mciSendString**](https://msdn.microsoft.com/en-us/library/Dd757161(v=VS.85).aspx) function. You can send this message explicitly or by using the [**MCIWndGetAlias**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetalias) macro.


```C++
MCIWNDM_GETALIAS 
wParam = 0; 
lParam = 0; 
```



## Return Value

Returns the device alias.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[**mciSendString**](https://msdn.microsoft.com/en-us/library/Dd757161(v=VS.85).aspx)
</dt> <dt>

[**MCIWndGetAlias**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetalias)
</dt> </dl>

 

 





