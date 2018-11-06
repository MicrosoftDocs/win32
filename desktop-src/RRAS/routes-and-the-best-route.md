---
title: Routes and the Best Route
description: A route is a \ 0034;network path \ 0034; to a destination that has a certain cost associated with it. The cost is represented by its administrative preference and its protocol-specific metric. Routes with lower costs are preferred over all other routes.
ms.assetid: c5a75308-42da-4ef9-a712-9987c87eef84
ms.topic: article
ms.date: 05/31/2018
---

# Routes and the Best Route

A route is a "network path" to a destination that has a certain cost associated with it. The cost is represented by its administrative preference and its protocol-specific metric. Routes with lower costs are preferred over all other routes.

A route entry in the routing table includes:

-   A handle to the destination
-   The owner of this route
-   The neighbor (peer) that provided the route information
-   Flags associated with the state of the route
-   Flags associated with the route
-   The preference and metric for the route
-   The list of views to which the route belongs
-   Information that is private to the owner of the route
-   A list of next hops used to reach the destination

The following values, taken together, uniquely identify a route in the routing table:

-   The destination network
-   The owner of the route
-   The neighbor who supplied the route

## Metrics and Preference

Each route has an administrative preference (specified by the routing policy), and a client-dependent metric. The routing table manager uses this information to determine which route is the better route to a destination. Routes with lower preference are better routes (one being lowest, and therefore best). If two routes have the same preference, the route with the lower metric is the better route.

Normally, the preference of a route is determined by the preference of the client that added the route. However, for any routes added using the Netsh.exe management tool, a preference value can be specified on a per-route basis.

Preference is normally used to indicate priority between clients. For example, an administrator can assign OSPF a lower (better) preference than RIP. In this case, OSPF routes are preferable to RIP routes.

 

 




