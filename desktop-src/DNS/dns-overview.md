---
title: DNS Overview
description: DNS is an industry-standard service used to locate computers on an Internet Protocol (IP)-based network.
ms.assetid: 98ecf24b-8bd5-4a75-a487-8af3080e8987
ms.topic: article
ms.date: 05/31/2018
---

# DNS Overview

DNS is an industry-standard service used to locate computers on an Internet Protocol (IP)-based network. IP networks, such as the Internet and Windows 2000 networks, rely on number-based addresses, such as 207.46.131.137 to ferry information throughout the network. Network users rely on character-based names, such as `www.microsoft.com`. Therefore, it is necessary to translate character or user-friendly addresses (`www.microsoft.com`) into the number-based addresses (207.46.131.137) that the network can recognize. DNS is the service of choice in Windows 2000 to locate resources and translate them into their corresponding IP addresses.

DNS uses a specialized database of resource records, commonly referred to simply as RRs, to respond to client name-resolution queries. Before DNS, name resolution on the Internet was achieved with [*hosts file*](h-gly.md), which are manually created files that associated host names with IP addresses.

When a new client was added to the network, an administrator had to manually update the hosts file and then copy (replicate) that file to all other computers on the network so that the new host could be reached by all. As the Internet grew, this form of name resolution was clearly insufficient; it was too management intensive, and it did not [*scale*](s-gly.md). The hosts file just got bigger, and because it used a [*flat name space*](f-gly.md) (see also [Name Space](name-space.md)), it could not be partitioned and had to be distributed in its entirety. The solution was DNS.

-   DNS replaced the hosts file's flat name space with a [*hierarchical name space*](h-gly.md). With a hierarchical name space, information about host names and IP addresses can be partitioned and distributed; thus, scalability is achieved. For example, in the fictional widgets.products.microsoft.com domain, responsibility for name resolution can be partitioned so that various servers can handle name resolution for different parts of the name space:
    -   One server can be responsible for resolving the first part (microsoft.com), and can then forward the name-resolution request to the next DNS Server in the hierarchy.
    -   The next DNS Server can be responsible for resolving the next part of the name space (products).
    -   Finally, the request can be forwarded to a third DNS server that is responsible for resolving the last part of the name (widgets).

DNS Servers in each part of the hierarchical name space need to maintain a database of resource records for hosts, but only in their part of the hierarchy. Thus, the server (or servers) in the products part of widgets.products.microsoft.com maintain RRs for only the products part of the hierarchical name space — not for the microsoft.com part or the widgets part of the name space.

 

 




