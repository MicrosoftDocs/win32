---
description: IPv6 link-local and site-local addresses are called scoped addresses.
ms.assetid: d31882f6-b747-47c7-83cb-a9a03fe11cb8
title: IPv6 Link-local and Site-local Addresses
ms.topic: article
ms.date: 05/31/2018
---

# IPv6 Link-local and Site-local Addresses

IPv6 link-local and site-local addresses are called scoped addresses. The Windows Sockets (Winsock) API supports the **sin6\_scope\_id** member in the [**sockaddr\_in6**](sockaddr-2.md) structure for use with scoped addresses. For IPv6 link-local addresses (fe80::/10 prefix), the **sin6\_scope\_id** member in the **sockaddr\_in6** structure is the interface number. For IPv6 site-local addresses (fec0::/10 prefix), the **sin6\_scope\_id** member in the **sockaddr\_in6** structure is a site identifier.

An example of a link-local IPv6 address on interface \#5 is the following:

``` syntax
fe80::208:74ff:feda:625c%5
```

The following command is available on Windows XP with Service Pack 1 (SP1) and later to query and configure IPv6 on a local computer:

-   [Netsh.exe](netsh-exe.md)

Configuration changes made using the Netsh.exe commands are permanent and are not lost when the computer or the IPv6 protocol is restarted.

Prior to Windows XP with Service Pack 1 (SP1), IPv6 configuration and management used several older command-line tools (Net.exe, Ipv6.exe, and Ipsec6.exe) to configure and manage IPv6. Using these older tools, the IPv6 changes are not permanent and are lost when the computer or the IPv6 protocol was restarted. These older command-line tools are only supported on Windows XP.

On Windows XP with SP1, the following command will display the list of IPv6 interfaces on a local computer including the interface index, the interface name, and various other interface properties.

**netsh interface ipv6 show interface**

On Windows XP with SP1, the following command will change the site identifier associated with an interface index.

**netsh interface ipv6 set interface <InterfaceIndex or Name> siteid=value**

On Windows XP, the following older command will also change the site identifier associated with a site-local address to 3.

**ipv6 rtu fec0::/10 3**

If you are sending or connecting to a scoped address, then the **sin6\_scope\_id** member in the [**sockaddr\_in6**](sockaddr-2.md) structure can be left unspecified (zero) which represents an ambiguous scoped address. For example, the following link-local address is ambiguous:

``` syntax
fe80::10
```

If you are binding to a scoped address, then the **sin6\_scope\_id** member in the [**sockaddr\_in6**](sockaddr-2.md) structure must contain a nonzero value that specifies a valid interface number for a link-local address or a site identifier for a site-local address.

## Ambiguous Scoped Addresses

If you are sending or connecting to a scoped address and have not specified the **sin6\_scope\_id** member in the [**sockaddr\_in6**](sockaddr-2.md) structure, then the scoped address is ambiguous. To resolve this, the IPv6 protocol first determines whether you have bound the socket to a source address. If so, the bound source address resolves the ambiguity by supplying an interface number or site identifier.

If you are sending or connecting to a scoped address and have neither specified the **sin6\_scope\_id** member nor bound a source address, then the IPv6 protocol checks the routing table. For example, the following command will display the IPv6 routing table on a local computer:

**netsh interface ipv6 show route**

``` syntax
No   Manual   256  fe80::/64      13  Local Area Connection
No   Manual   256  fe80::/64      14  Wireless Network Connection
```

This indicates that link-local addresses are treated as on-link to interface \#13 and \#14 by default.

Ambiguity arises when a local computer has multiple network adapters. For example, the **netsh** command above indicates there are two network interfaces (Local Area Connection and Wireless Network Connection). When an application specifies a destination link-local address (fe80::10, for example) without a scope ID, it is not clear which adapter to use to send the packet. Only a link-local unicast (fe80::/64) or a link-scope multicast (ff00::/8) IPv6 destination address can suffer from not having a scope ID when sending a packet.

## Neighbor Discovery

If you have not specified the **sin6\_scope\_id** member in the [**sockaddr\_in6**](sockaddr-2.md) structure, have not bound a source address, and have not specified a route for link-local addresses, then the IPv6 protocol will try Neighbor Discovery to resolve the destination link-local address. For a given packet being sent, one interface is tried. This first interface that is tried is considered the most preferred interface. If Neighbor Discovery fails to resolve the link-local address on an interface, the packet to be sent is dropped and the system remembers that the destination link-local address is not reachable over that interface. On the next packet to be sent under all of the same conditions, a different interface is tried for Neighbor Discovery. This process continues through each of the interfaces on a local computer for each new packet until Neighbor Discovery responds for the destination link-local address or all of the possible interfaces have been tried and failed. Each time an attempt to resolve the neighbor fails, one interface is eliminated for that neighbor.

If the destination link-local address resolves, then that interface is used to send the current packet. This interface is also used for any subsequent ambiguously-scoped packets that are sent to the same link-local destination address.

If Neighbor Discovery fails to resolve the destination link-local address on all interfaces, the system then tries to send the packet on the most preferred interface (the first interface tried). The network stack keeps trying to resolve the destination link-local address on the most preferred interface. After a period of time after Neighbor Discovery has failed on all interfaces, the network stack will restart the process again and try to resolve the destination link-local address on all of the interfaces. Currently, this time interval when Neighbor Discovery is again tried on all interfaces is 60 seconds. However, this time interval may change on versions of Windows and should not be assumed by an application.

> [!Note]  
> If an application binds the same link-local address to a different interface after Neighbor Discovery has resolved the link-local address, that will not override the interface with the link-local destination address returned by Neighbor Discovery.

 

For more information on Neighbor Discovery for IP version 6, see [RFC4861](https://tools.ietf.org/html/rfc4861) published by the IETF.

## Related topics

<dl> <dt>

[IPv6 Site Prefixes](site-prefixes-2.md)
</dt> <dt>

[Ipv6.exe](ipv6-exe-2.md)
</dt> <dt>

[Netsh.exe](netsh-exe.md)
</dt> <dt>

[Using IPv6](using-ipv6-2.md)
</dt> </dl>

 

 



