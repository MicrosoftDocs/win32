---
Description: 'What''s New in IP Helper'
ms.assetid: 'fa9d72d0-2f9c-433d-b05a-8423664b2e3e'
title: 'What''s New in IP Helper'
---

# What's New in IP Helper

## Windows 8 and Windows Server 2012

The following features have been added to the IP Helper APIs on Windows 8 and Windows Server 2012.

A function that retrieves historical bandwidth estimates for a network connection. For more information, see:

-   [**GetIpNetworkConnectionBandwidthEstimates**](getipnetworkconnectionbandwidthestimates.md)

A structure that contains information on the available bandwidth estimates and associated variance as determined by the TCP/IP stack. For more information, see:

-   [**NL\_BANDWIDTH\_INFORMATION**](nl-bandwidth-information.md)

## Windows 7 and Windows Server 2008 R2

The following features have been added to the IP Helper APIs on Windows 7 and Windows Server 2008 R2.

Functions that convert an Ethernet address between a binary format and string format for the Ethernet MAC address. For more information, see:

-   [**RtlEthernetAddressToString**](rtlethernetaddresstostring.md)
-   [**RtlEthernetStringToAddress**](rtlethernetstringtoaddress.md)

## Windows Server 2008 and Windows Vista SP1

The following functions have been added to the IP Helper APIs on Windows Server 2008 and Windows Vista with Service Pack 1 (SP1).

A function that works with IPv4 and the Internet Control Message Protocol (ICMP). For more information, see:

-   [**IcmpSendEcho2Ex**](icmpsendecho2ex.md)

## Windows Vista

The following groups of functions have been added to the IP Helper APIs on Windows Vista and later.

Functions that work with both IPv6 and IPv4 for interface conversion. For more information, see:

-   [**ConvertInterfaceAliasToLuid**](convertinterfacealiastoluid.md)
-   [**ConvertInterfaceGuidToLuid**](convertinterfaceguidtoluid.md)
-   [**ConvertInterfaceIndexToLuid**](convertinterfaceindextoluid.md)
-   [**ConvertInterfaceLuidToGuid**](convertinterfaceluidtoguid.md)
-   [**ConvertInterfaceLuidToIndex**](convertinterfaceluidtoindex.md)
-   [**ConvertInterfaceLuidToNameA**](convertinterfaceluidtonamea.md)
-   [**ConvertInterfaceLuidToNameW**](convertinterfaceluidtonamew.md)
-   [**ConvertInterfaceNameToLuidA**](convertinterfacenametoluida.md)
-   [**ConvertInterfaceNameToLuidW**](convertinterfacenametoluidw.md)
-   [**if\_indextoname**](if-indextoname.md)
-   [**if\_nametoindex**](if-nametoindex.md)

Functions that work with both IPv6 and IPv4 for interface management. For more information, see:

-   [**GetIfEntry2**](getifentry2.md)
-   [**GetIfStackTable**](getifstacktable.md)
-   [**GetIfTable2**](getiftable2.md)
-   [**GetIfTable2Ex**](getiftable2ex.md)
-   [**GetInvertedIfStackTable**](getinvertedifstacktable.md)
-   [**GetIpInterfaceEntry**](getipinterfaceentry.md)
-   [**GetIpInterfaceTable**](getipinterfacetable.md)
-   [**InitializeIpInterfaceEntry**](initializeipinterfaceentry.md)
-   [**SetIpInterfaceEntry**](setipinterfaceentry.md)

Functions that work with both IPv6 and IPv4 for IP address management. For more information, see:

-   [**CreateAnycastIpAddressEntry**](createanycastipaddressentry.md)
-   [**CreateUnicastIpAddressEntry**](createunicastipaddressentry.md)
-   [**DeleteAnycastIpAddressEntry**](deleteanycastipaddressentry.md)
-   [**DeleteUnicastIpAddressEntry**](deleteunicastipaddressentry.md)
-   [**GetAnycastIpAddressEntry**](getanycastipaddressentry.md)
-   [**GetAnycastIpAddressTable**](getanycastipaddresstable.md)
-   [**GetMulticastIpAddressEntry**](getmulticastipaddressentry.md)
-   [**GetMulticastIpAddressTable**](getmulticastipaddresstable.md)
-   [**GetUnicastIpAddressEntry**](getunicastipaddressentry.md)
-   [**GetUnicastIpAddressTable**](getunicastipaddresstable.md)
-   [**InitializeUnicastIpAddressEntry**](initializeunicastipaddressentry.md)
-   [**NotifyStableUnicastIpAddressTable**](notifystableunicastipaddresstable.md)
-   [**SetUnicastIpAddressEntry**](setunicastipaddressentry.md)

A function that works with both IPv6 and IPv4 for IP table memory management. For more information, see:

-   [**FreeMibTable**](freemibtable.md)

Functions that work with both IPv6 and IPv4 for IP neighbor address management. For more information, see:

-   [**CreateIpNetEntry2**](createipnetentry2.md)
-   [**DeleteIpNetEntry2**](deleteipnetentry2.md)
-   [**FlushIpNetTable2**](flushipnettable2.md)
-   [**GetIpNetEntry2**](getipnetentry2.md)
-   [**GetIpNetTable2**](getipnettable2.md)
-   [**ResolveIpNetEntry2**](resolveipnetentry2.md)
-   [**ResolveNeighbor**](resolveneighbor.md)
-   [**SetIpNetEntry2**](setipnetentry2.md)

