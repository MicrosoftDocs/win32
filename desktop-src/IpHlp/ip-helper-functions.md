---
Description: The following functions retrieve and modify configuration settings for the TCP/IP transport on the local computer.
ms.assetid: 5f562470-f3e8-4305-a015-3a84cd09a1eb
title: IP Helper Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IP Helper Functions

The following functions retrieve and modify configuration settings for the TCP/IP transport on the local computer. The following categorical listing can help determine which collection of functions is best suited for a given task:

## Adapter Management

-   [**GetAdapterIndex**](/windows/win32/Iphlpapi/nf-iphlpapi-getadapterindex?branch=master)
-   [**GetAdaptersAddresses**](/windows/win32/Iphlpapi/nf-iphlpapi-getadaptersaddresses?branch=master)
-   [**GetAdaptersInfo**](/windows/win32/Iphlpapi/nf-iphlpapi-getadaptersinfo?branch=master)
-   [**GetPerAdapterInfo**](/windows/win32/Iphlpapi/nf-iphlpapi-getperadapterinfo?branch=master)
-   [**GetUniDirectionalAdapterInfo**](/windows/win32/Iphlpapi/nf-iphlpapi-getunidirectionaladapterinfo?branch=master)

## Address Resolution Protocol (ARP) Management

-   [**CreateIpNetEntry**](/windows/win32/Iphlpapi/nf-iphlpapi-createipnetentry?branch=master)
-   [**CreateProxyArpEntry**](/windows/win32/Iphlpapi/nf-iphlpapi-createproxyarpentry?branch=master)
-   [**DeleteIpNetEntry**](/windows/win32/Iphlpapi/nf-iphlpapi-deleteipnetentry?branch=master)
-   [**DeleteProxyArpEntry**](/windows/win32/Iphlpapi/nf-iphlpapi-deleteproxyarpentry?branch=master)
-   [**FlushIpNetTable**](/windows/win32/Iphlpapi/nf-iphlpapi-flushipnettable?branch=master)
-   [**GetIpNetTable**](/windows/win32/Iphlpapi/nf-iphlpapi-getipnettable?branch=master)
-   [**SendARP**](/windows/win32/Iphlpapi/nf-iphlpapi-sendarp?branch=master)
-   [**SetIpNetEntry**](/windows/win32/Iphlpapi/nf-iphlpapi-setipnetentry?branch=master)

## Interface Conversion

-   [**ConvertInterfaceAliasToLuid**](/windows/win32/Netioapi/nf-netioapi-convertinterfacealiastoluid?branch=master)
-   [**ConvertInterfaceGuidToLuid**](/windows/win32/Netioapi/nf-netioapi-convertinterfaceguidtoluid?branch=master)
-   [**ConvertInterfaceIndexToLuid**](/windows/win32/Netioapi/nf-netioapi-convertinterfaceindextoluid?branch=master)
-   [**ConvertInterfaceLuidToAlias**](/windows/win32/Netioapi/nf-netioapi-convertinterfaceluidtoalias?branch=master)
-   [**ConvertInterfaceLuidToGuid**](/windows/win32/Netioapi/nf-netioapi-convertinterfaceluidtoguid?branch=master)
-   [**ConvertInterfaceLuidToIndex**](/windows/win32/Netioapi/nf-netioapi-convertinterfaceluidtoindex?branch=master)
-   [**ConvertInterfaceLuidToNameA**](/windows/win32/Netioapi/nf-netioapi-convertinterfaceluidtonamea?branch=master)
-   [**ConvertInterfaceLuidToNameW**](/windows/win32/Netioapi/nf-netioapi-convertinterfaceluidtonamew?branch=master)
-   [**ConvertInterfaceNameToLuidA**](/windows/win32/Netioapi/nf-netioapi-convertinterfacenametoluida?branch=master)
-   [**ConvertInterfaceNameToLuidW**](/windows/win32/Netioapi/nf-netioapi-convertinterfacenametoluidw?branch=master)
-   [**if\_indextoname**](/windows/win32/Netioapi/nf-netioapi-if_indextoname?branch=master)
-   [**if\_nametoindex**](/windows/win32/Netioapi/nf-netioapi-if_nametoindex?branch=master)

