---
title: Managing Handles
description: The routing table manager maintains a reference count for all the information that it maintains.
ms.assetid: bcd02881-b021-414f-8a40-14baac5baac7
ms.topic: article
ms.date: 05/31/2018
---

# Managing Handles

The routing table manager maintains a reference count for all the information that it maintains. This prevents the routing table manager from returning to a client any handles to memory that has been freed. Each time a handle is returned to the caller, either as an explicit handle or as part of an information structure, such as [**RTM\_DEST\_INFO**](/windows/desktop/api/Rtmv2/ns-rtmv2-rtm_dest_info), the reference count for the object that corresponds to the handle is incremented. When the handle or the information structure is released, the appropriate reference count is decremented. When the reference count becomes zero, the object is freed.

The [**RtmGetDestInfo**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmgetdestinfo), [**RtmGetEntityInfo**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmgetentityinfo), [**RtmGetRouteInfo**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmgetrouteinfo) and [**RtmGetNextHopInfo**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmgetnexthopinfo) functions return information structures. These functions correspond to [**RtmReleaseDestInfo**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmreleasedestinfo), [**RtmReleaseEntityInfo**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmreleaseentityinfo), [**RtmReleaseRouteInfo**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmreleaserouteinfo) and [**RtmRelaseNextHopInfo**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmreleasenexthopinfo) functions, respectively.

> [!Note]  
> The [**RtmReleaseChangedDests**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmreleasechangeddests) function should be used to release handles that have been returned by a call to [**RtmGetChangedDests**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmgetchangeddests). Do not use [**RtmReleaseDests**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmreleasedests) for changed destination structures.

 

If a client must keep a specific handle in an information structure while releasing the rest, the client can call [**RtmReferenceHandles**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmreferencehandles) with that handle before releasing the information structure. The handle can then be released by a call to the [**RtmReleaseDestInfo**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmreleasedestinfo), [**RtmReleaseEntityInfo**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmreleaseentityinfo), [**RtmReleaseRouteInfo**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmreleaserouteinfo) and [**RtmRelaseNextHopInfo**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmreleasenexthopinfo) functions.

 

 




