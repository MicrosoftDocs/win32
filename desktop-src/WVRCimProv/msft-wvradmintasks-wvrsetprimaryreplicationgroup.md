---
title: WvrSetPrimaryReplicationGroup method of the MSFT\_WvrAdminTasks class
description: TBD.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 24b9bc11-7957-443f-be5a-cdb71d16b546
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- WvrSetPrimaryReplicationGroup method
- WvrSetPrimaryReplicationGroup method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, WvrSetPrimaryReplicationGroup method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WvrSetPrimaryReplicationGroup method of the MSFT\_WvrAdminTasks class

TBD

## Syntax


```mof
uint32 WvrSetPrimaryReplicationGroup(
  [in] string  ReplicationGroupName,
  [in] string  SecondaryReplicationGroupName[],
  [in] string  SecondaryReplicationGroupId[],
  [in] string  SecondaryComputerName[],
  [in] string  PartnershipId[],
  [in] boolean Force
);
```



## Parameters

<dl> <dt>

*ReplicationGroupName* \[in\]
</dt> <dd>

The name of the primary replication group.

</dd> <dt>

*SecondaryReplicationGroupName* \[in\]
</dt> <dd>

The names of the secondary replication groups.

</dd> <dt>

*SecondaryReplicationGroupId* \[in\]
</dt> <dd>

The IDs of the secondary replication groups.

</dd> <dt>

*SecondaryComputerName* \[in\]
</dt> <dd>

The FQDN or NetBIOS name of the secondary computer.

</dd> <dt>

*PartnershipId* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*Force* \[in\]
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

 

 





