---
title: GetVersionVector method of the DfsrReplicatedFolderInfo class
description: Retrieves the current version vector chain of this member.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 08c91057-872e-438d-a028-33f623b43f66
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetVersionVector method Distributed File System Replication
- GetVersionVector method Distributed File System Replication , DfsrReplicatedFolderInfo class
- DfsrReplicatedFolderInfo class Distributed File System Replication , GetVersionVector method
topic_type:
- apiref
api_name:
- DfsrReplicatedFolderInfo.GetVersionVector
api_location:
- DfsRWmiV2.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetVersionVector method of the DfsrReplicatedFolderInfo class

Retrieves the current version vector chain of this member.

## Syntax


```mof
uint32 GetVersionVector(
  [out] string VersionVector
);
```



## Parameters

<dl> <dt>

*VersionVector* \[out\]
</dt> <dd>

The version vector, in string format. During synchronization, partners exchange their version vectors and calculate the files and directories that have not yet been synchronized.

</dd> </dl>

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

 

 





