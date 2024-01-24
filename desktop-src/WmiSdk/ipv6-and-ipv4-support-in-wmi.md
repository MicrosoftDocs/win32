---
description: WMI IP Route Provider and network classes supply data for IPv4 addresses. Starting with Windows Vista, WMI also provides limited support for IPv6 network capabilities.
ms.assetid: 8ab6287d-be3f-4fa2-a9f5-fa5e1aba66c8
ms.tgt_platform: multiple
title: IPv6 and IPv4 Support in WMI
ms.topic: article
ms.date: 05/31/2018
---

# IPv6 and IPv4 Support in WMI

WMI [IP Route Provider](/previous-versions/windows/desktop/wmiiprouteprov/ip-route-provider) and network classes supply data for IPv4 addresses. Starting with Windows Vista, WMI also provides limited support for IPv6 network capabilities.

## WMI IP Data

The following classes supply only IPv4 data:

-   [**Win32\_IP4RouteTable**](/previous-versions/windows/desktop/wmiiprouteprov/win32-ip4routetable)
-   [**Win32\_IP4PersistedRouteTable**](/previous-versions/windows/desktop/wmiiprouteprov/win32-ip4persistedroutetable)
-   [**Win32\_IP4RouteTableEvent**](/previous-versions/windows/desktop/wmiiprouteprov/win32-ip4routetableevent)
-   [**Win32\_ActiveRoute**](/previous-versions/windows/desktop/wmiiprouteprov/win32-activeroute)
-   [**Win32\_NetworkAdapter**](/windows/desktop/CIMWin32Prov/win32-networkadapter)

The following classes supply data for both IPv4 and IPv6.

-   [**Win32\_NetworkAdapterConfiguration**](/windows/desktop/CIMWin32Prov/win32-networkadapterconfiguration)

    The **IpAddess** property contains the IPv6 address of the computer in an IPv6 network.

-   [**Win32\_PingStatus**](/previous-versions/windows/desktop/wmipicmp/win32-pingstatus)

    [**Win32\_PingStatus**](/previous-versions/windows/desktop/wmipicmp/win32-pingstatus) can return data for either IPv4 or IPv6 addresses.

## IPv4 and IPv6 Connections to WMI

When connecting to a WMI namespace on a remote computer, the target computer must be running the same IP software as the connecting computer. For example, a computer running IPv4 cannot connect to a computer running IPv6, even if the connection is attempted by using a computer name in the call to [**IWbemLocator::ConnectServer**](/windows/desktop/api/Wbemcli/nf-wbemcli-iwbemlocator-connectserver), [**SWbemLocator.ConnectServer**](swbemlocator-connectserver.md), or by using the `winmgmts` moniker connection. The reverse is also true: a computer running only IPv6 cannot connect to a computer running only IPv4.

If the target computer is running both IPv4 and IPv6, then a connection can be made from a computer running either IP software. A computer name or an IP address in either IPv4 or IPv6 format can be supplied in the connection to a WMI namespace.

A computer that runs both IPv4 and IPv6 and connects to a target computer running only IPv4 or only IPv6 must supply an IP address in the appropriate format for the target computer IP software.

## Related topics

<dl> <dt>

[About WMI](about-wmi.md)
</dt> </dl>

 

 
