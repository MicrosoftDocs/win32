---
title: DhcpServerv4ScopeStatistics class
description: Dhcp Server v4 Scope Statistics.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c5ee718b-86f9-4c39-b011-ead8d4c08449
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DhcpServerv4ScopeStatistics class
- DhcpServerv4ScopeStatistics class, described
topic_type:
- apiref
api_name:
- DhcpServerv4ScopeStatistics
- DhcpServerv4ScopeStatistics.AddressesFree
- DhcpServerv4ScopeStatistics.AddressesInUse
- DhcpServerv4ScopeStatistics.PendingOffers
- DhcpServerv4ScopeStatistics.ScopeId
- DhcpServerv4ScopeStatistics.SuperscopeName
- DhcpServerv4ScopeStatistics.ReservedAddress
- DhcpServerv4ScopeStatistics.PercentageInUse
- DhcpServerv4ScopeStatistics.AddressesFreeOnThisServer
- DhcpServerv4ScopeStatistics.AddressesFreeOnPartnerServer
- DhcpServerv4ScopeStatistics.AddressesInUseOnThisServer
- DhcpServerv4ScopeStatistics.AddressesInUseOnPartnerServer
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DhcpServerv4ScopeStatistics class

Dhcp Server v4 Scope Statistics.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class DhcpServerv4ScopeStatistics
{
  Uint32 AddressesFree;
  Uint32 AddressesInUse;
  Uint32 PendingOffers;
  string ScopeId;
  string SuperscopeName;
  Uint32 ReservedAddress;
  real32 PercentageInUse;
  Uint32 AddressesFreeOnThisServer;
  Uint32 AddressesFreeOnPartnerServer;
  Uint32 AddressesInUseOnThisServer;
  Uint32 AddressesInUseOnPartnerServer;
};
```

## Members

The **DhcpServerv4ScopeStatistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **DhcpServerv4ScopeStatistics** class has these properties.

<dl> <dt>

**AddressesFree**
</dt> <dd> <dl> <dt>

Data type: **Uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Addresses free on given scope on the Dhcp server.

</dd> <dt>

**AddressesFreeOnPartnerServer**
</dt> <dd> <dl> <dt>

Data type: **Uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

For a failover scope, indicates the number of addresses free on partner server based on the ownership assignment of the free address pool.

</dd> <dt>

**AddressesFreeOnThisServer**
</dt> <dd> <dl> <dt>

Data type: **Uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

For a failover scope, indicates the number of addresses free on this server based on the ownership assignment of the free address pool.

</dd> <dt>

**AddressesInUse**
</dt> <dd> <dl> <dt>

Data type: **Uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Addresses in use on given scope on the Dhcp server.

</dd> <dt>

**AddressesInUseOnPartnerServer**
</dt> <dd> <dl> <dt>

Data type: **Uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

For a failover scope, indicates the number of addresses leased/renewed by partner server.

</dd> <dt>

**AddressesInUseOnThisServer**
</dt> <dd> <dl> <dt>

Data type: **Uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

For a failover scope, indicates the number of addresses leased/renewed by this server.

</dd> <dt>

**PendingOffers**
</dt> <dd> <dl> <dt>

Data type: **Uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Pending offers on given scope on the Dhcp server.

</dd> <dt>

**PercentageInUse**
</dt> <dd> <dl> <dt>

Data type: **real32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Percentage of addresses in use on given scope on the Dhcp server.

</dd> <dt>

**ReservedAddress**
</dt> <dd> <dl> <dt>

Data type: **Uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reserved addresses on given scope on the Dhcp server.

</dd> <dt>

**ScopeId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Scope identifier(unique) for the given scope on Dhcp server

</dd> <dt>

**SuperscopeName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of Superscope to which given scope on Dhcp server belongs

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





