---
Description: The following functions retrieve and modify configuration settings for the TCP/IP transport on the local computer.
ms.assetid: 5f562470-f3e8-4305-a015-3a84cd09a1eb
title: IP Helper Functions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IP Helper Functions

The following functions retrieve and modify configuration settings for the TCP/IP transport on the local computer. The following categorical listing can help determine which collection of functions is best suited for a given task:

## Adapter Management

-   [**GetAdapterIndex**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getadapterindex)
-   [**GetAdaptersAddresses**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getadaptersaddresses)
-   [**GetAdaptersInfo**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getadaptersinfo)
-   [**GetPerAdapterInfo**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getperadapterinfo)
-   [**GetUniDirectionalAdapterInfo**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getunidirectionaladapterinfo)

## Address Resolution Protocol (ARP) Management

-   [**CreateIpNetEntry**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-createipnetentry)
-   [**CreateProxyArpEntry**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-createproxyarpentry)
-   [**DeleteIpNetEntry**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-deleteipnetentry)
-   [**DeleteProxyArpEntry**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-deleteproxyarpentry)
-   [**FlushIpNetTable**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-flushipnettable)
-   [**GetIpNetTable**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getipnettable)
-   [**SendARP**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-sendarp)
-   [**SetIpNetEntry**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-setipnetentry)

## Interface Conversion

-   [**ConvertInterfaceAliasToLuid**](/windows/desktop/api/Netioapi/nf-netioapi-convertinterfacealiastoluid)
-   [**ConvertInterfaceGuidToLuid**](/windows/desktop/api/Netioapi/nf-netioapi-convertinterfaceguidtoluid)
-   [**ConvertInterfaceIndexToLuid**](/windows/desktop/api/Netioapi/nf-netioapi-convertinterfaceindextoluid)
-   [**ConvertInterfaceLuidToAlias**](/windows/desktop/api/Netioapi/nf-netioapi-convertinterfaceluidtoalias)
-   [**ConvertInterfaceLuidToGuid**](/windows/desktop/api/Netioapi/nf-netioapi-convertinterfaceluidtoguid)
-   [**ConvertInterfaceLuidToIndex**](/windows/desktop/api/Netioapi/nf-netioapi-convertinterfaceluidtoindex)
-   [**ConvertInterfaceLuidToNameA**](/windows/desktop/api/Netioapi/nf-netioapi-convertinterfaceluidtonamea)
-   [**ConvertInterfaceLuidToNameW**](/windows/desktop/api/Netioapi/nf-netioapi-convertinterfaceluidtonamew)
-   [**ConvertInterfaceNameToLuidA**](/windows/desktop/api/Netioapi/nf-netioapi-convertinterfacenametoluida)
-   [**ConvertInterfaceNameToLuidW**](/windows/desktop/api/Netioapi/nf-netioapi-convertinterfacenametoluidw)
-   [**if\_indextoname**](/windows/desktop/api/Netioapi/nf-netioapi-if_indextoname)
-   [**if\_nametoindex**](/windows/desktop/api/Netioapi/nf-netioapi-if_nametoindex)

## Interface Management

-   [**GetFriendlyIfIndex**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getfriendlyifindex)
-   [**GetIfEntry**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getifentry)
-   [**GetIfEntry2**](/windows/desktop/api/Netioapi/nf-netioapi-getifentry2)
-   [**GetIfEntry2Ex**](/windows/desktop/api/Netioapi/nf-netioapi-getifentry2ex)
-   [**GetIfStackTable**](/windows/desktop/api/Netioapi/nf-netioapi-getifstacktable)
-   [**GetIfTable**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getiftable)
-   [**GetIfTable2**](/windows/desktop/api/Netioapi/nf-netioapi-getiftable2)
-   [**GetIfTable2Ex**](/windows/desktop/api/Netioapi/nf-netioapi-getiftable2ex)
-   [**GetInterfaceInfo**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getinterfaceinfo)
-   [**GetInvertedIfStackTable**](/windows/desktop/api/Netioapi/nf-netioapi-getinvertedifstacktable)
-   [**GetIpInterfaceEntry**](/windows/desktop/api/Netioapi/nf-netioapi-getipinterfaceentry)
-   [**GetIpInterfaceTable**](/windows/desktop/api/Netioapi/nf-netioapi-getipinterfacetable)
-   [**GetNumberOfInterfaces**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getnumberofinterfaces)
-   [**InitializeIpInterfaceEntry**](/windows/desktop/api/Netioapi/nf-netioapi-initializeipinterfaceentry)
-   [**SetIfEntry**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-setifentry)
-   [**SetIpInterfaceEntry**](/windows/desktop/api/Netioapi/nf-netioapi-setipinterfaceentry)

