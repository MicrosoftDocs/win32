---
title: DhcpServerv4Statistics class
description: Dhcp Server v4 Statistics.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a6fd11f6-197d-4892-b4a4-f4ec7bb50d5b
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DhcpServerv4Statistics class
- DhcpServerv4Statistics class, described
topic_type:
- apiref
api_name:
- DhcpServerv4Statistics
- DhcpServerv4Statistics.Discovers
- DhcpServerv4Statistics.Offers
- DhcpServerv4Statistics.Requests
- DhcpServerv4Statistics.Acks
- DhcpServerv4Statistics.Naks
- DhcpServerv4Statistics.Declines
- DhcpServerv4Statistics.Releases
- DhcpServerv4Statistics.ServerStartTime
- DhcpServerv4Statistics.DelayedOffers
- DhcpServerv4Statistics.TotalScopes
- DhcpServerv4Statistics.ScopesWithDelayConfigured
- DhcpServerv4Statistics.TotalAddresses
- DhcpServerv4Statistics.AddressesInUse
- DhcpServerv4Statistics.AddressesAvailable
- DhcpServerv4Statistics.PendingOffers
- DhcpServerv4Statistics.PercentageInUse
- DhcpServerv4Statistics.PercentageAvailable
- DhcpServerv4Statistics.PercentagePendingOffers
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DhcpServerv4Statistics class

Dhcp Server v4 Statistics.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class DhcpServerv4Statistics
{
  uint32   Discovers;
  uint32   Offers;
  uint32   Requests;
  uint32   Acks;
  uint32   Naks;
  uint32   Declines;
  uint32   Releases;
  DateTime ServerStartTime;
  uint32   DelayedOffers;
  uint32   TotalScopes;
  uint32   ScopesWithDelayConfigured;
  uint32   TotalAddresses;
  uint32   AddressesInUse;
  uint32   AddressesAvailable;
  uint32   PendingOffers;
  real32   PercentageInUse;
  real32   PercentageAvailable;
  real32   PercentagePendingOffers;
};
```

## Members

The **DhcpServerv4Statistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **DhcpServerv4Statistics** class has these properties.

<dl> <dt>

**Acks**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

No. of DHCPACK messages sent to IPv4 clients from the server.

</dd> <dt>

**AddressesAvailable**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Addresses available across all scopes on the Dhcp server.

</dd> <dt>

**AddressesInUse**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Addresses in use across all scopes on the Dhcp server.

</dd> <dt>

**Declines**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

No. of DHCPDECLINE messages sent to IPv4 clients from the server.

</dd> <dt>

**DelayedOffers**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

No. of delayed DHCPOFFER messages sent by DHCP server.

</dd> <dt>

**Discovers**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

No. of DHCPDISCOVER messages received from IPv4 clients.

</dd> <dt>

**Naks**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

No. of DHCPNAK messages sent to IPv4 clients from the server.

</dd> <dt>

**Offers**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

No. of unconfirmed DHCPOFFER messages sent to IPv4 clients.

</dd> <dt>

**PendingOffers**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Pending Offers across all scopes on the Dhcp server.

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

**PercentagePendingOffers**
</dt> <dd> <dl> <dt>

Data type: **real32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Percentage of addresses pending.

</dd> <dt>

**Releases**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

No. of DHCPRELEASE messages sent to IPv4 clients from the server.

</dd> <dt>

**Requests**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

No. of DHCPREQUEST messages received from IPv4 clients.

</dd> <dt>

**ScopesWithDelayConfigured**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

No. of scopes configured with subnet delay for DHCPOFFER messages.

</dd> <dt>

**ServerStartTime**
</dt> <dd> <dl> <dt>

Data type: **DateTime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Start time of the DHCP server.

</dd> <dt>

**TotalAddresses**
</dt> <dd> <dl> <dt>

Data type: **uint32**
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



 

 





