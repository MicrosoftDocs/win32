---
title: DnsServerQueryStatistics class
description: Represents query statistics for a DNS server.
audience: developer
ms.assetid: '28cc15da-45d4-46cc-beed-db6d4f8f2828'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DnsServerQueryStatistics class", "DnsServerQueryStatistics class, described"]
topic_type:
- apiref
api_name:
- DnsServerQueryStatistics
- DnsServerQueryStatistics.UdpQueries
- DnsServerQueryStatistics.UdpResponses
- DnsServerQueryStatistics.UdpQueriesSent
- DnsServerQueryStatistics.UdpResponsesReceived
- DnsServerQueryStatistics.TcpClientConnections
- DnsServerQueryStatistics.TcpQueries
- DnsServerQueryStatistics.TcpResponses
- DnsServerQueryStatistics.TcpQueriesSent
- DnsServerQueryStatistics.TcpResponsesReceived
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# DnsServerQueryStatistics class

Represents query statistics for a DNS server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerQueryStatistics
{
  uint32 UdpQueries;
  uint32 UdpResponses;
  uint32 UdpQueriesSent;
  uint32 UdpResponsesReceived;
  uint32 TcpClientConnections;
  uint32 TcpQueries;
  uint32 TcpResponses;
  uint32 TcpQueriesSent;
  uint32 TcpResponsesReceived;
};
```

## Members

The **DnsServerQueryStatistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerQueryStatistics** class has these properties.

<dl> <dt>

**TcpClientConnections**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of TCP connections accepted by the server.

</dd> <dt>

**TcpQueries**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of queries received over TCP.

</dd> <dt>

**TcpQueriesSent**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of queries sent over TCP by the server to remote servers.

</dd> <dt>

**TcpResponses**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of query responses sent over TCP.

</dd> <dt>

**TcpResponsesReceived**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of query responses over TCP that were received by the server.

</dd> <dt>

**UdpQueries**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of queries received over UDP.

</dd> <dt>

**UdpQueriesSent**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of queries sent over UDP by the server to remote servers.

</dd> <dt>

**UdpResponses**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of query responses sent over UDP.

</dd> <dt>

**UdpResponsesReceived**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of query responses received over UDP by the server.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