## Internet Protocol (IP) and Internet Control Message Protocol (ICMP)

-   [**GetIcmpStatistics**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-geticmpstatistics)
-   [**GetIpStatistics**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getipstatistics)
-   [**Icmp6CreateFile**](/windows/desktop/api/Icmpapi/nf-icmpapi-icmp6createfile)
-   [**Icmp6ParseReplies**](/windows/desktop/api/Icmpapi/nf-icmpapi-icmp6parsereplies)
-   [**Icmp6SendEcho2**](/windows/desktop/api/Icmpapi/nf-icmpapi-icmp6sendecho2)
-   [**IcmpCloseHandle**](/windows/desktop/api/Icmpapi/nf-icmpapi-icmpclosehandle)
-   [**IcmpCreateFile**](/windows/desktop/api/Icmpapi/nf-icmpapi-icmpcreatefile)
-   [**IcmpParseReplies**](/windows/desktop/api/Icmpapi/nf-icmpapi-icmpparsereplies)
-   [**IcmpSendEcho**](/windows/desktop/api/Icmpapi/nf-icmpapi-icmpsendecho)
-   [**IcmpSendEcho2**](/windows/desktop/api/Icmpapi/nf-icmpapi-icmpsendecho2)
-   [**IcmpSendEcho2Ex**](/windows/desktop/api/Icmpapi/nf-icmpapi-icmpsendecho2ex)
-   [**SetIpTTL**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-setipttl)

## IP Address Management

-   [**AddIPAddress**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-addipaddress)
-   [**CreateAnycastIpAddressEntry**](/windows/desktop/api/Netioapi/nf-netioapi-createanycastipaddressentry)
-   [**CreateUnicastIpAddressEntry**](/windows/desktop/api/Netioapi/nf-netioapi-createunicastipaddressentry)
-   [**DeleteIPAddress**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-deleteipaddress)
-   [**DeleteAnycastIpAddressEntry**](/windows/desktop/api/Netioapi/nf-netioapi-deleteanycastipaddressentry)
-   [**DeleteUnicastIpAddressEntry**](/windows/desktop/api/Netioapi/nf-netioapi-deleteunicastipaddressentry)
-   [**GetAnycastIpAddressEntry**](/windows/desktop/api/Netioapi/nf-netioapi-getanycastipaddressentry)
-   [**GetAnycastIpAddressTable**](/windows/desktop/api/Netioapi/nf-netioapi-getanycastipaddresstable)
-   [**GetIpAddrTable**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getipaddrtable)
-   [**GetMulticastIpAddressEntry**](/windows/desktop/api/Netioapi/nf-netioapi-getmulticastipaddressentry)
-   [**GetMulticastIpAddressTable**](/windows/desktop/api/Netioapi/nf-netioapi-getmulticastipaddresstable)
-   [**GetUnicastIpAddressEntry**](/windows/desktop/api/Netioapi/nf-netioapi-getunicastipaddressentry)
-   [**GetUnicastIpAddressTable**](/windows/desktop/api/Netioapi/nf-netioapi-getunicastipaddresstable)
-   [**InitializeUnicastIpAddressEntry**](/windows/desktop/api/Netioapi/nf-netioapi-initializeunicastipaddressentry)
-   [**IpReleaseAddress**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-ipreleaseaddress)
-   [**IpRenewAddress**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-iprenewaddress)
-   [**NotifyStableUnicastIpAddressTable**](/windows/desktop/api/Netioapi/nf-netioapi-notifystableunicastipaddresstable)
-   [**SetUnicastIpAddressEntry**](/windows/desktop/api/Netioapi/nf-netioapi-setunicastipaddressentry)

## IP Address String Conversion

