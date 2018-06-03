---
title: DnsServerMasterStatistics class
description: Represents DNS server statistics related to overall DNS protocol processing.
audience: developer
ms.assetid: 5f1911a8-2c97-4ede-a303-ed5f08d34be2
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerMasterStatistics class
- DnsServerMasterStatistics class, described
topic_type:
- apiref
api_name:
- DnsServerMasterStatistics
- DnsServerMasterStatistics.NotifySent
- DnsServerMasterStatistics.Request
- DnsServerMasterStatistics.NameError
- DnsServerMasterStatistics.FormError
- DnsServerMasterStatistics.AxfrLimit
- DnsServerMasterStatistics.Refused
- DnsServerMasterStatistics.RefuseSecurity
- DnsServerMasterStatistics.RefuseShutdown
- DnsServerMasterStatistics.RefuseLoading
- DnsServerMasterStatistics.RefuseZoneLocked
- DnsServerMasterStatistics.RefuseServerFailure
- DnsServerMasterStatistics.RefuseNotAuth
- DnsServerMasterStatistics.RefuseReadOnly
- DnsServerMasterStatistics.Failure
- DnsServerMasterStatistics.AxfrRequest
- DnsServerMasterStatistics.AxfrSuccess
- DnsServerMasterStatistics.StubAxfrRequest
- DnsServerMasterStatistics.IxfrRequest
- DnsServerMasterStatistics.IxfrNoVersion
- DnsServerMasterStatistics.IxfrUpdateSuccess
- DnsServerMasterStatistics.IxfrTcpRequest
- DnsServerMasterStatistics.IxfrTcpSuccess
- DnsServerMasterStatistics.IxfrAxfr
- DnsServerMasterStatistics.IxfrUdpRequest
- DnsServerMasterStatistics.IxfrUdpSuccess
- DnsServerMasterStatistics.IxfrUdpForceTcp
- DnsServerMasterStatistics.IxfrUdpForceAxfr
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DnsServerMasterStatistics class

Represents DNS server statistics related to overall DNS protocol processing.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerMasterStatistics
{
  uint32 NotifySent;
  uint32 Request;
  uint32 NameError;
  uint32 FormError;
  uint32 AxfrLimit;
  uint32 Refused;
  uint32 RefuseSecurity;
  uint32 RefuseShutdown;
  uint32 RefuseLoading;
  uint32 RefuseZoneLocked;
  uint32 RefuseServerFailure;
  uint32 RefuseNotAuth;
  uint32 RefuseReadOnly;
  uint32 Failure;
  uint32 AxfrRequest;
  uint32 AxfrSuccess;
  uint32 StubAxfrRequest;
  uint32 IxfrRequest;
  uint32 IxfrNoVersion;
  uint32 IxfrUpdateSuccess;
  uint32 IxfrTcpRequest;
  uint32 IxfrTcpSuccess;
  uint32 IxfrAxfr;
  uint32 IxfrUdpRequest;
  uint32 IxfrUdpSuccess;
  uint32 IxfrUdpForceTcp;
  uint32 IxfrUdpForceAxfr;
};
```

## Members

The **DnsServerMasterStatistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerMasterStatistics** class has these properties.

<dl> <dt>

**AxfrLimit**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of full zone transfer requests rejected due to time restrictions between successive full zone transfers.

</dd> <dt>

**AxfrRequest**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of full zone transfer requests received by the server.

</dd> <dt>

**AxfrSuccess**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of full zone transfers successfully completed by the server.

</dd> <dt>

**Failure**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server hit a zone transfer failure.

</dd> <dt>

**FormError**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of invalid format error responses returned by the server.

</dd> <dt>

**IxfrAxfr**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of incremental zone transfer requests received by the server, which required a full zone transfer.

</dd> <dt>

**IxfrNoVersion**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of servers that received an incremental zone transfer request, but there was not a suitable version number available for incremental zone transfer.

</dd> <dt>

**IxfrRequest**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of incremental zone transfer requests received by the server.

</dd> <dt>

**IxfrTcpRequest**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of incremental zone transfer requests received by the server over TCP.

</dd> <dt>

**IxfrTcpSuccess**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of success responses for incremental zone transfers sent by the server over TCP.

</dd> <dt>

**IxfrUdpForceAxfr**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of incremental zone transfer requests received by the server over UDP, for which the server responded with a full zone transfer.

</dd> <dt>

**IxfrUdpForceTcp**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of incremental zone transfer requests received by the server over UDP, for which the server responded using TCP.

</dd> <dt>

**IxfrUdpRequest**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of incremental zone transfer requests received by the server over UDP.

</dd> <dt>

**IxfrUdpSuccess**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of success responses for incremental zone transfers sent by the server over UDP.

</dd> <dt>

**IxfrUpdateSuccess**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of success responses for incremental zone transfer sent by the server.

</dd> <dt>

**NameError**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of name error responses returned by the server.

</dd> <dt>

**NotifySent**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of update notifications sent to secondaries by the server.

</dd> <dt>

**Refused**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total number of times the server rejected requests for dynamic updates or zone transfers.

</dd> <dt>

**RefuseLoading**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server rejected zone transfer requests, due to a zone not being fully loaded.

</dd> <dt>

**RefuseNotAuth**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server rejected zone transfer requests, because the zone is not authoritative on the server.

</dd> <dt>

**RefuseReadOnly**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server rejected zone transfer requests, due to the zone being hosted on an RODC.

</dd> <dt>

**RefuseSecurity**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server rejected zone transfer requests due to secondary security restrictions.

</dd> <dt>

**RefuseServerFailure**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server rejected zone transfer requests, due to processing failures at the server.

</dd> <dt>

**RefuseShutdown**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server rejected zone transfer requests because zone transfer was disabled, or because the requesting IP address was not allowed to transfer the zone.

</dd> <dt>

**RefuseZoneLocked**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server rejected zone transfer requests, due to the zone already being locked for an operation.

</dd> <dt>

**Request**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of zone transfer requests received by the server.

</dd> <dt>

**StubAxfrRequest**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of full zone transfer requests received by the server for stub zones.

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

 

 





