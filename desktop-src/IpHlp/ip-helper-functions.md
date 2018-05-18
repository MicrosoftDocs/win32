---
Description: 'The following functions retrieve and modify configuration settings for the TCP/IP transport on the local computer.'
ms.assetid: '5f562470-f3e8-4305-a015-3a84cd09a1eb'
title: IP Helper Functions
---

# IP Helper Functions

The following functions retrieve and modify configuration settings for the TCP/IP transport on the local computer. The following categorical listing can help determine which collection of functions is best suited for a given task:

## Adapter Management

-   [**GetAdapterIndex**](getadapterindex.md)
-   [**GetAdaptersAddresses**](getadaptersaddresses.md)
-   [**GetAdaptersInfo**](getadaptersinfo.md)
-   [**GetPerAdapterInfo**](getperadapterinfo.md)
-   [**GetUniDirectionalAdapterInfo**](getunidirectionaladapterinfo.md)

## Address Resolution Protocol (ARP) Management

-   [**CreateIpNetEntry**](createipnetentry.md)
-   [**CreateProxyArpEntry**](createproxyarpentry.md)
-   [**DeleteIpNetEntry**](deleteipnetentry.md)
-   [**DeleteProxyArpEntry**](deleteproxyarpentry.md)
-   [**FlushIpNetTable**](flushipnettable.md)
-   [**GetIpNetTable**](getipnettable.md)
-   [**SendARP**](sendarp.md)
-   [**SetIpNetEntry**](setipnetentry.md)

## Interface Conversion

-   [**ConvertInterfaceAliasToLuid**](convertinterfacealiastoluid.md)
-   [**ConvertInterfaceGuidToLuid**](convertinterfaceguidtoluid.md)
-   [**ConvertInterfaceIndexToLuid**](convertinterfaceindextoluid.md)
-   [**ConvertInterfaceLuidToAlias**](convertinterfaceluidtoalias.md)
-   [**ConvertInterfaceLuidToGuid**](convertinterfaceluidtoguid.md)
-   [**ConvertInterfaceLuidToIndex**](convertinterfaceluidtoindex.md)
-   [**ConvertInterfaceLuidToNameA**](convertinterfaceluidtonamea.md)
-   [**ConvertInterfaceLuidToNameW**](convertinterfaceluidtonamew.md)
-   [**ConvertInterfaceNameToLuidA**](convertinterfacenametoluida.md)
-   [**ConvertInterfaceNameToLuidW**](convertinterfacenametoluidw.md)
-   [**if\_indextoname**](if-indextoname.md)
-   [**if\_nametoindex**](if-nametoindex.md)

## Interface Management

-   [**GetFriendlyIfIndex**](getfriendlyifindex.md)
-   [**GetIfEntry**](getifentry.md)
-   [**GetIfEntry2**](getifentry2.md)
-   [**GetIfEntry2Ex**](getifentry2ex.md)
-   [**GetIfStackTable**](getifstacktable.md)
-   [**GetIfTable**](getiftable.md)
-   [**GetIfTable2**](getiftable2.md)
-   [**GetIfTable2Ex**](getiftable2ex.md)
-   [**GetInterfaceInfo**](getinterfaceinfo.md)
-   [**GetInvertedIfStackTable**](getinvertedifstacktable.md)
-   [**GetIpInterfaceEntry**](getipinterfaceentry.md)
-   [**GetIpInterfaceTable**](getipinterfacetable.md)
-   [**GetNumberOfInterfaces**](getnumberofinterfaces.md)
-   [**InitializeIpInterfaceEntry**](initializeipinterfaceentry.md)
-   [**SetIfEntry**](setifentry.md)
-   [**SetIpInterfaceEntry**](setipinterfaceentry.md)

## Internet Protocol (IP) and Internet Control Message Protocol (ICMP)

-   [**GetIcmpStatistics**](geticmpstatistics.md)
-   [**GetIpStatistics**](getipstatistics.md)
-   [**Icmp6CreateFile**](icmp6createfile.md)
-   [**Icmp6ParseReplies**](icmp6parsereplies.md)
-   [**Icmp6SendEcho2**](icmp6sendecho2.md)
-   [**IcmpCloseHandle**](icmpclosehandle.md)
-   [**IcmpCreateFile**](icmpcreatefile.md)
-   [**IcmpParseReplies**](icmpparsereplies.md)
-   [**IcmpSendEcho**](icmpsendecho.md)
-   [**IcmpSendEcho2**](icmpsendecho2.md)
-   [**IcmpSendEcho2Ex**](icmpsendecho2ex.md)
-   [**SetIpTTL**](setipttl.md)

