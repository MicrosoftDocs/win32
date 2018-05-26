---
title: WvrSuspendReplicationGroup method of the MSFT\_WvrAdminTasks class
description: Suspends all network and storage I/O for all volumes in a replication group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 24188c2b-0dcb-4294-b8c5-af636027bac7
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- WvrSuspendReplicationGroup method
- WvrSuspendReplicationGroup method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, WvrSuspendReplicationGroup method
topic_type:
- apiref
api_name:
- MSFT_WvrAdminTasks.WvrSuspendReplicationGroup
api_location:
- WvrCimProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# WvrSuspendReplicationGroup method of the MSFT\_WvrAdminTasks class

Suspends all network and storage I/O for all volumes in a replication group.

> \[!Warning\]  
> This method can result in application failures.

 

## Syntax


```mof
uint32 WvrSuspendReplicationGroup(
  [in] string ReplicationGroupName
);
```



## Parameters

<dl> <dt>

*ReplicationGroupName* \[in\]
</dt> <dd>

The name of the replication group.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\StorageReplica<br/>                                       |
| MOF<br/>                      | <dl> <dt>WVRCimProv.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WvrCimProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_WvrAdminTasks**](msft-wvradmintasks.md)
</dt> </dl>

 

 





