---
title: Update a Route In Place Using RtmUpdateAndUnlockRoute
description: The following procedure outlines the steps used to update a route in place. The sample code that follows shows how to implement the procedure.
ms.assetid: 3598a28f-8ade-4b3f-9d31-4f2c84df2dd6
ms.topic: article
ms.date: 05/31/2018
---

# Update a Route In Place Using RtmUpdateAndUnlockRoute

The following procedure outlines the steps used to update a route in place. The sample code that follows shows how to implement the procedure.

**To update a route in place, the client should take the following steps**

1.  Lock the route by calling [**RtmLockRoute**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmlockroute). Currently, this function actually locks the route's destination. The routing table manager returns a pointer to the route.
2.  Use the pointer to the routing table manager's [**RTM\_ROUTE\_INFO**](/windows/desktop/api/Rtmv2/ns-rtmv2-rtm_route_info) structure, obtained in step 1, to make the necessary changes to the route. Only certain members of the **RTM\_ROUTE\_INFO** structure can be modified when updating in place. These members are: **Neighbour**, **PrefInfo**, **EntitySpecificInfo**, **BelongsToViews**, and **NextHopsList**.
    > [!Note]  
    > If the client adds information to either the **Neighbour** or **NextHopsList** members, the client must call [**RtmReferenceHandles**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmreferencehandles) to explicitly increment the reference count that the routing table manager keeps on the next-hop object. Similarly, if the client removes information from the **NextHopsList** member, the client must call [**RtmReleaseNextHops**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmreleasenexthops) to decrement the reference count.

     

3.  Call [**RtmUpdateAndUnlockRoute**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmupdateandunlockroute) to notify the routing table manager that a change has taken place. The routing table manager commits the changes, updates the destination to reflect the new information, and then unlocks the route.

The following sample code shows how to update a route directly, using a pointer to the actual route information in the routing table.


```C++
Status = RtmLockRoute(RtmRegHandle,
                      RouteHandle,
                      TRUE,
                      TRUE,
                      &RoutePointer);

if (Status == NO_ERROR)
{
        // Update route parameters in place (i.e., directly on 
// the routing table manager's copy)
    
    // Update the metric and views of the route
    RoutePointer->PrefInfo.Metric = 16;

    // Change the views so that the route belongs to only the multicast view
    RoutePointer->BelongsToViews = RTM_VIEW_MASK_MCAST;

    // Set the entity-specific information to X
    RoutePointer->EntitySpecificInfo = X;

    // Note that the following manipulation of
    // next-hop references is not needed when
    // using RtmAddRouteToDest, as it is done
    // by the routing table manager automatically
    
    // Change next hop from NextHop1 to NextHop2
    NextHop1 = RoutePointer->NextHopsList.NextHop[0];

    // Explicitly dereference the old next hop
    RtmReleaseNextHops(RtmRegHandle, 1, &NextHop1);

    RoutePointer->NextHopsList.NextHop[0] = NextHop2;

    // Explicitly reference next hop being added
    RtmReferenceHandles(RtmRegHandle, 1, &NextHop2);

    // Call the routing table manager to indicate that route information
    // has changed, and that its position might
    // have to be rearranged and the corresponding destination
    // needs to be updated to reflect this change.
    
    Status = RtmUpdateAndUnlockRoute(RtmRegHandle,
                                     RouteHandle,
                                     INFINITE, // Keep forever
                                     NULL,
                                     0,
                                     NULL,
                                     &ChangeFlags);
    ASSERT(Status == NO_ERROR);
}
```



 

 




