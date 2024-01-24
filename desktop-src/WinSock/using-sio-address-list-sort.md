---
description: The SIO\_ADDRESS\_LIST\_SORT IOCTL allows application developers to sort a list of IPv6 and IPv4 destination addresses to determine the best available address for making a connection. The SIO\_ADDRESS\_LIST\_SORT IOCTL is supported on Windows XP and later.
ms.assetid: bf380ddf-8171-4ef4-be47-94c7a6aabf0a
title: Using SIO_ADDRESS_LIST_SORT
ms.topic: article
ms.date: 05/31/2018
---

# Using SIO\_ADDRESS\_LIST\_SORT

The **SIO\_ADDRESS\_LIST\_SORT** IOCTL allows application developers to sort a list of IPv6 and IPv4 destination addresses to determine the best available address for making a connection. The **SIO\_ADDRESS\_LIST\_SORT** IOCTL is supported on Windows XP and later.

On Windows Vista and later, the [**CreateSortedAddressPairs**](/windows/win32/api/netioapi/nf-netioapi-createsortedaddresspairs) function takes a supplied list of potential IP destination addresses, pairs the destination addresses with the host machine's local IP addresses, and sorts the pairs according to which address pair is best suited for communication between the two peers. The **CreateSortedAddressPairs** function should be used instead of the **SIO\_ADDRESS\_LIST\_SORT** IOCTL on Windows Vista and later.

The following sections describe usage considerations for **SIO\_ADDRESS\_LIST\_SORT**.

## Parameters

The buffer passed to **SIO\_ADDRESS\_LIST\_SORT** is a [**SOCKET\_ADDRESS\_LIST**](/previous-versions/windows/desktop/legacy/aa385467(v=vs.85)) structure. Each [**SOCKET\_ADDRESS**](/windows/desktop/api/Ws2def/ns-ws2def-socket_address) in the list must be in SOCKADDR\_IN6 format.

The **SIO\_ADDRESS\_LIST\_SORT** IOCTL sorts both IPv6 and IPv4 addresses on Windows Vista and later. Any IPv4 addresses in the list to be sorted must be in the IPv4-mapped IPv6 address format. For more information on the IPv4-mapped IPv6 address format, see [Dual-Stack Sockets](dual-stack-sockets.md).

On Windows Server 2003, and Windows XP, **SIO\_ADDRESS\_LIST\_SORT** sorts only IPv6 addresses. IPv4 addresses in the IPv4-mapped IPv6 address format are not supported.

On output, the **iAddressCount** member of the [**SOCKET\_ADDRESS\_LIST**](/previous-versions/windows/desktop/legacy/aa385467(v=vs.85)) structure may be smaller than on input if the IOCTL code determines that some destination addresses are invalid.

## Sorting Determination

The sorting order for IPv6 addresses for the SIO\_ADDRESS\_LIST\_SORT IOCTL is based on the prefix policy table. The prefix policy table is configured using the *Netsh.exe* command line utility. The following command line snippets illustrate basic *Netsh.exe* prefix policy table configuration commands:

``` syntax
netsh interface ipv6 show prefixpolicies
netsh interface ipv6 add prefixpolicy ::/96 3 4
netsh interface ipv6 delete prefixpolicy ::/96
netsh interface ipv6 set prefixpolicy ::/96 3 4
```

> [!Note]  
> On Windows Server 2003 and Windows XP, the first netsh command listed above was as follows. All other related commands are the same.

 

``` syntax
netsh interface ipv6 show prefixpolicy
```

Address ordering is also determined by an algorithm outlined in the RFC 3484 on *Default Address Selection for Internet Protocol version 6 (IPv6)* published by the IETF. For more information, see [https://www.ietf.org/rfc/rfc3484.txt](https://tools.ietf.org/html/rfc3484). (This resource may only be available in English.)

The **SIO\_ADDRESS\_LIST\_SORT** IOCTL sorts addresses from best to worst, and fills in **sin6\_scope\_id** members, if needed. For site-local addresses, SIO\_ADDRESS\_LIST\_SORT either fills in the scope-id, or removes the address.

The **SIO\_ADDRESS\_LIST\_SORT** IOCTL ignores the source address bound to the socket and only sorts by the destination address list passed as a parameter.

The [**CreateSortedAddressPairs**](/windows/win32/api/netioapi/nf-netioapi-createsortedaddresspairs) function should be used instead of the **SIO\_ADDRESS\_LIST\_SORT** IOCTL on Windows Vista and later. The **CreateSortedAddressPairs** function returns a list of address pairs that contains a local source address and a destination address. This provides an application the correct source address to use for each destination address. An application can also filter the results by looking for a specific source address. in the results.

## Requirements

The **SIO\_ADDRESS\_LIST\_SORT** IOCTL is defined in the *Winsock2.h* header file. On the Microsoft Windows Software Development Kit (SDK) released for Windows Vista and later, the organization of header files has changed and **SIO\_ADDRESS\_LIST\_SORT** IOCTL is defined in the *Ws2def.h* header file. Note that the *Ws2def.h* header file is automatically included in *Winsock2.h*, and should never be used directly.

The **SIO\_ADDRESS\_LIST\_SORT** IOCTL is supported on Windows XP and later.

## Related topics

<dl> <dt>

[**CreateSortedAddressPairs**](/windows/win32/api/netioapi/nf-netioapi-createsortedaddresspairs)
</dt> </dl>

 

 
