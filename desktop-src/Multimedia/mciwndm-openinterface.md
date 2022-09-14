---
title: MCIWNDM_OPENINTERFACE message (Vfw.h)
description: The MCIWNDM\_OPENINTERFACE message attaches the data stream or file associated with the specified interface to an MCIWnd window. You can send this message explicitly or by using the MCIWndOpenInterface macro.
ms.assetid: 73cbd637-d315-4b39-a978-2b72aed1f303
keywords:
- MCIWNDM_OPENINTERFACE message Windows Multimedia
topic_type:
- apiref
api_name:
- MCIWNDM_OPENINTERFACE
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCIWNDM\_OPENINTERFACE message

The **MCIWNDM\_OPENINTERFACE** message attaches the data stream or file associated with the specified interface to an MCIWnd window. You can send this message explicitly or by using the [**MCIWndOpenInterface**](/windows/desktop/api/Vfw/nf-vfw-mciwndopeninterface) macro.


```C++
MCIWNDM_OPENINTERFACE 
wParam = 0; 
lParam = (LPARAM) (LPUNKNOWN) pUnk; 
```



## Parameters

<dl> <dt>

<span id="pUnk"></span><span id="punk"></span><span id="PUNK"></span>*pUnk*
</dt> <dd>

Pointer to an IAVI interface that points to a file or a data stream in a file.

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

[**MCIWndOpenInterface**](/windows/desktop/api/Vfw/nf-vfw-mciwndopeninterface)
</dt> </dl>

 

 





