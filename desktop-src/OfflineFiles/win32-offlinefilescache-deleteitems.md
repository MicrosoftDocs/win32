---
Description: Deletes files and directories from the local cache.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ce729cda-b68d-4eb8-9782-8e2749d0e2fd
ms.prod: windows-server-dev
ms.technology: offline-files
ms.tgt_platform: multiple
title: DeleteItems method of the Win32\_OfflineFilesCache class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DeleteItems method of the Win32\_OfflineFilesCache class

Deletes files and directories from the local cache. Deleting a container item implies the deletion of all its contained items, recursively.

## Syntax


```mof
uint32 DeleteItems(
  [in] string Paths[],
  [in] uint32 Flags
);
```



## Parameters

<dl> <dt>

*Paths* \[in\]
</dt> <dd>

Array of strings, each of which contains the qualified UNC path of a file or directory to be deleted.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Flags controlling the behavior of the delete operation. This parameter can be one or more of the following values.

<dt>

<span id="OfflineFilesDeleteFlagNoAutoCached"></span><span id="offlinefilesdeleteflagnoautocached"></span><span id="OFFLINEFILESDELETEFLAGNOAUTOCACHED"></span>

<span id="OfflineFilesDeleteFlagNoAutoCached"></span><span id="offlinefilesdeleteflagnoautocached"></span><span id="OFFLINEFILESDELETEFLAGNOAUTOCACHED"></span>**OfflineFilesDeleteFlagNoAutoCached** (0x00000001)


</dt> <dd>

Do not delete automatically cached items. The default behavior is to delete automatically cached items.

</dd> <dt>

<span id="OfflineFilesDeleteFlagNoPinned"></span><span id="offlinefilesdeleteflagnopinned"></span><span id="OFFLINEFILESDELETEFLAGNOPINNED"></span>

<span id="OfflineFilesDeleteFlagNoPinned"></span><span id="offlinefilesdeleteflagnopinned"></span><span id="OFFLINEFILESDELETEFLAGNOPINNED"></span>**OfflineFilesDeleteFlagNoPinned** (0x00000002)


</dt> <dd>

Do not delete pinned items. The default behavior is to delete pinned items.

</dd> <dt>

<span id="OfflineFilesDeleteFlagDelModified"></span><span id="offlinefilesdeleteflagdelmodified"></span><span id="OFFLINEFILESDELETEFLAGDELMODIFIED"></span>

<span id="OfflineFilesDeleteFlagDelModified"></span><span id="offlinefilesdeleteflagdelmodified"></span><span id="OFFLINEFILESDELETEFLAGDELMODIFIED"></span>**OfflineFilesDeleteFlagDelModified** (0x00000004)


</dt> <dd>

Delete files even if files are locally modified in the cache. The default behavior is to not delete files with unsynchronized local changes.

</dd> <dt>

<span id="OfflineFilesDeleteFlagAdmin"></span><span id="offlinefilesdeleteflagadmin"></span><span id="OFFLINEFILESDELETEFLAGADMIN"></span>

<span id="OfflineFilesDeleteFlagAdmin"></span><span id="offlinefilesdeleteflagadmin"></span><span id="OFFLINEFILESDELETEFLAGADMIN"></span>**OfflineFilesDeleteFlagAdmin** (0x80000000)


</dt> <dd>

Allows administrators to enumerate and delete all files regardless of access rights. If this flag is set and the caller is not an administrator, the function fails.

</dd> </dl> </dd> </dl>

## Return value

This method returns either a [WMI return code](https://msdn.microsoft.com/library/aa394574) or a [system error code](https://msdn.microsoft.com/library/windows/desktop/ms681381).

## Remarks

The caller must have sufficient access to the files and directories to be deleted.

If a delete operation is canceled while the deletion operation is in progress, changes to files processed to that point are not rolled back.

If a delete operation on a directory cannot remove all of its contained files or directories (for example, if access is denied), the specified directory entry is not removed. Any files and directories deleted up to that point will remain deleted.

Files are deleted only from the local cache. Associated files on the network server are not affected.

Files that are deleted are not recoverable through the Recycle Bin. Files that are deleted must be re-cached to be available offline.

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Namespace<br/>                | Root\\CIMv2<br/>                                                                                 |
| MOF<br/>                      | <dl> <dt>OfflineFilesWmiProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CscObj.dll</dt> </dl>                  |



## See also

<dl> <dt>

[**Win32\_OfflineFilesCache**](win32-offlinefilescache.md)
</dt> </dl>

 

 




