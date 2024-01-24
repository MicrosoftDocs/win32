---
title: MMIOM_SEEK message (Mmsystem.h)
description: The MMIOM\_SEEK message is sent to an I/O procedure by the mmioSeek function to request that the current file position be moved.
ms.assetid: 428b231a-6e00-4458-9ba2-e9b0b028843a
keywords:
- MMIOM_SEEK message Windows Multimedia
topic_type:
- apiref
api_name:
- MMIOM_SEEK
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MMIOM\_SEEK message

The **MMIOM\_SEEK** message is sent to an I/O procedure by the [**mmioSeek**](/windows/win32/api/mmiscapi/nf-mmiscapi-mmioseek) function to request that the current file position be moved.


```C++
MMIOM_SEEK 
lParam1 = (LPARAM) lNewFilePos 
lParam2 = (LPARAM) lChangeFlag 
```



## Parameters

<dl> <dt>

<span id="lNewFilePos"></span><span id="lnewfilepos"></span><span id="LNEWFILEPOS"></span>*lNewFilePos*
</dt> <dd>

New file position. The meaning of this value is dependent on the flag specified in**lChangeFlag**.

</dd> <dt>

<span id="lChangeFlag"></span><span id="lchangeflag"></span><span id="LCHANGEFLAG"></span>*lChangeFlag*
</dt> <dd>

Flag specifying how the file position is changed. The following values are defined:



| Requirement | Value |
|-----------|------------------------------------------------------------------------------------------------------------------------|
| SEEK\_CUR | Move the file position to be *lNewFilePos* bytes from the current position. *lNewFilePos* can be positive or negative. |
| SEEK\_END | Move the file position to be *lNewFilePos* bytes from the end of the file.                                             |
| SEEK\_SET | Move the file position to be *lNewFilePos* bytes from the beginning of the file.                                       |



 

</dd> </dl>

## Return Value

Returns the new file position. If there is an error, the return value is  1.

## Remarks

The I/O procedure is responsible for maintaining the current file position in the **lDiskOffset** member of the [**MMIOINFO**](/previous-versions//dd757322(v=vs.85)) structure.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Mmsystem.h (include Windows.h)</dt> </dl> |



 

