---
title: GetOutboundBacklogFileCount method of the DfsrReplicatedFolderInfo class
description: Retrieves the number of files scheduled to be replicated to an outbound partner given its version vector.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 58394e1c-6818-4844-9b23-d20fe164e30e
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetOutboundBacklogFileCount method Distributed File System Replication
- GetOutboundBacklogFileCount method Distributed File System Replication , DfsrReplicatedFolderInfo class
- DfsrReplicatedFolderInfo class Distributed File System Replication , GetOutboundBacklogFileCount method
topic_type:
- apiref
api_name:
- DfsrReplicatedFolderInfo.GetOutboundBacklogFileCount
api_location:
- DfsRWmiV2.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetOutboundBacklogFileCount method of the DfsrReplicatedFolderInfo class

Retrieves the number of files scheduled to be replicated to an outbound partner given its version vector.

## Syntax


```mof
uint32 GetOutboundBacklogFileCount(
  [in]  string VersionVector,
  [out] uint32 BacklogFileCount,
  [out] uint32 IdRecordIndex
);
```



## Parameters

<dl> <dt>

*VersionVector* \[in\]
</dt> <dd>

The version vector of the outbound partner. This value should be obtained by calling the [**GetVersionVector**](getversionvector-dfsrreplicatedfolderinfo.md) method of the outbound partner for the same replicated folder.

</dd> <dt>

*BacklogFileCount* \[out\]
</dt> <dd>

The count of files in the backlog.

</dd> <dt>

*IdRecordIndex* \[out\]
</dt> <dd>

The index number of the last ID record processed.

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

 

 





