---
title: Managing Handles
description: The routing table manager maintains a reference count for all the information that it maintains.
ms.assetid: 'bcd02881-b021-414f-8a40-14baac5baac7'
---

# Managing Handles

The routing table manager maintains a reference count for all the information that it maintains. This prevents the routing table manager from returning to a client any handles to memory that has been freed. Each time a handle is returned to the caller, either as an explicit handle or as part of an information structure, such as [**RTM\_DEST\_INFO**](rtm-dest-info.md), the reference count for the object that corresponds to the handle is incremented. When the handle or the information structure is released, the appropriate reference count is decremented. When the reference count becomes zero, the object is freed.

The [**RtmGetDestInfo**](rtmgetdestinfo.md), [**RtmGetEntityInfo**](rtmgetentityinfo.md), [**RtmGetRouteInfo**](rtmgetrouteinfo.md) and [**RtmGetNextHopInfo**](rtmgetnexthopinfo.md) functions return information structures. These functions correspond to [**RtmReleaseDestInfo**](rtmreleasedestinfo.md), [**RtmReleaseEntityInfo**](rtmreleaseentityinfo.md), [**RtmReleaseRouteInfo**](rtmreleaserouteinfo.md) and [**RtmRelaseNextHopInfo**](rtmreleasenexthopinfo.md) functions, respectively.

> [!Note]  
> The [**RtmReleaseChangedDests**](rtmreleasechangeddests.md) function should be used to release handles that have been returned by a call to [**RtmGetChangedDests**](rtmgetchangeddests.md). Do not use [**RtmReleaseDests**](rtmreleasedests.md) for changed destination structures.

 

If a client must keep a specific handle in an information structure while releasing the rest, the client can call [**RtmReferenceHandles**](rtmreferencehandles.md) with that handle before releasing the information structure. The handle can then be released by a call to the [**RtmReleaseDestInfo**](rtmreleasedestinfo.md), [**RtmReleaseEntityInfo**](rtmreleaseentityinfo.md), [**RtmReleaseRouteInfo**](rtmreleaserouteinfo.md) and [**RtmRelaseNextHopInfo**](rtmreleasenexthopinfo.md) functions.

 

 




