---
title: DnsServerScavenging class
description: Represents scavenging settings on a DNS server.
audience: developer
ms.assetid: a3817bd2-f5e4-4731-bbd2-502e7120dcc5
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerScavenging class
- DnsServerScavenging class, described
topic_type:
- apiref
api_name:
- DnsServerScavenging
- DnsServerScavenging.ScavengingInterval
- DnsServerScavenging.RefreshInterval
- DnsServerScavenging.NoRefreshInterval
- DnsServerScavenging.ScavengingState
- DnsServerScavenging.LastScavengeTime
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DnsServerScavenging class

Represents scavenging settings on a DNS server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerScavenging
{
  datetime ScavengingInterval;
  datetime RefreshInterval;
  datetime NoRefreshInterval;
  boolean  ScavengingState;
  datetime LastScavengeTime;
};
```

## Members

The **DnsServerScavenging** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerScavenging** class has these properties.

<dl> <dt>

**LastScavengeTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time when the last scavenging cycle was executed.

</dd> <dt>

**NoRefreshInterval**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The time interval for a zone during which no refreshes can dynamically update DNS records in a specified zone.

</dd> <dt>

**RefreshInterval**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The time interval for a zone during which refreshes can dynamically update DNS records in a specified zone.

</dd> <dt>

**ScavengingInterval**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The time span between scavenging cycles.

</dd> <dt>

**ScavengingState**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**true** to enable the scavenging feature for the DNS server; otherwise, **false**.

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

 

 





