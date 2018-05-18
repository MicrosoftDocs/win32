---
title: Get method of the PS\_BgpRoute class
description: Retrieves the BGP route information for one or more network prefixes from the BGP routing table.
audience: developer
ms.assetid: '1c94bf45-3b7f-48c8-ab18-8ebbcc0c9b8b'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Get method", "Get method, PS_BgpRoute class", "PS_BgpRoute class, Get method"]
topic_type:
- apiref
api_name:
- PS_BgpRoute.Get
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
---

# Get method of the PS\_BgpRoute class

Retrieves the BGP route information for one or more network prefixes from the BGP routing table.

## Syntax


```mof
uint32 Get(
  [in]  string       Network[],
  [in]  string       RoutingDomain,
  [in]  uint32       Type,
  [out] BgpRouteInfo cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Network* \[in\]
</dt> <dd>

An array that contains the Classless Inter-Domain Routing (CIDR) IP network prefixes from which to retrieve BGP route information.

</dd> <dt>

*RoutingDomain* \[in\]
</dt> <dd>

The alphanumeric ID if the routing domain of the routing table.

</dd> <dt>

*Type* \[in\]
</dt> <dd>

The type of routes for which the information needs to be retrieved or listed.

**Windows Server 2012 R2:** This property is not supported before Windows Server 2016.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The [**BgpRouteInfo**](bgprouteinfo.md) object that receives the BGP route information.

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

[**PS\_BgpRoute**](ps-bgproute.md)
</dt> </dl>

 

 





