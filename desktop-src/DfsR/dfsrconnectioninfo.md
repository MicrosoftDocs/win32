---
title: DfsrConnectionInfo class
description: This class provides statistical and operational information for each incoming and outgoing connection of the local replication group members.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '0078773e-be4e-44a8-b856-8def753ce60b'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-file-system-replication'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DfsrConnectionInfo class Distributed File System Replication", "DfsrConnectionInfo class Distributed File System Replication , described"]
topic_type:
- apiref
api_name:
- DfsrConnectionInfo
- DfsrConnectionInfo.Caption
- DfsrConnectionInfo.Description
- DfsrConnectionInfo.InstallDate
- DfsrConnectionInfo.Name
- DfsrConnectionInfo.Status
- DfsrConnectionInfo.ConnectionGuid
- DfsrConnectionInfo.MemberGuid
- DfsrConnectionInfo.MemberName
- DfsrConnectionInfo.PartnerGuid
- DfsrConnectionInfo.PartnerName
- DfsrConnectionInfo.ReplicationGroupGuid
- DfsrConnectionInfo.ReplicationGroupName
- DfsrConnectionInfo.Inbound
- DfsrConnectionInfo.State
- DfsrConnectionInfo.LastSyncTime
- DfsrConnectionInfo.LastSyncDuration
- DfsrConnectionInfo.LastSuccessfulSyncTime
- DfsrConnectionInfo.NextSyncTime
- DfsrConnectionInfo.LastErrorCode
- DfsrConnectionInfo.LastErrorMessageId
api_location:
- DfsRWmiV2.dll
api_type:
- DllExport
---

# DfsrConnectionInfo class

This class provides statistical and operational information for each incoming and outgoing connection of the local replication group members.

## Syntax

``` syntax
[Dynamic, Provider("DfsrMonitorProv")]
class DfsrConnectionInfo : CIM_LogicalElement
{
  string       Caption;
  string       Description;
  datetime REF InstallDate;
  string       Name;
  string       Status;
  string       ConnectionGuid;
  string       MemberGuid;
  string       MemberName;
  string       PartnerGuid;
  string       PartnerName;
  string       ReplicationGroupGuid;
  string       ReplicationGroupName;
  boolean      Inbound;
  uint32       State;
  datetime     LastSyncTime;
  uint32       LastSyncDuration;
  datetime     LastSuccessfulSyncTime;
  datetime     NextSyncTime;
  uint32       LastErrorCode;
  uint32       LastErrorMessageId;
};
```

## Members

The **DfsrConnectionInfo** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **DfsrConnectionInfo** class has these methods.



| Method                                                                      | Description                                                                                                                                                                              |
|:----------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CheckConnectivity**](checkconnectivity-dfsrconnectioninfo.md)           | Checks connectivity with the partner's computer.<br/>                                                                                                                              |
| [**ForceDownload**](forcedownload-dfsrconnectioninfo.md)                   | Forces a download of a specified resource.<br/>                                                                                                                                    |
| [**ForceFolderReplication**](forcefolderreplication-dfsrconnectioninfo.md) | Controls replication by forcing a designated folder to replicate. After the duration expires, the DFS Replication service will revert to the configured replication schedule.<br/> |
| [**ForceReplication**](forcereplication-dfsrconnectioninfo.md)             | Controls replication by either forcing or suspending replication. DFSR will revert to the normal schedule at the end of the specified duration.<br/>                               |



 

### Properties

The **DfsrConnectionInfo** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxLen** (64)
</dt> </dl>

A short textual description of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

</dd> <dt>

**ConnectionGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Connection GUID"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36)
</dt> </dl>

The unique connection identifier.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

</dd> <dt>

**Inbound**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Incoming Connection")
</dt> </dl>

Indicates the direction of the connection between the local computer and this partner; it can be inbound (coming from the partner) or outbound (going to the partner).

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates when the object was installed. Lack of a value does not indicate that the object is not installed.

This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

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

For **DFSR\_E\_CANNOT\_CONNECT**, the **LastErrorMessageId** is one of the following values.

<dt>

<span id="Success"></span><span id="success"></span><span id="SUCCESS"></span>

<span id="Success"></span><span id="success"></span><span id="SUCCESS"></span>**Success** (0)


</dt> <dd></dd> <dt>

<span id="EVENT_DFSR_CONNECTION_ERROR"></span><span id="event_dfsr_connection_error"></span>

