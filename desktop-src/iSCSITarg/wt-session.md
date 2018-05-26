---
title: WT\_Session class
description: Represents a session from the initiator to the target.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 65daf76a-43fe-45ea-ae05-edc745c9443a
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- WT_Session class iSCSI Software Target API
- WT_Session class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- WT_Session
- WT_Session.TSIH
- WT_Session.ISID
- WT_Session.SessionType
- WT_Session.HostName
- WT_Session.InitiatorIQN
- WT_Session.Connections
- WT_Session.HostTargetIQN
- WT_Session.AllowInitialR2T
- WT_Session.AllowImmediateData
- WT_Session.MaxFirstDataBurstLength
- WT_Session.MaxDataBurstLength
- WT_Session.IsDataSequenceInOrder
- WT_Session.IsDataPduInOrder
- WT_Session.MaxConnections
- WT_Session.DefaultTime2Wait
- WT_Session.DefaultTime2Retain
- WT_Session.CurrentConnections
- WT_Session.MaxOutstandingR2T
- WT_Session.ErrorRecoveryLevel
api_location:
- WtWmiProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# WT\_Session class

Represents a session from the initiator to the target.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class WT_Session
{
  uint16        TSIH;
  uint64        ISID;
  uint32        SessionType;
  string        HostName;
  string        InitiatorIQN;
  WT_Connection Connections[];
  string        HostTargetIQN;
  boolean       AllowInitialR2T;
  boolean       AllowImmediateData;
  uint32        MaxFirstDataBurstLength;
  uint32        MaxDataBurstLength;
  boolean       IsDataSequenceInOrder;
  boolean       IsDataPduInOrder;
  uint32        MaxConnections;
  uint32        DefaultTime2Wait;
  uint32        DefaultTime2Retain;
  uint32        CurrentConnections;
  uint32        MaxOutstandingR2T;
  uint32        ErrorRecoveryLevel;
};
```

## Members

The **WT\_Session** class has these types of members:

-   [Properties](#properties)

### Properties

The **WT\_Session** class has these properties.

<dl> <dt>

**AllowImmediateData**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether immediate data is allowed.

</dd> <dt>

**AllowInitialR2T**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether initial R2T is allowed.

</dd> <dt>

**Connections**
</dt> <dd> <dl> <dt>

Data type: **WT\_Connection** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

List of connections in this session. Currently, there is only one connection per session.

</dd> <dt>

**CurrentConnections**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current number of connections.

</dd> <dt>

**DefaultTime2Retain**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum time, in seconds, after an initial wait (Time2Wait), before which an active task reassignment is still possible after an unexpected connection termination or a connection reset.

</dd> <dt>

**DefaultTime2Wait**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Minimum time, in seconds, to wait before attempting an explicit or implicit logout or an active task reassignment after an unexpected connection termination or a connection reset.

</dd> <dt>

**ErrorRecoveryLevel**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Error recovery level.

</dd> <dt>

**HostName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the iSCSI target that is servicing this session. If this is a discovery session, this property contains an empty string.

</dd> <dt>

**HostTargetIQN**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The iSCSI Qualified Name of the iSCSI target that is servicing this session.

</dd> <dt>

**InitiatorIQN**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The initiator iSCSI Qualified Name.

</dd> <dt>

**IsDataPduInOrder**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether data PDUs within sequences must be at continuously increasing addresses.

</dd> <dt>

**IsDataSequenceInOrder**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

</dd> <dt>

**ISID**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Initiator session identifier.

</dd> <dt>

**MaxConnections**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum number of connections allowed within the session.

</dd> <dt>

**MaxDataBurstLength**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum SCSI data payload in bytes in a Data-In or a solicited Data-Out iSCSI sequence.

</dd> <dt>

**MaxFirstDataBurstLength**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum amount of unsolicited data, in bytes, that an initiator may send during the execution of a single SCSI command.

</dd> <dt>

**MaxOutstandingR2T**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum number of outstanding R2T requests that are supported.

</dd> <dt>

**SessionType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Values** (Discovery, Normal), **ValueMap** (0, 1)
</dt> </dl>

The type of session.

</dd> <dt>

**TSIH**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

Unique target identifier of the session.

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\Wmi<br/>                                                                         |
| MOF<br/>                      | <dl> <dt>WmiWtProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WtWmiProv.dll</dt> </dl>     |



 

 





