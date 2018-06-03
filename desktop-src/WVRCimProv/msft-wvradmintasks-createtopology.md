---
title: CreateTopology method of the MSFT\_WvrAdminTasks class
description: Creates replication groups and a new replication partnership.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0532c8f1-94ed-4507-8e33-a7bcb74803ee
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CreateTopology method
- CreateTopology method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, CreateTopology method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreateTopology method of the MSFT\_WvrAdminTasks class

Creates replication groups and a new replication partnership.

## Syntax


```mof
uint32 CreateTopology(
  [in]  string                         PartnershipId,
  [in]  string                         SourceComputerName,
  [in]  string                         SourceRGName,
  [in]  string                         SourceRGDescription,
  [in]  string                         SourceVolumeName[],
  [in]  string                         SourceLogVolumeName,
  [in]  string                         DestinationComputerName,
  [in]  string                         DestinationRGName,
  [in]  string                         DestinationRGDescription,
  [in]  string                         DestinationVolumeName[],
  [in]  string                         DestinationLogVolumeName,
  [in]  uint64                         LogSizeInBytes,
  [in]  uint32                         ReplicationMode,
  [in]  boolean                        PreventReplication,
  [in]  boolean                        Seeded,
  [in]  uint32                         AsyncRPO,
  [in]  boolean                        EnableConsistencyGroups,
  [in]  boolean                        EnableEncryption,
  [out] MSFT_WvrReplicationPartnership Output[]
);
```



## Parameters

<dl> <dt>

*PartnershipId* \[in\]
</dt> <dd>

The partnership ID.

</dd> <dt>

*SourceComputerName* \[in\]
</dt> <dd>

The FQDN or NetBIOS name of the source computer.

</dd> <dt>

*SourceRGName* \[in\]
</dt> <dd>

The name of the source replication group.

</dd> <dt>

*SourceRGDescription* \[in\]
</dt> <dd>

The description of the source replication group.

</dd> <dt>

*SourceVolumeName* \[in\]
</dt> <dd>

The source volume name.

</dd> <dt>

*SourceLogVolumeName* \[in\]
</dt> <dd>

The source log volume name.

</dd> <dt>

*DestinationComputerName* \[in\]
</dt> <dd>

The FQDN or NetBIOS name of the destination computer.

</dd> <dt>

*DestinationRGName* \[in\]
</dt> <dd>

The name of the destination replication group.

</dd> <dt>

*DestinationRGDescription* \[in\]
</dt> <dd>

The description of the destination replication group.

</dd> <dt>

*DestinationVolumeName* \[in\]
</dt> <dd>

The destination volume name.

</dd> <dt>

*DestinationLogVolumeName* \[in\]
</dt> <dd>

The destination log volume name.

</dd> <dt>

*LogSizeInBytes* \[in\]
</dt> <dd>

The size of the log file in Bytes.

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

*PreventReplication* \[in\]
</dt> <dd>

**true** to prevent replication.

</dd> <dt>

*Seeded* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*AsyncRPO* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*EnableConsistencyGroups* \[in\]
</dt> <dd>

**true** to enable consistency groups.

</dd> <dt>

*EnableEncryption* \[in\]
</dt> <dd>

**true** to enable encryption; otherwise, **false**.

</dd> <dt>

*Output* \[out\]
</dt> <dd>

Returns the resulting [**MSFT\_WvrReplicationPartnership**](msft-wvrreplicationpartnership.md) embedded instance.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\StorageReplica<br/>                                       |
| Header<br/>                   | <dl> <dt>Bdaiface.h</dt> </dl>     |
| MOF<br/>                      | <dl> <dt>WVRCimProv.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WvrCimProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_WvrAdminTasks**](msft-wvradmintasks.md)
</dt> </dl>

 

 





