---
title: DnsServerPacketStatistics class
description: Represents DNS server statistics related to packets usage.
audience: developer
ms.assetid: c57afb37-97af-4b5a-8e8e-11a31ada9bf1
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerPacketStatistics class
- DnsServerPacketStatistics class, described
topic_type:
- apiref
api_name:
- DnsServerPacketStatistics
- DnsServerPacketStatistics.UdpAlloc
- DnsServerPacketStatistics.UdpFree
- DnsServerPacketStatistics.UdpNetAllocs
- DnsServerPacketStatistics.UdpMemory
- DnsServerPacketStatistics.UdpUsed
- DnsServerPacketStatistics.UdpReturn
- DnsServerPacketStatistics.UdpResponseReturn
- DnsServerPacketStatistics.UdpQueryReturn
- DnsServerPacketStatistics.UdpInUse
- DnsServerPacketStatistics.UdpInFreeList
- DnsServerPacketStatistics.TcpAlloc
- DnsServerPacketStatistics.TcpFree
- DnsServerPacketStatistics.TcpNetAllocs
- DnsServerPacketStatistics.TcpMemory
- DnsServerPacketStatistics.RecursePacketUsed
- DnsServerPacketStatistics.RecursePacketReturn
- DnsServerPacketStatistics.PacketsForNsListUsed
- DnsServerPacketStatistics.PacketsForNsListReturned
- DnsServerPacketStatistics.PacketsForNsListInUse
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DnsServerPacketStatistics class

Represents DNS server statistics related to packets usage.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerPacketStatistics
{
  uint32 UdpAlloc;
  uint32 UdpFree;
  uint32 UdpNetAllocs;
  uint32 UdpMemory;
  uint32 UdpUsed;
  uint32 UdpReturn;
  uint32 UdpResponseReturn;
  uint32 UdpQueryReturn;
  uint32 UdpInUse;
  uint32 UdpInFreeList;
  uint32 TcpAlloc;
  uint32 TcpFree;
  uint32 TcpNetAllocs;
  uint32 TcpMemory;
  uint32 RecursePacketUsed;
  uint32 RecursePacketReturn;
  uint32 PacketsForNsListUsed;
  uint32 PacketsForNsListReturned;
  uint32 PacketsForNsListInUse;
};
```

## Members

The **DnsServerPacketStatistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerPacketStatistics** class has these properties.

<dl> <dt>

**PacketsForNsListInUse**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of TCP buffers that are currently being used by the server for name lists in query messages.

</dd> <dt>

**PacketsForNsListReturned**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total number of TCP buffers that were used for name server lists in query messages that were returned by the server to the pool of packets.

</dd> <dt>

**PacketsForNsListUsed**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total number of TCP buffers used by the server for name server list query messages.

</dd> <dt>

**RecursePacketReturn**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The cumulative number of packets that were used for recursive queries and then returned by the server to the pool of packets.

</dd> <dt>

**RecursePacketUsed**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The cumulative number of packets used by the server for recursion queries.

</dd> <dt>

**TcpAlloc**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The cumulative number of TCP buffers allocated by the server from system memory.

</dd> <dt>

**TcpFree**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The cumulative number of TCP buffers returned by the server to system memory.

</dd> <dt>

**TcpMemory**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total system memory, in bytes, used by TCP buffers that are currently allocated by the server.

</dd> <dt>

**TcpNetAllocs**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of allocated TCP buffers that are currently allocated by the server.

</dd> <dt>

**UdpAlloc**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The cumulative number of UDP packets allocated by the server from system memory.

</dd> <dt>

**UdpFree**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The cumulative number of UDP packets returned by the server to system memory.

</dd> <dt>

**UdpInFreeList**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of UDP packets currently on the server's free list.

</dd> <dt>

**UdpInUse**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of UDP packets currently in use to process queries.

</dd> <dt>

**UdpMemory**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total size of allocated UDP packets, in bytes.

</dd> <dt>

**UdpNetAllocs**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of currently allocated UDP packets.

</dd> <dt>

**UdpQueryReturn**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of UDP query packets that were freed or returned to the free list.

</dd> <dt>

**UdpResponseReturn**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of UDP response packets that were freed or returned to the free list.

</dd> <dt>

**UdpReturn**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The cumulative number of UDP packets freed or returned to the free list by the server.

</dd> <dt>

**UdpUsed**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of UDP packets from the pool of packets used by the server.

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

 

 





