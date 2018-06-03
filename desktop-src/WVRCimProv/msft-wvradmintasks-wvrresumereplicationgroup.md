---
title: WvrResumeReplicationGroup method of the MSFT\_WvrAdminTasks class
description: Resumes all network and storage I/O for all replicas in a suspended replication group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b600d2ef-aeeb-4d7a-b76b-41fb749f8ce9
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- WvrResumeReplicationGroup method
- WvrResumeReplicationGroup method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, WvrResumeReplicationGroup method
topic_type:
- apiref
api_name:
- MSFT_WvrAdminTasks.WvrResumeReplicationGroup
api_location:
- WvrCimProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WvrResumeReplicationGroup method of the MSFT\_WvrAdminTasks class

Resumes all network and storage I/O for all replicas in a suspended replication group.

## Syntax


```mof
uint32 WvrResumeReplicationGroup(
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

 

 





