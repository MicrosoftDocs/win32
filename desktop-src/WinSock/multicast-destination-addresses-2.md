---
description: When sending to a multicast destination address, the Microsoft IPv6 protocol normally requires that the application have an outgoing interface specified.
ms.assetid: dbfeaa1f-a7c5-4a15-90f0-4d1cdaf798e9
title: IPv6 Multicast Destination Addresses
ms.topic: article
ms.date: 05/31/2018
---

# IPv6 Multicast Destination Addresses

When sending to a multicast destination address, the Microsoft IPv6 protocol normally requires that the application have an outgoing interface specified. This is done with the **IPV6\_MULTICAST\_IF** socket option or by binding the socket to a specific source address.

You can also specify a default interface for a specific multicast address, an entire multicast address scope, or all multicast addresses. This is done with a route that places the multicast prefix on-link to the desired outgoing interface. For following examples show how this can be specified:

``` syntax
ipv6 rtu ff02::5/128 3
ipv6 rtu ff0e::/16 3
ipv6 rtu ff00::/8 3
```

 

 



