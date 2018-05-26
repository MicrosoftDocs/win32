---
title: WvrModifyReplicationGroup method of the MSFT\_WvrAdminTasks class
description: Modifies the settings in a replication group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 70441e1c-57d9-435a-bb48-b393f6895dc8
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- WvrModifyReplicationGroup method
- WvrModifyReplicationGroup method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, WvrModifyReplicationGroup method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# WvrModifyReplicationGroup method of the MSFT\_WvrAdminTasks class

Modifies the settings in a replication group.

## Syntax


```mof
uint32 WvrModifyReplicationGroup(
  [in] string  ReplicationGroupName,
  [in] string  Description,
  [in] uint32  ReplicationMode,
  [in] uint64  MaxLogSizeInByte,
  [in] boolean EnableWriteConsistency,
  [in] boolean IsSeeded,
  [in] boolean Encryption,
  [in] boolean AllowVolumeResize,
  [in] uint32  AsyncRPO,
  [in] string  CertificateThumbprint
);
```



## Parameters

<dl> <dt>

*ReplicationGroupName* \[in\]
</dt> <dd>

The name of the replication group

</dd> <dt>

*Description* \[in\]
</dt> <dd>

A description of the replication group.

</dd> <dt>

*ReplicationMode* \[in\]
</dt> <dd>

Whether the replication is performed synchronously or asynchronously.

The possible values are.

<dt>

<span id="Sync"></span><span id="sync"></span><span id="SYNC"></span>

**Sync** (1)


</dt> <dd></dd> <dt>

<span id="Async"></span><span id="async"></span><span id="ASYNC"></span>

**Async** (2)


</dt> <dd></dd> </dl> </dd> <dt>

*MaxLogSizeInByte* \[in\]
</dt> <dd>

The maximum size of the log file in bytes.

</dd> <dt>

*EnableWriteConsistency* \[in\]
</dt> <dd>

Set **true** to enable write consistency.

</dd> <dt>

*IsSeeded* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*Encryption* \[in\]
</dt> <dd>

**true** to use encryption; otherwise, **false**.

</dd> <dt>

*AllowVolumeResize* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*AsyncRPO* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*CertificateThumbprint* \[in\]
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

 

 





