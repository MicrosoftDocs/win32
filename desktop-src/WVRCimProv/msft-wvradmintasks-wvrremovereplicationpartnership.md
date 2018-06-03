---
title: WvrRemoveReplicationPartnership method of the MSFT\_WvrAdminTasks class
description: Removes an existing replication partnership.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 802af940-1fca-4929-abae-340464839c7f
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- WvrRemoveReplicationPartnership method
- WvrRemoveReplicationPartnership method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, WvrRemoveReplicationPartnership method
topic_type:
- apiref
api_name:
- MSFT_WvrAdminTasks.WvrRemoveReplicationPartnership
api_location:
- WvrCimProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WvrRemoveReplicationPartnership method of the MSFT\_WvrAdminTasks class

Removes an existing replication partnership.

## Syntax


```mof
uint32 WvrRemoveReplicationPartnership(
  [in] string SourceReplicationGroupName,
  [in] string TargetReplicationGroupName,
  [in] string TargetComputerName
);
```



## Parameters

<dl> <dt>

*SourceReplicationGroupName* \[in\]
</dt> <dd>

The name of the source replication group.

</dd> <dt>

*TargetReplicationGroupName* \[in\]
</dt> <dd>

The name of the target replication group.

</dd> <dt>

*TargetComputerName* \[in\]
</dt> <dd>

The FQDN or NetBIOS name of the target computer.

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

 

 