## IP Address Management

-   [**AddIPAddress**](addipaddress.md)
-   [**CreateAnycastIpAddressEntry**](createanycastipaddressentry.md)
-   [**CreateUnicastIpAddressEntry**](createunicastipaddressentry.md)
-   [**DeleteIPAddress**](deleteipaddress.md)
-   [**DeleteAnycastIpAddressEntry**](deleteanycastipaddressentry.md)
-   [**DeleteUnicastIpAddressEntry**](deleteunicastipaddressentry.md)
-   [**GetAnycastIpAddressEntry**](getanycastipaddressentry.md)
-   [**GetAnycastIpAddressTable**](getanycastipaddresstable.md)
-   [**GetIpAddrTable**](getipaddrtable.md)
-   [**GetMulticastIpAddressEntry**](getmulticastipaddressentry.md)
-   [**GetMulticastIpAddressTable**](getmulticastipaddresstable.md)
-   [**GetUnicastIpAddressEntry**](getunicastipaddressentry.md)
-   [**GetUnicastIpAddressTable**](getunicastipaddresstable.md)
-   [**InitializeUnicastIpAddressEntry**](initializeunicastipaddressentry.md)
-   [**IpReleaseAddress**](ipreleaseaddress.md)
-   [**IpRenewAddress**](iprenewaddress.md)
-   [**NotifyStableUnicastIpAddressTable**](notifystableunicastipaddresstable.md)
-   [**SetUnicastIpAddressEntry**](setunicastipaddressentry.md)

## IP Address String Conversion

-   [**RtlIpv4AddressToString**](rtlipv4addresstostring.md)
-   [**RtlIpv4AddressToStringEx**](rtlipv4addresstostringex.md)
-   [**RtlIpv4StringToAddress**](rtlipv4stringtoaddress.md)
-   [**RtlIpv4StringToAddressEx**](rtlipv4stringtoaddressex.md)
-   [**RtlIpv6AddressToString**](rtlipv6addresstostring.md)
-   [**RtlIpv6AddressToStringEx**](rtlipv6addresstostringex.md)
-   [**RtlIpv6StringToAddress**](rtlipv6stringtoaddress.md)
-   [**RtlIpv6StringToAddressEx**](rtlipv6stringtoaddressex.md)

## IP Neighbor Address Management

-   [**CreateIpNetEntry2**](createipnetentry2.md)
-   [**DeleteIpNetEntry2**](deleteipnetentry2.md)
-   [**FlushIpNetTable2**](flushipnettable2.md)
-   [**GetIpNetEntry2**](getipnetentry2.md)
-   [**GetIpNetTable2**](getipnettable2.md)
-   [**ResolveIpNetEntry2**](resolveipnetentry2.md)
-   [**ResolveNeighbor**](resolveneighbor.md)
-   [**SetIpNetEntry2**](setipnetentry2.md)

## IP Path Management

-   [**FlushIpPathTable**](flushippathtable.md)
-   [**GetIpPathEntry**](getippathentry.md)
-   [**GetIpPathTable**](getippathtable.md)

## IP Route Management

-   [**CreateIpForwardEntry**](createipforwardentry.md)
-   [**CreateIpForwardEntry2**](createipforwardentry2.md)
-   [**DeleteIpForwardEntry**](deleteipforwardentry.md)
-   [**DeleteIpForwardEntry2**](deleteipforwardentry2.md)
-   [**EnableRouter**](enablerouter.md)
-   [**GetBestInterface**](getbestinterface.md)
-   [**GetBestInterfaceEx**](getbestinterfaceex.md)
-   [**GetBestRoute**](getbestroute.md)
-   [**GetBestRoute2**](getbestroute2.md)
-   [**GetIpForwardEntry2**](getipforwardentry2.md)
-   [**GetIpForwardTable**](getipforwardtable.md)
-   [**GetIpForwardTable2**](getipforwardtable2.md)
-   [**GetRTTAndHopCount**](getrttandhopcount.md)
-   [**InitializeIpForwardEntry**](initializeipforwardentry.md)
-   [**SetIpForwardEntry**](setipforwardentry.md)
-   [**SetIpForwardEntry2**](setipforwardentry2.md)
-   [**SetIpStatistics**](setipstatistics.md)
-   [**SetIpStatisticsEx**](setipstatisticsex.md)
-   [**UnenableRouter**](unenablerouter.md)

