---
title: MMIOM_CLOSE message (Mmsystem.h)
description: The MMIOM\_CLOSE message is sent to an I/O procedure by the mmioClose function to request that a file be closed.
ms.assetid: 9d0dad5b-fd0a-4948-a4cf-9d138e353c76
keywords:
- MMIOM_CLOSE message Windows Multimedia
topic_type:
- apiref
api_name:
- MMIOM_CLOSE
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MMIOM\_CLOSE message

The **MMIOM\_CLOSE** message is sent to an I/O procedure by the [**mmioClose**](/windows/win32/api/mmiscapi/nf-mmiscapi-mmioclose) function to request that a file be closed.


```C++
MMIOM_CLOSE 
lParam1 = (LPARAM) lCloseFlags 
lParam2 = reserved 
```



## Parameters

<dl> <dt>

<span id="lCloseFlags"></span><span id="lcloseflags"></span><span id="LCLOSEFLAGS"></span>*lCloseFlags*
</dt> <dd>

Flags contained in the**wFlags**parameter of**mmioClose**.

</dd> </dl>

## Return Value

Returns zero if the file is successfully closed or an error otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Mmsystem.h (include Windows.h)</dt> </dl> |



 