## Interface Management

-   [**GetFriendlyIfIndex**](/windows/win32/Iphlpapi/nf-iphlpapi-getfriendlyifindex?branch=master)
-   [**GetIfEntry**](/windows/win32/Iphlpapi/nf-iphlpapi-getifentry?branch=master)
-   [**GetIfEntry2**](/windows/win32/Netioapi/nf-netioapi-getifentry2?branch=master)
-   [**GetIfEntry2Ex**](/windows/win32/Netioapi/nf-netioapi-getifentry2ex?branch=master)
-   [**GetIfStackTable**](/windows/win32/Netioapi/nf-netioapi-getifstacktable?branch=master)
-   [**GetIfTable**](/windows/win32/Iphlpapi/nf-iphlpapi-getiftable?branch=master)
-   [**GetIfTable2**](/windows/win32/Netioapi/nf-netioapi-getiftable2?branch=master)
-   [**GetIfTable2Ex**](/windows/win32/Netioapi/nf-netioapi-getiftable2ex?branch=master)
-   [**GetInterfaceInfo**](/windows/win32/Iphlpapi/nf-iphlpapi-getinterfaceinfo?branch=master)
-   [**GetInvertedIfStackTable**](/windows/win32/Netioapi/nf-netioapi-getinvertedifstacktable?branch=master)
-   [**GetIpInterfaceEntry**](/windows/win32/Netioapi/nf-netioapi-getipinterfaceentry?branch=master)
-   [**GetIpInterfaceTable**](/windows/win32/Netioapi/nf-netioapi-getipinterfacetable?branch=master)
-   [**GetNumberOfInterfaces**](/windows/win32/Iphlpapi/nf-iphlpapi-getnumberofinterfaces?branch=master)
-   [**InitializeIpInterfaceEntry**](/windows/win32/Netioapi/nf-netioapi-initializeipinterfaceentry?branch=master)
-   [**SetIfEntry**](/windows/win32/Iphlpapi/nf-iphlpapi-setifentry?branch=master)
-   [**SetIpInterfaceEntry**](/windows/win32/Netioapi/nf-netioapi-setipinterfaceentry?branch=master)

## Internet Protocol (IP) and Internet Control Message Protocol (ICMP)

-   [**GetIcmpStatistics**](/windows/win32/Iphlpapi/nf-iphlpapi-geticmpstatistics?branch=master)
-   [**GetIpStatistics**](/windows/win32/Iphlpapi/nf-iphlpapi-getipstatistics?branch=master)
-   [**Icmp6CreateFile**](/windows/win32/Icmpapi/nf-icmpapi-icmp6createfile?branch=master)
-   [**Icmp6ParseReplies**](/windows/win32/Icmpapi/nf-icmpapi-icmp6parsereplies?branch=master)
-   [**Icmp6SendEcho2**](/windows/win32/Icmpapi/nf-icmpapi-icmp6sendecho2?branch=master)
-   [**IcmpCloseHandle**](/windows/win32/Icmpapi/nf-icmpapi-icmpclosehandle?branch=master)
-   [**IcmpCreateFile**](/windows/win32/Icmpapi/nf-icmpapi-icmpcreatefile?branch=master)
-   [**IcmpParseReplies**](/windows/win32/Icmpapi/nf-icmpapi-icmpparsereplies?branch=master)
-   [**IcmpSendEcho**](/windows/win32/Icmpapi/nf-icmpapi-icmpsendecho?branch=master)
-   [**IcmpSendEcho2**](/windows/win32/Icmpapi/nf-icmpapi-icmpsendecho2?branch=master)
-   [**IcmpSendEcho2Ex**](/windows/win32/Icmpapi/nf-icmpapi-icmpsendecho2ex?branch=master)
-   [**SetIpTTL**](/windows/win32/Iphlpapi/nf-iphlpapi-setipttl?branch=master)

