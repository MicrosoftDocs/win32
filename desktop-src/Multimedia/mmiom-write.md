---
title: MMIOM_WRITE message (Mmsystem.h)
description: The MMIOM\_WRITE message is sent to an I/O procedure by the mmioWrite function to request that data be written to an open file.
ms.assetid: 46e2dd9a-c4a7-4c99-86e4-a67b424411d1
keywords:
- MMIOM_WRITE message Windows Multimedia
topic_type:
- apiref
api_name:
- MMIOM_WRITE
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MMIOM\_WRITE message

The **MMIOM\_WRITE** message is sent to an I/O procedure by the [**mmioWrite**](/windows/win32/api/mmiscapi/nf-mmiscapi-mmiowrite) function to request that data be written to an open file.


```C++
MMIOM_WRITE 
lParam1 = (LPARAM) lpBuffer 
lParam2 = (LPARAM) cbWrite 
```



## Parameters

<dl> <dt>

<span id="lpBuffer"></span><span id="lpbuffer"></span><span id="LPBUFFER"></span>*lpBuffer*
</dt> <dd>

Pointer to a buffer containing the data to write to the file.

</dd> <dt>

<span id="cbWrite"></span><span id="cbwrite"></span><span id="CBWRITE"></span>*cbWrite*
</dt> <dd>

Number of bytes to write to file.

</dd> </dl>

## Return Value

Returns the number of bytes actually written to the file. If there is an error, the return value is  1.

## Remarks

The I/O procedure is responsible for updating the **lDiskOffset** member of the [**MMIOINFO**](/previous-versions//dd757322(v=vs.85)) structure to reflect the new file position after the write operation.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Mmsystem.h (include Windows.h)</dt> </dl> |



 

