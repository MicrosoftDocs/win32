---
title: GetOutboundBacklogFileIdRecords method of the MSFT\_DfsrReplicatedFolderInfo class
description: Retrieves the list of ID records for the files that are scheduled to be replicated to the outbound partner given its version vector.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '4fe29072-c41d-4c9e-ac8c-0fce2d4dc5ae'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-file-system-replication'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetOutboundBacklogFileIdRecords method Distributed File System Replication", "GetOutboundBacklogFileIdRecords method Distributed File System Replication , MSFT_DfsrReplicatedFolderInfo class", "MSFT_DfsrReplicatedFolderInfo class Distributed File System Replication , GetOutboundBacklogFileIdRecords method"]
topic_type:
- apiref
api_name:
- MSFT_DfsrReplicatedFolderInfo.GetOutboundBacklogFileIdRecords
api_location:
- DfsRWmiV2.dll
api_type:
- COM
---

# GetOutboundBacklogFileIdRecords method of the MSFT\_DfsrReplicatedFolderInfo class

Retrieves the list of ID records for the files that are scheduled to be replicated to the outbound partner given its version vector.

## Syntax


```mof
uint32 GetOutboundBacklogFileIdRecords(
  [in]  string                VersionVector,
  [out] MSFT_DfsrIdRecordInfo BacklogIdRecords[],
  [out] uint32                IdRecordIndex
);
```



## Parameters

<dl> <dt>

*VersionVector* \[in\]
</dt> <dd>

The version vector of the outbound partner. This value should be obtained by calling the [**GetVersionVector**](getversionvector-msft-dfsrreplicatedfolderinfo.md) method of the outbound partner for the same replicated folder.

</dd> <dt>

*BacklogIdRecords* \[out\]
</dt> <dd>

An array of [**MSFT\_DfsrIdRecordInfo**](msft-dfsridrecordinfo.md) records for the files in the backlog.

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
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                        |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dfsr<br/>                                                |
| MOF<br/>                      | <dl> <dt>Dfsrwmiv2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DfsRWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_DfsrReplicatedFolderInfo**](msft-dfsrreplicatedfolderinfo.md)
</dt> </dl>

 

 