## IP Address Management

-   [**AddIPAddress**](/windows/win32/Iphlpapi/nf-iphlpapi-addipaddress?branch=master)
-   [**CreateAnycastIpAddressEntry**](/windows/win32/Netioapi/nf-netioapi-createanycastipaddressentry?branch=master)
-   [**CreateUnicastIpAddressEntry**](/windows/win32/Netioapi/nf-netioapi-createunicastipaddressentry?branch=master)
-   [**DeleteIPAddress**](/windows/win32/Iphlpapi/nf-iphlpapi-deleteipaddress?branch=master)
-   [**DeleteAnycastIpAddressEntry**](/windows/win32/Netioapi/nf-netioapi-deleteanycastipaddressentry?branch=master)
-   [**DeleteUnicastIpAddressEntry**](/windows/win32/Netioapi/nf-netioapi-deleteunicastipaddressentry?branch=master)
-   [**GetAnycastIpAddressEntry**](/windows/win32/Netioapi/nf-netioapi-getanycastipaddressentry?branch=master)
-   [**GetAnycastIpAddressTable**](/windows/win32/Netioapi/nf-netioapi-getanycastipaddresstable?branch=master)
-   [**GetIpAddrTable**](/windows/win32/Iphlpapi/nf-iphlpapi-getipaddrtable?branch=master)
-   [**GetMulticastIpAddressEntry**](/windows/win32/Netioapi/nf-netioapi-getmulticastipaddressentry?branch=master)
-   [**GetMulticastIpAddressTable**](/windows/win32/Netioapi/nf-netioapi-getmulticastipaddresstable?branch=master)
-   [**GetUnicastIpAddressEntry**](/windows/win32/Netioapi/nf-netioapi-getunicastipaddressentry?branch=master)
-   [**GetUnicastIpAddressTable**](/windows/win32/Netioapi/nf-netioapi-getunicastipaddresstable?branch=master)
-   [**InitializeUnicastIpAddressEntry**](/windows/win32/Netioapi/nf-netioapi-initializeunicastipaddressentry?branch=master)
-   [**IpReleaseAddress**](/windows/win32/Iphlpapi/nf-iphlpapi-ipreleaseaddress?branch=master)
-   [**IpRenewAddress**](/windows/win32/Iphlpapi/nf-iphlpapi-iprenewaddress?branch=master)
-   [**NotifyStableUnicastIpAddressTable**](/windows/win32/Netioapi/nf-netioapi-notifystableunicastipaddresstable?branch=master)
-   [**SetUnicastIpAddressEntry**](/windows/win32/Netioapi/nf-netioapi-setunicastipaddressentry?branch=master)

## IP Address String Conversion

-   [**RtlIpv4AddressToString**](/windows/win32/ip2string/nf-ip2string-rtlipv4addresstostringa?branch=master)
-   [**RtlIpv4AddressToStringEx**](/windows/win32/ip2string/nf-ip2string-rtlipv4addresstostringexw?branch=master)
-   [**RtlIpv4StringToAddress**](/windows/win32/ip2string/nf-ip2string-rtlipv4stringtoaddressa?branch=master)
-   [**RtlIpv4StringToAddressEx**](/windows/win32/ip2string/nf-ip2string-rtlipv4stringtoaddressexw?branch=master)
-   [**RtlIpv6AddressToString**](/windows/win32/ip2string/nf-ip2string-rtlipv6addresstostringa?branch=master)
-   [**RtlIpv6AddressToStringEx**](/windows/win32/ip2string/nf-ip2string-rtlipv6addresstostringexw?branch=master)
-   [**RtlIpv6StringToAddress**](/windows/win32/ip2string/nf-ip2string-rtlipv6stringtoaddressa?branch=master)
-   [**RtlIpv6StringToAddressEx**](/windows/win32/ip2string/nf-ip2string-rtlipv6stringtoaddressexw?branch=master)

