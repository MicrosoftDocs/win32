---
Description: Whats New in IP Helper
ms.assetid: fa9d72d0-2f9c-433d-b05a-8423664b2e3e
title: Whats New in IP Helper
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# What's New in IP Helper

## Windows 8 and Windows Server 2012

The following features have been added to the IP Helper APIs on Windows 8 and Windows Server 2012.

A function that retrieves historical bandwidth estimates for a network connection. For more information, see:

-   [**GetIpNetworkConnectionBandwidthEstimates**](/windows/win32/Netioapi/nf-netioapi-getipnetworkconnectionbandwidthestimates?branch=master)

A structure that contains information on the available bandwidth estimates and associated variance as determined by the TCP/IP stack. For more information, see:

-   [**NL\_BANDWIDTH\_INFORMATION**](/windows/win32/Nldef/ns-nldef-_nl_bandwidth_information?branch=master)

## Windows 7 and Windows Server 2008 R2

The following features have been added to the IP Helper APIs on Windows 7 and Windows Server 2008 R2.

Functions that convert an Ethernet address between a binary format and string format for the Ethernet MAC address. For more information, see:

-   [**RtlEthernetAddressToString**](/windows/win32/ip2string/nf-ip2string-rtlethernetaddresstostringa?branch=master)
-   [**RtlEthernetStringToAddress**](/windows/win32/ip2string/nf-ip2string-rtlethernetstringtoaddressa?branch=master)

## Windows Server 2008 and Windows Vista SP1

The following functions have been added to the IP Helper APIs on Windows Server 2008 and Windows Vista with Service Pack 1 (SP1).

A function that works with IPv4 and the Internet Control Message Protocol (ICMP). For more information, see:

-   [**IcmpSendEcho2Ex**](/windows/win32/Icmpapi/nf-icmpapi-icmpsendecho2ex?branch=master)

## Windows Vista

The following groups of functions have been added to the IP Helper APIs on Windows Vista and later.

Functions that work with both IPv6 and IPv4 for interface conversion. For more information, see:

-   [**ConvertInterfaceAliasToLuid**](/windows/win32/Netioapi/nf-netioapi-convertinterfacealiastoluid?branch=master)
-   [**ConvertInterfaceGuidToLuid**](/windows/win32/Netioapi/nf-netioapi-convertinterfaceguidtoluid?branch=master)
-   [**ConvertInterfaceIndexToLuid**](/windows/win32/Netioapi/nf-netioapi-convertinterfaceindextoluid?branch=master)
-   [**ConvertInterfaceLuidToGuid**](/windows/win32/Netioapi/nf-netioapi-convertinterfaceluidtoguid?branch=master)
-   [**ConvertInterfaceLuidToIndex**](/windows/win32/Netioapi/nf-netioapi-convertinterfaceluidtoindex?branch=master)
-   [**ConvertInterfaceLuidToNameA**](/windows/win32/Netioapi/nf-netioapi-convertinterfaceluidtonamea?branch=master)
-   [**ConvertInterfaceLuidToNameW**](/windows/win32/Netioapi/nf-netioapi-convertinterfaceluidtonamew?branch=master)
-   [**ConvertInterfaceNameToLuidA**](/windows/win32/Netioapi/nf-netioapi-convertinterfacenametoluida?branch=master)
-   [**ConvertInterfaceNameToLuidW**](/windows/win32/Netioapi/nf-netioapi-convertinterfacenametoluidw?branch=master)
-   [**if\_indextoname**](/windows/win32/Netioapi/nf-netioapi-if_indextoname?branch=master)
-   [**if\_nametoindex**](/windows/win32/Netioapi/nf-netioapi-if_nametoindex?branch=master)

Functions that work with both IPv6 and IPv4 for interface management. For more information, see:

