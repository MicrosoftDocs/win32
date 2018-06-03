---
title: Add method of the PS\_BgpRouter class
description: Adds a new BGP router to the specified tenant.
audience: developer
ms.assetid: 422cd005-edd7-49f5-ba3b-6d01bb5d5394
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Add method
- Add method, PS_BgpRouter class
- PS_BgpRouter class, Add method
topic_type:
- apiref
api_name:
- PS_BgpRouter.Add
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Add method of the PS\_BgpRouter class

Adds a new BGP router to the specified tenant.

## Syntax


```mof
uint32 Add(
  [in]  string          BgpIdentifier,
  [in]  uint32          LocalASN,
  [in]  uint32          IPv6Routing,
  [in]  boolean         CompareMEDAcrossASN,
  [in]  boolean         DefaultGatewayRouting,
  [in]  boolean         PassThru,
  [in]  boolean         Force,
  [in]  string          RoutingDomain,
  [in]  string          LocalIPv6Address,
  [in]  uint32          TransitRouting,
  [in]  uint32          RouteReflector,
  [in]  uint32          ClusterId,
  [in]  uint32          ClientToClientReflection,
  [out] BgpRouterConfig cmdletOutput
);
```



## Parameters

<dl> <dt>

*BgpIdentifier* \[in\]
</dt> <dd>

The IPv4 address of the new BGP router.

</dd> <dt>

*LocalASN* \[in\]
</dt> <dd>

The local Autonomous System Number (ASN) of the new BGP router instance.

</dd> <dt>

*IPv6Routing* \[in\]
</dt> <dd>

Indicates whether IPv6 routing is enabled for the new BGP router.

</dd> <dt>

*CompareMEDAcrossASN* \[in\]
</dt> <dd>

Indicates whether to enable the BGP router to compare multi-exit discriminator (MED) values across autonomous systems. **True** to enable to router to compare MED values across autonomous systems; otherwise **false**.

</dd> <dt>

*DefaultGatewayRouting* \[in\]
</dt> <dd>

Indicates whether the BGP router routes network traffic to the default internet gateway. **True** to route network traffic to the default internet gateway; otherwise **false**.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Indicates whether the *cmdletOutput* parameter returns an object. **True** to return an object; otherwise **false**.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Set **True** for no confirmation prompt before adding the configuration for the router.

**Windows Server 2012 R2:** This parameter is not supported before Windows Server 2016.

</dd> <dt>

*RoutingDomain* \[in\]
</dt> <dd>

The user-defined unique alphanumeric ID of the routing domain.

</dd> <dt>

*LocalIPv6Address* \[in\]
</dt> <dd>

The IPv6 IP address of the next-hop value for IPv6 route advertisements.

</dd> <dt>

*TransitRouting* \[in\]
</dt> <dd>

whether Transit routing is enabled .

**Windows Server 2012 R2:** This parameter is not supported before Windows Server 2016.

</dd> <dt>

*RouteReflector* \[in\]
</dt> <dd>

Whether the BGP router acts as a route reflector.

**Windows Server 2012 R2:** This parameter is not supported before Windows Server 2016.

</dd> <dt>

*ClusterId* \[in\]
</dt> <dd>

The cluster id of the route reflector.

**Windows Server 2012 R2:** This parameter is not supported before Windows Server 2016.

</dd> <dt>

*ClientToClientReflection* \[in\]
</dt> <dd>

Whether client to client reflection is enabled.

**Windows Server 2012 R2:** This parameter is not supported before Windows Server 2016.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The [**BgpRouterConfig**](bgprouterconfig.md) object that receives the new BGP router.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                               |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_BgpRouter**](ps-bgprouter.md)
</dt> </dl>

 

 





