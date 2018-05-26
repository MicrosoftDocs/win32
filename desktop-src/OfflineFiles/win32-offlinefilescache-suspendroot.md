---
Description: Suspends or releases a share root or directory tree.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0439fcfd-3e05-427f-948b-c41a9ebc4f52
ms.prod: windows-server-dev
ms.technology: offline-files
ms.tgt_platform: multiple
title: SuspendRoot method of the Win32\_OfflineFilesCache class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SuspendRoot method of the Win32\_OfflineFilesCache class

Suspends or releases a share root or directory tree. A suspended item is always in the offline state and is excluded from automatic synchronization by Offline Files.

## Syntax


```mof
uint32 SuspendRoot(
  [in] string  Path,
  [in] boolean Suspend
);
```



## Parameters

<dl> <dt>

*Path* \[in\]
</dt> <dd>

The UNC path of the directory to be suspended. The path must exist in the Offline Files cache.

</dd> <dt>

*Suspend* \[in\]
</dt> <dd>

Specify **TRUE** to suspend, or **FALSE** to release.

</dd> </dl>

## Return value

This method returns either a [WMI return code](https://msdn.microsoft.com/library/aa394574) or a [system error code](https://msdn.microsoft.com/library/windows/desktop/ms681381).

## Remarks

When a share root or directory tree is suspended, all directories and files contained in the share or directory or in any subfolders are suspended as well. This means that both directories and files may be suspended. Note that a directory can be suspended directly (if it is the root of the share or directory tree) or indirectly (if it is one of the items contained in the share or directory tree).

Suspended items are always offline and are excluded from automatic synchronization by the Offline Files service. Nevertheless, suspended items can still be synchronized by using the [**Synchronize**](win32-offlinefilescache-synchronize.md) method, or one of the user interface Sync points in either the Sync Center or Windows Explorer.

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Namespace<br/>                | Root\\CIMv2<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Cscobj.h</dt> </dl>                    |
| MOF<br/>                      | <dl> <dt>OfflineFilesWmiProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CscObj.dll</dt> </dl>                  |



## See also

<dl> <dt>

[**Win32\_OfflineFilesCache**](win32-offlinefilescache.md)
</dt> </dl>

 

 




