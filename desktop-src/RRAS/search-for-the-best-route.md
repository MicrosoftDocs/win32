---
title: Search For the Best Route
description: The following sample code shows how to search the routing table for the best route.
ms.assetid: 559459e9-8446-4f37-8123-7d01f8ed427b
ms.topic: article
ms.date: 05/31/2018
---

# Search For the Best Route

The following sample code shows how to search the routing table for the best route.


```C++
// Search for a best matching route to a network 
// given (address,mask) for this destination network

// First get the best matching destination

RTM_IPV4_SET_ADDR_AND_MASK(NetAddress, Addr, Mask);

Status = RtmGetMostSpecificDestination(RtmRegHandle,
                                       &NetAddress,
                                       RTM_BEST_PROTOCOL,   // Determines which route information is returned.
                                       RTM_VIEW_MASK_UCAST, // Give the information for the best unicast route
                                       DestInfo);
if (Status == NO_ERROR)
{
    ASSERT(DestInfo->ViewInfo[0].ViewId == RTM_VIEW_ID_UCAST);

    // Get the best unicast route for the destination
    NewBestRoute = DestInfo.ViewInfo[0].Route;

    // Call RtmGetRouteInfo using the handle for information
    //...

    // Release information from RtmGetMostSpecificDestination
    RtmReleaseDestInfo(RtmRegHandle, DestInfo);
}

// To search for an exact match, use RtmGetExactMatchDestionation
```



 

 




