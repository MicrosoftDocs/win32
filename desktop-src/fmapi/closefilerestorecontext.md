---
title: CloseFileRestoreContext function
description: Closes the context that is used to restore files. If the file system volume is exclusively locked, this function removes the lock.
ms.assetid: 'c98b72a1-d097-4993-8ee0-7b6c6dc7904e'
keywords: ["CloseFileRestoreContext function Files"]
topic_type:
- apiref
api_name:
- CloseFileRestoreContext
api_location:
- Fmapi.dll
api_type:
- DllExport
---

# CloseFileRestoreContext function

Closes the context that is used to restore files. If the file system volume is exclusively locked, this function removes the lock.

> [!Note]  
> FMAPI can only be used in the Windows Preinstallation Environment (WinPE) for Windows Vista, Windows Server 2008, and later. Applications that use FMAPI must license WinPE.

 

## Syntax


```C++
BOOL WINAPI CloseFileRestoreContext(
  _In_ PFILE_RESTORE_CONTEXT Context
);
```



## Parameters

<dl> <dt>

*Context* \[in\]
</dt> <dd>

A pointer to the file restore context created by the [**CreateFileRestoreContext**](createfilerestorecontext.md) function.

</dd> </dl>

## Return value

If the function succeeds, the return value is nonzero.

If the function fails, the return value is zero. To get extended error information, call [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360).

## Remarks

This function has no associated header file or import library. You must use the [**LoadLibrary**](https://msdn.microsoft.com/library/windows/desktop/ms684175) and [**GetProcAddress**](https://msdn.microsoft.com/library/windows/desktop/ms683212) functions to dynamically link to fmapi.dll.

This function cancels an ongoing restoration process that was initiated with the [**RestoreFile**](restorefile.md) function.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                 |
| DLL<br/>                      | <dl> <dt>Fmapi.dll</dt> </dl> |



## See also

<dl> <dt>

[**RestoreFile**](restorefile.md)
</dt> </dl>

 

 





