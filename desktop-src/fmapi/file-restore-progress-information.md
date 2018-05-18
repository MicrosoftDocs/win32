---
title: FILE\_RESTORE\_PROGRESS\_INFORMATION structure
description: Provides information about the progress of the restoration of a file.
ms.assetid: 'f33fc463-acc7-4b46-b379-fa4edd46152d'
keywords: ["FILE_RESTORE_PROGRESS_INFORMATION structure Files", "PFILE_RESTORE_PROGRESS_INFORMATION structure pointer Files"]
topic_type:
- apiref
api_name:
- FILE_RESTORE_PROGRESS_INFORMATION
api_type:
- NA
---

# FILE\_RESTORE\_PROGRESS\_INFORMATION structure

Provides information about the progress of the restoration of a file. This structure is used in the [**RestoreFile**](restorefile.md) function and defines the format of the callback buffer for the **FileRestoreProgressInfo** message type.

> [!Note]  
> FMAPI can only be used in the Windows Preinstallation Environment (WinPE) for Windows Vista, Windows Server 2008, and later. Applications that use FMAPI must license WinPE.

 

## Syntax


```C++
typedef struct _FILE_RESTORE_PROGRESS_INFORMATION {
  LONGLONG TotalFileSize;
  LONGLONG TotalBytesCompleted;
  LONGLONG StreamSize;
  LONGLONG StreamBytesCompleted;
  PVOID    ClbkArg;
} FILE_RESTORE_PROGRESS_INFORMATION, *PFILE_RESTORE_PROGRESS_INFORMATION;
```



## Members

<dl> <dt>

**TotalFileSize**
</dt> <dd>

The total size of the restorable file, in bytes.

</dd> <dt>

**TotalBytesCompleted**
</dt> <dd>

The total number of bytes that have been restored.

</dd> <dt>

**StreamSize**
</dt> <dd>

The size of the current stream, in bytes.

</dd> <dt>

**StreamBytesCompleted**
</dt> <dd>

The number of bytes in the stream that have been restored.

</dd> <dt>

**ClbkArg**
</dt> <dd>

The callback arguments that are passed to **RestoreFile**.

</dd> </dl>

## Remarks

Note that there is no associated header file for this structure.

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**RestoreFile**](restorefile.md)
</dt> </dl>

 

 





