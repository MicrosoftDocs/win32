---
title: SisCreateRestoreStructure function (Sisbkup.h)
description: Creates a SIS restore structure based on the supplied information.
ms.assetid: acdd4258-813d-42af-a2e1-e59a1426f86c
keywords:
- SisCreateRestoreStructure function Backup
topic_type:
- apiref
api_name:
- SisCreateRestoreStructure
api_location:
- Sisbkup.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# SisCreateRestoreStructure function

The **SisCreateRestoreStructure** function creates a SIS restore structure based on the supplied information.

## Syntax


```C++
BOOL SisCreateRestoreStructure(
  _In_  PWCHAR volumeRoot,
  _Out_ PVOID  *sisRestoreStructure,
  _Out_ PWCHAR *commonStoreRootPathname,
  _Out_ PULONG countOfCommonStoreFilesToRestore,
  _Out_ PWCHAR **commonStoreFilesToRestore
);
```



## Parameters

<dl> <dt>

*volumeRoot* \[in\]
</dt> <dd>

File name of the volume root, without the trailing backslash, of the volume to be backed up. For example, specify "C:" and not "C:\\". The volume cannot be the system or boot volume.

</dd> <dt>

*sisRestoreStructure* \[out\]
</dt> <dd>

Returned SIS restore structure. This structure should be treated as opaque by the caller.

</dd> <dt>

*commonStoreRootPathname* \[out\]
</dt> <dd>

Fully qualified path name of the specified volume's common store. For example, "c:\\SIS Common Store".

</dd> <dt>

*countOfCommonStoreFilesToRestore* \[out\]
</dt> <dd>

Number of files listed in the *commonStoreFilesToRestore* parameter.

</dd> <dt>

*commonStoreFilesToRestore* \[out\]
</dt> <dd>

Pointer to an array of file names that specifies the list of internal files used by SIS to manage the specified volume. These files should be restored at the same time and in the same manner as the common-store files requested by [**SisCSFilesToBackupForLink**](siscsfilestobackupforlink.md).

</dd> </dl>

## Return value

This function returns **TRUE** if it completes successfully and **FALSE** otherwise. Call [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) to get more information about the reason the call failed.

## Remarks

This function establishes the restore environment on the specified volume in the way that [**SisCreateBackupStructure**](siscreatebackupstructure.md) establishes the backup environment on the specified volume.

Note that this function will not necessarily identify the common-store file or files corresponding to a set of SIS links on the backup media if those common store file or files still exist on disk. The contents of a common-store file's data stream never change once it is created, so if the file already exists on the disk there is no need to restore it.

Common-store file names are globally unique to ensure the integrity of the restore operation even if it does not occur on the same SIS-enabled volume that the backup operation has accessed.

After the restore operation is complete, deallocate the memory used by the *commonStoreFilesToRestore* array of strings by calling [**SisFreeAllocatedMemory**](sisfreeallocatedmemory.md).

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

[**SisCSFilesToBackupForLink**](siscsfilestobackupforlink.md)
</dt> <dt>

[**SisFreeAllocatedMemory**](sisfreeallocatedmemory.md)
</dt> <dt>

[**SisFreeBackupStructure**](sisfreebackupstructure.md)
</dt> </dl>

 

