---
title: DnsServerSecondaryStatistics class
description: Represents DNS server statistics for secondary zone processing.
audience: developer
ms.assetid: d940d185-186e-4a11-8baf-6d98996d8f18
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerSecondaryStatistics class
- DnsServerSecondaryStatistics class, described
topic_type:
- apiref
api_name:
- DnsServerSecondaryStatistics
- DnsServerSecondaryStatistics.NotifyReceived
- DnsServerSecondaryStatistics.NotifyInvalid
- DnsServerSecondaryStatistics.NotifyPrimary
- DnsServerSecondaryStatistics.NotifyNonPrimary
- DnsServerSecondaryStatistics.NotifyNoVersion
- DnsServerSecondaryStatistics.NotifyNewVersion
- DnsServerSecondaryStatistics.NotifyCurrentVersion
- DnsServerSecondaryStatistics.NotifyOldVersion
- DnsServerSecondaryStatistics.NotifyMasterUnknown
- DnsServerSecondaryStatistics.SoaRequest
- DnsServerSecondaryStatistics.SoaResponse
- DnsServerSecondaryStatistics.SoaResponseInvalid
- DnsServerSecondaryStatistics.AxfrRequest
- DnsServerSecondaryStatistics.AxfrResponse
- DnsServerSecondaryStatistics.AxfrSuccess
- DnsServerSecondaryStatistics.AxfrRefused
- DnsServerSecondaryStatistics.AxfrInvalid
- DnsServerSecondaryStatistics.StubAxfrRequest
- DnsServerSecondaryStatistics.StubAxfrResponse
- DnsServerSecondaryStatistics.StubAxfrSuccess
- DnsServerSecondaryStatistics.StubAxfrRefused
- DnsServerSecondaryStatistics.StubAxfrInvalid
- DnsServerSecondaryStatistics.IxfrUdpRequest
- DnsServerSecondaryStatistics.IxfrUdpResponse
- DnsServerSecondaryStatistics.IxfrUdpSuccess
- DnsServerSecondaryStatistics.IxfrUdpUseTcp
- DnsServerSecondaryStatistics.IxfrUdpUseAxfr
- DnsServerSecondaryStatistics.IxfrUdpWrongServer
- DnsServerSecondaryStatistics.IxfrUdpNoUpdate
- DnsServerSecondaryStatistics.IxfrUdpNewPrimary
- DnsServerSecondaryStatistics.IxfrUdpFormError
- DnsServerSecondaryStatistics.IxfrUdpRefused
- DnsServerSecondaryStatistics.IxfrUdpInvalid
- DnsServerSecondaryStatistics.IxfrTcpRequest
- DnsServerSecondaryStatistics.IxfrTcpResponse
- DnsServerSecondaryStatistics.IxfrTcpSuccess
- DnsServerSecondaryStatistics.IxfrTcpAxfr
- DnsServerSecondaryStatistics.IxfrTcpFormError
- DnsServerSecondaryStatistics.IxfrTcpRefused
- DnsServerSecondaryStatistics.IxfrTcpInvalid
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DnsServerSecondaryStatistics class

