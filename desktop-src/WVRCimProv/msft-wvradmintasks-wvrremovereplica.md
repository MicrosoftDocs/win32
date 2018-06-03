---
title: WvrRemoveReplica method of the MSFT\_WvrAdminTasks class
description: Removes a volume from an existing replication group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ba9bd6b8-69f6-4ae6-b747-e98528527c77
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- WvrRemoveReplica method
- WvrRemoveReplica method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, WvrRemoveReplica method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WvrRemoveReplica method of the MSFT\_WvrAdminTasks class

Removes a volume from an existing replication group.

## Syntax


```mof
uint32 WvrRemoveReplica(
  [in] string ReplicationGroupName,
  [in] string VolumeName
);
```



## Parameters

<dl> <dt>

*ReplicationGroupName* \[in\]
</dt> <dd>

The name of the replication group.

</dd> <dt>

*VolumeName* \[in\]
</dt> <dd>

TBD

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

 

 





