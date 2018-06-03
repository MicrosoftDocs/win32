---
Description: Renames an item in the cache. This method is identical to the RenameItem method, except that it will attempt to do the rename operation right away.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3D25C334-132A-46F4-B281-4B6EE27552CB
ms.prod: windows-server-dev
ms.technology: offline-files
ms.tgt_platform: multiple
title: RenameItemEx method of the Win32\_OfflineFilesCache class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RenameItemEx method of the Win32\_OfflineFilesCache class

Renames an item in the cache. This method is identical to the [**RenameItem**](win32-offlinefilescache-renameitem.md) method, except that it will attempt to do the rename operation right away.

## Syntax


```mof
uint32 RenameItemEx(
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

This method does not require system administrator privilege.

If the item to be renamed is a file or directory, it must obey the file system semantics for the rename operation. If the file or a child file (for a directory) is already open, the rename will fail. Also, this method attempts to perform the rename as long as the user has access to the item that is being renamed.

If you need to minimize the chance that the item is in use, call the [**RenameItem**](win32-offlinefilescache-renameitem.md) method instead.

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 with SP1<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2008 R2 with SP1<br/>                                                             |
| Namespace<br/>                | Root\\CIMv2<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Cscobj.h</dt> </dl>                    |
| MOF<br/>                      | <dl> <dt>OfflineFilesWmiProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CscObj.dll</dt> </dl>                  |



## See also

<dl> <dt>

[**Win32\_OfflineFilesCache**](win32-offlinefilescache.md)
</dt> </dl>

 

 




