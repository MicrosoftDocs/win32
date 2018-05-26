---
title: Add and Update Routes Using RtmAddRouteToDest
description: The function RtmAddRouteToDest is used to add new routes and update existing routes for a destination. The following procedures explain both cases. The sample code that follows shows how to implement the first procedure.
ms.assetid: 17a04511-69f8-4e50-993c-0e558ee72184
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Add and Update Routes Using RtmAddRouteToDest

The function [**RtmAddRouteToDest**](/windows/win32/Rtmv2/nf-rtmv2-rtmaddroutetodest?branch=master) is used to add new routes and update existing routes for a destination. The following procedures explain both cases. The sample code that follows shows how to implement the first procedure.

**To add a route, the client should take the following steps**

1.  If the client has already cached the next-hop handle, go to step 4.
2.  Create an [**RTM\_NEXTHOP\_INFO**](/windows/win32/Rtmv2/ns-rtmv2-_rtm_nexthop_info?branch=master) structure and fill it with the appropriate information.
3.  Add the next hop to the routing table by calling [**RtmAddNextHop**](/windows/win32/Rtmv2/nf-rtmv2-rtmaddnexthop?branch=master). The routing table manager returns a handle to the next hop. If the next hop already exists, the routing table does not add the next hop; instead it returns the handle to the next hop.
4.  Create an [**RTM\_ROUTE\_INFO**](/windows/win32/Rtmv2/ns-rtmv2-_rtm_route_info?branch=master) structure and fill it with the appropriate information, including the next-hop handle returned by the routing table manager.
5.  Add the route to the routing table by calling [**RtmAddRouteToDest**](/windows/win32/Rtmv2/nf-rtmv2-rtmaddroutetodest?branch=master). The routing table manager compares the new route to the routes that are already in the routing table. Two routes are equal if all of the following conditions are true:

    -   The route is being added to the same destination.
    -   The route is being added by the same client as specified by the **Owner** member of the [**RTM\_ROUTE\_INFO**](/windows/win32/Rtmv2/ns-rtmv2-_rtm_route_info?branch=master) structure.
    -   The route is advertised by the same neighbor as specified by the **Neighbor** member of the [**RTM\_ROUTE\_INFO**](/windows/win32/Rtmv2/ns-rtmv2-_rtm_route_info?branch=master) structure.

    If the route exists, the routing table manager returns the handle to the existing route. Otherwise, the routing table manager adds the route and returns the handle to the new route.

    The client can set the *Change\_Flags* parameter to RTM\_ROUTE\_CHANGE\_NEW to instruct the routing table manager to add a new route on the destination, even if another route with the same owner and neighbor fields exists.

    The client can set the *Change\_Flags* parameter to RTM\_ROUTE\_CHANGE\_FIRST to tell the routing table manager to update the first route on the destination owned by the client. This update can be performed if such a route exists, even if the neighbor field does not match. This flag is used by clients that maintain a single route per destination.

**To update a route, the client should take the following steps**

1.  Call [**RtmGetRouteInfo**](/windows/win32/Rtmv2/nf-rtmv2-rtmgetrouteinfo?branch=master) with the handle to the route. The handle is either one previously cached by the client, or returned by the routing table manager from a call that returns a route handle such as **RtmGetRouteInfo**.
2.  Make the changes to the [**RTM\_ROUTE\_INFO**](/windows/win32/Rtmv2/ns-rtmv2-_rtm_route_info?branch=master) structure that is returned by the routing table manager.
3.  Call [**RtmAddRouteToDest**](/windows/win32/Rtmv2/nf-rtmv2-rtmaddroutetodest?branch=master) with the handle to the route and the changed [**RTM\_ROUTE\_INFO**](/windows/win32/Rtmv2/ns-rtmv2-_rtm_route_info?branch=master) structure.

The following sample code shows how to add a route to a destination using the routing table manager as an intermediary.


```C++
// Add a route to a destination given by (addr, masklen)
// using a next hop reachable with an interface

RTM_NEXTHOP_INFO NextHopInfo;

// First, create and add a next hop to the caller's
// next-hop tree (if it does not already exist)

ZeroMemory(&amp;NextHopInfo, sizeof(RTM_NEXTHOP_INFO);

RTM_IPV4_MAKE_NET_ADDRESS(&amp;NextHopInfo.NextHopAddress,
                          nexthop, // Address of the next hop
                          32);

NextHopInfo.InterfaceIndex = interface;

NextHopHandle = NULL;

Status = RtmAddNextHop(RtmRegHandle,
                       &amp;NextHopInfo,
                       &amp;NextHopHandle,
                       &amp;ChangeFlags);

if (Status == NO_ERROR)
{
    // Created a new next hop or found an old one

        // Fill in the route information for the route
    
    ZeroMemory(&amp;RouteInfo, sizeof(RTM_ROUTE_INFO);

    // Fill in the destination network's address and mask values
    RTM_IPV4_MAKE_NET_ADDRESS(&amp;NetAddress, addr, masklen);

    // Assume 'neighbour learnt from' is the first next hop
    RouteInfo.Neighbour = NextHopHandle;

    // Set metric for route; Preference set internally
    RouteInfo.PrefInfo.Metric = metric;

    // Adding a route to both the unicast and multicast views
    RouteInfo.BelongsToViews = RTM_VIEW_MASK_UCAST|RTM_VIEW_MASK_MCAST;

    RouteInfo.NextHopsList.NumNextHops = 1;
    RouteInfo.NextHopsList.NextHops[0] = NextHopHandle;

    // If you want to add a new route, regardless of
    // whether a similar route already exists, use the following 
    //     ChangeFlags = RTM_ROUTE_CHANGE_NEW;

    ChangeFlags = 0;

    Status = RtmAddRouteToDest(RtmRegHandle,
                               &amp;RouteHandle,     // Can be NULL if you do not need handle
                               &amp;NetAddress,
                               &amp;RouteInfo,
                               1000,             // Time out route after 1000 ms
                               RouteListHandle1, // Also add the route to this list
                               0,
                               NULL,
                               &amp;ChangeFlags);

    if (Status == NO_ERROR)
    {
        if (ChangeFlags & RTM_ROUTE_CHANGE_NEW)
        {
        ; // A new route has been created
        }
        else
        {
        ; // An existing route is updated
        }

        if (ChangeFlags & RTM_ROUTE_CHANGE_BEST)
        {
        ; // Best route information has changed
        }

        // Release the route handle if you do not need it
        RtmReleaseRoutes(RtmRegHandle, 1, &amp;RouteHandle);
    }

    // Also release the next hop since it is no longer needed 
    RtmReleaseNextHops(RtmRegHandle, 1, &amp;NextHopHandle);
}
```



 

 