<span id="EVENT_DFSR_CONNECTION_ERROR"></span><span id="event_dfsr_connection_error"></span>**EVENT\_DFSR\_CONNECTION\_ERROR**


</dt> <dd>

The DFS Replication service encountered an error communicating with the partner. The service will retry the connection periodically.

</dd> <dt>

<span id="EVENT_DFSR_CONNECTION_SERVICE_UNREACHABLE"></span><span id="event_dfsr_connection_service_unreachable"></span>

<span id="EVENT_DFSR_CONNECTION_SERVICE_UNREACHABLE"></span><span id="event_dfsr_connection_service_unreachable"></span>**EVENT\_DFSR\_CONNECTION\_SERVICE\_UNREACHABLE**


</dt> <dd>

The DFS Replication service failed to communicate with the partner. This error can occur if the host is unreachable or if the DFS Replication service is not running on the server. The service will retry the connection periodically.

</dd> <dt>

<span id="EVENT_DFSR_CONNECTION_UNRECOGNIZED"></span><span id="event_dfsr_connection_unrecognized"></span>

<span id="EVENT_DFSR_CONNECTION_UNRECOGNIZED"></span><span id="event_dfsr_connection_unrecognized"></span>**EVENT\_DFSR\_CONNECTION\_UNRECOGNIZED**


</dt> <dd>

The DFS Replication service failed to communicate with the partner. The partner did not recognize the connection or the replication group configuration. The service will retry the connection periodically.

</dd> <dt>

<span id="EVENT_DFSR_INCOMPATIBLE_VERSION"></span><span id="event_dfsr_incompatible_version"></span>

<span id="EVENT_DFSR_INCOMPATIBLE_VERSION"></span><span id="event_dfsr_incompatible_version"></span>**EVENT\_DFSR\_INCOMPATIBLE\_VERSION**


</dt> <dd>

The DFS Replication service failed to communicate with the partner. The partner is running a different version of the communication protocol. This error can be avoided by ensuring that the correct version of DFS Replication is installed on both servers, including any service packs and downloads.

</dd> </dl>

</dd> <dt>

**LastSuccessfulSyncTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Last Successful Sync Time")
</dt> </dl>

The time stamp of the last successful synchronization session since the service was started. The default value is 1/1/9999.

This property is valid only for inbound connections.

</dd> <dt>

**LastSyncDuration**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Last Sync Duration In Seconds"), [**Units**](https://msdn.microsoft.com/library/aa393650) ("Seconds")
</dt> </dl>

The duration of the last successful synchronization session, in seconds. The default value is 0.

This property is valid only for inbound connections.

</dd> <dt>

**LastSyncTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Last Sync Time")
</dt> </dl>

The time stamp of the last attempted synchronization operation. The default is 1/1/9999.

This property is valid only for inbound connections.

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

**NextSyncTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Next Sync Time")
</dt> </dl>

The time stamp of next scheduled synchronization session. The default value is 1/1/9999.

This property is valid only for inbound connections.

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

The name of the replication group that owns this connection.

</dd> <dt>

**State**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Connection State")
</dt> </dl>

The current connection state.

<dt>

<span id="Connecting"></span><span id="connecting"></span><span id="CONNECTING"></span>

**Connecting** (0)


</dt> <dd></dd> <dt>

<span id="Online"></span><span id="online"></span><span id="ONLINE"></span>

**Online** (1)


</dt> <dd></dd> <dt>

<span id="Offline"></span><span id="offline"></span><span id="OFFLINE"></span>

**Offline** (2)


</dt> <dd></dd> <dt>

<span id="In_Error"></span><span id="in_error"></span><span id="IN_ERROR"></span>

**In Error** (3)


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

</dd> </dl>

## Remarks

Outbound connections are created on demand after the partner establishes a connection. The DFSR service cannot detect when an outbound connection has been deleted; by default, it waits for 12 hours idle time before determining that the connection has been lost.

Inbound connections persist as long as they are configured.

The following state diagram illustrates the transitions between the connection states.

![dfsr connection state diagram](images/connection-state.png)

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| End of client support<br/>    | Windows Vista<br/>                                                                 |
| Namespace<br/>                | Root\\MicrosoftDfs<br/>                                                            |
| MOF<br/>                      | <dl> <dt>DfsRProvs.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DfsRWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_LogicalElement**](https://msdn.microsoft.com/library/aa387892)
</dt> <dt>

[DFSR WMI Classes](dfsr-wmi-classes.md)
</dt> </dl>

 

 





