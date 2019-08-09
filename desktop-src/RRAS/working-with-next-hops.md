---
title: Working with Next Hops
description: The RTMv2 API allows clients to work with the list of next hops that are associated with routes and destinations.
ms.assetid: ef474091-48fe-48e5-b476-73d77dbcbec5
ms.topic: article
ms.date: 05/31/2018
---

# Working with Next Hops

The RTMv2 API allows clients to work with the list of next hops that are associated with routes and destinations. Clients can add or update a next hop by calling [**RtmAddNextHop**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmaddnexthop). Clients can delete a next hop using [**RtmDeleteNextHop**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmdeletenexthop). Clients can search for next hops by calling [**RtmFindNextHop**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmfindnexthop).

Clients can also update the next hop directly. To do so, the client must first lock the next hop with the [**RtmLockNextHop**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmlocknexthop) function. Then the client can use the direct pointer to the routing table manager's [**RTM\_NEXTHOP\_INFO**](/windows/desktop/api/Rtmv2/ns-rtmv2-rtm_nexthop_info) structure to make necessary modifications. Finally, the client can unlock the next hop.

> [!Note]  
> The next-hop address and interface index fields in the next hop uniquely identify the next hop and should not be modified.

 

 

 




