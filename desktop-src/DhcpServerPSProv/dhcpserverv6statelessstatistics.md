---
title: DhcpServerv6StatelessStatistics class
description: Dhcp Server v6StatelessStatistics.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '6e976f6c-f8ad-4ec9-a543-5a87b5c0cff2'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DhcpServerv6StatelessStatistics class", "DhcpServerv6StatelessStatistics class, described"]
topic_type:
- apiref
api_name:
- DhcpServerv6StatelessStatistics
- DhcpServerv6StatelessStatistics.Prefix
- DhcpServerv6StatelessStatistics.AddressesInUse
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
---

# DhcpServerv6StatelessStatistics class

Dhcp Server v6StatelessStatistics.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class DhcpServerv6StatelessStatistics
{
  string Prefix;
  uint64 AddressesInUse;
};
```

## Members

The **DhcpServerv6StatelessStatistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **DhcpServerv6StatelessStatistics** class has these properties.

<dl> <dt>

**AddressesInUse**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of stateless addresses in use in the scope.

</dd> <dt>

**Prefix**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Scope identifier for the given scope on Dhcp server.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





