---
title: Route Tables and Route Table Entries
description: The routing table manager maintains distinct route tables for each protocol family.
ms.assetid: 3848d93d-cc54-4a08-bd36-a9700cde6ce0
ms.topic: article
ms.date: 05/31/2018
---

# Route Tables and Route Table Entries

**Windows Server 2003:** This API has been superseded by the [Routing Table Manager Version 2](about-routing-table-manager-version-2.md) API and will not be available beyond Windows Server 2003. New applications should use the Routing Table Manager Version 2 API.

The routing table manager maintains distinct route tables for each protocol family. Currently, explicit support is provided for the Internet Protocol (IP) and Internet Packet Exchange (IPX) routing protocol families. Regardless of the protocol family, each route entry contains the following information:

-   Destination network.
-   Identifier of the protocol that added the route.
-   Index of interface through which the route was obtained. This index value is the numeric value assigned to a network interface (hardware-based or virtual) that transmits the data onto the network. (For example, an Ethernet NIC, or a 802.1b wireless card.)
-   Address of the next hop router. RRAS uses this router to forward packets to the destination network if the network is not directly connected.
-   The time the route was created or last updated.
-   The amount of time this route is kept in the routing table. If this amount of time elapses, and the route has not been updated, the routing table manager removes the route from the table. In this case, the route is said to have *aged out*.
-   Data specific to the protocol family. This data is transparent to RTMv1. However, if this data changes for a route designated as a "best route," the routing table manager sends out route-change notification.
-   Data specific to the routing protocol. This data is completely transparent to the routing table manager, in that, changes to this data do not cause route change notification.

The following values taken together uniquely identify a route in the routing table:

-   Destination network
-   Protocol identifier
-   Interface index
-   Address of next-hop router

In general, the routing table manager creates separate entries for routes that differ in any of these parameter values. However, an exception is made for routing protocols that do not keep more than one entry for each destination network. For these protocols, the routing table manager ignores differences in interface index or next-hop address. An example of such a protocol is the RRAS implementation of Open Shortest Path First (OSPF).

 

 




