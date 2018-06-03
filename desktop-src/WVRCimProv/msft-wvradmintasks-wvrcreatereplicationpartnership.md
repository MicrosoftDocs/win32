---
title: WvrCreateReplicationPartnership method of the MSFT\_WvrAdminTasks class
description: Creates a new replication partnership between existing replication groups.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 82dd9d01-7113-4dd2-865d-5c5a59a997fb
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- WvrCreateReplicationPartnership method
- WvrCreateReplicationPartnership method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, WvrCreateReplicationPartnership method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WvrCreateReplicationPartnership method of the MSFT\_WvrAdminTasks class

Creates a new replication partnership between existing replication groups.

## Syntax


```mof
uint32 WvrCreateReplicationPartnership(
  [in] string SourceReplicationGroupName,
  [in] string TargetReplicationGroupName,
  [in] string TargetComputerName,
  [in] string PartnershipId
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

</dd> <dt>

*PartnershipId* \[in\]
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

 

 





