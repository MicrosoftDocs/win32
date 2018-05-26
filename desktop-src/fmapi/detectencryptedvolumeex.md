---
title: DetectEncryptedVolumeEx function
description: This function is obsolete in Windows 8, Windows Server 2012, and later. Determines whether the volume is encrypted with BitLocker technology. If the volume is encrypted, the function determines whether it is unlocked.
ms.assetid: F95E0FB0-5301-4B05-B874-44254D6582C0
keywords:
- DetectEncryptedVolumeEx function
topic_type:
- apiref
api_name:
- DetectEncryptedVolumeEx
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

# DetectEncryptedVolumeEx function

This function is obsolete in Windows 8, Windows Server 2012, and later. Determines whether the volume is encrypted with BitLocker technology. If the volume is encrypted, the function determines whether it is unlocked. This function is identical to the [**DetectEncryptedVolume**](detectencryptedvolume.md) function, except that it has an additional *VolumeSize* parameter.

> [!Note]  
> FMAPI can only be used in the Windows Preinstallation Environment (WinPE) for Windows Vista, Windows Server 2008, and later. Applications that use FMAPI must license WinPE.

 

## Syntax


```C++
BOOL WINAPI DetectEncryptedVolumeEx(
  _In_  PFILE_RESTORE_CONTEXT Context,
  _Out_ PDWORD                VolumeEncryptionInfo,
  _Out_ PULONGLONG            VolumeSize
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

</dd> <dt>

*VolumeSize* \[out\]
</dt> <dd>

Receives the size, in bytes, of the volume. For partially encrypted volumes, *VolumeSize* is zero on return.

**Windows Server 2008 and Windows Vista:  ***VolumeSize* is not zero on return for partially encrypted volumes.

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
| DLL<br/>                      | <dl> <dt>Fmapi.dll</dt> </dl> |



## See also

<dl> <dt>

[**CreateFileRestoreContext**](createfilerestorecontext.md)
</dt> <dt>

[**DetectEncryptedVolume**](detectencryptedvolume.md)
</dt> </dl>

 

 





