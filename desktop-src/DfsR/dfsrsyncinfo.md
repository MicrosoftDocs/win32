---
title: DfsrSyncInfo class
description: This class provides statistical and operational information for active synchronization sessions between the local replication group member and one of its partners.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0503e6bb-7f9f-489f-99a5-9a0c34416912
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DfsrSyncInfo class Distributed File System Replication
- DfsrSyncInfo class Distributed File System Replication , described
topic_type:
- apiref
api_name:
- DfsrSyncInfo
- DfsrSyncInfo.Caption
- DfsrSyncInfo.Description
- DfsrSyncInfo.InstallDate
- DfsrSyncInfo.Name
- DfsrSyncInfo.Status
- DfsrSyncInfo.SyncGuid
- DfsrSyncInfo.ConnectionGuid
- DfsrSyncInfo.MemberGuid
- DfsrSyncInfo.MemberName
- DfsrSyncInfo.PartnerGuid
- DfsrSyncInfo.PartnerName
- DfsrSyncInfo.ReplicationGroupGuid
- DfsrSyncInfo.ReplicationGroupName
- DfsrSyncInfo.Inbound
- DfsrSyncInfo.State
- DfsrSyncInfo.InitiationReason
- DfsrSyncInfo.StartTime
- DfsrSyncInfo.EndTime
- DfsrSyncInfo.UpdatesTransferred
- DfsrSyncInfo.BytesTransferred
- DfsrSyncInfo.UpdatesNotTransferred
- DfsrSyncInfo.UpdatesToBeTransferred
- DfsrSyncInfo.ConflictsGenerated
- DfsrSyncInfo.TombstonesGenerated
- DfsrSyncInfo.LastErrorCode
- DfsrSyncInfo.LastErrorMessageId
- DfsrSyncInfo.ForceReplicationEndTime
- DfsrSyncInfo.ForceReplicationBandwidthlevel
api_location:
- DfsRWmiV2.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DfsrSyncInfo class

This class provides statistical and operational information for active synchronization sessions between the local replication group member and one of its partners.

## Syntax

``` syntax
[Dynamic, Provider("DfsrMonitorProv")]
class DfsrSyncInfo : CIM_LogicalElement
{
  string       Caption;
  string       Description;
  datetime REF InstallDate;
  string       Name;
  string       Status;
  string       SyncGuid;
  string       ConnectionGuid;
  string       MemberGuid;
  string       MemberName;
  string       PartnerGuid;
  string       PartnerName;
  string       ReplicationGroupGuid;
  string       ReplicationGroupName;
  boolean      Inbound;
  uint32       State;
  uint32       InitiationReason;
  datetime     StartTime;
  datetime     EndTime;
  uint32       UpdatesTransferred;
  uint64       BytesTransferred;
  uint32       UpdatesNotTransferred;
  uint32       UpdatesToBeTransferred;
  uint32       ConflictsGenerated;
  uint32       TombstonesGenerated;
  uint32       LastErrorCode;
  uint32       LastErrorMessageId;
  datetime     ForceReplicationEndTime;
  uint32       ForceReplicationBandwidthlevel;
};
```

## Members

The **DfsrSyncInfo** class has these types of members:

