---
title: DnsServerStatistics class
description: Retrieves DNS server statistics.
audience: developer
ms.assetid: 'd256df31-22cd-4935-8722-9b5df5cf026b'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DnsServerStatistics class", "DnsServerStatistics class, described"]
topic_type:
- apiref
api_name:
- DnsServerStatistics
- DnsServerStatistics.TimeStatistics
- DnsServerStatistics.QueryStatistics
- DnsServerStatistics.Query2Statistics
- DnsServerStatistics.RecursionStatistics
- DnsServerStatistics.DnssecStatistics
- DnsServerStatistics.MasterStatistics
- DnsServerStatistics.SecondaryStatistics
- DnsServerStatistics.WinsStatistics
- DnsServerStatistics.UpdateStatistics
- DnsServerStatistics.SecurityStatistics
- DnsServerStatistics.DsStatistics
- DnsServerStatistics.MemoryStatistics
- DnsServerStatistics.TimeoutStatistics
- DnsServerStatistics.DatabaseStatistics
- DnsServerStatistics.RecordStatistics
- DnsServerStatistics.PacketStatistics
- DnsServerStatistics.NetBiosStatistics
- DnsServerStatistics.PrivateStatistics
- DnsServerStatistics.ErrorStatistics
- DnsServerStatistics.CacheStatistics
- DnsServerStatistics.RRLStatistics
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# DnsServerStatistics class

