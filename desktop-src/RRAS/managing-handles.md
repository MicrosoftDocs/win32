---
title: Managing Handles
description: The routing table manager maintains a reference count for all the information that it maintains.
ms.assetid: bcd02881-b021-414f-8a40-14baac5baac7
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Managing Handles

The routing table manager maintains a reference count for all the information that it maintains. This prevents the routing table manager from returning to a client any handles to memory that has been freed. Each time a handle is returned to the caller, either as an explicit handle or as part of an information structure, such as [**RTM\_DEST\_INFO**](/windows/win32/Rtmv2/ns-rtmv2-_rtm_dest_info?branch=master), the reference count for the object that corresponds to the handle is incremented. When the handle or the information structure is released, the appropriate reference count is decremented. When the reference count becomes zero, the object is freed.

The [**RtmGetDestInfo**](/windows/win32/Rtmv2/nf-rtmv2-rtmgetdestinfo?branch=master), [**RtmGetEntityInfo**](/windows/win32/Rtmv2/nf-rtmv2-rtmgetentityinfo?branch=master), [**RtmGetRouteInfo**](/windows/win32/Rtmv2/nf-rtmv2-rtmgetrouteinfo?branch=master) and [**RtmGetNextHopInfo**](/windows/win32/Rtmv2/nf-rtmv2-rtmgetnexthopinfo?branch=master) functions return information structures. These functions correspond to [**RtmReleaseDestInfo**](/windows/win32/Rtmv2/nf-rtmv2-rtmreleasedestinfo?branch=master), [**RtmReleaseEntityInfo**](/windows/win32/Rtmv2/nf-rtmv2-rtmreleaseentityinfo?branch=master), [**RtmReleaseRouteInfo**](/windows/win32/Rtmv2/nf-rtmv2-rtmreleaserouteinfo?branch=master) and [**RtmRelaseNextHopInfo**](/windows/win32/Rtmv2/nf-rtmv2-rtmreleasenexthopinfo?branch=master) functions, respectively.

> [!Note]  
> The [**RtmReleaseChangedDests**](/windows/win32/Rtmv2/nf-rtmv2-rtmreleasechangeddests?branch=master) function should be used to release handles that have been returned by a call to [**RtmGetChangedDests**](/windows/win32/Rtmv2/nf-rtmv2-rtmgetchangeddests?branch=master). Do not use [**RtmReleaseDests**](/windows/win32/Rtmv2/nf-rtmv2-rtmreleasedests?branch=master) for changed destination structures.

 

If a client must keep a specific handle in an information structure while releasing the rest, the client can call [**RtmReferenceHandles**](/windows/win32/Rtmv2/nf-rtmv2-rtmreferencehandles?branch=master) with that handle before releasing the information structure. The handle can then be released by a call to the [**RtmReleaseDestInfo**](/windows/win32/Rtmv2/nf-rtmv2-rtmreleasedestinfo?branch=master), [**RtmReleaseEntityInfo**](/windows/win32/Rtmv2/nf-rtmv2-rtmreleaseentityinfo?branch=master), [**RtmReleaseRouteInfo**](/windows/win32/Rtmv2/nf-rtmv2-rtmreleaserouteinfo?branch=master) and [**RtmRelaseNextHopInfo**](/windows/win32/Rtmv2/nf-rtmv2-rtmreleasenexthopinfo?branch=master) functions.

 

 