Functions that work with both IPv6 and IPv4 for IP path management. For more information, see:

-   [**FlushIpPathTable**](flushippathtable.md)
-   [**GetIpPathEntry**](getippathentry.md)
-   [**GetIpPathTable**](getippathtable.md)

Functions that work with both IPv6 and IPv4 for IP route management. For more information, see:

-   [**CreateIpForwardEntry2**](createipforwardentry2.md)
-   [**DeleteIpForwardEntry2**](deleteipforwardentry2.md)
-   [**GetBestRoute2**](getbestroute2.md)
-   [**GetIpForwardEntry2**](getipforwardentry2.md)
-   [**GetIpForwardTable2**](getipforwardtable2.md)
-   [**InitializeIpForwardEntry**](initializeipforwardentry.md)
-   [**SetIpForwardEntry2**](setipforwardentry2.md)
-   [**SetIpStatisticsEx**](setipstatisticsex.md)

Functions that work with both IPv6 and IPv4 for notification. For more information, see:

-   [**CancelMibChangeNotify2**](cancelmibchangenotify2.md)
-   [**NotifyIpInterfaceChange**](notifyipinterfacechange.md)
-   [**NotifyRouteChange2**](notifyroutechange2.md)
-   [**NotifyUnicastIpAddressChange**](notifyunicastipaddresschange.md)

Utility functions that work with IP addresses. For more information, see:

-   [**ConvertIpv4MaskToLength**](convertipv4masktolength.md)
-   [**ConvertLengthToIpv4Mask**](convertlengthtoipv4mask.md)
-   [**CreateSortedAddressPairs**](createsortedaddresspairs.md)
-   [**ParseNetworkString**](parsenetworkstring.md)

Functions that work with Transmission Control Protocol (TCP) and User Datagram Protocol (UDP) to retrieve the IPv6 or IPv4 TCP connection table or UDP listener table. For more information, see:

-   [**GetTcp6Table**](gettcp6table.md)
-   [**GetTcp6Table2**](gettcp6table2.md)
-   [**GetTcpTable2**](gettcptable2.md)
-   [**GetUdp6Table**](getudp6table.md)

Functions that work with Transmission Control Protocol (TCP) to retrieve extended TCP statistics on a connection. For more information, see:

-   [**GetPerTcp6ConnectionEStats**](getpertcp6connectionestats.md)
-   [**GetPerTcpConnectionEStats**](getpertcpconnectionestats.md)
-   [**SetPerTcp6ConnectionEStats**](setpertcp6connectionestats.md)
-   [**SetPerTcpConnectionEStats**](setpertcpconnectionestats.md)

New functions that work for Teredo IPv6 client management. For more information, see:

-   [**GetTeredoPort**](getteredoport.md)
-   [**NotifyTeredoPortChange**](notifyteredoportchange.md)
-   [**NotifyStableUnicastIpAddressTable**](notifystableunicastipaddresstable.md)

Utility functions that provide conversions between IP addresses and string representations of IP addresses. For more information, see:

-   [**RtlIpv4AddressToString**](rtlipv4addresstostring.md)
-   [**RtlIpv4AddressToStringEx**](rtlipv4addresstostringex.md)
-   [**RtlIpv4StringToAddress**](rtlipv4stringtoaddress.md)
-   [**RtlIpv4StringToAddressEx**](rtlipv4stringtoaddressex.md)
-   [**RtlIpv6AddressToString**](rtlipv6addresstostring.md)
-   [**RtlIpv6AddressToStringEx**](rtlipv6addresstostringex.md)
-   [**RtlIpv6StringToAddress**](rtlipv6stringtoaddress.md)
-   [**RtlIpv6StringToAddressEx**](rtlipv6stringtoaddressex.md)

Functions that provide persistent reservations for a consecutive block of TCP or UDP ports on the local computer. For more information, see:

-   [**CreatePersistentTcpPortReservation**](createpersistenttcpportreservation.md)
-   [**CreatePersistentUdpPortReservation**](createpersistentudpportreservation.md)
-   [**DeletePersistentTcpPortReservation**](deletepersistenttcpportreservation.md)
-   [**DeletePersistentUdpPortReservation**](deletepersistentudpportreservation.md)
-   [**LookupPersistentTcpPortReservation**](lookuppersistenttcpportreservation.md)
-   [**LookupPersistentUdpPortReservation**](lookuppersistentudpportreservation.md)

## Windows Server 2003

The following functions have been added to the IP Helper APIs on Windows Server 2003 and later:

-   [**CancelSecurityHealthChangeNotify**](cancelsecurityhealthchangenotify.md)
-   [**NotifySecurityHealthChange**](notifysecurityhealthchange.md)

## Windows XP SP2

The following functions have been added to the IP Helper APIs on Windows XP with Service Pack 2 (SP2) and later:

-   [**GetOwnerModuleFromTcpEntry**](getownermodulefromtcpentry.md)
-   [**GetOwnerModuleFromTcp6Entry**](getownermodulefromtcp6entry.md)
-   [**GetOwnerModuleFromUdpEntry**](getownermodulefromudpentry.md)
-   [**GetOwnerModuleFromUdp6Entry**](getownermodulefromudp6entry.md)

 

 



