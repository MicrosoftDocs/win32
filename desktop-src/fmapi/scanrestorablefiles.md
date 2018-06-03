---
title: ScanRestorableFiles function
description: Searches for files that are available to be restored.
ms.assetid: 35dac36f-ea54-4392-994b-9d386ad9ee5a
keywords:
- ScanRestorableFiles function Files
topic_type:
- apiref
api_name:
- ScanRestorableFiles
api_location:
- Fmapi.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ScanRestorableFiles function

Searches for files that are available to be restored. The behavior of this function depends on the *Flags* parameter of the [**CreateFileRestoreContext**](createfilerestorecontext.md) function.

> [!Note]  
> FMAPI can only be used in the Windows Preinstallation Environment (WinPE) for Windows Vista, Windows Server 2008, and later. Applications that use FMAPI must license WinPE.

 

## Syntax


```C++
BOOL WINAPI ScanRestorableFiles(
  _In_  PFILE_RESTORE_CONTEXT Context,
  _In_  PCWSTR                Path,
  _In_  ULONG                 FileInfoSize,
  _Out_ PRESTORABLE_FILE_INFO FileInfo,
  _Out_ PULONG                FileInfoUsed
);
```



## Parameters

<dl> <dt>

*Context* \[in\]
</dt> <dd>

A pointer to the file restore context created using the [**CreateFileRestoreContext**](createfilerestorecontext.md) function.

</dd> <dt>

*Path* \[in\]
</dt> <dd>

The initial path of where to begin the scan for files to restore.

</dd> <dt>

*FileInfoSize* \[in\]
</dt> <dd>

The size of the buffer that contains the [**RESTORABLE\_FILE\_INFO**](restorable-file-info.md) structure to which the *FileInfo* parameter points, in bytes.

</dd> <dt>

*FileInfo* \[out\]
</dt> <dd>

A pointer to a [**RESTORABLE\_FILE\_INFO**](restorable-file-info.md) structure that contains information about the file or directory to be restored.

</dd> <dt>

*FileInfoUsed* \[out\]
</dt> <dd>

A pointer to a variable that contains the length of the [**RESTORABLE\_FILE\_INFO**](restorable-file-info.md) structure or specifies the required space for the structure.

</dd> </dl>

## Return value

If the function succeeds, returns **TRUE**.

If the function fails, returns **FALSE**. To get extended error information, call the [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360) function.

If **TRUE** is returned, the [**RESTORABLE\_FILE\_INFO**](restorable-file-info.md) structure that is pointed to by the *FileInfo* parameter contains information about the file or directory to be restored.

If **FALSE** is returned and the value of *FileInfoSize* is less than the value that the *FileInfoUsed* parameter points to, the buffer is too small. [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360) returns **ERROR\_INSUFFICIENT\_BUFFER**.

When scanning is complete, **FALSE** is returned and [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360) returns **ERROR\_NO\_MORE\_FILES**.

## Remarks

This function has no associated header file or import library. You must use the [**LoadLibrary**](https://msdn.microsoft.com/library/windows/desktop/ms684175) and [**GetProcAddress**](https://msdn.microsoft.com/library/windows/desktop/ms683212) functions to dynamically link to fmapi.dll.

Typically, scanning is performed to discover files that have been removed. To discover files that have been removed, the *FlagScanRemovedFiles* flag must be set in the *Flags* parameter of the [**CreateFileRestoreContext**](createfilerestorecontext.md) function. If the *FlagScanIncludeRemovedDirectories* flag is also set, the scan includes both files and directories.

Sometimes it is necessary to restore regular files on lost volumes. To scan for regular files, the *FlagScanRegularFiles* flag must be set in the *Flags* parameter of the [**CreateFileRestoreContext**](createfilerestorecontext.md) function.

The **ScanRestorableFiles** function populates the [**RESTORABLE\_FILE\_INFO**](restorable-file-info.md) structure for one file or directory that is found on the volume. To restore multiple files or directories, the **ScanRestorableFiles** function must be called for each file or directory that you want to discover.

The [**RESTORABLE\_FILE\_INFO**](restorable-file-info.md) structure can be variable in size. To determine the size that is required for the structure, the **ScanRestorableFiles** function should be called the first time with the *FileInfoSize* parameter set to zero. The **ScanRestorableFiles** function returns the required size of the **RESTORABLE\_FILE\_INFO** structure in the *FileInfoUsed* parameter. If subsequent calls to the **ScanRestorableFiles** function return **FALSE**, the value in the *FileInfoUsed* parameter is greater than the value in the *FileInfoSize* parameter, and [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360) returns **ERROR\_INSUFFICIENT\_BUFFER**, this means that there is not enough space and the *FileInfo* buffer must be expanded. After the buffer has been expanded, the scan can be resumed with the same file restore context without the loss of data.

**ScanRestorableFiles**'s scanning process uses a find-first, find-next mechanism for finding files. The first time **ScanRestorableFiles** is called, the *Path* parameter is used to find the first restorable file. Each subsequent call to **ScanRestorableFiles** ignores the *Path* parameter and searches for the next file. The scan process cannot be restarted from the beginning with an existing file restore context. To restart the scan process, call the [**CloseFileRestoreContext**](closefilerestorecontext.md) function, and then create a new file restore context using the [**CreateFileRestoreContext**](createfilerestorecontext.md) function.

If a restorable file is found, each call to **ScanRestorableFiles** returns a [**RESTORABLE\_FILE\_INFO**](restorable-file-info.md) in the *FileInfo* parameter that references the restorable file or a partial path to the restorable file. Check the **IsRemoved** member of the **RESTORABLE\_FILE\_INFO** structure to determine whether the file returned is restorable.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                 |
| DLL<br/>                      | <dl> <dt>Fmapi.dll</dt> </dl> |



## See also

<dl> <dt>

[**CloseFileRestoreContext**](closefilerestorecontext.md)
</dt> <dt>

[**CreateFileRestoreContext**](createfilerestorecontext.md)
</dt> </dl>

 

 





