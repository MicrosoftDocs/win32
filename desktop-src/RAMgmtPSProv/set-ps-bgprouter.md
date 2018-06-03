---
title: Set method of the PS\_BgpRouter class
description: Updates the configuration of a BGP router.
audience: developer
ms.assetid: fc7cbc79-4a77-4d08-9c39-82fe9f993640
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_BgpRouter class
- PS_BgpRouter class, Set method
topic_type:
- apiref
api_name:
- PS_BgpRouter.Set
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Set method of the PS\_BgpRouter class

Updates the configuration of a BGP router.

## Syntax


```mof
uint32 Set(
  [in]  string          BgpIdentifier,
  [in]  uint32          LocalASN,
  [in]  boolean         CompareMEDAcrossASN,
  [in]  boolean         DefaultGatewayRouting,
  [in]  uint32          IPv6Routing,
  [in]  string          RoutingDomain,
  [in]  boolean         PassThru,
  [in]  boolean         Force,
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

The IPv4 address of the BGP router to update.

</dd> <dt>

*LocalASN* \[in\]
</dt> <dd>

The local Autonomous System Number (ASN) of the BGP router.

</dd> <dt>

*CompareMEDAcrossASN* \[in\]
</dt> <dd>

Indicates whether to enable the BGP router to compare multi-exit discriminator (MED) values across autonomous systems. **True** to enable to router to compare MED values across autonomous systems; otherwise **false**.

</dd> <dt>

*DefaultGatewayRouting* \[in\]
</dt> <dd>

Indicates whether the BGP router routes network traffic to the default internet gateway. **True** to route network traffic to the default internet gateway; otherwise **false**.

</dd> <dt>

*IPv6Routing* \[in\]
</dt> <dd>

Enables IPv6 routing for the BGP router.

</dd> <dt>

*RoutingDomain* \[in\]
</dt> <dd>

The user-defined unique alphanumeric ID of the routing domain.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Indicates whether the *cmdletOutput* parameter returns an object. **True** to return an object; otherwise **false**.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Indicates whether to use a confirmation prompt to modify the configuration of the router. **True** to use a confirmation prompt; otherwise **false**.

</dd> <dt>

*LocalIPv6Address* \[in\]
</dt> <dd>

The IPv6 IP address of the next-hop value for IPv6 route advertisements.

</dd> <dt>

*TransitRouting* \[in\]
</dt> <dd>

whether Transit routing is enabled.

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

The [**BgpRouterConfig**](bgprouterconfig.md) object that receives the updated BGP router instance.

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

 

 





