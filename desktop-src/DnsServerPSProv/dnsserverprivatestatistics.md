---
title: DnsServerPrivateStatistics class
description: Represents DNS server statistics related to internal server processing.
audience: developer
ms.assetid: c26d96aa-e8cb-4649-8b4e-3e410bd83c2b
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerPrivateStatistics class
- DnsServerPrivateStatistics class, described
topic_type:
- apiref
api_name:
- DnsServerPrivateStatistics
- DnsServerPrivateStatistics.UdpSocketPnpDelete
- DnsServerPrivateStatistics.UdpRecvFailure
- DnsServerPrivateStatistics.UdpErrorMessageSize
- DnsServerPrivateStatistics.UdpConnResets
- DnsServerPrivateStatistics.UdpConnResetRetryOverflow
- DnsServerPrivateStatistics.UdpGQCSFailure
- DnsServerPrivateStatistics.UdpGQCSFailureWithContext
- DnsServerPrivateStatistics.UdpGQCSConnReset
- DnsServerPrivateStatistics.UdpIndicateRecvFailures
- DnsServerPrivateStatistics.UdpRestartRecvOnSockets
- DnsServerPrivateStatistics.TcpConnect
- DnsServerPrivateStatistics.TcpQuery
- DnsServerPrivateStatistics.TcpDisconnect
- DnsServerPrivateStatistics.SecBigTimeSkewBypass
- DnsServerPrivateStatistics.ZoneLoadInit
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DnsServerPrivateStatistics class

Represents DNS server statistics related to internal server processing.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerPrivateStatistics
{
  uint32 UdpSocketPnpDelete;
  uint32 UdpRecvFailure;
  uint32 UdpErrorMessageSize;
  uint32 UdpConnResets;
  uint32 UdpConnResetRetryOverflow;
  uint32 UdpGQCSFailure;
  uint32 UdpGQCSFailureWithContext;
  uint32 UdpGQCSConnReset;
  uint32 UdpIndicateRecvFailures;
  uint32 UdpRestartRecvOnSockets;
  uint32 TcpConnect;
  uint32 TcpQuery;
  uint32 TcpDisconnect;
  uint32 SecBigTimeSkewBypass;
  uint32 ZoneLoadInit;
};
```

## Members

The **DnsServerPrivateStatistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerPrivateStatistics** class has these properties.

<dl> <dt>

**SecBigTimeSkewBypass**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server received a TKEY that had a time-skew within the allowable range of 1 day.

</dd> <dt>

**TcpConnect**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server was able to successfully establish a TCP connection to a remote server.

</dd> <dt>

**TcpDisconnect**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server disconnected a TCP connection.

</dd> <dt>

**TcpQuery**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server sent a recursive query over a TCP connection.

</dd> <dt>

**UdpConnResetRetryOverflow**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server received a connection reset error from UDP and could not clear the error by resubmitting the operation.

</dd> <dt>

**UdpConnResets**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server received a connection reset error from UDP.

</dd> <dt>

**UdpErrorMessageSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server received an error from a UDP socket due to the large size of the receive packet.

</dd> <dt>

**UdpGQCSConnReset**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server received an error from UDP indicating that a remote address was unreachable.

</dd> <dt>

**UdpGQCSFailure**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server received an error from UDP.

</dd> <dt>

**UdpGQCSFailureWithContext**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server received an error from UDP where no internal state for the operation was available.

</dd> <dt>

**UdpIndicateRecvFailures**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server received a critical error while attempting to perform a UDP receive operation.

</dd> <dt>

**UdpRecvFailure**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server failed to receive a UDP packet.

</dd> <dt>

**UdpRestartRecvOnSockets**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server attempted to restart receive operations on its UDP sockets due to UDP errors.

</dd> <dt>

**UdpSocketPnpDelete**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of UDP sockets that have been closed and had their locally allocated state freed by the server because a UDP error occurred, or because the socket was closed in response to an IP address change on the local machine.

</dd> <dt>

**ZoneLoadInit**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server prepared to load or reload a zone from persistent storage or from a zone transfer.

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

 

 