## IP Neighbor Address Management

-   [**CreateIpNetEntry2**](/windows/win32/Netioapi/nf-netioapi-createipnetentry2?branch=master)
-   [**DeleteIpNetEntry2**](/windows/win32/Netioapi/nf-netioapi-deleteipnetentry2?branch=master)
-   [**FlushIpNetTable2**](/windows/win32/Netioapi/nf-netioapi-flushipnettable2?branch=master)
-   [**GetIpNetEntry2**](/windows/win32/Netioapi/nf-netioapi-getipnetentry2?branch=master)
-   [**GetIpNetTable2**](/windows/win32/Netioapi/nf-netioapi-getipnettable2?branch=master)
-   [**ResolveIpNetEntry2**](/windows/win32/Netioapi/nf-netioapi-resolveipnetentry2?branch=master)
-   [**ResolveNeighbor**](/windows/win32/Iphlpapi/nf-iphlpapi-resolveneighbor?branch=master)
-   [**SetIpNetEntry2**](/windows/win32/Netioapi/nf-netioapi-setipnetentry2?branch=master)

## IP Path Management

-   [**FlushIpPathTable**](/windows/win32/Netioapi/nf-netioapi-flushippathtable?branch=master)
-   [**GetIpPathEntry**](/windows/win32/Netioapi/nf-netioapi-getippathentry?branch=master)
-   [**GetIpPathTable**](/windows/win32/Netioapi/nf-netioapi-getippathtable?branch=master)

## IP Route Management

-   [**CreateIpForwardEntry**](/windows/win32/Iphlpapi/nf-iphlpapi-createipforwardentry?branch=master)
-   [**CreateIpForwardEntry2**](/windows/win32/Netioapi/nf-netioapi-createipforwardentry2?branch=master)
-   [**DeleteIpForwardEntry**](/windows/win32/Iphlpapi/nf-iphlpapi-deleteipforwardentry?branch=master)
-   [**DeleteIpForwardEntry2**](/windows/win32/Netioapi/nf-netioapi-deleteipforwardentry2?branch=master)
-   [**EnableRouter**](/windows/win32/Iphlpapi/nf-iphlpapi-enablerouter?branch=master)
-   [**GetBestInterface**](/windows/win32/Iphlpapi/nf-iphlpapi-getbestinterface?branch=master)
-   [**GetBestInterfaceEx**](/windows/win32/Iphlpapi/nf-iphlpapi-getbestinterfaceex?branch=master)
-   [**GetBestRoute**](/windows/win32/Iphlpapi/nf-iphlpapi-getbestroute?branch=master)
-   [**GetBestRoute2**](/windows/win32/Netioapi/nf-netioapi-getbestroute2?branch=master)
-   [**GetIpForwardEntry2**](/windows/win32/Netioapi/nf-netioapi-getipforwardentry2?branch=master)
-   [**GetIpForwardTable**](/windows/win32/Iphlpapi/nf-iphlpapi-getipforwardtable?branch=master)
-   [**GetIpForwardTable2**](/windows/win32/Netioapi/nf-netioapi-getipforwardtable2?branch=master)
-   [**GetRTTAndHopCount**](/windows/win32/Iphlpapi/nf-iphlpapi-getrttandhopcount?branch=master)
-   [**InitializeIpForwardEntry**](/windows/win32/Netioapi/nf-netioapi-initializeipforwardentry?branch=master)
-   [**SetIpForwardEntry**](/windows/win32/Iphlpapi/nf-iphlpapi-setipforwardentry?branch=master)
-   [**SetIpForwardEntry2**](/windows/win32/Netioapi/nf-netioapi-setipforwardentry2?branch=master)
-   [**SetIpStatistics**](/windows/win32/Iphlpapi/nf-iphlpapi-setipstatistics?branch=master)
-   [**SetIpStatisticsEx**](/windows/win32/Iphlpapi/nf-iphlpapi-setipstatisticsex?branch=master)
-   [**UnenableRouter**](/windows/win32/Iphlpapi/nf-iphlpapi-unenablerouter?branch=master)

