---
title: SisCreateBackupStructure function (Sisbkup.h)
description: Creates a SIS backup structure based on the supplied information.
ms.assetid: a8c48961-fa24-4eb6-92cd-1b9bc83cec41
keywords:
- SisCreateBackupStructure function Backup
topic_type:
- apiref
api_name:
- SisCreateBackupStructure
api_location:
- Sisbkup.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# SisCreateBackupStructure function

The **SisCreateBackupStructure** function creates a SIS backup structure based on the supplied information.

## Syntax


```C++
BOOL SisCreateBackupStructure(
  _In_  PWCHAR volumeRoot,
  _Out_ PVOID  *sisBackupStructure,
  _Out_ PWCHAR *commonStoreRootPathname,
  _Out_ PULONG countOfCommonStoreFilesToBackUp,
  _Out_ PWCHAR **commonStoreFilesToBackUp
);
```



## Parameters

<dl> <dt>

*volumeRoot* \[in\]
</dt> <dd>

File name of the volume root, without the trailing backslash, of the volume to be backed up. For example, specify "C:" and not "C:\\".

</dd> <dt>

*sisBackupStructure* \[out\]
</dt> <dd>

Returned SIS backup structure.

</dd> <dt>

*commonStoreRootPathname* \[out\]
</dt> <dd>

Fully qualified path name of the specified volume's common store. For example, "c:\\SIS Common Store".

</dd> <dt>

*countOfCommonStoreFilesToBackUp* \[out\]
</dt> <dd>

Number of files listed in the *commonStoreFilesToBackUp* parameter.

</dd> <dt>

*commonStoreFilesToBackUp* \[out\]
</dt> <dd>

Pointer to an array of file names that specifies a list of internal files used by SIS to manage the specified volume. These files should be backed up at the same time and in the same manner as the common-store files requested by [**SisCSFilesToBackupForLink**](siscsfilestobackupforlink.md)

</dd> </dl>

## Return value

This function returns **TRUE** if it completes successfully and **FALSE** otherwise. Call [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) to get more information about the reason the call failed.

## Remarks

This function creates a SIS backup structure, which is used by the SIS backup API to create and maintain a list of the file links on the volume and the original files the links point to. This function should be called only once for each SIS-enabled volume being backed up. All files within the specified volume should be treated as common-store files and backed up only if SIS indicates that they should.

The *countOfCommonStoreFilesToBackUp* and *commonStoreFilesToBackUp* parameters together return a list of files that must be backed up regardless of which links are backed up.

If *countOfCommonStoreFilesToBackUp* is 0, *commonStoreFilesToBackUp* may be a **NULL** pointer. The value of the *commonStoreFilesToBackUp* parameter should be ignored.

After the backup operation is complete, deallocate the memory used by the *commonStoreFilesToBackUp* array of strings by calling [**SisFreeAllocatedMemory**](sisfreeallocatedmemory.md).

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

[**SisCreateRestoreStructure**](siscreaterestorestructure.md)
</dt> <dt>

[**SisCSFilesToBackupForLink**](siscsfilestobackupforlink.md)
</dt> <dt>

[**SisFreeAllocatedMemory**](sisfreeallocatedmemory.md)
</dt> </dl>

 

