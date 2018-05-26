---
title: DnsServerUpdateStatistics class
description: Represents DNS server statistics related to dynamic updates processing.
audience: developer
ms.assetid: 5015e0d1-4915-46bb-922b-2af8c0f120ae
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerUpdateStatistics class
- DnsServerUpdateStatistics class, described
topic_type:
- apiref
api_name:
- DnsServerUpdateStatistics
- DnsServerUpdateStatistics.Received
- DnsServerUpdateStatistics.Empty
- DnsServerUpdateStatistics.NoOps
- DnsServerUpdateStatistics.Completed
- DnsServerUpdateStatistics.Rejected
- DnsServerUpdateStatistics.FormError
- DnsServerUpdateStatistics.NxDomain
- DnsServerUpdateStatistics.NotImplemented
- DnsServerUpdateStatistics.Refused
- DnsServerUpdateStatistics.YxDomain
- DnsServerUpdateStatistics.YxRRset
- DnsServerUpdateStatistics.NxRRset
- DnsServerUpdateStatistics.NotAuthoritative
- DnsServerUpdateStatistics.NotZone
- DnsServerUpdateStatistics.RefusedNonSecure
- DnsServerUpdateStatistics.RefusedAccessDenied
- DnsServerUpdateStatistics.SecureSuccess
- DnsServerUpdateStatistics.SecureFailure
- DnsServerUpdateStatistics.SecureDsWriteFailure
- DnsServerUpdateStatistics.DsSuccess
- DnsServerUpdateStatistics.DsWriteFailure
- DnsServerUpdateStatistics.Queued
- DnsServerUpdateStatistics.Timeout
- DnsServerUpdateStatistics.InQueue
- DnsServerUpdateStatistics.Forwards
- DnsServerUpdateStatistics.TcpForwards
- DnsServerUpdateStatistics.ForwardResponses
- DnsServerUpdateStatistics.ForwardTimeouts
- DnsServerUpdateStatistics.ForwardInQueue
- DnsServerUpdateStatistics.UpdateType
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DnsServerUpdateStatistics class

Represents DNS server statistics related to dynamic updates processing.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerUpdateStatistics
{
  uint32                 Received;
  uint32                 Empty;
  uint32                 NoOps;
  uint32                 Completed;
  uint32                 Rejected;
  uint32                 FormError;
  uint32                 NxDomain;
  uint32                 NotImplemented;
  uint32                 Refused;
  uint32                 YxDomain;
  uint32                 YxRRset;
  uint32                 NxRRset;
  uint32                 NotAuthoritative;
  uint32                 NotZone;
  uint32                 RefusedNonSecure;
  uint32                 RefusedAccessDenied;
  uint32                 SecureSuccess;
  uint32                 SecureFailure;
  uint32                 SecureDsWriteFailure;
  uint32                 DsSuccess;
  uint32                 DsWriteFailure;
  uint32                 Queued;
  uint32                 Timeout;
  uint32                 InQueue;
  uint32                 Forwards;
  uint32                 TcpForwards;
  uint32                 ForwardResponses;
  uint32                 ForwardTimeouts;
  uint32                 ForwardInQueue;
  DnsServerRecordRequest UpdateType[];
};
```

## Members

The **DnsServerUpdateStatistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerUpdateStatistics** class has these properties.

<dl> <dt>

**Completed**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of completed dynamic update requests received by the server.

</dd> <dt>

**DsSuccess**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of unsecure dynamic update requests received by the server, that were successfully updated in the directory server.

</dd> <dt>

**DsWriteFailure**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of unsecured dynamic update requests received by the server that the server failed to update in the directory server.

</dd> <dt>

**Empty**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of empty dynamic update requests received by the server.

</dd> <dt>

**FormError**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of dynamic update requests rejected by the server, due to malformed packets.

</dd> <dt>

**ForwardInQueue**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of update packets forwarded to other servers and which are waiting for a response.

</dd> <dt>

**ForwardResponses**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of response packets received for the update requests that were forwarded to other servers.

</dd> <dt>

**Forwards**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of update packets received that were forwarded to other servers.

</dd> <dt>

**ForwardTimeouts**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of update packets which timed out waiting for a response from other servers.

</dd> <dt>

**InQueue**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of update packets received which are waiting in the update queue for updates to complete on the remote server.

</dd> <dt>

**NoOps**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of no-op dynamic update requests, such as a dynamic update request with no update records, received by the server.

</dd> <dt>

**NotAuthoritative**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of dynamic update requests rejected by the server, due to the server not being authoritative for the zone.

</dd> <dt>

**NotImplemented**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of dynamic update requests rejected by the server, due to unimplemented functionality.

</dd> <dt>

**NotZone**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of dynamic update requests rejected by the server, due to the zone name not being recognized as one for which it is authoritative

</dd> <dt>

**NxDomain**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of dynamic update requests rejected by the server, due to name error.

</dd> <dt>

**NxRRset**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of dynamic update requests rejected by the server, due to an unknown resource record name.

</dd> <dt>

**Queued**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of updates packets received that needed to be sent to other remote server.

</dd> <dt>

**Received**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of WINS lookup requests received by the server.

</dd> <dt>

**Refused**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of dynamic update requests rejected by the server, due to malformed packets.

</dd> <dt>

**RefusedAccessDenied**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of dynamic update requests rejected by the server, due to a failure to update records in the directory server.

</dd> <dt>

**RefusedNonSecure**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of dynamic update requests rejected by the server, due to a non-secure update request received for a zone where secure updates are required.

</dd> <dt>

**Rejected**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of dynamic update requests rejected by the server.

</dd> <dt>

**SecureDsWriteFailure**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of secure dynamic update requests received by the server that the server failed to update in the directory server.

</dd> <dt>

**SecureFailure**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of secure dynamic update requests received by the server that could not be successfully applied.

</dd> <dt>

**SecureSuccess**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of secure dynamic update requests received by the server that were successfully applied.

</dd> <dt>

**TcpForwards**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of update packets received over TCP that were forwarded to other servers.

</dd> <dt>

**Timeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of update packets received, that timed-out while waiting to update the remote server.

</dd> <dt>

**UpdateType**
</dt> <dd> <dl> <dt>

Data type: **DnsServerRecordRequest** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerRecordRequest**](dnsserverrecordrequest.md)")
</dt> </dl>

An array of counters that keep track of the number of update requests received for different DNS record types.

</dd> <dt>

**YxDomain**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of dynamic update requests rejected by the server, due to policy restrictions.

</dd> <dt>

**YxRRset**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of dynamic update requests rejected by the server, due to an unknown domain name.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