Retrieves DNS server statistics.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerStatistics
{
  DnsServerTimeStatistics      TimeStatistics;
  DnsServerQueryStatistics     QueryStatistics;
  DnsServerQuery2Statistics    Query2Statistics;
  DnsServerRecursionStatistics RecursionStatistics;
  DnsServerDnssecStatistics    DnssecStatistics;
  DnsServerMasterStatistics    MasterStatistics;
  DnsServerSecondaryStatistics SecondaryStatistics;
  DnsServerWinsStatistics      WinsStatistics;
  DnsServerUpdateStatistics    UpdateStatistics;
  DnsServerSecurityStatistics  SecurityStatistics;
  DnsServerDsStatistics        DsStatistics;
  DnsServerMemoryStatistics    MemoryStatistics;
  DnsServerTimeoutStatistics   TimeoutStatistics;
  DnsServerDatabaseStatistics  DatabaseStatistics;
  DnsServerRecordStatistics    RecordStatistics;
  DnsServerPacketStatistics    PacketStatistics;
  DnsServerNetBiosStatistics   NetBiosStatistics;
  DnsServerPrivateStatistics   PrivateStatistics;
  DnsServerErrorStatistics     ErrorStatistics;
  DnsServerCacheStatistics     CacheStatistics;
  DnsServerRRLStatistics       RRLStatistics;
};
```

## Members

The **DnsServerStatistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerStatistics** class has these properties.

<dl> <dt>

**CacheStatistics**
</dt> <dd> <dl> <dt>

Data type: **DnsServerCacheStatistics**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerCacheStatistics**](dnsservercachestatistics.md)")
</dt> </dl>

The server cache statistics for the DNS server.

</dd> <dt>

**DatabaseStatistics**
</dt> <dd> <dl> <dt>

Data type: **DnsServerDatabaseStatistics**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerDatabaseStatistics**](dnsserverdatabasestatistics.md)")
</dt> </dl>

DNS server statistics related to the database tree.

</dd> <dt>

**DnssecStatistics**
</dt> <dd> <dl> <dt>

Data type: **DnsServerDnssecStatistics**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerDnssecStatistics**](dnsserverdnssecstatistics.md)")
</dt> </dl>

The DNSSEC statistics for the DNS server.

</dd> <dt>

**DsStatistics**
</dt> <dd> <dl> <dt>

Data type: **DnsServerDsStatistics**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerDsStatistics**](dnsserverdsstatistics.md)")
</dt> </dl>

DNS server statistics related to directory server processing.

</dd> <dt>

**ErrorStatistics**
</dt> <dd> <dl> <dt>

Data type: **DnsServerErrorStatistics**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerErrorStatistics**](dnsservererrorstatistics.md)")
</dt> </dl>

DNS server statistics related to the different types of errors returned by the server.

</dd> <dt>

**MasterStatistics**
</dt> <dd> <dl> <dt>

Data type: **DnsServerMasterStatistics**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerMasterStatistics**](dnsservermasterstatistics.md)")
</dt> </dl>

The DNS protocol processing statistics for the DNS server.

</dd> <dt>

**MemoryStatistics**
</dt> <dd> <dl> <dt>

Data type: **DnsServerMemoryStatistics**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerMemoryStatistics**](dnsservermemorystatistics.md)")
</dt> </dl>

DNS server statistics related to memory usage for different operations on the server.

</dd> <dt>

**NetBiosStatistics**
</dt> <dd> <dl> <dt>

Data type: **DnsServerNetBiosStatistics**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerNetBiosStatistics**](dnsservernetbiosstatistics.md)")
</dt> </dl>

DNS server statistics related to NBSTAT buffers usage.

</dd> <dt>

**PacketStatistics**
</dt> <dd> <dl> <dt>

Data type: **DnsServerPacketStatistics**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerPacketStatistics**](dnsserverpacketstatistics.md)")
</dt> </dl>

DNS server statistics related to packets usage.

</dd> <dt>

**PrivateStatistics**
</dt> <dd> <dl> <dt>

Data type: **DnsServerPrivateStatistics**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerPrivateStatistics**](dnsserverprivatestatistics.md)")
</dt> </dl>

DNS server statistics related to internal server processing.

</dd> <dt>

**Query2Statistics**
</dt> <dd> <dl> <dt>

Data type: **DnsServerQuery2Statistics**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerQuery2Statistics**](dnsserverquery2statistics.md)")
</dt> </dl>

The query2 statistics for the DNS server.

</dd> <dt>

**QueryStatistics**
</dt> <dd> <dl> <dt>

Data type: **DnsServerQueryStatistics**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerQueryStatistics**](dnsserverquerystatistics.md)")
</dt> </dl>

The query statistics for the DNS server.

</dd> <dt>

**RecordStatistics**
</dt> <dd> <dl> <dt>

Data type: **DnsServerRecordStatistics**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerRecordStatistics**](dnsserverrecordstatistics.md)")
</dt> </dl>

DNS server statistics related to record usage.

</dd> <dt>

**RecursionStatistics**
</dt> <dd> <dl> <dt>

Data type: **DnsServerRecursionStatistics**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerRecursionStatistics**](dnsserverrecursionstatistics.md)")
</dt> </dl>

The lookup statistics for recursive resource records.

</dd> <dt>

**RRLStatistics**
</dt> <dd> <dl> <dt>

Data type: **DnsServerRRLStatistics**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerRRLStatistics**](dnsserverrrlstatistics.md)")
</dt> </dl>

The DNS server statistics related to the server RRL.

**Windows Server 2012 R2 and Windows Server 2012:** Not supported.

</dd> <dt>

**SecondaryStatistics**
</dt> <dd> <dl> <dt>

Data type: **DnsServerSecondaryStatistics**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerSecondaryStatistics**](dnsserversecondarystatistics.md)")
</dt> </dl>

The secondary zone processing statistics for the DNS server.

</dd> <dt>

**SecurityStatistics**
</dt> <dd> <dl> <dt>

Data type: **DnsServerSecurityStatistics**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerSecurityStatistics**](dnsserversecuritystatistics.md)")
</dt> </dl>

DNS server statistics related to security context processing.

</dd> <dt>

**TimeoutStatistics**
</dt> <dd> <dl> <dt>

Data type: **DnsServerTimeoutStatistics**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerTimeoutStatistics**](dnsservertimeoutstatistics.md)")
</dt> </dl>

DNS server statistics related to timeout operations on the server.

</dd> <dt>

**TimeStatistics**
</dt> <dd> <dl> <dt>

Data type: **DnsServerTimeStatistics**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerTimeStatistics**](dnsservertimestatistics.md)")
</dt> </dl>

The time statistics for the DNS server.

</dd> <dt>

**UpdateStatistics**
</dt> <dd> <dl> <dt>

Data type: **DnsServerUpdateStatistics**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerUpdateStatistics**](dnsserverupdatestatistics.md)")
</dt> </dl>

The dynamic update protocol statistics for the DNS server.

</dd> <dt>

**WinsStatistics**
</dt> <dd> <dl> <dt>

Data type: **DnsServerWinsStatistics**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerWinsStatistics**](dnsserverwinsstatistics.md)")
</dt> </dl>

The WINS statistics for the DNS server.

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

 

 





