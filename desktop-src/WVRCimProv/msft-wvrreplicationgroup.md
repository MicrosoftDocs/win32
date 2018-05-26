---
title: MSFT\_WvrReplicationGroup class
description: Represents a group of replicas.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0858ffec-06ba-4613-a860-358e002b3582
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_WvrReplicationGroup class
- MSFT_WvrReplicationGroup class, described
topic_type:
- apiref
api_name:
- MSFT_WvrReplicationGroup
- MSFT_WvrReplicationGroup.Name
- MSFT_WvrReplicationGroup.ComputerName
- MSFT_WvrReplicationGroup.Description
- MSFT_WvrReplicationGroup.Id
- MSFT_WvrReplicationGroup.LogVolume
- MSFT_WvrReplicationGroup.LogSizeInBytes
- MSFT_WvrReplicationGroup.Partitions
- MSFT_WvrReplicationGroup.IsCluster
- MSFT_WvrReplicationGroup.IsAutoFailover
- MSFT_WvrReplicationGroup.IsPrimary
- MSFT_WvrReplicationGroup.IsSuspended
- MSFT_WvrReplicationGroup.IsInPartnership
- MSFT_WvrReplicationGroup.IsWriteConsistency
- MSFT_WvrReplicationGroup.AsyncRPO
- MSFT_WvrReplicationGroup.IsEncrypted
- MSFT_WvrReplicationGroup.AllowVolumeResize
- MSFT_WvrReplicationGroup.NumOfReplicas
- MSFT_WvrReplicationGroup.ReplicationMode
- MSFT_WvrReplicationGroup.ReplicationStatus
- MSFT_WvrReplicationGroup.LastInSyncTime
- MSFT_WvrReplicationGroup.Replicas
api_location:
- WvrCimProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_WvrReplicationGroup class

