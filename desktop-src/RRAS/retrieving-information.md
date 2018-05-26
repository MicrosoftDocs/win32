---
title: Retrieving Information
description: RTMv2 allows a client to retrieve the information referred to by a given handle using the RtmGetEntityInfo, RtmGetDestInfo, RtmGetRouteInfo, and RtmGetNextHopInfo functions.
ms.assetid: a3fc2020-eac4-40a1-9a6e-6eaa2bcc582c
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Retrieving Information

RTMv2 allows a client to retrieve the information referred to by a given handle using the [**RtmGetEntityInfo**](/windows/win32/Rtmv2/nf-rtmv2-rtmgetentityinfo?branch=master), [**RtmGetDestInfo**](/windows/win32/Rtmv2/nf-rtmv2-rtmgetdestinfo?branch=master), [**RtmGetRouteInfo**](/windows/win32/Rtmv2/nf-rtmv2-rtmgetrouteinfo?branch=master), and [**RtmGetNextHopInfo**](/windows/win32/Rtmv2/nf-rtmv2-rtmgetnexthopinfo?branch=master) functions.

These function calls have corresponding functions ([**RtmReleaseEntityInfo**](/windows/win32/Rtmv2/nf-rtmv2-rtmreleaseentityinfo?branch=master), [**RtmReleaseDestInfo**](/windows/win32/Rtmv2/nf-rtmv2-rtmreleasedestinfo?branch=master), [**RtmReleaseRouteInfo**](/windows/win32/Rtmv2/nf-rtmv2-rtmreleaserouteinfo?branch=master), [**RtmReleaseNextHopInfo**](/windows/win32/Rtmv2/nf-rtmv2-rtmreleasenexthopinfo?branch=master)) to release the handles associated with the information structure returned by the routing table manager.

> [!Note]  
> Information for clients is available only in the current instance and address family.

 

For sample code that shows how to use these functions, see [Search For the Best Route](search-for-the-best-route.md).

## Using RtmGetExactMatchRoute and RtmGetExactMatchDestination

The [**RtmGetExactMatchRoute**](/windows/win32/Rtmv2/nf-rtmv2-rtmgetexactmatchroute?branch=master) and [**RtmGetExactMatchDestination**](/windows/win32/Rtmv2/nf-rtmv2-rtmgetexactmatchdestination?branch=master) functions are used by clients to find a specific route or destination. These functions save time by doing the comparison work for the client.

For example, when RIP updates a route, RIP must retain the old metric information. RIP searches for the route and its information. Then RIP can copy the information and update the route.

## Using RtmGetMostSpecificDestination

The [**RtmGetMostSpecificDestination**](/windows/win32/Rtmv2/nf-rtmv2-rtmgetmostspecificdestination?branch=master) function is used to locate the destination that best matches the specified network prefix.

For example, the multicast group manager uses this function to perform a reverse-path-forwarding (RPF) check on a single address. The function can also be used to find the local next hop for a given remote next hop.

For sample code that shows how to use these functions, see [Search for Routes Using a Prefix Tree](search-for-routes-using-rtmgetmostspecificdestination-and-rtmgetlessspecificdestination.md) and [Search For the Best Route](search-for-the-best-route.md).

## Using RtmGetLessSpecificDestination

The [**RtmGetLessSpecificDestination**](/windows/win32/Rtmv2/nf-rtmv2-rtmgetlessspecificdestination?branch=master) function is used to locate the destination that is the next-best match for the specified network prefix. This function can be called repeatedly to return the next successive less-specific match, until no more destinations match.

This function is called after a call to [**RtmGetMostSpecificDestination**](/windows/win32/Rtmv2/nf-rtmv2-rtmgetmostspecificdestination?branch=master).

For sample code that illustrates how to use these functions, see [Search for Routes Using a Prefix Tree](search-for-routes-using-rtmgetmostspecificdestination-and-rtmgetlessspecificdestination.md).

## Using RtmIsBestRoute

The [**RtmIsBestRoute**](/windows/win32/Rtmv2/nf-rtmv2-rtmisbestroute?branch=master) function enables a client to quickly find out whether or not a particular route is the best route to a destination. For example, a client may need to store a particular route only if it is the best route. Therefore, the client can call this function, instead of enumerating all routes and making the comparison itself.

 

 