-   [**RtlIpv4AddressToString**](/windows/desktop/api/ip2string/nf-ip2string-rtlipv4addresstostringa)
-   [**RtlIpv4AddressToStringEx**](/windows/desktop/api/ip2string/nf-ip2string-rtlipv4addresstostringexw)
-   [**RtlIpv4StringToAddress**](/windows/desktop/api/ip2string/nf-ip2string-rtlipv4stringtoaddressa)
-   [**RtlIpv4StringToAddressEx**](/windows/desktop/api/ip2string/nf-ip2string-rtlipv4stringtoaddressexw)
-   [**RtlIpv6AddressToString**](/windows/desktop/api/ip2string/nf-ip2string-rtlipv6addresstostringa)
-   [**RtlIpv6AddressToStringEx**](/windows/desktop/api/ip2string/nf-ip2string-rtlipv6addresstostringexw)
-   [**RtlIpv6StringToAddress**](/windows/desktop/api/ip2string/nf-ip2string-rtlipv6stringtoaddressa)
-   [**RtlIpv6StringToAddressEx**](/windows/desktop/api/ip2string/nf-ip2string-rtlipv6stringtoaddressexw)

## IP Neighbor Address Management

-   [**CreateIpNetEntry2**](/windows/desktop/api/Netioapi/nf-netioapi-createipnetentry2)
-   [**DeleteIpNetEntry2**](/windows/desktop/api/Netioapi/nf-netioapi-deleteipnetentry2)
-   [**FlushIpNetTable2**](/windows/desktop/api/Netioapi/nf-netioapi-flushipnettable2)
-   [**GetIpNetEntry2**](/windows/desktop/api/Netioapi/nf-netioapi-getipnetentry2)
-   [**GetIpNetTable2**](/windows/desktop/api/Netioapi/nf-netioapi-getipnettable2)
-   [**ResolveIpNetEntry2**](/windows/desktop/api/Netioapi/nf-netioapi-resolveipnetentry2)
-   [**ResolveNeighbor**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-resolveneighbor)
-   [**SetIpNetEntry2**](/windows/desktop/api/Netioapi/nf-netioapi-setipnetentry2)

## IP Path Management

-   [**FlushIpPathTable**](/windows/desktop/api/Netioapi/nf-netioapi-flushippathtable)
-   [**GetIpPathEntry**](/windows/desktop/api/Netioapi/nf-netioapi-getippathentry)
-   [**GetIpPathTable**](/windows/desktop/api/Netioapi/nf-netioapi-getippathtable)

## IP Route Management

-   [**CreateIpForwardEntry**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-createipforwardentry)
-   [**CreateIpForwardEntry2**](/windows/desktop/api/Netioapi/nf-netioapi-createipforwardentry2)
-   [**DeleteIpForwardEntry**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-deleteipforwardentry)
-   [**DeleteIpForwardEntry2**](/windows/desktop/api/Netioapi/nf-netioapi-deleteipforwardentry2)
-   [**EnableRouter**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-enablerouter)
-   [**GetBestInterface**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getbestinterface)
-   [**GetBestInterfaceEx**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getbestinterfaceex)
-   [**GetBestRoute**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getbestroute)
-   [**GetBestRoute2**](/windows/desktop/api/Netioapi/nf-netioapi-getbestroute2)
-   [**GetIpForwardEntry2**](/windows/desktop/api/Netioapi/nf-netioapi-getipforwardentry2)
-   [**GetIpForwardTable**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getipforwardtable)
-   [**GetIpForwardTable2**](/windows/desktop/api/Netioapi/nf-netioapi-getipforwardtable2)
-   [**GetRTTAndHopCount**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getrttandhopcount)
-   [**InitializeIpForwardEntry**](/windows/desktop/api/Netioapi/nf-netioapi-initializeipforwardentry)
-   [**SetIpForwardEntry**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-setipforwardentry)
-   [**SetIpForwardEntry2**](/windows/desktop/api/Netioapi/nf-netioapi-setipforwardentry2)
-   [**SetIpStatistics**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-setipstatistics)
-   [**SetIpStatisticsEx**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-setipstatisticsex)
-   [**UnenableRouter**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-unenablerouter)

## IP Table Memory Management

-   [**FreeMibTable**](/windows/desktop/api/Netioapi/nf-netioapi-freemibtable)

## IP Utility

-   [**ConvertIpv4MaskToLength**](/windows/desktop/api/Netioapi/nf-netioapi-convertipv4masktolength)
-   [**ConvertLengthToIpv4Mask**](/windows/desktop/api/Netioapi/nf-netioapi-convertlengthtoipv4mask)
-   [**CreateSortedAddressPairs**](/windows/desktop/api/Netioapi/nf-netioapi-createsortedaddresspairs)
-   [**ParseNetworkString**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-parsenetworkstring)

