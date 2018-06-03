---
title: FILE\_RESTORE\_FINISHED\_INFORMATION structure
description: Provides information about the final status of the restored file. This structure is used in RestoreFile and defines the format of the callback buffer for the FileRestoreFinished message type.
ms.assetid: 7ce27ed1-b856-452c-aebc-676ee7cf9c32
keywords:
- FILE_RESTORE_FINISHED_INFORMATION structure Files
- PFILE_RESTORE_FINISHED_INFORMATION structure pointer Files
topic_type:
- apiref
api_name:
- FILE_RESTORE_FINISHED_INFORMATION
api_type:
- NA
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# FILE\_RESTORE\_FINISHED\_INFORMATION structure

Provides information about the final status of the restored file. This structure is used in [**RestoreFile**](restorefile.md) and defines the format of the callback buffer for the **FileRestoreFinished** message type.

> [!Note]  
> FMAPI can only be used in the Windows Preinstallation Environment (WinPE) for Windows Vista, Windows Server 2008, and later. Applications that use FMAPI must license WinPE.

 

## Syntax


```C++
typedef struct _FILE_RESTORE_FINISHED_INFORMATION {
  BOOL  Success;
  ULONG FinalResult;
  PVOID ClbkArg;
} FILE_RESTORE_FINISHED_INFORMATION, *PFILE_RESTORE_FINISHED_INFORMATION;
```



## Members

<dl> <dt>

**Success**
</dt> <dd>

**TRUE** if the file was successfully restored; otherwise, **FALSE**.

</dd> <dt>

**FinalResult**
</dt> <dd>

The final error code that was returned by [**RestoreFile**](restorefile.md).

</dd> <dt>

**ClbkArg**
</dt> <dd>

The callback arguments that are passed with [**RestoreFile**](restorefile.md).

</dd> </dl>

## Remarks

Note that there is no associated header file for this structure.

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**RestoreFile**](restorefile.md)
</dt> </dl>

 

 





