---
title: DhcpServerv4SuperscopeStatistics class
description: Dhcp Server v4 Superscope Statistics class.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d55a1dd8-3152-4b66-8810-467a14418b13
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DhcpServerv4SuperscopeStatistics class
- DhcpServerv4SuperscopeStatistics class, described
topic_type:
- apiref
api_name:
- DhcpServerv4SuperscopeStatistics
- DhcpServerv4SuperscopeStatistics.SuperscopeName
- DhcpServerv4SuperscopeStatistics.NumScopes
- DhcpServerv4SuperscopeStatistics.AddressesFree
- DhcpServerv4SuperscopeStatistics.AddressesInUse
- DhcpServerv4SuperscopeStatistics.PercentageInUse
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DhcpServerv4SuperscopeStatistics class

Dhcp Server v4 Superscope Statistics class.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class DhcpServerv4SuperscopeStatistics
{
  string SuperscopeName;
  Uint32 NumScopes;
  uint32 AddressesFree;
  uint32 AddressesInUse;
  real32 PercentageInUse;
};
```

## Members

The **DhcpServerv4SuperscopeStatistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **DhcpServerv4SuperscopeStatistics** class has these properties.

<dl> <dt>

**AddressesFree**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

No. of free addresses that can be leased out to DHCPv4 clients in the Superscope.

</dd> <dt>

**AddressesInUse**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

No. of addresses leased out to DHCPv4 clients in the Superscope.

</dd> <dt>

**NumScopes**
</dt> <dd> <dl> <dt>

Data type: **Uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Number of scopes in the superscope.

</dd> <dt>

**PercentageInUse**
</dt> <dd> <dl> <dt>

Data type: **real32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Scope address utilization percentage.

</dd> <dt>

**SuperscopeName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Superscope Name.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                   |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





