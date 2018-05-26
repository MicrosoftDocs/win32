---
title: Remove method of the PS\_BgpRouteAggregate class
description: Remove-BgpRouteAggregate cmdlet removes the set of specified Aggregate BGP Routes.
audience: developer
ms.assetid: 8a9affb6-00a0-47db-8ecf-06c27dcc4e87
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Remove method
- Remove method, PS_BgpRouteAggregate class
- PS_BgpRouteAggregate class, Remove method
topic_type:
- apiref
api_name:
- PS_BgpRouteAggregate.Remove
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Remove method of the PS\_BgpRouteAggregate class

Remove-BgpRouteAggregate cmdlet removes the set of specified Aggregate BGP Routes.

## Syntax


```mof
uint32 Remove(
  [in] string  RoutingDomain,
  [in] string  Prefix[],
  [in] boolean Force
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

List of the aggregate IP Addresses (classless IP address prefixes and their prefix lengths) to be removed from BGP.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Indicates no confirmation prompt for removing Aggregate routes.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>Ramgmtpsprovider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_BgpRouteAggregate**](ps-bgprouteaggregate.md)
</dt> </dl>

 

 