Represents a group of replicas.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("wvrcimprov"), AMENDMENT]
class MSFT_WvrReplicationGroup
{
  string          Name;
  string          ComputerName;
  string          Description;
  string          Id;
  string          LogVolume;
  uint64          LogSizeInBytes;
  string          Partitions[];
  boolean         IsCluster;
  boolean         IsAutoFailover;
  boolean         IsPrimary;
  boolean         IsSuspended;
  boolean         IsInPartnership;
  boolean         IsWriteConsistency;
  uint32          AsyncRPO;
  boolean         IsEncrypted;
  boolean         AllowVolumeResize;
  uint32          NumOfReplicas;
  uint32          ReplicationMode;
  uint32          ReplicationStatus;
  datetime        LastInSyncTime;
  MSFT_WvrReplica Replicas[];
};
```

## Members

The **MSFT\_WvrReplicationGroup** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_WvrReplicationGroup** class has these properties.

<dl> <dt>

**AllowVolumeResize**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies whether the replicas in this replication group are allowed to be resized (expanded).

</dd> <dt>

**AsyncRPO**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum difference in time that an asynchronous partnerships data should differ between source and destination as a Recovery Point Objective.

When not set, the default asynchronous RPO time is 5 minutes. After this time is exceeded, the source server sends repeated notifications and event log messages warnings to the administrator. Furthermore, an administrator can configure write IO throttles in order to allow the destination server to catch up.

</dd> <dt>

**ComputerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The fully qualified domain name (FQDN) or NetBIOS name of the computer.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A description of the replication group.

</dd> <dt>

**Id**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Identifies the replication group.

</dd> <dt>

**IsAutoFailover**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether this replication group is able to automatically fail over between asymmetric storage synchronizations.

</dd> <dt>

**IsCluster**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether this replication group is a clustered replication group.

</dd> <dt>

**IsEncrypted**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether this replication group uses an encrypted channel for communication.

</dd> <dt>

**IsInPartnership**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether this replication group contains replication partners.

</dd> <dt>

**IsPrimary**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether this replication group acts as the source of replication.

</dd> <dt>

**IsSuspended**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether replication in the group is suspended.

</dd> <dt>

**IsWriteConsistency**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether this replication group has write consistency turned on.

</dd> <dt>

**LastInSyncTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The last time this replication group was in sync.

</dd> <dt>

**LogSizeInBytes**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Size of log in Bytes.

</dd> <dt>

**LogVolume**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Full path of the log container.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Friendly name of the replication group.

</dd> <dt>

**NumOfReplicas**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of replicas in this replication group.

</dd> <dt>

**Partitions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The replicated partitions.

</dd> <dt>

**Replicas**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_WvrReplica** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**MSFT\_WvrReplica**](msft-wvrreplica.md)")
</dt> </dl>

Embedded instances of the [**MSFT\_WvrReplica**](msft-wvrreplica.md) instances in the group.

</dd> <dt>

**ReplicationMode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether the replication is performed synchronously or asynchronously.

The possible values are.

<dt>

<span id="Sync"></span><span id="sync"></span><span id="SYNC"></span>

**Sync** (1)


</dt> <dd></dd> <dt>

<span id="Async"></span><span id="async"></span><span id="ASYNC"></span>

**Async** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**ReplicationStatus**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current status of the replication group.

The possible values are.

<dt>

<span id="ContinuouslyReplicating"></span><span id="continuouslyreplicating"></span><span id="CONTINUOUSLYREPLICATING"></span>

**ContinuouslyReplicating** (1)


</dt> <dd></dd> <dt>

<span id="WaitingForQuorum"></span><span id="waitingforquorum"></span><span id="WAITINGFORQUORUM"></span>

**WaitingForQuorum** (2)


</dt> <dd></dd> <dt>

<span id="RecoveringFromReplicationLog"></span><span id="recoveringfromreplicationlog"></span><span id="RECOVERINGFROMREPLICATIONLOG"></span>

**RecoveringFromReplicationLog** (3)


</dt> <dd></dd> <dt>

<span id="Failed"></span><span id="failed"></span><span id="FAILED"></span>

**Failed** (4)


</dt> <dd></dd> <dt>

<span id="ReplicationSuspended"></span><span id="replicationsuspended"></span><span id="REPLICATIONSUSPENDED"></span>

**ReplicationSuspended** (5)


</dt> <dd></dd> <dt>

<span id="ConnectingToSource"></span><span id="connectingtosource"></span><span id="CONNECTINGTOSOURCE"></span>

**ConnectingToSource** (6)


</dt> <dd></dd> <dt>

<span id="WaitingForDestination"></span><span id="waitingfordestination"></span><span id="WAITINGFORDESTINATION"></span>

**WaitingForDestination** (7)


</dt> <dd></dd> <dt>

<span id="LogRecordCopyFromSource"></span><span id="logrecordcopyfromsource"></span><span id="LOGRECORDCOPYFROMSOURCE"></span>

**LogRecordCopyFromSource** (8)


</dt> <dd></dd> <dt>

<span id="BlockCopyFromSource"></span><span id="blockcopyfromsource"></span><span id="BLOCKCOPYFROMSOURCE"></span>

**BlockCopyFromSource** (9)


</dt> <dd></dd> <dt>

<span id="InitialBlockCopy"></span><span id="initialblockcopy"></span><span id="INITIALBLOCKCOPY"></span>

**InitialBlockCopy** (10)


</dt> <dd></dd> <dt>

<span id="ContinuouslyReplicating_OutOfRPO"></span><span id="continuouslyreplicating_outofrpo"></span><span id="CONTINUOUSLYREPLICATING_OUTOFRPO"></span>

**ContinuouslyReplicating\_OutOfRPO** (11)


</dt> <dd></dd> <dt>

<span id="ContinuouslyReplicating_InRPO"></span><span id="continuouslyreplicating_inrpo"></span><span id="CONTINUOUSLYREPLICATING_INRPO"></span>

**ContinuouslyReplicating\_InRPO** (12)


</dt> <dd></dd> <dt>

<span id="LogRecordCopyToDestination"></span><span id="logrecordcopytodestination"></span><span id="LOGRECORDCOPYTODESTINATION"></span>

**LogRecordCopyToDestination** (13)


</dt> <dd></dd> <dt>

<span id="BlockCopyToDestination"></span><span id="blockcopytodestination"></span><span id="BLOCKCOPYTODESTINATION"></span>

**BlockCopyToDestination** (14)


</dt> <dd></dd> <dt>

<span id="NotInPartnership"></span><span id="notinpartnership"></span><span id="NOTINPARTNERSHIP"></span>

**NotInPartnership** (15)


</dt> <dd></dd> </dl>

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

[**MSFT\_WvrReplicationPartnership**](msft-wvrreplicationpartnership.md)
</dt> <dt>

[**MSFT\_WvrReplica**](msft-wvrreplica.md)
</dt> </dl>

 

 





