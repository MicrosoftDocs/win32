---
title: BgpStatistics class
description: Retrieves BGP peering message and route advertisement statistics.
audience: developer
ms.assetid: 6ca92044-067b-400a-9d78-8628448a6dd9
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- BgpStatistics class
- BgpStatistics class, described
topic_type:
- apiref
api_name:
- BgpStatistics
- BgpStatistics.RoutingDomain
- BgpStatistics.PeerName
- BgpStatistics.TcpConnectionEstablished
- BgpStatistics.TcpConnectionClosed
- BgpStatistics.OpenMessage
- BgpStatistics.UpdateMessage
- BgpStatistics.NotificationMessage
- BgpStatistics.KeepAliveMessage
- BgpStatistics.RouteRefreshMessage
- BgpStatistics.IPv4Route
- BgpStatistics.IPv6Route
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# BgpStatistics class

Retrieves BGP peering message and route advertisement statistics.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class BgpStatistics
{
  string               RoutingDomain;
  string               PeerName;
  datetime             TcpConnectionEstablished;
  datetime             TcpConnectionClosed;
  BgpMessageStatistics OpenMessage;
  BgpMessageStatistics UpdateMessage;
  BgpMessageStatistics NotificationMessage;
  BgpMessageStatistics KeepAliveMessage;
  BgpMessageStatistics RouteRefreshMessage;
  BgpRouteCounter      IPv4Route;
  BgpRouteCounter      IPv6Route;
};
```

## Members

The **BgpStatistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **BgpStatistics** class has these properties.

<dl> <dt>

**IPv4Route**
</dt> <dd> <dl> <dt>

Data type: **BgpRouteCounter**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**BgpRouteCounter**](bgproutecounter.md)")
</dt> </dl>

Gets the statistics for IPv4 BGP Route advertisements.

</dd> <dt>

**IPv6Route**
</dt> <dd> <dl> <dt>

Data type: **BgpRouteCounter**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**BgpRouteCounter**](bgproutecounter.md)")
</dt> </dl>

A [**BgpRouteCounter**](bgproutecounter.md) embedded instance for IPv6 BGP Route advertisements.

</dd> <dt>

**KeepAliveMessage**
</dt> <dd> <dl> <dt>

Data type: **BgpMessageStatistics**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**BgpMessageStatistics**](bgpmessagestatistics.md)")
</dt> </dl>

A [**BgpMessageStatistics**](bgpmessagestatistics.md) embedded instance for the BGP KEEP-ALIVE message.

</dd> <dt>

**NotificationMessage**
</dt> <dd> <dl> <dt>

Data type: **BgpMessageStatistics**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**BgpMessageStatistics**](bgpmessagestatistics.md)")
</dt> </dl>

A [**BgpMessageStatistics**](bgpmessagestatistics.md) embedded instance for the BGP NOTIFICATION message.

</dd> <dt>

**OpenMessage**
</dt> <dd> <dl> <dt>

Data type: **BgpMessageStatistics**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**BgpMessageStatistics**](bgpmessagestatistics.md)")
</dt> </dl>

A [**BgpMessageStatistics**](bgpmessagestatistics.md) embedded instance for the BGP OPEN message.

</dd> <dt>

**PeerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The BGP peer name.

</dd> <dt>

**RouteRefreshMessage**
</dt> <dd> <dl> <dt>

Data type: **BgpMessageStatistics**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**BgpMessageStatistics**](bgpmessagestatistics.md)")
</dt> </dl>

A [**BgpMessageStatistics**](bgpmessagestatistics.md) embedded instance for the BGP ROUTE-REFRESH message.

</dd> <dt>

**RoutingDomain**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The user defined alphanumeric ID of the BGP routing domain.

> [!Note]  
> This property is only used with multi-tenant deployments.

 

</dd> <dt>

**TcpConnectionClosed**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The timestamp of the last TCP connection that was closed.

</dd> <dt>

**TcpConnectionEstablished**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The timestamp of the last TCP connection that was established.

</dd> <dt>

**UpdateMessage**
</dt> <dd> <dl> <dt>

Data type: **BgpMessageStatistics**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**BgpMessageStatistics**](bgpmessagestatistics.md)")
</dt> </dl>

A [**BgpMessageStatistics**](bgpmessagestatistics.md) embedded instance for the BGP UPDATE message.

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

[RAMgmtPSProvider Provider Classes](remote-access-management.md)
</dt> </dl>

 

 





