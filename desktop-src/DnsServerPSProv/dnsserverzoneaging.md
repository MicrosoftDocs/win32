---
title: DnsServerZoneAging class
description: Manages aging settings for a DNS zone.
audience: developer
ms.assetid: '5b45aae7-deca-418e-859f-bf88a85414a1'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DnsServerZoneAging class", "DnsServerZoneAging class, described"]
topic_type:
- apiref
api_name:
- DnsServerZoneAging
- DnsServerZoneAging.ZoneName
- DnsServerZoneAging.AgingEnabled
- DnsServerZoneAging.AvailForScavengeTime
- DnsServerZoneAging.RefreshInterval
- DnsServerZoneAging.NoRefreshInterval
- DnsServerZoneAging.ScavengeServers
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# DnsServerZoneAging class

Manages aging settings for a DNS zone.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerZoneAging
{
  string   ZoneName;
  boolean  AgingEnabled;
  datetime AvailForScavengeTime;
  datetime RefreshInterval;
  datetime NoRefreshInterval;
  string   ScavengeServers[];
};
```

## Members

The **DnsServerZoneAging** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerZoneAging** class has these properties.

<dl> <dt>

**AgingEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**true** to enable aging in the zone; otherwise, **false**.

</dd> <dt>

**AvailForScavengeTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The duration in which scavenging of stale DNS records is possible for the zone.

</dd> <dt>

**NoRefreshInterval**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The time interval that indicates when refresh operations can not be used to dynamically update DNS records in the zone.

</dd> <dt>

**RefreshInterval**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The time interval that indicates when refresh operations can be used to dynamically update DNS records in the zone.

</dd> <dt>

**ScavengeServers**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

An array that contains the names of the servers in the zone that perform scavenging.

</dd> <dt>

**ZoneName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The name of the zone.

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

 

 





