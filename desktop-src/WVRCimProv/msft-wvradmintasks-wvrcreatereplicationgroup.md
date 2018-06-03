---
title: WvrCreateReplicationGroup method of the MSFT\_WvrAdminTasks class
description: Creates a new replication group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4800b87e-06e9-4867-94c0-13114aae4265
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- WvrCreateReplicationGroup method
- WvrCreateReplicationGroup method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, WvrCreateReplicationGroup method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WvrCreateReplicationGroup method of the MSFT\_WvrAdminTasks class

Creates a new replication group.

## Syntax


```mof
uint32 WvrCreateReplicationGroup(
  [in]  string         ReplicationGroupName,
  [in]  string         Description,
  [in]  string         VolumeNames[],
  [in]  string         LogPath,
  [in]  uint64         MaxLogSizeInByte,
  [in]  uint32         ReplicationMode,
  [in]  uint32         MinimumPartnersInSync,
  [in]  boolean        EnableWriteConsistency,
  [in]  boolean        EnableEncryption,
  [in]  string         CertificateThumbprint,
  [out] MSFT_SrJob REF Task
);
```



## Parameters

<dl> <dt>

*ReplicationGroupName* \[in\]
</dt> <dd>

The name of the replication group to create.

</dd> <dt>

*Description* \[in\]
</dt> <dd>

A text description of the group.

</dd> <dt>

*VolumeNames* \[in\]
</dt> <dd>

A collection of volume names.

</dd> <dt>

*LogPath* \[in\]
</dt> <dd>

Full path of the log container.

</dd> <dt>

*MaxLogSizeInByte* \[in\]
</dt> <dd>

The maximum size of the log file in Bytes.

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

*MinimumPartnersInSync* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*EnableWriteConsistency* \[in\]
</dt> <dd>

Set **true** to enable write consistency.

</dd> <dt>

*EnableEncryption* \[in\]
</dt> <dd>

**true** to enable encryption; otherwise, **false**.

</dd> <dt>

*CertificateThumbprint* \[in\]
</dt> <dd>

The certificate thumbprint.

</dd> <dt>

*Task* \[out\]
</dt> <dd>

Returns a reference to the [**MSFT\_SrJob**](msft-srjob.md) instance that represents the asynchronous process of creating the replication group.

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

 

 





