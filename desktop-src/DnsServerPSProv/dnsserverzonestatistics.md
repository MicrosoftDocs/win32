---
title: DnsServerZoneStatistics class
description: Represents statistics for the specified zone on a DNS server.
audience: developer
ms.assetid: 'b000bd3c-b919-4c4c-abd1-3e1b7974125d'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DnsServerZoneStatistics class", "DnsServerZoneStatistics class, described"]
topic_type:
- apiref
api_name:
- DnsServerZoneStatistics
- DnsServerZoneStatistics.Name
- DnsServerZoneStatistics.StatsCollectionStartTime
- DnsServerZoneStatistics.ZoneQueryStatistics
- DnsServerZoneStatistics.ZoneTransferStatistics
- DnsServerZoneStatistics.ZoneUpdateStatistics
- DnsServerZoneStatistics.ZoneRRLStatistics
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# DnsServerZoneStatistics class

Represents statistics for the specified zone on a DNS server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerZoneStatistics
{
  string                          Name;
  datetime                        StatsCollectionStartTime;
  DnsServerZoneQueryStatistics    ZoneQueryStatistics[];
  DnsServerZoneTransferStatistics ZoneTransferStatistics[];
  DnsServerZoneUpdateStatistics   ZoneUpdateStatistics;
  DnsServerZoneRRLStatistics      ZoneRRLStatistics;
};
```

## Members

The **DnsServerZoneStatistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerZoneStatistics** class has these properties.

<dl> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the zone.

</dd> <dt>

**StatsCollectionStartTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time when collection of the statistics began.

</dd> <dt>

**ZoneQueryStatistics**
</dt> <dd> <dl> <dt>

Data type: **DnsServerZoneQueryStatistics** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerZoneQueryStatistics**](dnsserverzonequerystatistics.md)")
</dt> </dl>

An array that contains the query statistics for record types.

</dd> <dt>

**ZoneRRLStatistics**
</dt> <dd> <dl> <dt>

Data type: **DnsServerZoneRRLStatistics**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerZoneRRLStatistics**](dnsserverzonerrlstatistics.md)")
</dt> </dl>

A [**DnsServerZoneRRLStatistics**](dnsserverzonerrlstatistics.md) that contains the statistics for response rate limiting.

**Windows Server 2012 R2:** This property is supported beginning with Windows Server 2016.

</dd> <dt>

**ZoneTransferStatistics**
</dt> <dd> <dl> <dt>

Data type: **DnsServerZoneTransferStatistics** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerZoneTransferStatistics**](dnsserverzonetransferstatistics.md)")
</dt> </dl>

Array that contains transfer statistics for transfer types.

</dd> <dt>

**ZoneUpdateStatistics**
</dt> <dd> <dl> <dt>

Data type: **DnsServerZoneUpdateStatistics**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerZoneUpdateStatistics**](dnsserverzoneupdatestatistics.md)")
</dt> </dl>

The object that contains statistics for dynamic updates in the zone.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





