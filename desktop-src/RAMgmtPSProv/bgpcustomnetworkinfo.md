---
title: BgpCustomNetworkInfo class
description: Retrieves the network configuration of a custom Border Gateway Protocol (BGP) network.
audience: developer
ms.assetid: '1ed85479-f84d-4684-9244-5cfe53f22a9f'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["BgpCustomNetworkInfo class", "BgpCustomNetworkInfo class, described"]
topic_type:
- apiref
api_name:
- BgpCustomNetworkInfo
- BgpCustomNetworkInfo.RoutingDomain
- BgpCustomNetworkInfo.Network
- BgpCustomNetworkInfo.Interface
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# BgpCustomNetworkInfo class

Retrieves the network configuration of a custom Border Gateway Protocol (BGP) network.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class BgpCustomNetworkInfo
{
  string RoutingDomain;
  string Network[];
  string Interface[];
};
```

## Members

The **BgpCustomNetworkInfo** class has these types of members:

-   [Properties](#properties)

### Properties

The **BgpCustomNetworkInfo** class has these properties.

<dl> <dt>

**Interface**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the network's BGP router interface.

</dd> <dt>

**Network**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array of the IPv4 or IPv6 network address from the BGP router's Local Routing Information Base (Local-RIB), and the network mask for the Classless Inter-Domain Routing (CIDR) network address.

</dd> <dt>

**RoutingDomain**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The user defined alphanumeric ID of the network's routing domain. This property is only used for multi-tenant deployments.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                               |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[RAMgmtPSProvider Provider Classes](remote-access-management.md)
</dt> </dl>

 

 





