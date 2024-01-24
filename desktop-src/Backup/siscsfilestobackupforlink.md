---
title: SisCSFilesToBackupForLink function (Sisbkup.h)
description: Returns information describing the common-store files the specified SIS link points to.
ms.assetid: 0580c34e-195a-4a2c-893f-bc339dcc88d7
keywords:
- SisCSFilesToBackupForLink function Backup
topic_type:
- apiref
api_name:
- SisCSFilesToBackupForLink
api_location:
- Sisbkup.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# SisCSFilesToBackupForLink function

The **SisCSFilesToBackupForLink** function returns information describing the common-store files the specified SIS link points to.

## Syntax


```C++
BOOL SisCSFilesToBackupForLink(
  _In_  PVOID  sisBackupStructure,
  _In_  PVOID  reparseData,
  _In_  ULONG  reparseDataSize,
  _Out_ PVOID  thisFileContext,
  _Out_ PVOID  *matchingFileContext,
  _Out_ PULONG countOfCommonStoreFilesToBackUp,
  _Out_ PWCHAR **commonStoreFilesToBackUp
);
```



## Parameters

<dl> <dt>

*sisBackupStructure* \[in\]
</dt> <dd>

Pointer to the SIS backup structure returned from [**SisCreateBackupStructure**](siscreatebackupstructure.md).

</dd> <dt>

*reparseData* \[in\]
</dt> <dd>

Pointer to the contents of the SIS reparse point. This reparse point contains data describing a SIS link. To retrieve the reparse point data for a file, use the [**FSCTL\_GET\_REPARSE\_POINT**](/windows/desktop/api/winioctl/ni-winioctl-fsctl_get_reparse_point) control code.

</dd> <dt>

*reparseDataSize* \[in\]
</dt> <dd>

Size of the contents of the SIS reparse point pointed to by *reparseData*, in bytes.

</dd> <dt>

*thisFileContext* \[out\]
</dt> <dd>

Pointer to a context string supplied by the backup application calling this function. The contents of this content string are entirely determined by this backup application and is not interpreted by the SIS Backup API. This parameter is optional; if not used, set the value of this parameter to **NULL**. The value of this parameter will not be processed in this case.

</dd> <dt>

*matchingFileContext* \[out\]
</dt> <dd>

Doubly-indirect pointer to the context string of the SIS link identified by the information passed in the first four parameters of this function. This parameter is optional; if a context string is not provided as the value of the *thisFileContext* parameter, set the value of this parameter to **NULL**. The value of this parameter will not be processed in this case.

</dd> <dt>

*countOfCommonStoreFilesToBackUp* \[out\]
</dt> <dd>

Number of files listed in the *commonStoreFilesToBackUp* parameter.

</dd> <dt>

*commonStoreFilesToBackUp* \[out\]
</dt> <dd>

Pointer to an array of file names. These files should be backed up at the same time and in the same manner as the common-store files requested by [**SisCreateBackupStructure**](siscreatebackupstructure.md).

</dd> </dl>

## Return value

This function returns **TRUE** if it completes successfully and **FALSE** otherwise. Call [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) to get more information about the reason the call failed.

## Remarks

The backup application should call this function only once for each SIS link file being backed up.

The backup application can identify a SIS reparse point by its tag, IO\_REPARSE\_TAG\_SIS. This tag is defined in Winnt.h.

If this reparse point identified by the value of the *reparseData* parameter describes the first instance of a file to be backed up, this function will return **NULL** as the value of the *matchingFileContext* parameter, and initialize the value of the *commonStoreFilesToBackUp* array of strings with the names of the common-store file or files to be backed up. Otherwise, this function will set the value of the *matchingFileContext* parameter to the context string corresponding to the first instance of the specified file and set the value of the *countOfCommonStoreFilesToBackUp* parameter to 0. If there are multiple common-store files corresponding to the specified link, the value of the *thisFileContext* parameter will be the context string corresponding to the first common-store file returned in the array that is, commonStoreFilesToBackUp\[0\].

The current version of this function will return at most one common-store file, but it is possible that in future versions a single link may be backed by several common-store files for example, one for each stream in the file so your backup application should support multiple files in each call to this function. In any case, each common-store file will be returned at most once for each backup pass.

Your backup application should back up or restore the common-store file or files identified by the file name or file names returned in the *commonStoreFilesToBackUp* parameter. Regardless of whether there is a corresponding common-store file, your backup application should back up the SIS link file as it exists on the disk for example, as a reparse point and a sparse file, and most likely with no ranges filled in. Your backup application may back up or restore the common-store file or files immediately, postpone backing them up, or mix them together as necessary.

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

[**SisFreeAllocatedMemory**](sisfreeallocatedmemory.md)
</dt> <dt>

[**SisCreateBackupStructure**](siscreatebackupstructure.md)
</dt> </dl>

 

