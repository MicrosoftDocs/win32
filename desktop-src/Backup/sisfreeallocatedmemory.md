---
title: SisFreeAllocatedMemory function (Sisbkup.h)
description: Frees memory allocated by SIS API functions.
ms.assetid: 8fab79c8-593c-46df-a885-09a59620a977
keywords:
- SisFreeAllocatedMemory function Backup
topic_type:
- apiref
api_name:
- SisFreeAllocatedMemory
api_location:
- Sisbkup.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# SisFreeAllocatedMemory function

The **SisFreeAllocatedMemory** function frees memory allocated by SIS API functions.

## Syntax


```C++
void SisFreeAllocatedMemory(
  _In_ PVOID allocatedSpace
);
```



## Parameters

<dl> <dt>

*allocatedSpace* \[in\]
</dt> <dd>

Pointer to the memory allocated by the SIS API.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

After the call to this function completes, the caller may no longer access the freed memory.

This call should be used to deallocate the memory allocated for the *commonStoreRootPathname* parameter strings returned from [**SisCreateBackupStructure**](siscreatebackupstructure.md) and [**SisCreateRestoreStructure**](siscreaterestorestructure.md), and the array of strings containing common-store file names returned from **SisCreateBackupStructure**, [**SisCSFilesToBackupForLink**](siscsfilestobackupforlink.md), **SisCreateRestoreStructure**, and [**SisRestoredLink**](sisrestoredlink.md). In the latter case, the array itself also must be freed by calling **SisFreeAllocatedMemory**.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Sisbkup.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Sisbkup.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Sisbkup.dll</dt> </dl> |



## See also

<dl> <dt>

[**SisCreateBackupStructure**](siscreatebackupstructure.md)
</dt> <dt>

[**SisCreateRestoreStructure**](siscreaterestorestructure.md)
</dt> <dt>

[**SisCSFilesToBackupForLink**](siscsfilestobackupforlink.md)
</dt> <dt>

[**SisRestoredLink**](sisrestoredlink.md)
</dt> </dl>

 

 





