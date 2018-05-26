---
title: WvrQueryReplicationGroupInfo method of the MSFT\_WvrAdminTasks class
description: This routine queries metadata of a replication group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f7416360-3cc1-4ce1-b291-72eebf532b29
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- WvrQueryReplicationGroupInfo method
- WvrQueryReplicationGroupInfo method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, WvrQueryReplicationGroupInfo method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# WvrQueryReplicationGroupInfo method of the MSFT\_WvrAdminTasks class

This routine queries metadata of a replication group.

## Syntax


```mof
uint32 WvrQueryReplicationGroupInfo(
  [in]  string  ReplicationGroupName,
  [out] uint64  LogSizeInBytes,
  [out] uint32  LogVolumeSectorSize,
  [out] boolean IsWriteConsistent,
  [out] uint64  DataVolumeSize[],
  [out] uint32  DataVolumeSectorSize[]
);
```



## Parameters

<dl> <dt>

*ReplicationGroupName* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*LogSizeInBytes* \[out\]
</dt> <dd>

TBD

</dd> <dt>

*LogVolumeSectorSize* \[out\]
</dt> <dd>

TBD

</dd> <dt>

*IsWriteConsistent* \[out\]
</dt> <dd>

TBD

</dd> <dt>

*DataVolumeSize* \[out\]
</dt> <dd>

TBD

</dd> <dt>

*DataVolumeSectorSize* \[out\]
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

 

 





