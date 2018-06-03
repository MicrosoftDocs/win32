---
Description: Renames an item in the cache.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 10370f22-a326-416e-b32d-ea06f661f696
ms.prod: windows-server-dev
ms.technology: offline-files
ms.tgt_platform: multiple
title: RenameItem method of the Win32\_OfflineFilesCache class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RenameItem method of the Win32\_OfflineFilesCache class

Renames an item in the cache. This method logs a request with Offline Files for a path to be renamed on the next system restart.

## Syntax


```mof
uint32 RenameItem(
  [in] string  OriginalPath,
  [in] string  NewPath,
  [in] boolean ReplaceIfExists
);
```



## Parameters

<dl> <dt>

*OriginalPath* \[in\]
</dt> <dd>

Fully qualified UNC path of the item (server, share, file or directory) to be renamed.

</dd> <dt>

*NewPath* \[in\]
</dt> <dd>

The new path to replace *OriginalPath* if the item that *OriginalPath* points to exists in the cache.

</dd> <dt>

*ReplaceIfExists* \[in\]
</dt> <dd>

This parameter is reserved for future use.

</dd> </dl>

## Return value

This method returns either a [WMI return code](https://msdn.microsoft.com/library/aa394574) or a [system error code](https://msdn.microsoft.com/library/windows/desktop/ms681381).

## Remarks

This method is most often used after a directory tree has been renamed or moved on a remote server.

This method requires system administrator privilege.

> [!Note]  
> A restart of the system is necessary for the rename operation to be applied to the Offline Files cache.

 

This method fails if the path referenced by the *NewPath* parameter already exists in the Offline Files cache.

Beginning with Windows 7 with Service Pack 1 (SP1) and Windows Server 2008 R2 with Service Pack 1 (SP1) you can also use the [**RenameItemEx**](win32-offlinefilescache-renameitemex.md) method to rename an item. It does not require system administrator privilege or a system restart. However, it will fail if the item is currently in use.

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
</dt> <dt>

[**RenameItemEx**](win32-offlinefilescache-renameitemex.md)
</dt> </dl>

 

 




