---
title: DetectEncryptedVolume function
description: This function is obsolete in Windows 8, Windows Server 2012, and later. Determines whether the volume is encrypted with BitLocker technology. If the volume is encrypted, the function determines whether it is unlocked.
ms.assetid: f826f2b5-2296-434e-8843-5b9ae3ad4c65
keywords:
- DetectEncryptedVolume function Files
topic_type:
- apiref
api_name:
- DetectEncryptedVolume
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

# DetectEncryptedVolume function

This function is obsolete in Windows 8, Windows Server 2012, and later. Determines whether the volume is encrypted with BitLocker technology. If the volume is encrypted, the function determines whether it is unlocked.

> [!Note]  
> FMAPI can only be used in the Windows Preinstallation Environment (WinPE) for Windows Vista, Windows Server 2008, and later. Applications that use FMAPI must license WinPE.

 

## Syntax


```C++
BOOL WINAPI DetectEncryptedVolume(
  _In_  PFILE_RESTORE_CONTEXT Context,
  _Out_ PDWORD                VolumeEncryptionInfo
);
```



## Parameters

<dl> <dt>

*Context* \[in\]
</dt> <dd>

A [**PFILE\_RESTORE\_CONTEXT**](file-management-data-types.md) pointer to the file restore context that was created by calling the [**CreateFileRestoreContext**](createfilerestorecontext.md) function.

</dd> <dt>

*VolumeEncryptionInfo* \[out\]
</dt> <dd>

A bitmask of flags that indicate the status of the volume. This value can be any combination of **VOLUME\_INFO\_ENCRYPTED** and **VOLUME\_INFO\_LOCKED**. For more information about these values, see [File Management Constants](file-management-constants.md).

</dd> </dl>

## Return value

If the function succeeds, the return value is TRUE.

If the function fails, the return value is FALSE. To get extended error information, call [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360).

In Windows 8, Windows Server 2012, and later, this function always returns FALSE, and [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360) returns ERROR\_NOT\_SUPPORTED.

## Remarks

This function is obsolete in Windows 8, Windows Server 2012, and later.

This function has no associated header file or import library. You must use the [**LoadLibrary**](https://msdn.microsoft.com/library/windows/desktop/ms684175) and [**GetProcAddress**](https://msdn.microsoft.com/library/windows/desktop/ms683212) functions to dynamically link to fmapi.dll.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows 7<br/>                                                                 |
| End of server support<br/>    | Windows Server 2008 R2<br/>                                                    |
| DLL<br/>                      | <dl> <dt>Fmapi.dll</dt> </dl> |



## See also

<dl> <dt>

[**CreateFileRestoreContext**](createfilerestorecontext.md)
</dt> <dt>

[**DetectEncryptedVolumeEx**](detectencryptedvolumeex.md)
</dt> </dl>

 

 





