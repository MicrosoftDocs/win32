---
title: IP Route Provider
description: The preinstalled IP Route provider supplies IPV4 network routing information, including (but not limited to) the information available through the route print command.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6ac242fe-df33-406f-854c-e87423c03726
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- IP Route Provider
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IP Route Provider

The preinstalled IP Route provider supplies IPV4 network routing information, including (but not limited to) the information available through the **route print** command. This provider allows you to examine how packets are routed through the network to and from a particular machine. The provided data comes from the IP4 route tables and the persisted route table in the registry. The provider allows update of a route table entry, assuming all the property values to be written are valid. It also supplies events for route table changes.

The IP Route provider supplies only IPv4 data, not IPv6. For more information, see [IPv6 and IPv4 Support in WMI](https://msdn.microsoft.com/library/aa822883).

The names of the [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688) instances that implement the IP Route functionality are "RouteProvider"and "RouteEventProvider".

As an instance and event provider, the IP Route provider implements the standard [**IWbemProviderInit**](https://msdn.microsoft.com/library/aa391853) interface and the following [**IWbemServices**](https://msdn.microsoft.com/library/aa392093) methods:

-   [**CreateInstanceEnumAsync**](https://msdn.microsoft.com/library/aa392098)
-   [**DeleteInstanceAsync**](https://msdn.microsoft.com/library/aa392102)
-   [**ExecQueryAsync**](https://msdn.microsoft.com/library/aa392108)
-   [**GetObjectAsync**](https://msdn.microsoft.com/library/aa392110)
-   [**PutInstanceAsync**](https://msdn.microsoft.com/library/aa392116)

The IP Route provider supports the following classes:

-   [**Win32\_IP4RouteTable**](win32-ip4routetable.md)
-   [**Win32\_IP4PersistedRouteTable**](win32-ip4persistedroutetable.md)
-   [**Win32\_ActiveRoute**](win32-activeroute.md)
-   [**Win32\_IP4RouteTableEvent**](win32-ip4routetableevent.md)

## Related topics

<dl> <dt>

[WMI Providers](https://msdn.microsoft.com/library/aa394570)
</dt> </dl>

 

 




