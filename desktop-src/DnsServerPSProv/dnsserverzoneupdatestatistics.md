---
title: DnsServerZoneUpdateStatistics class
description: Represents the dynamic update statistics for a DNS zone.
audience: developer
ms.assetid: 8c9ff3c0-4ef0-4f31-8f00-43935ab0353d
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerZoneUpdateStatistics class
- DnsServerZoneUpdateStatistics class, described
topic_type:
- apiref
api_name:
- DnsServerZoneUpdateStatistics
- DnsServerZoneUpdateStatistics.DynamicUpdateReceived
- DnsServerZoneUpdateStatistics.DynamicUpdateRejected
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DnsServerZoneUpdateStatistics class

Represents the dynamic update statistics for a DNS zone.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerZoneUpdateStatistics
{
  uint64 DynamicUpdateReceived;
  uint64 DynamicUpdateRejected;
};
```

## Members

The **DnsServerZoneUpdateStatistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerZoneUpdateStatistics** class has these properties.

<dl> <dt>

**DynamicUpdateReceived**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total number of dynamic updates received by the DNS server for the zone.

</dd> <dt>

**DynamicUpdateRejected**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total number of dynamic updates rejected by the DNS server for the zone.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





