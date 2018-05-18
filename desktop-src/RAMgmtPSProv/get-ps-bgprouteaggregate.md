---
title: Get method of the PS\_BgpRouteAggregate class
description: Retrieves all the aggregate BGP Routes configured by the administrator.
audience: developer
ms.assetid: 'ef010ecb-fd3a-4f11-a2a6-1966eec52120'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Get method", "Get method, PS_BgpRouteAggregate class", "PS_BgpRouteAggregate class, Get method"]
topic_type:
- apiref
api_name:
- PS_BgpRouteAggregate.Get
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
---

# Get method of the PS\_BgpRouteAggregate class

Retrieves all the aggregate BGP Routes configured by the administrator.

## Syntax


```mof
uint32 Get(
  [in]  string                  RoutingDomain,
  [in]  string                  Prefix[],
  [out] BgpRouteAggregateConfig cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*RoutingDomain* \[in\]
</dt> <dd>

User-defined unique alphanumeric identifier for the Routing domain / Tenant.

</dd> <dt>

*Prefix* \[in\]
</dt> <dd>

List of the aggregate IP addresses (classless IP address prefixes and their prefix lengths) whose properties are to be retrieved.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Returns an embedded instance of the current object.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>Ramgmtpsprovider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_BgpRouteAggregate**](ps-bgprouteaggregate.md)
</dt> </dl>

 

 





