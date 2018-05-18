---
title: ExchangeReplicationGroupId method of the MSFT\_WvrAdminTasks class
description: Exchanges the replication group ID between source and destination replication groups.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '7a4159df-d4ac-4011-afb0-3b99b0ccb1c4'
ms.prod: 'windows-server-dev'
ms.technology:
- 'storage-replica'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["ExchangeReplicationGroupId method", "ExchangeReplicationGroupId method, MSFT_WvrAdminTasks class", "MSFT_WvrAdminTasks class, ExchangeReplicationGroupId method"]
topic_type:
- apiref
api_name:
- MSFT_WvrAdminTasks.ExchangeReplicationGroupId
api_location:
- WvrCimProv.dll
api_type:
- COM
---

# ExchangeReplicationGroupId method of the MSFT\_WvrAdminTasks class

Exchanges the replication group ID between source and destination replication groups.

## Syntax


```mof
uint32 ExchangeReplicationGroupId(
  [in]  string SourceReplicationGroupName,
  [in]  string SourceReplicationGroupId,
  [in]  string TargetReplicationGroupName,
  [out] string TargetReplicationGroupId
);
```



## Parameters

<dl> <dt>

*SourceReplicationGroupName* \[in\]
</dt> <dd>

The name of the source replication group.

</dd> <dt>

*SourceReplicationGroupId* \[in\]
</dt> <dd>

The ID of the source replication group.

</dd> <dt>

*TargetReplicationGroupName* \[in\]
</dt> <dd>

The name of the target replication group.

</dd> <dt>

*TargetReplicationGroupId* \[out\]
</dt> <dd>

The ID of the target replication group.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\StorageReplica<br/>                                       |
| MOF<br/>                      | <dl> <dt>WVRCimProv.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WvrCimProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_WvrAdminTasks**](msft-wvradmintasks.md)
</dt> </dl>

 

 





