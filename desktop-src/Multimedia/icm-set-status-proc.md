---
title: ICM_SET_STATUS_PROC message (Vfw.h)
description: The ICM\_SET\_STATUS\_PROC message provides a status callback function with the status of a lengthy operation.
ms.assetid: a1bcd840-b94b-487e-91d6-67411a8a3a2d
keywords:
- ICM_SET_STATUS_PROC message Windows Multimedia
topic_type:
- apiref
api_name:
- ICM_SET_STATUS_PROC
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# ICM\_SET\_STATUS\_PROC message

The **ICM\_SET\_STATUS\_PROC** message provides a status callback function with the status of a lengthy operation.


```C++
ICM_SET_STATUS_PROC 
wParam = (DWORD_PTR)icsetstatusProc; 
lParam = sizeof(ICSETSTATUSPROC); 
```



## Parameters

<dl> <dt>

<span id="icsetstatusProc"></span><span id="icsetstatusproc"></span><span id="ICSETSTATUSPROC"></span>*icsetstatusProc*
</dt> <dd>

Pointer to an [**ICSETSTATUSPROC**](/windows/desktop/api/Vfw/ns-vfw-icsetstatusproc) structure.

</dd> <dt>

<span id="lParam"></span><span id="lparam"></span><span id="LPARAM"></span>*lParam*
</dt> <dd>

Size, in bytes, of **ICSETSTATUSPROC**.

</dd> </dl>

## Return Value

Returns ICERR\_OK if successful or an error otherwise.

## Remarks

Support of this message is optional but strongly recommended if compression or decompression takes longer than approximately one-tenth of a second.

An application can send this message periodically to a status callback function during lengthy operations.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[Video Compression Manager](video-compression-manager.md)
</dt> <dt>

[Video Compression Messages](video-compression-messages.md)
</dt> </dl>

 

 





