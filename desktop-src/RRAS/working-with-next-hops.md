---
title: Working with Next Hops
description: The RTMv2 API allows clients to work with the list of next hops that are associated with routes and destinations.
ms.assetid: 'ef474091-48fe-48e5-b476-73d77dbcbec5'
---

# Working with Next Hops

The RTMv2 API allows clients to work with the list of next hops that are associated with routes and destinations. Clients can add or update a next hop by calling [**RtmAddNextHop**](rtmaddnexthop.md). Clients can delete a next hop using [**RtmDeleteNextHop**](rtmdeletenexthop.md). Clients can search for next hops by calling [**RtmFindNextHop**](rtmfindnexthop.md).

Clients can also update the next hop directly. To do so, the client must first lock the next hop with the [**RtmLockNextHop**](rtmlocknexthop.md) function. Then the client can use the direct pointer to the routing table manager's [**RTM\_NEXTHOP\_INFO**](rtm-nexthop-info.md) structure to make necessary modifications. Finally, the client can unlock the next hop.

> [!Note]  
> The next-hop address and interface index fields in the next hop uniquely identify the next hop and should not be modified.

 

 

 




