---
title: MSFT\_DfsrConnectionInfo class
description: This class provides statistical and operational information for each incoming and outgoing connection of the local replication group members.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3279f9e6-482b-483c-bf02-15077c877d3b
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_DfsrConnectionInfo class Distributed File System Replication
- MSFT_DfsrConnectionInfo class Distributed File System Replication , described
topic_type:
- apiref
api_name:
- MSFT_DfsrConnectionInfo
- MSFT_DfsrConnectionInfo.ConnectionGuid
- MSFT_DfsrConnectionInfo.MemberGuid
- MSFT_DfsrConnectionInfo.MemberName
- MSFT_DfsrConnectionInfo.PartnerGuid
- MSFT_DfsrConnectionInfo.PartnerName
- MSFT_DfsrConnectionInfo.ReplicationGroupGuid
- MSFT_DfsrConnectionInfo.ReplicationGroupName
- MSFT_DfsrConnectionInfo.Inbound
- MSFT_DfsrConnectionInfo.State
- MSFT_DfsrConnectionInfo.LastSyncTime
- MSFT_DfsrConnectionInfo.LastSyncDuration
- MSFT_DfsrConnectionInfo.LastSuccessfulSyncTime
- MSFT_DfsrConnectionInfo.NextSyncTime
- MSFT_DfsrConnectionInfo.LastErrorCode
- MSFT_DfsrConnectionInfo.LastErrorMessageId
api_location:
- DfsRWmiV2.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_DfsrConnectionInfo class

This class provides statistical and operational information for each incoming and outgoing connection of the local replication group members.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DfsrWMIV2"), AMENDMENT]
class MSFT_DfsrConnectionInfo
{
  string   ConnectionGuid;
  string   MemberGuid;
  string   MemberName;
  string   PartnerGuid;
  string   PartnerName;
  string   ReplicationGroupGuid;
  string   ReplicationGroupName;
  boolean  Inbound;
  uint32   State;
  datetime LastSyncTime;
  uint32   LastSyncDuration;
  datetime LastSuccessfulSyncTime;
  datetime NextSyncTime;
  uint32   LastErrorCode;
  uint32   LastErrorMessageId;
};
```

## Members

The **MSFT\_DfsrConnectionInfo** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_DfsrConnectionInfo** class has these methods.



| Method                                                                           | Description                                                                                                                                                                              |
|:---------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CheckConnectivity**](checkconnectivity-msft-dfsrconnectioninfo.md)           | Checks connectivity with the partner's computer.<br/>                                                                                                                              |
| [**ForceDownload**](forcedownload-msft-dfsrconnectioninfo.md)                   | Forces a download of a specified resource.<br/>                                                                                                                                    |
| [**ForceFolderReplication**](forcefolderreplication-msft-dfsrconnectioninfo.md) | Controls replication by forcing a designated folder to replicate. After the duration expires, the DFS Replication service will revert to the configured replication schedule.<br/> |
| [**ForceReplication**](forcereplication-msft-dfsrconnectioninfo.md)             | Controls replication by either forcing or suspending replication. DFSR will revert to the normal schedule at the end of the specified duration.<br/>                               |



 

### Properties

The **MSFT\_DfsrConnectionInfo** class has these properties.

<dl> <dt>

**ConnectionGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Connection GUID")
</dt> </dl>

The unique connection identifier.

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

<span id="DFSR_E_CANNOT_CONNECT"></span><span id="dfsr_e_cannot_connect"></span>**DFSR\_E\_CANNOT\_CONNECT** (0)


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

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Seconds"), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Last Sync Duration In Seconds")
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

</dd> </dl>

## Remarks

Outbound connections are created on demand after the partner establishes a connection. The DFSR service cannot detect when an outbound connection has been deleted; by default, it waits for 12 hours idle time before determining that the connection has been lost.

Inbound connections persist as long as they are configured.

The following state diagram illustrates the transitions between the connection states.

![dfsr connection state diagram](images/connection-state.png)

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

 

 





