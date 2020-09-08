---
title: Receiving Solicited Traffic Over Teredo
description: Many applications such as Microsoft Internet Explorer and Microsoft Outlook only initiate connections to the Internet.
ms.assetid: bff5d65e-050d-4b09-9982-8024612ffa6e
ms.topic: article
ms.date: 05/31/2018
---

# Receiving Solicited Traffic Over Teredo

Many applications such as Microsoft Internet Explorer and Microsoft Outlook only initiate connections to the Internet. For these applications, [Teredo](about-teredo.md) can provide seamless connectivity over IPv6 in the absence of other IPv6 interfaces. Additionally, solicited traffic can be received over the Teredo Interface on the earlier Microsoft Windows XP with Service Pack 2 (SP2) and Windows Server 2003 platforms.

The following documentation explains how these applications achieve connectivity, and the circumstances under which Teredo is used.

## Obtaining a Destination Address

An application attempts to obtain the destination address using various methods such as Domain Name System (DNS) or Peer Name Resolution Protocol (PNRP). It is possible for the application to obtain multiple IPv4 and IPv6 IP addresses using these methods. The typical APIs used to obtain IP addresses include the Windows XP API [**GetHostByName**](/windows/desktop/api/wsipv6ok/nf-wsipv6ok-gethostbyname) and the new Windows Vista API [**GetAddrInfo**](/windows/desktop/api/ws2tcpip/nf-ws2tcpip-getaddrinfo). For example, using the GetAddrInfo API with the *ai\_family* parameter set to AF\_INET6 as the addrinfo/protocol hint allows the user to query DNS servers for IPv6 addresses specifically. The [**DnsQuery**](/windows/desktop/api/windns/nf-windns-dnsquery_a) API with the type DNS\_TYPE\_AAAA can also be used to query the DNS servers for AAAA records.

## Establishing a Connection

A connection established with Teredo is described as 'seamless' because it is handled like any other IPv6 connection. The programming of an application does not require special consideration to be capable of utilizing the Teredo interface. When a connection is established between Teredo interfaces, a relay router, typical of 6to4 and other native interfaces, is not required. However, Teredo is designed as a last resort transition technology for IPv6 connectivity.

> [!Note]  
> Teredo is not utilized if the supplied hostname resolves to IPv4 addresses only.

 

When an application attempts to connect to a destination using IPv6 addresses, the following will occur:

-   The application obtains a list of IPv6 addresses by calling the [**GetAdaptersAddresses**](/windows/desktop/api/iphlpapi/nf-iphlpapi-getadaptersaddresses) API. The Windows Vista stack returns a list of all interfaces based on the sorting order specified in [RFC 3484](https://www.irt.org/rfc/rfc3484.htm). As a result, IPv6 and 6to4 IPv6 interfaces will be listed before Teredo interface. However, when native IPv6 or 6to4 connectivity is not available, Teredo will be the only IPv6 capable interface listed.

    It is important to remember that an application can use any interface provided by the Windows Vista stack, however the ordering of the interface list returned will most often result in Teredo being attempted last.

-   Before Windows Vista attempts a connection over the Teredo interface, the operating system ensures that the IPv6 address has stabilized. This is done automatically for outgoing connections and is not a crucial consideration for an application. In the event the application is required to guarantee address stability, the [**NotifyStableUnicastIpAddressTable**](/windows/desktop/api/netioapi/nf-netioapi-notifystableunicastipaddresstable) API can be called to ensure that the Teredo address is stable.

-   A Teredo interface will attempt to connect to another Teredo interface at the destination. If a Teredo interface is not present, a connection is established with a native or 6to4 destination address through a host-specific relay.

It is also possible for applications that initiate connections to the Internet to receive unsolicited traffic. For more details see [Receiving Unsolicited Traffic Over Teredo](receiving-unsolicited-traffic-over-teredo.md).

## Using the WSAConnectByName API

By calling the WSAConnectByName API, it is possible for an application to connect to a destination name instead of specifying the exact IP address. The Windows Vista stack prefers IPv6 over IPv4, and as a result any connection attempts will be made to IPv6 addresses first.

Calling the WSAConnectByName API will sort all destination IP addresses obtained in the following order:

-   Native IPv6 address
-   6to4 IP address
-   IPv4 address
-   Teredo address

After the destination addresses are sorted internally, a connection to the destination is attempted based on the best route available on the local host for the destination address. As indicated by the order of the sorted addresses, if the destination name resolves to a IPv4 and Teredo address, the IPv4 address will be used to establish the connection.

The WSAConnectByName API works internally to find the best match between addresses. This attempt is based on the routes available on the local host and the destination addresses.

Due to current absence of Teredo relays on the Internet, connections to native IPv6 addresses are unlikely to succeed over the Teredo interface. If WSAConnectByName is called, Windows Vista will not issue AAAA queries when Teredo is the only IPv6 capable interface available. This ensures that native IPv6 addresses are not obtained as a destination and that connections are attempted over IPv4, which has the highest chance of success. In order to obtain IPv6 addresses when Teredo is the only IPv6 capable interface, an application must explicitly use the DnsQuery API for AAAA records.

 

 