-   [**GetIfEntry2**](/windows/win32/Netioapi/nf-netioapi-getifentry2?branch=master)
-   [**GetIfStackTable**](/windows/win32/Netioapi/nf-netioapi-getifstacktable?branch=master)
-   [**GetIfTable2**](/windows/win32/Netioapi/nf-netioapi-getiftable2?branch=master)
-   [**GetIfTable2Ex**](/windows/win32/Netioapi/nf-netioapi-getiftable2ex?branch=master)
-   [**GetInvertedIfStackTable**](/windows/win32/Netioapi/nf-netioapi-getinvertedifstacktable?branch=master)
-   [**GetIpInterfaceEntry**](/windows/win32/Netioapi/nf-netioapi-getipinterfaceentry?branch=master)
-   [**GetIpInterfaceTable**](/windows/win32/Netioapi/nf-netioapi-getipinterfacetable?branch=master)
-   [**InitializeIpInterfaceEntry**](/windows/win32/Netioapi/nf-netioapi-initializeipinterfaceentry?branch=master)
-   [**SetIpInterfaceEntry**](/windows/win32/Netioapi/nf-netioapi-setipinterfaceentry?branch=master)

Functions that work with both IPv6 and IPv4 for IP address management. For more information, see:

-   [**CreateAnycastIpAddressEntry**](/windows/win32/Netioapi/nf-netioapi-createanycastipaddressentry?branch=master)
-   [**CreateUnicastIpAddressEntry**](/windows/win32/Netioapi/nf-netioapi-createunicastipaddressentry?branch=master)
-   [**DeleteAnycastIpAddressEntry**](/windows/win32/Netioapi/nf-netioapi-deleteanycastipaddressentry?branch=master)
-   [**DeleteUnicastIpAddressEntry**](/windows/win32/Netioapi/nf-netioapi-deleteunicastipaddressentry?branch=master)
-   [**GetAnycastIpAddressEntry**](/windows/win32/Netioapi/nf-netioapi-getanycastipaddressentry?branch=master)
-   [**GetAnycastIpAddressTable**](/windows/win32/Netioapi/nf-netioapi-getanycastipaddresstable?branch=master)
-   [**GetMulticastIpAddressEntry**](/windows/win32/Netioapi/nf-netioapi-getmulticastipaddressentry?branch=master)
-   [**GetMulticastIpAddressTable**](/windows/win32/Netioapi/nf-netioapi-getmulticastipaddresstable?branch=master)
-   [**GetUnicastIpAddressEntry**](/windows/win32/Netioapi/nf-netioapi-getunicastipaddressentry?branch=master)
-   [**GetUnicastIpAddressTable**](/windows/win32/Netioapi/nf-netioapi-getunicastipaddresstable?branch=master)
-   [**InitializeUnicastIpAddressEntry**](/windows/win32/Netioapi/nf-netioapi-initializeunicastipaddressentry?branch=master)
-   [**NotifyStableUnicastIpAddressTable**](/windows/win32/Netioapi/nf-netioapi-notifystableunicastipaddresstable?branch=master)
-   [**SetUnicastIpAddressEntry**](/windows/win32/Netioapi/nf-netioapi-setunicastipaddressentry?branch=master)

A function that works with both IPv6 and IPv4 for IP table memory management. For more information, see:

-   [**FreeMibTable**](/windows/win32/Netioapi/nf-netioapi-freemibtable?branch=master)

Functions that work with both IPv6 and IPv4 for IP neighbor address management. For more information, see:

-   [**CreateIpNetEntry2**](/windows/win32/Netioapi/nf-netioapi-createipnetentry2?branch=master)
-   [**DeleteIpNetEntry2**](/windows/win32/Netioapi/nf-netioapi-deleteipnetentry2?branch=master)
-   [**FlushIpNetTable2**](/windows/win32/Netioapi/nf-netioapi-flushipnettable2?branch=master)
-   [**GetIpNetEntry2**](/windows/win32/Netioapi/nf-netioapi-getipnetentry2?branch=master)
-   [**GetIpNetTable2**](/windows/win32/Netioapi/nf-netioapi-getipnettable2?branch=master)
-   [**ResolveIpNetEntry2**](/windows/win32/Netioapi/nf-netioapi-resolveipnetentry2?branch=master)
-   [**ResolveNeighbor**](/windows/win32/Iphlpapi/nf-iphlpapi-resolveneighbor?branch=master)
-   [**SetIpNetEntry2**](/windows/win32/Netioapi/nf-netioapi-setipnetentry2?branch=master)