## Network Configuration

-   [**GetNetworkParams**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getnetworkparams)

## Notification

-   [**CancelMibChangeNotify2**](/windows/desktop/api/Netioapi/nf-netioapi-cancelmibchangenotify2)
-   [**NotifyAddrChange**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-notifyaddrchange)
-   [**NotifyIpInterfaceChange**](/windows/desktop/api/Netioapi/nf-netioapi-notifyipinterfacechange)
-   [**NotifyRouteChange**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-notifyroutechange)
-   [**NotifyRouteChange2**](/windows/desktop/api/Netioapi/nf-netioapi-notifyroutechange2)
-   [**NotifyUnicastIpAddressChange**](/windows/desktop/api/Netioapi/nf-netioapi-notifyunicastipaddresschange)

## Persistent Port Reservarion

-   [**CreatePersistentTcpPortReservation**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-createpersistenttcpportreservation)
-   [**CreatePersistentUdpPortReservation**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-createpersistentudpportreservation)
-   [**DeletePersistentTcpPortReservation**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-deletepersistenttcpportreservation)
-   [**DeletePersistentUdpPortReservation**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-deletepersistentudpportreservation)
-   [**LookupPersistentTcpPortReservation**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-lookuppersistenttcpportreservation)
-   [**LookupPersistentUdpPortReservation**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-lookuppersistentudpportreservation)

## Security Health

-   [**CancelSecurityHealthChangeNotify**](/windows/desktop/api/Iphlpapi/)
-   [**NotifySecurityHealthChange**](/windows/desktop/api/Iphlpapi/)

These functions are defined only on Windows Server 2003.

> [!Note]  
> These functions are not available Windows Vista and Windows Server 2008.

 

## Teredo IPv6 Client Management

-   [**GetTeredoPort**](/windows/desktop/api/Netioapi/nf-netioapi-getteredoport)
-   [**NotifyTeredoPortChange**](/windows/desktop/api/Netioapi/nf-netioapi-notifyteredoportchange)
-   [**NotifyStableUnicastIpAddressTable**](/windows/desktop/api/Netioapi/nf-netioapi-notifystableunicastipaddresstable)

## Transmission Control Protocol (TCP) and User Datagram Protocol (UDP)

-   [**GetExtendedTcpTable**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getextendedtcptable)
-   [**GetExtendedUdpTable**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getextendedudptable)
-   [**GetOwnerModuleFromTcp6Entry**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getownermodulefromtcp6entry)
-   [**GetOwnerModuleFromTcpEntry**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getownermodulefromtcpentry)
-   [**GetOwnerModuleFromUdp6Entry**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getownermodulefromudp6entry)
-   [**GetOwnerModuleFromUdpEntry**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getownermodulefromudpentry)
-   [**GetPerTcp6ConnectionEStats**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getpertcp6connectionestats)
-   [**GetPerTcpConnectionEStats**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getpertcpconnectionestats)
-   [**GetTcpStatistics**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-gettcpstatistics)
-   [**GetTcpStatisticsEx**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-gettcpstatisticsex)
-   [**GetTcpStatisticsEx2**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-gettcpstatisticsex2)
-   [**GetTcp6Table**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-gettcp6table)
-   [**GetTcp6Table2**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-gettcp6table2)
-   [**GetTcpTable**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-gettcptable)
-   [**GetTcpTable2**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-gettcptable2)
-   [**SetPerTcp6ConnectionEStats**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-setpertcp6connectionestats)
-   [**SetPerTcpConnectionEStats**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-setpertcpconnectionestats)
-   [**SetTcpEntry**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-settcpentry)
-   [**GetUdp6Table**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getudp6table)
-   [**GetUdpStatistics**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getudpstatistics)
-   [**GetUdpStatisticsEx**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getudpstatisticsex)
-   [**GetUdpStatisticsEx2**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getudpstatisticsex2)
-   [**GetUdpTable**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getudptable)

## Deprecated APIs

> [!Note]  
> These functions are deprecated and not supported by Microsoft.

 

-   [**AllocateAndGetTcpExTableFromStack**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-allocateandgettcpextablefromstack)
-   [**AllocateAndGetUdpExTableFromStack**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-allocateandgetudpextablefromstack)

 

 



