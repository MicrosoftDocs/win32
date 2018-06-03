---
title: SyncGroup method of the MSFT\_WvrAdminTasks class
description: Starts or resumes replication for a replication group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1b9818ee-a043-4ce1-b5a8-a0c885e6c6ed
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SyncGroup method
- SyncGroup method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, SyncGroup method
topic_type:
- apiref
api_name:
- MSFT_WvrAdminTasks.SyncGroup
api_location:
- WvrCimProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SyncGroup method of the MSFT\_WvrAdminTasks class

Starts or resumes replication for a replication group.

## Syntax


```mof
uint32 SyncGroup(
  [in] string ComputerName,
  [in] string Name
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

The FQDN or NetBIOS name of the computer.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

The name of the replication group to sync.

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

 

 





