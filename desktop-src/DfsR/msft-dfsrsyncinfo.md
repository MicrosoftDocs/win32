---
title: MSFT\_DfsrSyncInfo class
description: This class provides statistical and operational information for active synchronization sessions between the local replication group member and one of its partners.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 51e182b2-89fc-4cb3-a510-dba2b7adb3ea
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_DfsrSyncInfo class Distributed File System Replication
- MSFT_DfsrSyncInfo class Distributed File System Replication , described
topic_type:
- apiref
api_name:
- MSFT_DfsrSyncInfo
- MSFT_DfsrSyncInfo.SyncGuid
- MSFT_DfsrSyncInfo.ConnectionGuid
- MSFT_DfsrSyncInfo.MemberGuid
- MSFT_DfsrSyncInfo.MemberName
- MSFT_DfsrSyncInfo.PartnerGuid
- MSFT_DfsrSyncInfo.PartnerName
- MSFT_DfsrSyncInfo.ReplicationGroupGuid
- MSFT_DfsrSyncInfo.ReplicationGroupName
- MSFT_DfsrSyncInfo.Inbound
- MSFT_DfsrSyncInfo.State
- MSFT_DfsrSyncInfo.InitiationReason
- MSFT_DfsrSyncInfo.StartTime
- MSFT_DfsrSyncInfo.EndTime
- MSFT_DfsrSyncInfo.UpdatesTransferred
- MSFT_DfsrSyncInfo.BytesTransferred
- MSFT_DfsrSyncInfo.UpdatesNotTransferred
- MSFT_DfsrSyncInfo.UpdatesToBeTransferred
- MSFT_DfsrSyncInfo.ConflictsGenerated
- MSFT_DfsrSyncInfo.TombstonesGenerated
- MSFT_DfsrSyncInfo.LastErrorCode
- MSFT_DfsrSyncInfo.LastErrorMessageId
- MSFT_DfsrSyncInfo.ForceReplicationEndTime
- MSFT_DfsrSyncInfo.ForceReplicationBandwidthlevel
api_location:
- DfsRWmiV2.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_DfsrSyncInfo class

