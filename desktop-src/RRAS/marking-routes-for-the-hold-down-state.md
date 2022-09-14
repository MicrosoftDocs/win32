---
title: Marking Routes for the Hold-Down State
description: Some clients, such as distance vector protocols like RIP and DVMRP, require that destinations be advertised as unreachable for a certain time after the last route to the destination is deleted.
ms.assetid: 2a86c092-d8a6-4fd4-8b2e-451c160f743f
ms.topic: article
ms.date: 05/31/2018
---

# Marking Routes for the Hold-Down State

Some clients, such as distance vector protocols like RIP and DVMRP, require that destinations be advertised as unreachable for a certain time after the last route to the destination is deleted. The last route that is deleted must be advertised as unreachable even if newer routes arrive in the meantime. The last route deleted is marked as being in a *hold-down state*. The hold-down process prevents the formation of routing loops. Routing loops are caused when a routing protocol advertises obsolete routing information. When the hold-down expires, these protocols resume their advertisement with the new best route.

A protocol that implements hold-down states indicates that a destination is in a hold-down state by using the [**RtmHoldDestination**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmholddestination) function. The client calls this function when it advertises the best route to this destination. If all routes to this destination are later deleted, the last route that is deleted is kept in a hold-down state for the period of time specified in the earlier call to **RtmHoldDestination**.

When a protocol advertises a destination, the route information that is used depends on whether the protocol uses hold-down states and if a route in the hold-down state exists for the destination.

Protocols that do not use hold-down states can ignore route information that relates to hold-down states for a destination, and always advertise the best route.

For sample code that shows how to use these functions, see [Use the Route Hold-Down State](use-the-route-hold-down-state.md).

 

 




