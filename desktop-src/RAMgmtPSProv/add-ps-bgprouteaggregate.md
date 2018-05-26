---
title: Add method of the PS\_BgpRouteAggregate class
description: Adds a new aggregate route for more specific BGP routes.
audience: developer
ms.assetid: 822e7990-b267-4737-8fe7-a132afc4ab9a
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Add method
- Add method, PS_BgpRouteAggregate class
- PS_BgpRouteAggregate class, Add method
topic_type:
- apiref
api_name:
- PS_BgpRouteAggregate.Add
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Add method of the PS\_BgpRouteAggregate class

Adds a new aggregate route for more specific BGP routes.

## Syntax


```mof
uint32 Add(
  [in]  string                  RoutingDomain,
  [in]  string                  Prefix,
  [in]  uint32                  SummaryOnly,
  [in]  string                  AttributePolicy[],
  [in]  uint32                  PreserveASPath,
  [in]  boolean                 PassThru,
  [in]  boolean                 Force,
  [out] BgpRouteAggregateConfig cmdletOutput
);
```



## Parameters

<dl> <dt>

*RoutingDomain* \[in\]
</dt> <dd>

A user-defined alphanumeric ID of the routing Domain / Tenant.

</dd> <dt>

*Prefix* \[in\]
</dt> <dd>

Classless IP address prefix for the aggregate IP Address and its prefix length.

</dd> <dt>

*SummaryOnly* \[in\]
</dt> <dd>

Flag to indicate that only the aggregate address is to be advertised to peers.

</dd> <dt>

*AttributePolicy* \[in\]
</dt> <dd>

A list of policy names that are to be applied to the Aggregate route to configure its attributes.

</dd> <dt>

*PreserveASPath* \[in\]
</dt> <dd>

Flag to keep the aggregated AS Paths in the AS Set of the aggregate IP Address.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to indicate that the method returns an output object. The default is **false**.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

**true** for no confirmation prompt for suppressing specific routes in favor of the newly added Aggregate route. The default is **false**.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

If *PassThru* is **true**, returns an embedded instance of the current object.

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

 

 





