---
title: Routing Table Manager Version 2 Functions
description: The following functions are used to interact with the routing table manager.
ms.assetid: ac5c6ada-c38e-476a-9896-cdd8c51cc0be
keywords:
- Routing and Remote Access Service RRAS ,Routing Table Manager Version 2, functions
- Routing Table Manager Version 2 RRAS ,functions
ms.topic: article
ms.date: 05/31/2018
---

# Routing Table Manager Version 2 Functions

The following functions are used to interact with the routing table manager.

## Registration Functions

[**RtmRegisterEntity**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmregisterentity)

[**RtmDeregisterEntity**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmderegisterentity)

[**RtmGetRegisteredEntities**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmgetregisteredentities)

[**RtmReleaseEntities**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmreleaseentities)

## Opaque Pointer Functions

[**RtmLockDestination**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmlockdestination)

[**RtmGetOpaqueInformationPointer**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmgetopaqueinformationpointer)

## Export Method Functions

[**RtmGetEntityMethods**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmgetentitymethods)

[**RtmInvokeMethod**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtminvokemethod)

[**RtmBlockMethods**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmblockmethods)

## Handle to Information Structure Functions

[**RtmGetEntityInfo**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmgetentityinfo)

[**RtmGetDestInfo**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmgetdestinfo)

[**RtmGetRouteInfo**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmgetrouteinfo)

[**RtmGetNextHopInfo**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmgetnexthopinfo)

[**RtmReleaseEntityInfo**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmreleaseentityinfo)

[**RtmReleaseDestInfo**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmreleasedestinfo)

[**RtmReleaseRouteInfo**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmreleaserouteinfo)

[**RtmReleaseNextHopInfo**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmreleasenexthopinfo)

## Routing Table Insertion and Deletion Functions

[**RtmAddRouteToDest**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmaddroutetodest)

[**RtmDeleteRouteToDest**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmdeleteroutetodest)

[**RtmHoldDestination**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmholddestination)

[**RtmGetRoutePointer**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmgetroutepointer)

[**RtmLockRoute**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmlockroute)

[**RtmUpdateAndUnlockRoute**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmupdateandunlockroute)

## Routing Table Query Functions

[**RtmGetExactMatchDestination**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmgetexactmatchdestination)

[**RtmGetMostSpecificDestination**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmgetmostspecificdestination)

[**RtmGetLessSpecificDestination**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmgetlessspecificdestination)

[**RtmGetExactMatchRoute**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmgetexactmatchroute)

[**RtmIsBestRoute**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmisbestroute)

## Next-Hop Insertion and Deletion Functions

[**RtmAddNextHop**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmaddnexthop)

[**RtmFindNextHop**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmfindnexthop)

[**RtmDeleteNextHop**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmdeletenexthop)

[**RtmGetNextHopPointer**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmgetnexthoppointer)

[**RtmLockNextHop**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmlocknexthop)

## Routing Table Enumeration Functions

[**RtmCreateDestEnum**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmcreatedestenum)

[**RtmGetEnumDests**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmgetenumdests)

[**RtmReleaseDests**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmreleasedests)

[**RtmCreateRouteEnum**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmcreaterouteenum)

[**RtmGetEnumRoutes**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmgetenumroutes)

[**RtmReleaseRoutes**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmreleaseroutes)

[**RtmCreateNextHopEnum**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmcreatenexthopenum)

[**RtmGetEnumNextHops**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmgetenumnexthops)

[**RtmReleaseNextHops**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmreleasenexthops)

[**RtmDeleteEnumHandle**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmdeleteenumhandle)

## Change Notification Functions

[**RtmRegisterForChangeNotification**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmregisterforchangenotification)

[**RtmGetChangedDests**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmgetchangeddests)

[**RtmReleaseChangedDests**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmreleasechangeddests)

[**RtmIgnoreChangedDests**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmignorechangeddests)

[**RtmGetChangeStatus**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmgetchangestatus)

[**RtmMarkDestForChangeNotification**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmmarkdestforchangenotification)

[**RtmIsMarkedForChangeNotification**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmismarkedforchangenotification)

[**RtmDeregisterFromChangeNotification**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmderegisterfromchangenotification)

## Route List Function

[**RtmCreateRouteList**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmcreateroutelist)

[**RtmInsertInRouteList**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtminsertinroutelist)

[**RtmCreateRouteListEnum**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmcreateroutelistenum)

[**RtmGetListEnumRoutes**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmgetlistenumroutes)

[**RtmDeleteRouteList**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmdeleteroutelist)

## Handle Management Functions

[**RtmReferenceHandles**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmreferencehandles)

 

 




