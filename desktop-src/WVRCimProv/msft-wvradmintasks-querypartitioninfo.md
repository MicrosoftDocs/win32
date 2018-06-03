---
title: QueryPartitionInfo method of the MSFT\_WvrAdminTasks class
description: Queries the partition related information.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8aece83e-c379-4661-82c4-cc3f90bd4878
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- QueryPartitionInfo method
- QueryPartitionInfo method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, QueryPartitionInfo method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# QueryPartitionInfo method of the MSFT\_WvrAdminTasks class

Queries the partition related information.

## Syntax


```mof
uint32 QueryPartitionInfo(
  [in]  string ReplicationGroupName,
  [in]  string PartitionId,
  [out] uint64 CapacityInBytes,
  [out] uint64 FreeSpaceInBytes,
  [out] uint16 PercentLogConsumed,
  [out] uint64 TimeToLogWrapInSeconds,
  [out] uint64 IndexSizeInBytes
);
```



## Parameters

<dl> <dt>

*ReplicationGroupName* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*PartitionId* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*CapacityInBytes* \[out\]
</dt> <dd>

TBD

</dd> <dt>

*FreeSpaceInBytes* \[out\]
</dt> <dd>

TBD

</dd> <dt>

*PercentLogConsumed* \[out\]
</dt> <dd>

TBD

</dd> <dt>

*TimeToLogWrapInSeconds* \[out\]
</dt> <dd>

TBD

</dd> <dt>

*IndexSizeInBytes* \[out\]
</dt> <dd>

TBD

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\StorageReplica<br/>                                       |
| MOF<br/>                      | <dl> <dt>Wvrcimprov.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wvrcimprov.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_WvrAdminTasks**](msft-wvradmintasks.md)
</dt> </dl>

 

 





