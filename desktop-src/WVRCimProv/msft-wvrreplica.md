---
title: MSFT\_WvrReplica class
description: Represents a partition.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: efbfd924-127a-4d3e-b151-04d907a57778
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_WvrReplica class
- MSFT_WvrReplica class, described
topic_type:
- apiref
api_name:
- MSFT_WvrReplica
- MSFT_WvrReplica.PartitionId
- MSFT_WvrReplica.DataVolume
- MSFT_WvrReplica.PartitionSize
- MSFT_WvrReplica.NumOfBytesRecovered
- MSFT_WvrReplica.NumOfBytesRemaining
- MSFT_WvrReplica.CurrentLsn
- MSFT_WvrReplica.LastKnownPrimaryLsn
- MSFT_WvrReplica.LastInSyncTime
- MSFT_WvrReplica.LastOutOfSyncTime
- MSFT_WvrReplica.ReplicationMode
- MSFT_WvrReplica.ReplicationStatus
api_location:
- WvrCimProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_WvrReplica class

Represents a partition.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("wvrcimprov"), AMENDMENT]
class MSFT_WvrReplica
{
  string   PartitionId;
  string   DataVolume;
  uint64   PartitionSize;
  uint64   NumOfBytesRecovered;
  uint64   NumOfBytesRemaining;
  uint64   CurrentLsn;
  uint64   LastKnownPrimaryLsn;
  datetime LastInSyncTime;
  datetime LastOutOfSyncTime;
  uint32   ReplicationMode;
  uint32   ReplicationStatus;
};
```

## Members

The **MSFT\_WvrReplica** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_WvrReplica** class has these properties.

<dl> <dt>

**CurrentLsn**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current sequence number of the log.

</dd> <dt>

**DataVolume**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Full path of the data partition.

</dd> <dt>

**LastInSyncTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The last time this replica was in sync.

</dd> <dt>

**LastKnownPrimaryLsn**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Latest log sequence number from source replica.

</dd> <dt>

**LastOutOfSyncTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The last time this replica was out of sync.

</dd> <dt>

**NumOfBytesRecovered**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Data recovered in bytes.

</dd> <dt>

**NumOfBytesRemaining**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Data to be recovered in bytes.

</dd> <dt>

**PartitionId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The GUID identifying the partition.

</dd> <dt>

**PartitionSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Size of partition in bytes.

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

Current status of the replica.

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

[**MSFT\_WvrReplicationGroup**](msft-wvrreplicationgroup.md)
</dt> </dl>

 

 





