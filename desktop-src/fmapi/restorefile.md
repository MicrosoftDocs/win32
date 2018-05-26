---
title: RestoreFile function
description: Copies a deleted or regular file from a volume that is defined in the file restore context to a new file on an available logical drive. The volume path is set in the Volume parameter of the CreateFileRestoreContext function.
ms.assetid: cd13f321-2ebd-421b-9a5f-b4bcac9a60ea
keywords:
- RestoreFile function Files
topic_type:
- apiref
api_name:
- RestoreFile
api_location:
- Fmapi.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RestoreFile function

Copies a deleted or regular file from a volume that is defined in the file restore context to a new file on an available logical drive. The volume path is set in the *Volume* parameter of the [**CreateFileRestoreContext**](createfilerestorecontext.md) function.

> [!Note]  
> FMAPI can only be used in the Windows Preinstallation Environment (WinPE) for Windows Vista, Windows Server 2008, and later. Applications that use FMAPI must license WinPE.

 

## Syntax


```C++
BOOL WINAPI RestoreFile(
  _In_     PFILE_RESTORE_CONTEXT Context,
  _In_     PRESTORABLE_FILE_INFO RestorableFile,
  _In_     PCWSTR                DstFile,
  _In_opt_ FILE_RESTORE_CALLBACK Callback,
  _In_opt_ PVOID                 ClbkArg
);
```



## Parameters

<dl> <dt>

*Context* \[in\]
</dt> <dd>

A pointer to the file restore context that was created by calling the [**CreateFileRestoreContext**](createfilerestorecontext.md) function.

</dd> <dt>

*RestorableFile* \[in\]
</dt> <dd>

A pointer to a [**RESTORABLE\_FILE\_INFO**](restorable-file-info.md) structure that specifies the file to restore that was discovered by the [**ScanRestorableFiles**](scanrestorablefiles.md) function.

</dd> <dt>

*DstFile* \[in\]
</dt> <dd>

The path of the destination file where the restored data will be saved.

</dd> <dt>

*Callback* \[in, optional\]
</dt> <dd>

The [**FILE\_RESTORE\_CALLBACK**](file-restore-callback.md) callback function to use for reporting the progress of the copying process.

</dd> <dt>

*ClbkArg* \[in, optional\]
</dt> <dd>

The argument to be returned with the callback function.

</dd> </dl>

## Return value

If the function succeeds, the return value is nonzero.

If the function fails, the return value is zero. To get extended error information, call [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360).

## Remarks

This function has no associated header file or import library. You must use the [**LoadLibrary**](https://msdn.microsoft.com/library/windows/desktop/ms684175) and [**GetProcAddress**](https://msdn.microsoft.com/library/windows/desktop/ms683212) functions to dynamically link to fmapi.dll.

For removed files, the **RestoreFile** function tries to restore the file. It is possible that some of the file data might not be restored. Only data streams of the restorable file are copied, all other file information is not restored. The **RestoreFile** function can only be used to restore files; directories cannot be restored.

The **RestoreFile** function can call a callback function to report the progress of the copy process and the final status of the operation. For more information about the parameters that are used by the **RestoreFile** function to send information to a callback function, see the [**FILE\_RESTORE\_PACKET\_TYPE**](file-restore-packet-type.md) enumeration.

The restore process can be canceled by returning **FALSE** in the callback function.

In general, FMAPI cannot guarantee the success of the restore. It uses a best-effort approach. Files that have been overwritten may not be restorable, or may be only partially restorable. In addition, limitations of the FAT file system make FMAPI inefficient in restoring fragmented files in their entirety. FMAPI will attempt to restore as much of the file as possible. In some cases, FMAPI's restored version of a file may be fully or partially corrupted (compared to the original), if the file contents and meta data were overwritten by some other file. FMAPI may not be successful in restoring very large files, due to file system restrictions.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                 |
| DLL<br/>                      | <dl> <dt>Fmapi.dll</dt> </dl> |



## See also

<dl> <dt>

[**CreateFileRestoreContext**](createfilerestorecontext.md)
</dt> <dt>

[**ScanRestorableFiles**](scanrestorablefiles.md)
</dt> </dl>

 

 