This class provides statistical and operational information for active synchronization sessions between the local replication group member and one of its partners.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DfsrWMIV2"), AMENDMENT]
class MSFT_DfsrSyncInfo
{
  string   SyncGuid;
  string   ConnectionGuid;
  string   MemberGuid;
  string   MemberName;
  string   PartnerGuid;
  string   PartnerName;
  string   ReplicationGroupGuid;
  string   ReplicationGroupName;
  boolean  Inbound;
  uint32   State;
  uint32   InitiationReason;
  datetime StartTime;
  datetime EndTime;
  uint32   UpdatesTransferred;
  uint64   BytesTransferred;
  uint32   UpdatesNotTransferred;
  uint32   UpdatesToBeTransferred;
  uint32   ConflictsGenerated;
  uint32   TombstonesGenerated;
  uint32   LastErrorCode;
  uint32   LastErrorMessageId;
  datetime ForceReplicationEndTime;
  uint32   ForceReplicationBandwidthlevel;
};
```

## Members

The **MSFT\_DfsrSyncInfo** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_DfsrSyncInfo** class has these properties.

<dl> <dt>

**BytesTransferred**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Number of Bytes Transferred")
</dt> </dl>

The total number of bytes that have been transferred since the synchronization session was started.

</dd> <dt>

**ConflictsGenerated**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Number of Conflicts Generated")
</dt> </dl>

The total number of conflicts encountered while processing updates for this session.

This property is valid only for inbound connections.

</dd> <dt>

**ConnectionGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Connection GUID")
</dt> </dl>

The unique connection identifier.

</dd> <dt>

**EndTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Sync End Time")
</dt> </dl>

The time stamp for the end of the synchronization session. If the session is still in progress, this value of this property is January 1, 1601.

</dd> <dt>

**ForceReplicationBandwidthlevel**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Current Force Replication bandwidth level")
</dt> </dl>

The bandwidth level of the current [**ForceReplication**](forcereplication-msft-dfsrconnectioninfo.md) operation.

</dd> <dt>

**ForceReplicationEndTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Current Force Replication End Time")
</dt> </dl>

The time stamp for the end of the current [**ForceReplication**](forcereplication-msft-dfsrconnectioninfo.md) operation.

</dd> <dt>

**Inbound**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Is Incoming Sync")
</dt> </dl>

Indicates the direction of the flow of updates between the synchronization partner and the synchronization member; it can be inbound (coming from the partner) or outbound (going to the partner).

</dd> <dt>

**InitiationReason**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Initiation Reason")
</dt> </dl>

The reason why the synchronization session was started. The following values are supported.

<dt>

<span id="Schedule"></span><span id="schedule"></span><span id="SCHEDULE"></span>

<span id="Schedule"></span><span id="schedule"></span><span id="SCHEDULE"></span>**Schedule** (0)


</dt> <dd>

Synchronization started according to the schedule.

</dd> <dt>

<span id="Forced"></span><span id="forced"></span><span id="FORCED"></span>

<span id="Forced"></span><span id="forced"></span><span id="FORCED"></span>**Forced** (1)


</dt> <dd>

Synchronization started as a response to a call to the [**ForceReplication**](forcereplication-msft-dfsrconnectioninfo.md) method.

</dd> <dt>

<span id="Paused"></span><span id="paused"></span><span id="PAUSED"></span>

<span id="Paused"></span><span id="paused"></span><span id="PAUSED"></span>**Paused** (2)


</dt> <dd>

Pause synchronization as a response to a call to [**ForceReplication**](forcereplication-msft-dfsrconnectioninfo.md).

</dd> <dt>

<span id="ForcedUntilSync"></span><span id="forceduntilsync"></span><span id="FORCEDUNTILSYNC"></span>

<span id="ForcedUntilSync"></span><span id="forceduntilsync"></span><span id="FORCEDUNTILSYNC"></span>**ForcedUntilSync** (3)


</dt> <dd>

Synchronization started as a response to a call to [**ForceReplication**](forcereplication-msft-dfsrconnectioninfo.md) with a value of Sync Until-In-Sync.

</dd> </dl>

This property is valid only for inbound connections.

</dd> <dt>

**LastErrorCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Last Error Code")
</dt> </dl>

The last error code.

<dt>

<span id="Success"></span><span id="success"></span><span id="SUCCESS"></span>

<span id="Success"></span><span id="success"></span><span id="SUCCESS"></span>**Success** (0)


</dt> <dd></dd> <dt>

<span id="DFSR_E_CANNOT_CONNECT"></span><span id="dfsr_e_cannot_connect"></span>

<span id="DFSR_E_CANNOT_CONNECT"></span><span id="dfsr_e_cannot_connect"></span>**DFSR\_E\_CANNOT\_CONNECT**


</dt> <dd>

Could not connect to the partner.

This value is returned only for inbound connections.

</dd> </dl>

</dd> <dt>

**LastErrorMessageId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Last Error Message ID")
</dt> </dl>

The event log message identifier that corresponds to the last error code.

<dt>

<span id="Success"></span><span id="success"></span><span id="SUCCESS"></span>

**Success** (0)


</dt> <dd></dd> </dl>

</dd> <dt>

**MemberGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Member GUID")
</dt> </dl>

The local replication group member identifier.

</dd> <dt>

**MemberName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Member Name")
</dt> </dl>

The member name. This is typically the unqualified DNS name of the local computer.

</dd> <dt>

**PartnerGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Partner GUID")
</dt> </dl>

The unique identifier of the partner object.

</dd> <dt>

**PartnerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Partner Name")
</dt> </dl>

The partner name. This is typically the unqualified DNS name of the partner computer.

</dd> <dt>

**ReplicationGroupGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Replication Group GUID")
</dt> </dl>

The unique replication group identifier.

</dd> <dt>

**ReplicationGroupName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Replication Group Name")
</dt> </dl>

The name of the replication group that owns the connection.

</dd> <dt>

**StartTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Sync Start Time")
</dt> </dl>

The time stamp for the start of the synchronization session.

</dd> <dt>

**State**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Sync Session State")
</dt> </dl>

The state of the current synchronization session.

<dt>

<span id="Initialized"></span><span id="initialized"></span><span id="INITIALIZED"></span>

**Initialized** (0)


</dt> <dd></dd> <dt>

<span id="Connecting"></span><span id="connecting"></span><span id="CONNECTING"></span>

**Connecting** (1)


</dt> <dd></dd> <dt>

<span id="In_Progress"></span><span id="in_progress"></span><span id="IN_PROGRESS"></span>

**In Progress** (2)


</dt> <dd></dd> <dt>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>

**Completed** (3)


</dt> <dd></dd> <dt>

<span id="In_Sync"></span><span id="in_sync"></span><span id="IN_SYNC"></span>

**In Sync** (4)


</dt> <dd></dd> <dt>

<span id="Interrupted"></span><span id="interrupted"></span><span id="INTERRUPTED"></span>

**Interrupted** (5)


</dt> <dd></dd> <dt>

<span id="In_Error"></span><span id="in_error"></span><span id="IN_ERROR"></span>

**In Error** (6)


</dt> <dd></dd> </dl>

</dd> <dt>

**SyncGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Sync GUID")
</dt> </dl>

The unique synchronization identifier for this operation.

</dd> <dt>

**TombstonesGenerated**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Number of Tombstones Generated")
</dt> </dl>

The total number of tombstones encountered while processing updates for this session.

This property is valid only for inbound connections.

</dd> <dt>

**UpdatesNotTransferred**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Number of Updates Not Transferred")
</dt> </dl>

Total number of updates in the queue for transfer in this synchronization session.

</dd> <dt>

**UpdatesToBeTransferred**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Number of Updates Not Transferred")
</dt> </dl>

The total number of updates that need to be synchronized with the partner.

This property is valid only for inbound connections.

</dd> <dt>

**UpdatesTransferred**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Number of Updates Transferred")
</dt> </dl>

The total number of updates that have been transferred since the synchronization session was started.

</dd> </dl>

## Remarks

A synchronization operation may involve more than one session to avoid being blocked on an update that has not been transferred yet.

The following state diagram illustrates the transitions between the synchronization states.

![dfsr synchronization state diagram](images/sync-state.png)

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                        |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dfsr<br/>                                                |
| MOF<br/>                      | <dl> <dt>Dfsrwmiv2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DfsRWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[DFSR WMI Classes](dfsr-wmi-classes.md)
</dt> </dl>

 

 





