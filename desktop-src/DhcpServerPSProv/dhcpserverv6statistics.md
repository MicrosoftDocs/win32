---
title: DhcpServerv6Statistics class
description: Dhcp Server v6 Statistics.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: cda7ea01-e74a-4d17-9913-3a8c9f98ce57
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DhcpServerv6Statistics class
- DhcpServerv6Statistics class, described
topic_type:
- apiref
api_name:
- DhcpServerv6Statistics
- DhcpServerv6Statistics.Solicits
- DhcpServerv6Statistics.Advertises
- DhcpServerv6Statistics.Confirms
- DhcpServerv6Statistics.Declines
- DhcpServerv6Statistics.Informs
- DhcpServerv6Statistics.Rebinds
- DhcpServerv6Statistics.Releases
- DhcpServerv6Statistics.Renews
- DhcpServerv6Statistics.Replies
- DhcpServerv6Statistics.Requests
- DhcpServerv6Statistics.ServerStartTime
- DhcpServerv6Statistics.TotalScopes
- DhcpServerv6Statistics.TotalAddresses
- DhcpServerv6Statistics.AddressesInUse
- DhcpServerv6Statistics.AddressesAvailable
- DhcpServerv6Statistics.PendingAdvertises
- DhcpServerv6Statistics.PercentageInUse
- DhcpServerv6Statistics.PercentageAvailable
- DhcpServerv6Statistics.PercentagePendingAdvertises
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DhcpServerv6Statistics class

Dhcp Server v6 Statistics.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class DhcpServerv6Statistics
{
  uint32   Solicits;
  uint32   Advertises;
  uint32   Confirms;
  uint32   Declines;
  uint32   Informs;
  uint32   Rebinds;
  uint32   Releases;
  uint32   Renews;
  uint32   Replies;
  uint32   Requests;
  DateTime ServerStartTime;
  uint32   TotalScopes;
  uint64   TotalAddresses;
  uint64   AddressesInUse;
  uint64   AddressesAvailable;
  uint64   PendingAdvertises;
  real32   PercentageInUse;
  real32   PercentageAvailable;
  real32   PercentagePendingAdvertises;
};
```

## Members

The **DhcpServerv6Statistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **DhcpServerv6Statistics** class has these properties.

<dl> <dt>

**AddressesAvailable**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Addresses available across all scopes on the Dhcp server.

</dd> <dt>

**AddressesInUse**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Addresses in use across all scopes on the Dhcp server.

</dd> <dt>

**Advertises**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of advertises received by the Dhcp server.

</dd> <dt>

**Confirms**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of confirms received by the Dhcp server.

</dd> <dt>

**Declines**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of declines received by the Dhcp server.

</dd> <dt>

**Informs**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of informs received by the Dhcp server.

</dd> <dt>

**PendingAdvertises**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Pending Advertises across all scopes on the Dhcp server.

</dd> <dt>

**PercentageAvailable**
</dt> <dd> <dl> <dt>

Data type: **real32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Percentage of addresses available.

</dd> <dt>

**PercentageInUse**
</dt> <dd> <dl> <dt>

Data type: **real32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Percentage of addresses in use.

</dd> <dt>

**PercentagePendingAdvertises**
</dt> <dd> <dl> <dt>

Data type: **real32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Percentage of addresses pending.

</dd> <dt>

**Rebinds**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of rebinds received by the Dhcp server.

</dd> <dt>

**Releases**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of releases received by the Dhcp server.

</dd> <dt>

**Renews**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of renews received by the Dhcp server.

</dd> <dt>

**Replies**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of replies received by the Dhcp server.

</dd> <dt>

**Requests**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of requests received by the Dhcp server.

</dd> <dt>

**ServerStartTime**
</dt> <dd> <dl> <dt>

Data type: **DateTime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Start time of the DHCP server.

</dd> <dt>

**Solicits**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of solicits received by the Dhcp server.

</dd> <dt>

**TotalAddresses**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total addresses across all scopes on the Dhcp server.

</dd> <dt>

**TotalScopes**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total number of scopes configured on the Dhcp server.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