Represents DNS server statistics for secondary zone processing.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerSecondaryStatistics
{
  uint32 NotifyReceived;
  uint32 NotifyInvalid;
  uint32 NotifyPrimary;
  uint32 NotifyNonPrimary;
  uint32 NotifyNoVersion;
  uint32 NotifyNewVersion;
  uint32 NotifyCurrentVersion;
  uint32 NotifyOldVersion;
  uint32 NotifyMasterUnknown;
  uint32 SoaRequest;
  uint32 SoaResponse;
  uint32 SoaResponseInvalid;
  uint32 AxfrRequest;
  uint32 AxfrResponse;
  uint32 AxfrSuccess;
  uint32 AxfrRefused;
  uint32 AxfrInvalid;
  uint32 StubAxfrRequest;
  uint32 StubAxfrResponse;
  uint32 StubAxfrSuccess;
  uint32 StubAxfrRefused;
  uint32 StubAxfrInvalid;
  uint32 IxfrUdpRequest;
  uint32 IxfrUdpResponse;
  uint32 IxfrUdpSuccess;
  uint32 IxfrUdpUseTcp;
  uint32 IxfrUdpUseAxfr;
  uint32 IxfrUdpWrongServer;
  uint32 IxfrUdpNoUpdate;
  uint32 IxfrUdpNewPrimary;
  uint32 IxfrUdpFormError;
  uint32 IxfrUdpRefused;
  uint32 IxfrUdpInvalid;
  uint32 IxfrTcpRequest;
  uint32 IxfrTcpResponse;
  uint32 IxfrTcpSuccess;
  uint32 IxfrTcpAxfr;
  uint32 IxfrTcpFormError;
  uint32 IxfrTcpRefused;
  uint32 IxfrTcpInvalid;
};
```

## Members

The **DnsServerSecondaryStatistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerSecondaryStatistics** class has these properties.

<dl> <dt>

**AxfrInvalid**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of full zone transfer invalid responses received by the server.

</dd> <dt>

**AxfrRefused**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of full zone transfer rejection responses received by the server.

</dd> <dt>

**AxfrRequest**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of full zone transfer requests sent by the server.

</dd> <dt>

**AxfrResponse**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of full zone transfer responses received by the server.

</dd> <dt>

**AxfrSuccess**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of full zone transfer success responses received by the server.

</dd> <dt>

**IxfrTcpAxfr**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of incremental zone transfer responses received by the server over TCP, indicating that full zone transfer is needed.

</dd> <dt>

**IxfrTcpFormError**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of incremental zone transfer responses received by the server over TCP, where either the primary DNS server does not support incremental zone transfer or the primary DNS server indicated that the zone transfer request was malformed.

</dd> <dt>

**IxfrTcpInvalid**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of incremental zone transfer invalid responses received by the server over TCP.

</dd> <dt>

**IxfrTcpRefused**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of incremental zone transfer rejection responses received by the server over TCP.

</dd> <dt>

**IxfrTcpRequest**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of incremental zone transfer requests sent by the server over TCP.

</dd> <dt>

**IxfrTcpResponse**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of incremental zone transfer success responses received by the server over TCP.

</dd> <dt>

**IxfrTcpSuccess**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of incremental zone transfer success responses received by the server over TCP.

</dd> <dt>

**IxfrUdpFormError**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of incremental zone transfer responses received by the server over UDP, where either the master does not support incremental zone transfer or the master indicated that the zone transfer request was malformed.

</dd> <dt>

**IxfrUdpInvalid**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of incremental zone transfer invalid responses received by the server over UDP.

</dd> <dt>

**IxfrUdpNewPrimary**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of incremental zone transfer responses received by the server over UDP, where the SOA indicates a new primary server name.

</dd> <dt>

**IxfrUdpNoUpdate**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of incremental zone transfer responses received by the server over UDP, where no updates were found and hence no zone transfer is needed.

</dd> <dt>

**IxfrUdpRefused**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of incremental zone transfer rejection responses received by the server over UDP.

</dd> <dt>

**IxfrUdpRequest**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of incremental zone transfer requests sent by the server over UDP.

</dd> <dt>

**IxfrUdpResponse**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of incremental zone transfer success responses received by the server over UDP.

</dd> <dt>

**IxfrUdpSuccess**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of incremental zone transfer success responses received by the server over UDP.

</dd> <dt>

**IxfrUdpUseAxfr**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of incremental zone transfer responses received by the server over UDP, indicating that full zone transfer is needed.

</dd> <dt>

**IxfrUdpUseTcp**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of incremental zone transfer responses received by the server over UDP, indicating that TCP is needed.

</dd> <dt>

**IxfrUdpWrongServer**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of incremental zone transfer responses received by the server over UDP, where the remote sender is not among the masters for this zone.

</dd> <dt>

**NotifyCurrentVersion**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of zone notifications received by the server where the received SOA has same version number as that of the SOA already present on the server.

</dd> <dt>

**NotifyInvalid**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of invalid zone notifications received by the server.

</dd> <dt>

**NotifyMasterUnknown**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of zone notifications received by the server, where notifications are received from a server that is not present in the list of masters for the zone.

</dd> <dt>

**NotifyNewVersion**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of zone notifications received by the server, where the received SOA has a newer version number than that of the SOA already present on the server.

</dd> <dt>

**NotifyNonPrimary**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of zone notifications for non-primary zones received by the server.

</dd> <dt>

**NotifyNoVersion**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of zone notifications received by the server, for which the server has no SOA.

</dd> <dt>

**NotifyOldVersion**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of zone notifications received by the server, where the received SOA has an older version number than the SOA already present on the server.

</dd> <dt>

**NotifyPrimary**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of zone notifications for primary zones received by the server.

</dd> <dt>

**NotifyReceived**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of zone notifications received by the server.

</dd> <dt>

**SoaRequest**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of SOA query requests sent by the server to zone masters, to initiate zone transfer.

</dd> <dt>

**SoaResponse**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of SOA responses received by the server from the zone master.

</dd> <dt>

**SoaResponseInvalid**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of invalid SOA responses received by the server from the zone master.

</dd> <dt>

**StubAxfrInvalid**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of full zone transfer invalid responses received by the server.

</dd> <dt>

**StubAxfrRefused**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of full zone transfer rejection responses received by the server.

</dd> <dt>

**StubAxfrRequest**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of full zone transfer requests sent by the server for stub zones.

</dd> <dt>

**StubAxfrResponse**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of full zone transfer responses received by the server for stub zones.

</dd> <dt>

**StubAxfrSuccess**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of full zone transfer success responses received by the server for stub zones.

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

 

 





