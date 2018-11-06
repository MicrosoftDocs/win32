---
title: Routing Table Manager
description: The routing table manager is the central repository of routing information for all routing protocols that operate under the Routing and Remote Access Service (RRAS).
ms.assetid: '7b01704e-c1fb-40e3-89cf-1206fdf9fd75'
ms.topic: article
ms.date: 05/31/2018
---

# Routing Table Manager

The routing table manager is the central repository of routing information for all routing protocols that operate under the Routing and Remote Access Service (RRAS). It notifies clients when changes have occurred, and allows clients to exchange private information.

The routing table manager provides routing information to all interested clients, such as routing protocols, management programs, and monitoring programs. The routing table manager also determines the best route to each destination network that is known to the routing protocols. The routing table manager determines this route based on routing protocol priorities and on the metrics associated with the routes. The person administering the router can configure routing protocol priorities using the RRAS management console.

The routing table manager passes the best-route information to the forwarders (one per address family, or one per interface) and to all interested clients.

Each client registers with the routing table manager, and in return receives a handle that the client uses to add or delete routes. Clients can retrieve information stored in the routing table. Additionally, clients can register with the routing table manager to receive notification of changes to the best route to a destination.

 

 




