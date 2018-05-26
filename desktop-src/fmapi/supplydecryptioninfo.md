---
title: SupplyDecryptionInfo function
description: This function is obsolete in Windows 8, Windows Server 2012, and later. Provides the full path for a file that contains a decryption key and provides a BitLocker information block that is stored in Active Directory.
ms.assetid: e8eaf83a-4fbe-4a5e-90a6-701069fb1ff5
keywords:
- SupplyDecryptionInfo function Files
topic_type:
- apiref
api_name:
- SupplyDecryptionInfo
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

# SupplyDecryptionInfo function

This function is obsolete in Windows 8, Windows Server 2012, and later. Provides the full path for a file that contains a decryption key and provides a BitLocker information block that is stored in Active Directory. The data provided with this function is required when using the [**ScanRestorableFiles**](scanrestorablefiles.md) function and the [**RestoreFile**](restorefile.md) function to access data that is encrypted on a disk.

> [!Note]  
> FMAPI can only be used in the Windows Preinstallation Environment (WinPE) for Windows Vista, Windows Server 2008, and later. Applications that use FMAPI must license WinPE.

 

## Syntax


```C++
BOOL WINAPI SupplyDecryptionInfo(
  _In_     PFILE_RESTORE_CONTEXT Context,
  _In_opt_ PCWSTR                RecoveryKeyFilePath,
  _In_opt_ PVOID                 RecoveryPassword,
  _In_opt_ PVOID                 KeyPackage,
  _In_opt_ ULONG                 KeyPackageSize
);
```



## Parameters

<dl> <dt>

*Context* \[in\]
</dt> <dd>

A pointer to the file restore context that was created by calling the [**CreateFileRestoreContext**](createfilerestorecontext.md) function.

</dd> <dt>

*RecoveryKeyFilePath* \[in, optional\]
</dt> <dd>

The full path to the .bek file that contains the recovery key. Only one of *RecoveryKeyFilePath* or *RecoveryPassword* is required.

</dd> <dt>

*RecoveryPassword* \[in, optional\]
</dt> <dd>

The recovery password string.

</dd> <dt>

*KeyPackage* \[in, optional\]
</dt> <dd>

The Binary Large Object (BLOB) that contains the BitLocker key package (metadata). The key package is usually backed up to the Active Directory during the BitLocker setup. If the metadata is not readable on the disk, this parameter is required.

</dd> <dt>

*KeyPackageSize* \[in, optional\]
</dt> <dd>

The size of the BitLocker key package, in bytes.

</dd> </dl>

## Return value

If the function succeeds, the return value is TRUE.

If the function fails, the return value is FALSE. To get extended error information, call [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360).

In Windows 8, Windows Server 2012, and later, this function always returns FALSE, and [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360) returns ERROR\_NOT\_SUPPORTED.

## Remarks

This function is obsolete in Windows 8, Windows Server 2012, and later.

This function has no associated header file or import library. You must use the [**LoadLibrary**](https://msdn.microsoft.com/library/windows/desktop/ms684175) and [**GetProcAddress**](https://msdn.microsoft.com/library/windows/desktop/ms683212) functions to dynamically link to fmapi.dll.

You must use the **SupplyDecryptionInfo** function for the following scenarios:

-   The volume was encrypted with the BitLocker technology.
-   BitLocker indicates that the metadata on the disk is corrupted. The metadata must be retrieved from Active Directory and provided using the *KeyPackage* parameter.

If required, the **SupplyDecryptionInfo** function must be called before any call to the [**ScanRestorableFiles**](scanrestorablefiles.md) function or the [**RestoreFile**](restorefile.md) function.

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
</dt> <dt>

[**RestoreFile**](restorefile.md)
</dt> </dl>

 

 