Functions that work with both IPv6 and IPv4 for IP path management. For more information, see:

-   [**FlushIpPathTable**](/windows/win32/Netioapi/nf-netioapi-flushippathtable?branch=master)
-   [**GetIpPathEntry**](/windows/win32/Netioapi/nf-netioapi-getippathentry?branch=master)
-   [**GetIpPathTable**](/windows/win32/Netioapi/nf-netioapi-getippathtable?branch=master)

Functions that work with both IPv6 and IPv4 for IP route management. For more information, see:

-   [**CreateIpForwardEntry2**](/windows/win32/Netioapi/nf-netioapi-createipforwardentry2?branch=master)
-   [**DeleteIpForwardEntry2**](/windows/win32/Netioapi/nf-netioapi-deleteipforwardentry2?branch=master)
-   [**GetBestRoute2**](/windows/win32/Netioapi/nf-netioapi-getbestroute2?branch=master)
-   [**GetIpForwardEntry2**](/windows/win32/Netioapi/nf-netioapi-getipforwardentry2?branch=master)
-   [**GetIpForwardTable2**](/windows/win32/Netioapi/nf-netioapi-getipforwardtable2?branch=master)
-   [**InitializeIpForwardEntry**](/windows/win32/Netioapi/nf-netioapi-initializeipforwardentry?branch=master)
-   [**SetIpForwardEntry2**](/windows/win32/Netioapi/nf-netioapi-setipforwardentry2?branch=master)
-   [**SetIpStatisticsEx**](/windows/win32/Iphlpapi/nf-iphlpapi-setipstatisticsex?branch=master)

Functions that work with both IPv6 and IPv4 for notification. For more information, see:

-   [**CancelMibChangeNotify2**](/windows/win32/Netioapi/nf-netioapi-cancelmibchangenotify2?branch=master)
-   [**NotifyIpInterfaceChange**](/windows/win32/Netioapi/nf-netioapi-notifyipinterfacechange?branch=master)
-   [**NotifyRouteChange2**](/windows/win32/Netioapi/nf-netioapi-notifyroutechange2?branch=master)
-   [**NotifyUnicastIpAddressChange**](/windows/win32/Netioapi/nf-netioapi-notifyunicastipaddresschange?branch=master)

Utility functions that work with IP addresses. For more information, see:

-   [**ConvertIpv4MaskToLength**](/windows/win32/Netioapi/nf-netioapi-convertipv4masktolength?branch=master)
-   [**ConvertLengthToIpv4Mask**](/windows/win32/Netioapi/nf-netioapi-convertlengthtoipv4mask?branch=master)
-   [**CreateSortedAddressPairs**](/windows/win32/Netioapi/nf-netioapi-createsortedaddresspairs?branch=master)
-   [**ParseNetworkString**](/windows/win32/Iphlpapi/nf-iphlpapi-parsenetworkstring?branch=master)

Functions that work with Transmission Control Protocol (TCP) and User Datagram Protocol (UDP) to retrieve the IPv6 or IPv4 TCP connection table or UDP listener table. For more information, see:

-   [**GetTcp6Table**](/windows/win32/Iphlpapi/nf-iphlpapi-gettcp6table?branch=master)
-   [**GetTcp6Table2**](/windows/win32/Iphlpapi/nf-iphlpapi-gettcp6table2?branch=master)
-   [**GetTcpTable2**](/windows/win32/Iphlpapi/nf-iphlpapi-gettcptable2?branch=master)
-   [**GetUdp6Table**](/windows/win32/Iphlpapi/nf-iphlpapi-getudp6table?branch=master)

Functions that work with Transmission Control Protocol (TCP) to retrieve extended TCP statistics on a connection. For more information, see:

-   [**GetPerTcp6ConnectionEStats**](/windows/win32/Iphlpapi/nf-iphlpapi-getpertcp6connectionestats?branch=master)
-   [**GetPerTcpConnectionEStats**](/windows/win32/Iphlpapi/nf-iphlpapi-getpertcpconnectionestats?branch=master)
-   [**SetPerTcp6ConnectionEStats**](/windows/win32/Iphlpapi/nf-iphlpapi-setpertcp6connectionestats?branch=master)
-   [**SetPerTcpConnectionEStats**](/windows/win32/Iphlpapi/nf-iphlpapi-setpertcpconnectionestats?branch=master)

