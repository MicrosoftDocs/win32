---
title: DhcpServerv6ScopeStatistics class
description: Dhcp Server v6 Scope Statistics.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 403d5134-d18a-4396-b431-bb542d9f2936
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DhcpServerv6ScopeStatistics class
- DhcpServerv6ScopeStatistics class, described
topic_type:
- apiref
api_name:
- DhcpServerv6ScopeStatistics
- DhcpServerv6ScopeStatistics.AddressesFree
- DhcpServerv6ScopeStatistics.AddressesInUse
- DhcpServerv6ScopeStatistics.PendingAdvertises
- DhcpServerv6ScopeStatistics.Prefix
- DhcpServerv6ScopeStatistics.ReservedAddress
- DhcpServerv6ScopeStatistics.PercentageInUse
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DhcpServerv6ScopeStatistics class

Dhcp Server v6 Scope Statistics.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class DhcpServerv6ScopeStatistics
{
  Uint64 AddressesFree;
  Uint64 AddressesInUse;
  Uint64 PendingAdvertises;
  string Prefix;
  Uint64 ReservedAddress;
  real32 PercentageInUse;
};
```

## Members

The **DhcpServerv6ScopeStatistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **DhcpServerv6ScopeStatistics** class has these properties.

<dl> <dt>

**AddressesFree**
</dt> <dd> <dl> <dt>

Data type: **Uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Addresses free on given scope on the Dhcp server.

</dd> <dt>

**AddressesInUse**
</dt> <dd> <dl> <dt>

Data type: **Uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Addresses in use on given scope on the Dhcp server.

</dd> <dt>

**PendingAdvertises**
</dt> <dd> <dl> <dt>

Data type: **Uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Pending Advertises on given scope on the Dhcp server.

</dd> <dt>

**PercentageInUse**
</dt> <dd> <dl> <dt>

Data type: **real32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Percentage of addresses in use on given scope on the Dhcp server.

</dd> <dt>

**Prefix**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Scope identifier(unique) for the given scope on Dhcp server

</dd> <dt>

**ReservedAddress**
</dt> <dd> <dl> <dt>

Data type: **Uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reserved addresses on given scope on the Dhcp server.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





