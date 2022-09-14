---
title: Static and Autostatic Routes
description: Typically, routes to remote networks are obtained dynamically through routing protocols.
ms.assetid: af2f2039-8131-4ca9-98bf-6aeb7a511034
ms.topic: article
ms.date: 05/31/2018
---

# Static and Autostatic Routes

Typically, routes to remote networks are obtained dynamically through routing protocols. However, the administrator can also *seed* the routing table by providing routes manually. These routes are referred to as *static*. A static route is associated with an interface that represents the remote network. Unlike dynamic routes, static routes are retained even if the router is restarted or the interface is disabled.

An *autostatic* route is obtained through a routing protocol, but once obtained behaves like a static route. The process for obtaining autostatic routes is as follows: The IP or IPX router manager issues a request that a routing protocol update the routing information for a specific interface. The results of the update are then converted into static routes. Note that only certain routing protocols support requests for autostatic route updates.

 

 




