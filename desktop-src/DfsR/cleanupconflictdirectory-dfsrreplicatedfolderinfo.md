---
title: CleanupConflictDirectory method of the DfsrReplicatedFolderInfo class
description: Starts the Conflict and Deleted folder cleanup process.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7077c2cc-b324-40ac-b2c2-29c334fe3828
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CleanupConflictDirectory method Distributed File System Replication
- CleanupConflictDirectory method Distributed File System Replication , DfsrReplicatedFolderInfo class
- DfsrReplicatedFolderInfo class Distributed File System Replication , CleanupConflictDirectory method
topic_type:
- apiref
api_name:
- DfsrReplicatedFolderInfo.CleanupConflictDirectory
api_location:
- DfsRWmiV2.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CleanupConflictDirectory method of the DfsrReplicatedFolderInfo class

Starts the Conflict and Deleted folder cleanup process.

## Syntax


```mof
uint32 CleanupConflictDirectory();
```



## Parameters

This method has no parameters.

## Return value

This method returns one of the [MONITOR\_STATUS return codes](monitor-status-return-codes.md) or one of the [system error codes](https://msdn.microsoft.com/library/windows/desktop/ms681381).

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| End of client support<br/>    | Windows Vista<br/>                                                                 |
| Namespace<br/>                | Root\\MicrosoftDfs<br/>                                                            |
| MOF<br/>                      | <dl> <dt>DfsRProvs.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DfsRWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[**DfsrReplicatedFolderInfo**](dfsrreplicatedfolderinfo.md)
</dt> </dl>

 

 





