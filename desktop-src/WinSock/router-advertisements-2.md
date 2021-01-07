---
description: The content of IPv6 router advertisements is automatically derived from the published routes in the routing table. Nonpublished routes are used for routing but are ignored when constructing router advertisements.
ms.assetid: 27b735db-4e87-497b-b39c-e464cf44f09e
title: IPv6 Router Advertisements
ms.topic: article
ms.date: 05/31/2018
---

# IPv6 Router Advertisements

The content of IPv6 router advertisements is automatically derived from the published routes in the routing table. Nonpublished routes are used for routing but are ignored when constructing router advertisements.

Router advertisements for IPv6 always contain a source link-layer address option and an MTU option. The value for the MTU option is taken from the sending interface's current link MTU. This value can be changed with the ipv6 ifc mtu command.

The router advertisement only has a nonzero router lifetime if there is a published default route. A default route is a route for the zero-length prefix.

Published on-link routes result in prefix information options in router advertisements. If the on-link prefix has 64 bits, the prefix information option has both the L and A bits set and hosts receiving it will autoconfigure addresses.

An interface that sends router advertisements will also autoconfigure addresses for itself based on the prefix information options that it sends.

A finite nonaging lifetime on all published routes (for example, 30 minutes) is recommended. If you decide to retract a route, you can change the route to have an aging lifetime. The route will age over the course of several router advertisements and then disappear from both the router and any hosts receiving the router advertisements.

Routes that hosts find through router advertisements age and are not published. Addresses autoconfigured from router advertisements age as well.

 

 



