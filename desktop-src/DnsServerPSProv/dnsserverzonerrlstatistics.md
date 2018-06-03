---
title: DnsServerZoneRRLStatistics class
description: Contains the Zone response rate limiting (RRL) statistics.
audience: developer
ms.assetid: a6a622d8-11e6-4bbc-82e0-c18b765cc397
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerZoneRRLStatistics class
- DnsServerZoneRRLStatistics class, described
topic_type:
- apiref
api_name:
- DnsServerZoneRRLStatistics
- DnsServerZoneRRLStatistics.TotalResponsesSent
- DnsServerZoneRRLStatistics.TotalResponsesDropped
- DnsServerZoneRRLStatistics.TotalResponsesLeaked
- DnsServerZoneRRLStatistics.TotalResponsesTruncated
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DnsServerZoneRRLStatistics class

Contains the Zone response rate limiting (RRL) statistics.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerZoneRRLStatistics
{
  uint64 TotalResponsesSent;
  uint64 TotalResponsesDropped;
  uint64 TotalResponsesLeaked;
  uint64 TotalResponsesTruncated;
};
```

## Members

The **DnsServerZoneRRLStatistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerZoneRRLStatistics** class has these properties.

<dl> <dt>

**TotalResponsesDropped**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total number of responses dropped by the DNS server for the zone.

</dd> <dt>

**TotalResponsesLeaked**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total number of responses leaked by the DNS server for the zone.

</dd> <dt>

**TotalResponsesSent**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total number of responses sent by the DNS server for the zone.

</dd> <dt>

**TotalResponsesTruncated**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total number of responses truncated by the DNS server for the zone.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



 

 





