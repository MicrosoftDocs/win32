---
title: CreateFileRestoreContext function
description: Initializes the context that is used to restore files. The context can be created for an existing recognized volume or for a lost (unrecognized) volume.
ms.assetid: 0875bc51-a0d8-4490-a594-ceb6ea50c46d
keywords:
- CreateFileRestoreContext function Files
topic_type:
- apiref
api_name:
- CreateFileRestoreContext
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

# CreateFileRestoreContext function

Initializes the context that is used to restore files. The context can be created for an existing recognized volume or for a lost (unrecognized) volume.

> [!Note]  
> FMAPI can only be used in the Windows Preinstallation Environment (WinPE) for Windows Vista, Windows Server 2008, and later. Applications that use FMAPI must license WinPE.

 

## Syntax


```C++
BOOL WINAPI CreateFileRestoreContext(
  _In_     PCWSTR                Volume,
  _In_     RESTORE_CONTEXT_FLAGS Flags,
  _In_opt_ LONGLONG              StartSector,
  _In_     LONGLONG              BootSector,
  _In_     DWORD                 Version,
  _Out_    PFILE_RESTORE_CONTEXT Context
);
```



## Parameters

<dl> <dt>

*Volume* \[in\]
</dt> <dd>

The path of the volume or physical drive to be used.

To specify a physical drive, use the following syntax: "\\\\.\\PhysicalDrive*N*", where *N* is a valid drive number, for example, "\\\\.\\PhysicalDrive0".

To specify a mounted volume, use the following syntax: "\\\\.\\*N*:", where *N* is a valid drive letter, for example, "\\\\.\\C:".

If *Flags* is set to **ContextFlagVolume**, this parameter identifies a volume. If *Flags* is set to **ContextFlagDisk**, this parameter identifies a physical drive.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

The type of context that is created. The value of this parameter can be a combination of constants from the [**RESTORE\_CONTEXT\_FLAGS**](restore-context-flags.md) enumeration.

</dd> <dt>

*StartSector* \[in, optional\]
</dt> <dd>

If *Flags* contains **ContextFlagDisk**, this parameter specifies the first sector offset of the lost volume. If *Flags* does not contain **ContextFlagDisk**, this parameter is ignored.

</dd> <dt>

*BootSector* \[in\]
</dt> <dd>

If *Flags* contains **ContextFlagDisk**, this parameter specifies the boot sector offset of the lost volume. The value of this parameter can be the same as the value of *StartSector* or it can be the last volume sector.

</dd> <dt>

*Version* \[in\]
</dt> <dd>

The major and minor version number. This parameter must match the version of FMAPI that is being used, according to the following table.



| Value                                                                                                                                                                                      | Meaning                                                                              |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| <span id="FILE_RESTORE_VERSION_1"></span><span id="file_restore_version_1"></span><dl> <dt>**FILE\_RESTORE\_VERSION\_1**</dt> </dl> | Windows 7, Windows Server 2008 R2, Windows Server 2008, and Windows Vista<br/> |
| <span id="FILE_RESTORE_VERSION_2"></span><span id="file_restore_version_2"></span><dl> <dt>**FILE\_RESTORE\_VERSION\_2**</dt> </dl> | Windows 8 and Windows Server 2012<br/>                                         |



 

</dd> <dt>

*Context* \[out\]
</dt> <dd>

A [**PFILE\_RESTORE\_CONTEXT**](file-management-data-types.md) pointer to save the file restore context.

</dd> </dl>

## Return value

If the function succeeds, the return value is TRUE.

If the function fails, the return value is FALSE. To get extended error information, call [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360).

If the *Version* parameter does not match the version of FMAPI that is being used, this function returns FALSE, and [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360) returns **ERROR\_INVALID\_PARAMETER**.

## Remarks

This function has no associated header file or import library. You must use the [**LoadLibrary**](https://msdn.microsoft.com/library/windows/desktop/ms684175) and [**GetProcAddress**](https://msdn.microsoft.com/library/windows/desktop/ms683212) functions to dynamically link to fmapi.dll.

If *Flags* contains ContextFlagVolume, the **CreateFileRestoreContext** function uses the [**FSCTL\_LOCK\_VOLUME**](https://msdn.microsoft.com/library/windows/desktop/aa364575) control code to lock the volume.

If the files to be restored are encrypted with BitLocker, the **CreateFileRestoreContext** function does one of the following:

-   On Windows 8 and Windows Server 2012 (FMAPI version 2),
-   On Windows 7, Windows Server 2008 R2, and Windows Server 2008, if *Flags* contains **ContextFlagDisk**, the **CreateFileRestoreContext** function tries to retrieve all of the required BitLocker key information from the disk and the Trusted Platform Module (TPM). If the necessary information for BitLocker decryption is not available, the file restore context is created with minimal validation. In such cases, you must call the [**SupplyDecryptionInfo**](supplydecryptioninfo.md) function to provide the restore context with the keys that are needed to perform data decryption. Supplying this information is required only if BitLocker setup was completed with an external startup-key file on a USB drive without using a TPM. The call to the **SupplyDecryptionInfo** function must be completed before any call to [**ScanRestorableFiles**](scanrestorablefiles.md) or [**RestoreFile**](restorefile.md).
-   On Windows Vista, if *Flags* contains **ContextFlagVolume**, the function succeeds only if the volume is unlocked by BitLocker. If the volume is not unlocked, the function returns an error.

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

[**RestoreFile**](restorefile.md)
</dt> <dt>

[**ScanRestorableFiles**](scanrestorablefiles.md)
</dt> <dt>

[**SupplyDecryptionInfo**](supplydecryptioninfo.md)
</dt> </dl>

 

 