New functions that work for Teredo IPv6 client management. For more information, see:

-   [**GetTeredoPort**](/windows/win32/Netioapi/nf-netioapi-getteredoport?branch=master)
-   [**NotifyTeredoPortChange**](/windows/win32/Netioapi/nf-netioapi-notifyteredoportchange?branch=master)
-   [**NotifyStableUnicastIpAddressTable**](/windows/win32/Netioapi/nf-netioapi-notifystableunicastipaddresstable?branch=master)

Utility functions that provide conversions between IP addresses and string representations of IP addresses. For more information, see:

-   [**RtlIpv4AddressToString**](/windows/win32/ip2string/nf-ip2string-rtlipv4addresstostringa?branch=master)
-   [**RtlIpv4AddressToStringEx**](/windows/win32/ip2string/nf-ip2string-rtlipv4addresstostringexw?branch=master)
-   [**RtlIpv4StringToAddress**](/windows/win32/ip2string/nf-ip2string-rtlipv4stringtoaddressa?branch=master)
-   [**RtlIpv4StringToAddressEx**](/windows/win32/ip2string/nf-ip2string-rtlipv4stringtoaddressexw?branch=master)
-   [**RtlIpv6AddressToString**](/windows/win32/ip2string/nf-ip2string-rtlipv6addresstostringa?branch=master)
-   [**RtlIpv6AddressToStringEx**](/windows/win32/ip2string/nf-ip2string-rtlipv6addresstostringexw?branch=master)
-   [**RtlIpv6StringToAddress**](/windows/win32/ip2string/nf-ip2string-rtlipv6stringtoaddressa?branch=master)
-   [**RtlIpv6StringToAddressEx**](/windows/win32/ip2string/nf-ip2string-rtlipv6stringtoaddressexw?branch=master)

Functions that provide persistent reservations for a consecutive block of TCP or UDP ports on the local computer. For more information, see:

-   [**CreatePersistentTcpPortReservation**](/windows/win32/Iphlpapi/nf-iphlpapi-createpersistenttcpportreservation?branch=master)
-   [**CreatePersistentUdpPortReservation**](/windows/win32/Iphlpapi/nf-iphlpapi-createpersistentudpportreservation?branch=master)
-   [**DeletePersistentTcpPortReservation**](/windows/win32/Iphlpapi/nf-iphlpapi-deletepersistenttcpportreservation?branch=master)
-   [**DeletePersistentUdpPortReservation**](/windows/win32/Iphlpapi/nf-iphlpapi-deletepersistentudpportreservation?branch=master)
-   [**LookupPersistentTcpPortReservation**](/windows/win32/Iphlpapi/nf-iphlpapi-lookuppersistenttcpportreservation?branch=master)
-   [**LookupPersistentUdpPortReservation**](/windows/win32/Iphlpapi/nf-iphlpapi-lookuppersistentudpportreservation?branch=master)

## Windows Server 2003

The following functions have been added to the IP Helper APIs on Windows Server 2003 and later:

-   [**CancelSecurityHealthChangeNotify**](/windows/win32/Iphlpapi/?branch=master)
-   [**NotifySecurityHealthChange**](/windows/win32/Iphlpapi/?branch=master)

## Windows XP SP2

The following functions have been added to the IP Helper APIs on Windows XP with Service Pack 2 (SP2) and later:

-   [**GetOwnerModuleFromTcpEntry**](/windows/win32/Iphlpapi/nf-iphlpapi-getownermodulefromtcpentry?branch=master)
-   [**GetOwnerModuleFromTcp6Entry**](/windows/win32/Iphlpapi/nf-iphlpapi-getownermodulefromtcp6entry?branch=master)
-   [**GetOwnerModuleFromUdpEntry**](/windows/win32/Iphlpapi/nf-iphlpapi-getownermodulefromudpentry?branch=master)
-   [**GetOwnerModuleFromUdp6Entry**](/windows/win32/Iphlpapi/nf-iphlpapi-getownermodulefromudp6entry?branch=master)

 

 