## IP Table Memory Management

-   [**FreeMibTable**](/windows/win32/Netioapi/nf-netioapi-freemibtable?branch=master)

## IP Utility

-   [**ConvertIpv4MaskToLength**](/windows/win32/Netioapi/nf-netioapi-convertipv4masktolength?branch=master)
-   [**ConvertLengthToIpv4Mask**](/windows/win32/Netioapi/nf-netioapi-convertlengthtoipv4mask?branch=master)
-   [**CreateSortedAddressPairs**](/windows/win32/Netioapi/nf-netioapi-createsortedaddresspairs?branch=master)
-   [**ParseNetworkString**](/windows/win32/Iphlpapi/nf-iphlpapi-parsenetworkstring?branch=master)

## Network Configuration

-   [**GetNetworkParams**](/windows/win32/Iphlpapi/nf-iphlpapi-getnetworkparams?branch=master)

## Notification

-   [**CancelMibChangeNotify2**](/windows/win32/Netioapi/nf-netioapi-cancelmibchangenotify2?branch=master)
-   [**NotifyAddrChange**](/windows/win32/Iphlpapi/nf-iphlpapi-notifyaddrchange?branch=master)
-   [**NotifyIpInterfaceChange**](/windows/win32/Netioapi/nf-netioapi-notifyipinterfacechange?branch=master)
-   [**NotifyRouteChange**](/windows/win32/Iphlpapi/nf-iphlpapi-notifyroutechange?branch=master)
-   [**NotifyRouteChange2**](/windows/win32/Netioapi/nf-netioapi-notifyroutechange2?branch=master)
-   [**NotifyUnicastIpAddressChange**](/windows/win32/Netioapi/nf-netioapi-notifyunicastipaddresschange?branch=master)

## Persistent Port Reservarion

-   [**CreatePersistentTcpPortReservation**](/windows/win32/Iphlpapi/nf-iphlpapi-createpersistenttcpportreservation?branch=master)
-   [**CreatePersistentUdpPortReservation**](/windows/win32/Iphlpapi/nf-iphlpapi-createpersistentudpportreservation?branch=master)
-   [**DeletePersistentTcpPortReservation**](/windows/win32/Iphlpapi/nf-iphlpapi-deletepersistenttcpportreservation?branch=master)
-   [**DeletePersistentUdpPortReservation**](/windows/win32/Iphlpapi/nf-iphlpapi-deletepersistentudpportreservation?branch=master)
-   [**LookupPersistentTcpPortReservation**](/windows/win32/Iphlpapi/nf-iphlpapi-lookuppersistenttcpportreservation?branch=master)
-   [**LookupPersistentUdpPortReservation**](/windows/win32/Iphlpapi/nf-iphlpapi-lookuppersistentudpportreservation?branch=master)

## Security Health

-   [**CancelSecurityHealthChangeNotify**](/windows/win32/Iphlpapi/?branch=master)
-   [**NotifySecurityHealthChange**](/windows/win32/Iphlpapi/?branch=master)

These functions are defined only on Windows Server 2003.

> [!Note]  
> These functions are not available Windows Vista and Windows Server 2008.

 

## Teredo IPv6 Client Management

-   [**GetTeredoPort**](/windows/win32/Netioapi/nf-netioapi-getteredoport?branch=master)
-   [**NotifyTeredoPortChange**](/windows/win32/Netioapi/nf-netioapi-notifyteredoportchange?branch=master)
-   [**NotifyStableUnicastIpAddressTable**](/windows/win32/Netioapi/nf-netioapi-notifystableunicastipaddresstable?branch=master)