-   [Properties](#properties)

### Properties

The **DfsrSyncInfo** class has these properties.

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

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxLen** (64)
</dt> </dl>

A short textual description of the object. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

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

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Connection GUID"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36)
</dt> </dl>

The unique connection identifier.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

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

The bandwidth level of the current [**ForceReplication**](forcereplication-dfsrconnectioninfo.md) operation.

</dd> <dt>

**ForceReplicationEndTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Current Force Replication End Time")
</dt> </dl>

The time stamp for the end of the current [**ForceReplication**](forcereplication-dfsrconnectioninfo.md) operation.

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

<span id="Schedule"></span><span id="schedule"></span><span id="SCHEDULE"></span>**Schedule**


</dt> <dd>

Synchronization started according to the schedule.

</dd> <dt>

<span id="Forced"></span><span id="forced"></span><span id="FORCED"></span>

<span id="Forced"></span><span id="forced"></span><span id="FORCED"></span>**Forced**


</dt> <dd>

Synchronization started as a response to a call to the [**ForceReplication**](forcereplication-dfsrconnectioninfo.md) method.

</dd> <dt>

<span id="Paused"></span><span id="paused"></span><span id="PAUSED"></span>

<span id="Paused"></span><span id="paused"></span><span id="PAUSED"></span>**Paused**


</dt> <dd>

Pause synchronization as a response to a call to [**ForceReplication**](forcereplication-dfsrconnectioninfo.md).

</dd> <dt>

<span id="ForcedUntilSync"></span><span id="forceduntilsync"></span><span id="FORCEDUNTILSYNC"></span>

<span id="ForcedUntilSync"></span><span id="forceduntilsync"></span><span id="FORCEDUNTILSYNC"></span>**ForcedUntilSync**


</dt> <dd>

Synchronization started as a response to a call to [**ForceReplication**](forcereplication-dfsrconnectioninfo.md) with a value of Sync Until-In-Sync.

</dd> </dl>

This property is valid only for inbound connections.

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates when the object was installed. Lack of a value does not indicate that the object is not installed. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

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

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Member GUID"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36)
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

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Label by which the object is known. When subclassed, this property can be overridden to be a key property. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

</dd> <dt>

**PartnerGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Partner GUID"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36)
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

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Replication Group GUID"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36)
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

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

String that indicates the current status of the object. Operational and non-operational status can be defined. Operational status can include "OK", "Degraded", and "Pred Fail". "Pred Fail" indicates that an element is functioning properly, but is predicting a failure (for example, a SMART-enabled hard disk drive).

Non-operational status can include "Error", "Starting", "Stopping", and "Service". "Service" can apply during disk mirror-resilvering, reloading a user permissions list, or other administrative work. Not all such work is online, but the managed element is neither "OK" nor in one of the other states. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

Values include the following:

<dt>

<span id="OK"></span><span id="ok"></span>

**OK** ("OK")


</dt> <dd></dd> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>

**Error** ("Error")


</dt> <dd></dd> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>

**Degraded** ("Degraded")


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** ("Unknown")


</dt> <dd></dd> <dt>

<span id="Pred_Fail"></span><span id="pred_fail"></span><span id="PRED_FAIL"></span>

**Pred Fail** ("Pred Fail")


</dt> <dd></dd> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>

**Starting** ("Starting")


</dt> <dd></dd> <dt>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>

**Stopping** ("Stopping")


</dt> <dd></dd> <dt>

<span id="Service"></span><span id="service"></span><span id="SERVICE"></span>

**Service** ("Service")


</dt> <dd></dd> <dt>

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>

**Stressed** ("Stressed")


</dt> <dd></dd> <dt>

<span id="NonRecover"></span><span id="nonrecover"></span><span id="NONRECOVER"></span>

**NonRecover** ("NonRecover")


</dt> <dd></dd> <dt>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>

**No Contact** ("No Contact")


</dt> <dd></dd> <dt>

<span id="Lost_Comm"></span><span id="lost_comm"></span><span id="LOST_COMM"></span>

**Lost Comm** ("Lost Comm")


</dt> <dd></dd> </dl>

</dd> <dt>

**SyncGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Sync GUID"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36)
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
| Minimum supported client<br/> | Windows Vista<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| End of client support<br/>    | Windows Vista<br/>                                                                 |
| Namespace<br/>                | Root\\MicrosoftDfs<br/>                                                            |
| MOF<br/>                      | <dl> <dt>DfsRProvs.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DfsRWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_LogicalElement**](https://msdn.microsoft.com/library/aa387892)
</dt> <dt>

[DFSR WMI Classes](dfsr-wmi-classes.md)
</dt> </dl>

 

 





