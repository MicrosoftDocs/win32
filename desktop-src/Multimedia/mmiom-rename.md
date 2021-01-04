---
title: MMIOM_RENAME message (Mmsystem.h)
description: The MMIOM\_RENAME message is sent to an I/O procedure by the mmioRename function to request that the specified file be renamed.
ms.assetid: 38a746c8-3a6f-4cb2-a5b4-c11bd1e73c8a
keywords:
- MMIOM_RENAME message Windows Multimedia
topic_type:
- apiref
api_name:
- MMIOM_RENAME
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MMIOM\_RENAME message

The **MMIOM\_RENAME** message is sent to an I/O procedure by the [**mmioRename**](/windows/win32/api/mmiscapi/nf-mmiscapi-mmiorename) function to request that the specified file be renamed.


```C++
MMIOM_RENAME 
lParam1 = (LPARAM) lpszOldFilename 
lParam2 = (LPARAM) lpszNewFilename 
```



## Parameters

<dl> <dt>

<span id="lpszOldFilename"></span><span id="lpszoldfilename"></span><span id="LPSZOLDFILENAME"></span>*lpszOldFilename*
</dt> <dd>

Pointer to a string containing the filename of the file to rename.

</dd> <dt>

<span id="lpszNewFilename"></span><span id="lpsznewfilename"></span><span id="LPSZNEWFILENAME"></span>*lpszNewFilename*
</dt> <dd>

Pointer to a string containing the new filename.

</dd> </dl>

## Return Value

If the file is renamed successfully, the return value is zero. If the specified file was not found, the return value is MMIOERR\_FILENOTFOUND.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Mmsystem.h (include Windows.h)</dt> </dl> |



 

