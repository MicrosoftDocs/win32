---
title: GetOutboundBacklogFileCount method of the MSFT\_DfsrReplicatedFolderInfo class
description: Retrieves the number of files scheduled to be replicated to an outbound partner given its version vector.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 78be19ba-0dd7-4237-ad2d-531157f391e4
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetOutboundBacklogFileCount method Distributed File System Replication
- GetOutboundBacklogFileCount method Distributed File System Replication , MSFT_DfsrReplicatedFolderInfo class
- MSFT_DfsrReplicatedFolderInfo class Distributed File System Replication , GetOutboundBacklogFileCount method
topic_type:
- apiref
api_name:
- MSFT_DfsrReplicatedFolderInfo.GetOutboundBacklogFileCount
api_location:
- DfsRWmiV2.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetOutboundBacklogFileCount method of the MSFT\_DfsrReplicatedFolderInfo class

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

The version vector of the outbound partner. This value should be obtained by calling the [**GetVersionVector**](getversionvector-msft-dfsrreplicatedfolderinfo.md) method of the outbound partner for the same replicated folder.

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
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                        |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dfsr<br/>                                                |
| MOF<br/>                      | <dl> <dt>Dfsrwmiv2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DfsRWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_DfsrReplicatedFolderInfo**](msft-dfsrreplicatedfolderinfo.md)
</dt> </dl>

 

 





