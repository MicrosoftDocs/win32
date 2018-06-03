---
title: SetSecondaryReplicationGroup method of the MSFT\_WvrAdminTasks class
description: Assigns a source to a destination replication group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 197d2cb2-bea6-40ea-b925-090db0497102
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetSecondaryReplicationGroup method
- SetSecondaryReplicationGroup method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, SetSecondaryReplicationGroup method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetSecondaryReplicationGroup method of the MSFT\_WvrAdminTasks class

Assigns a source to a destination replication group.

## Syntax


```mof
uint32 SetSecondaryReplicationGroup(
  [in]  string ReplicationGroupName,
  [in]  string PrimaryComputerName,
  [in]  string PrimaryReplicationGroupId,
  [in]  string PrimaryReplicationGroupName,
  [in]  string PartnershipId,
  [out] uint32 ReturnedErrorType
);
```



## Parameters

<dl> <dt>

*ReplicationGroupName* \[in\]
</dt> <dd>

The name of the destination replication group.

</dd> <dt>

*PrimaryComputerName* \[in\]
</dt> <dd>

The FQDN or NetBIOS name of the computer.

</dd> <dt>

*PrimaryReplicationGroupId* \[in\]
</dt> <dd>

The ID of the source replication group.

</dd> <dt>

*PrimaryReplicationGroupName* \[in\]
</dt> <dd>

The name of the source replication group.

</dd> <dt>

*PartnershipId* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*ReturnedErrorType* \[out\]
</dt> <dd>

Whether the returned error code is a warning or an error.

The possible values are.

<dt>

<span id="Warning"></span><span id="warning"></span><span id="WARNING"></span>

**Warning** (1)


</dt> <dd></dd> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>

**Error** (2)


</dt> <dd></dd> </dl> </dd> </dl>

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

 

 