## IP Table Memory Management

-   [**FreeMibTable**](freemibtable.md)

## IP Utility

-   [**ConvertIpv4MaskToLength**](convertipv4masktolength.md)
-   [**ConvertLengthToIpv4Mask**](convertlengthtoipv4mask.md)
-   [**CreateSortedAddressPairs**](createsortedaddresspairs.md)
-   [**ParseNetworkString**](parsenetworkstring.md)

## Network Configuration

-   [**GetNetworkParams**](getnetworkparams.md)

## Notification

-   [**CancelMibChangeNotify2**](cancelmibchangenotify2.md)
-   [**NotifyAddrChange**](notifyaddrchange.md)
-   [**NotifyIpInterfaceChange**](notifyipinterfacechange.md)
-   [**NotifyRouteChange**](notifyroutechange.md)
-   [**NotifyRouteChange2**](notifyroutechange2.md)
-   [**NotifyUnicastIpAddressChange**](notifyunicastipaddresschange.md)

## Persistent Port Reservarion

-   [**CreatePersistentTcpPortReservation**](createpersistenttcpportreservation.md)
-   [**CreatePersistentUdpPortReservation**](createpersistentudpportreservation.md)
-   [**DeletePersistentTcpPortReservation**](deletepersistenttcpportreservation.md)
-   [**DeletePersistentUdpPortReservation**](deletepersistentudpportreservation.md)
-   [**LookupPersistentTcpPortReservation**](lookuppersistenttcpportreservation.md)
-   [**LookupPersistentUdpPortReservation**](lookuppersistentudpportreservation.md)

## Security Health

-   [**CancelSecurityHealthChangeNotify**](cancelsecurityhealthchangenotify.md)
-   [**NotifySecurityHealthChange**](notifysecurityhealthchange.md)

These functions are defined only on Windows Server 2003.

> [!Note]  
> These functions are not available Windows Vista and Windows Server 2008.

 

## Teredo IPv6 Client Management

-   [**GetTeredoPort**](getteredoport.md)
-   [**NotifyTeredoPortChange**](notifyteredoportchange.md)
-   [**NotifyStableUnicastIpAddressTable**](notifystableunicastipaddresstable.md)

## Transmission Control Protocol (TCP) and User Datagram Protocol (UDP)

-   [**GetExtendedTcpTable**](getextendedtcptable.md)
-   [**GetExtendedUdpTable**](getextendedudptable.md)
-   [**GetOwnerModuleFromTcp6Entry**](getownermodulefromtcp6entry.md)
-   [**GetOwnerModuleFromTcpEntry**](getownermodulefromtcpentry.md)
-   [**GetOwnerModuleFromUdp6Entry**](getownermodulefromudp6entry.md)
-   [**GetOwnerModuleFromUdpEntry**](getownermodulefromudpentry.md)
-   [**GetPerTcp6ConnectionEStats**](getpertcp6connectionestats.md)
-   [**GetPerTcpConnectionEStats**](getpertcpconnectionestats.md)
-   [**GetTcpStatistics**](gettcpstatistics.md)
-   [**GetTcpStatisticsEx**](gettcpstatisticsex.md)
-   [**GetTcpStatisticsEx2**](gettcpstatisticsex2.md)
-   [**GetTcp6Table**](gettcp6table.md)
-   [**GetTcp6Table2**](gettcp6table2.md)
-   [**GetTcpTable**](gettcptable.md)
-   [**GetTcpTable2**](gettcptable2.md)
-   [**SetPerTcp6ConnectionEStats**](setpertcp6connectionestats.md)
-   [**SetPerTcpConnectionEStats**](setpertcpconnectionestats.md)
-   [**SetTcpEntry**](settcpentry.md)
-   [**GetUdp6Table**](getudp6table.md)
-   [**GetUdpStatistics**](getudpstatistics.md)
-   [**GetUdpStatisticsEx**](getudpstatisticsex.md)
-   [**GetUdpStatisticsEx2**](getudpstatisticsex2.md)
-   [**GetUdpTable**](getudptable.md)

## Deprecated APIs

> [!Note]  
> These functions are deprecated and not supported by Microsoft.

 

-   [**AllocateAndGetTcpExTableFromStack**](allocateandgettcpextablefromstack.md)
-   [**AllocateAndGetUdpExTableFromStack**](allocateandgetudpextablefromstack.md)

 

 



