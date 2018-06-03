---
title: DhcpServerv4MulticastScopeStatistics class
description: Dhcp Server v4 Multicast Scope Statistics class.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b4379525-2fa2-4bd2-a1d6-b30c2cc0a493
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DhcpServerv4MulticastScopeStatistics class
- DhcpServerv4MulticastScopeStatistics class, described
topic_type:
- apiref
api_name:
- DhcpServerv4MulticastScopeStatistics
- DhcpServerv4MulticastScopeStatistics.Name
- DhcpServerv4MulticastScopeStatistics.AddressesFree
- DhcpServerv4MulticastScopeStatistics.AddressesInUse
- DhcpServerv4MulticastScopeStatistics.PendingOffers
- DhcpServerv4MulticastScopeStatistics.PercentageInUse
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DhcpServerv4MulticastScopeStatistics class

Dhcp Server v4 Multicast Scope Statistics class.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class DhcpServerv4MulticastScopeStatistics
{
  string Name;
  uint32 AddressesFree;
  uint32 AddressesInUse;
  uint32 PendingOffers;
  real32 PercentageInUse;
};
```

## Members

The **DhcpServerv4MulticastScopeStatistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **DhcpServerv4MulticastScopeStatistics** class has these properties.

<dl> <dt>

**AddressesFree**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Number of free addresses that can be leased out to multicast clients in the Scope.

</dd> <dt>

**AddressesInUse**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Number of addresses leased out to multicast clients in the Scope.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Multicast scope Name.

</dd> <dt>

**PendingOffers**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Number of unconfirmed addresses in the Scope (offered to multicast clients but requests have not been received).

</dd> <dt>

**PercentageInUse**
</dt> <dd> <dl> <dt>

Data type: **real32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Scope address utilization percentage.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                   |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





