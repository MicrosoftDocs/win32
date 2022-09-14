---
title: Next Hops
description: Routes have one or more next hops associated with them.
ms.assetid: 90e5a79b-4fee-479c-9888-fcb3b6d38c1f
ms.topic: article
ms.date: 05/31/2018
---

# Next Hops

Routes have one or more next hops associated with them. If the destination is not on a directly connected network, the next hop is the address of the next router (or network) on the outgoing network that can best route data to the destination. The best route is the route that has the least cost, based on the routing policy in use. Each next hop can be used to forward data on the path to the destination. All routes owned by a client share a common set of next-hop entries that were added by the client.

Each next hop is uniquely identified by the address of the next hop and the interface index used to reach the next hop.

If the next hop itself is not directly connected, it is marked as a "remote" next hop. In this case, the forwarder must perform another lookup using the next hop's network address. This lookup is necessary to find the "local" next hop used to reach the remote next hop and the destination.

A next-hop entry in the routing table includes:

-   The network address of the next hop
-   The owner of the next hop
-   The identifier of the outgoing interface
-   The state of the next hop
-   Flags associated with the next hop
-   Information that is private to the owner of the next hop
-   A handle to the destination corresponding to the remote next hop

 

 