## Transmission Control Protocol (TCP) and User Datagram Protocol (UDP)

-   [**GetExtendedTcpTable**](/windows/win32/Iphlpapi/nf-iphlpapi-getextendedtcptable?branch=master)
-   [**GetExtendedUdpTable**](/windows/win32/Iphlpapi/nf-iphlpapi-getextendedudptable?branch=master)
-   [**GetOwnerModuleFromTcp6Entry**](/windows/win32/Iphlpapi/nf-iphlpapi-getownermodulefromtcp6entry?branch=master)
-   [**GetOwnerModuleFromTcpEntry**](/windows/win32/Iphlpapi/nf-iphlpapi-getownermodulefromtcpentry?branch=master)
-   [**GetOwnerModuleFromUdp6Entry**](/windows/win32/Iphlpapi/nf-iphlpapi-getownermodulefromudp6entry?branch=master)
-   [**GetOwnerModuleFromUdpEntry**](/windows/win32/Iphlpapi/nf-iphlpapi-getownermodulefromudpentry?branch=master)
-   [**GetPerTcp6ConnectionEStats**](/windows/win32/Iphlpapi/nf-iphlpapi-getpertcp6connectionestats?branch=master)
-   [**GetPerTcpConnectionEStats**](/windows/win32/Iphlpapi/nf-iphlpapi-getpertcpconnectionestats?branch=master)
-   [**GetTcpStatistics**](/windows/win32/Iphlpapi/nf-iphlpapi-gettcpstatistics?branch=master)
-   [**GetTcpStatisticsEx**](/windows/win32/Iphlpapi/nf-iphlpapi-gettcpstatisticsex?branch=master)
-   [**GetTcpStatisticsEx2**](/windows/win32/Iphlpapi/nf-iphlpapi-gettcpstatisticsex2?branch=master)
-   [**GetTcp6Table**](/windows/win32/Iphlpapi/nf-iphlpapi-gettcp6table?branch=master)
-   [**GetTcp6Table2**](/windows/win32/Iphlpapi/nf-iphlpapi-gettcp6table2?branch=master)
-   [**GetTcpTable**](/windows/win32/Iphlpapi/nf-iphlpapi-gettcptable?branch=master)
-   [**GetTcpTable2**](/windows/win32/Iphlpapi/nf-iphlpapi-gettcptable2?branch=master)
-   [**SetPerTcp6ConnectionEStats**](/windows/win32/Iphlpapi/nf-iphlpapi-setpertcp6connectionestats?branch=master)
-   [**SetPerTcpConnectionEStats**](/windows/win32/Iphlpapi/nf-iphlpapi-setpertcpconnectionestats?branch=master)
-   [**SetTcpEntry**](/windows/win32/Iphlpapi/nf-iphlpapi-settcpentry?branch=master)
-   [**GetUdp6Table**](/windows/win32/Iphlpapi/nf-iphlpapi-getudp6table?branch=master)
-   [**GetUdpStatistics**](/windows/win32/Iphlpapi/nf-iphlpapi-getudpstatistics?branch=master)
-   [**GetUdpStatisticsEx**](/windows/win32/Iphlpapi/nf-iphlpapi-getudpstatisticsex?branch=master)
-   [**GetUdpStatisticsEx2**](/windows/win32/Iphlpapi/nf-iphlpapi-getudpstatisticsex2?branch=master)
-   [**GetUdpTable**](/windows/win32/Iphlpapi/nf-iphlpapi-getudptable?branch=master)

## Deprecated APIs

> [!Note]  
> These functions are deprecated and not supported by Microsoft.

 

-   [**AllocateAndGetTcpExTableFromStack**](/windows/win32/Iphlpapi/nf-iphlpapi-allocateandgettcpextablefromstack?branch=master)
-   [**AllocateAndGetUdpExTableFromStack**](/windows/win32/Iphlpapi/nf-iphlpapi-allocateandgetudpextablefromstack?branch=master)

 

 



