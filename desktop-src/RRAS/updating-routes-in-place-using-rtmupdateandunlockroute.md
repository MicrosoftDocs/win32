---
title: Updating Routes In Place Using RtmUpdateAndUnlockRoute
description: Updating in place is generally more efficient than updating the routing table with an indirect method such as that used by the RtmAddRouteToDest function.
ms.assetid: d4b0b14e-957a-43d5-bacc-8eee4512e2ab
ms.topic: article
ms.date: 05/31/2018
---

# Updating Routes In Place Using RtmUpdateAndUnlockRoute

Updating in place is generally more efficient than updating the routing table with an indirect method such as that used by the [**RtmAddRouteToDest**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmaddroutetodest) function. This method is more efficient because the client is not required to obtain a handle, nor to pass the [**RTM\_ROUTE\_INFO**](/windows/desktop/api/Rtmv2/ns-rtmv2-rtm_route_info) structure to and from the routing table manager. This method also takes less time. However, directly updating the routing table can be risky, since the routing table manager is not functioning as an intermediary.

For sample code that shows how to use these functions, see [Update a Route In Place Using RtmUpdateAndUnlockRoute](update-a-route-in-place-using-rtmupdateandunlockroute.md).

 

 




