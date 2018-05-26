---
title: Routing Table Manager Version 2 Functions
description: The following functions are used to interact with the routing table manager.
ms.assetid: ac5c6ada-c38e-476a-9896-cdd8c51cc0be
keywords:
- Routing and Remote Access Service RRAS ,Routing Table Manager Version 2, functions
- Routing Table Manager Version 2 RRAS ,functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Routing Table Manager Version 2 Functions

The following functions are used to interact with the routing table manager.

## Registration Functions

[**RtmRegisterEntity**](/windows/win32/Rtmv2/nf-rtmv2-rtmregisterentity?branch=master)

[**RtmDeregisterEntity**](/windows/win32/Rtmv2/nf-rtmv2-rtmderegisterentity?branch=master)

[**RtmGetRegisteredEntities**](/windows/win32/Rtmv2/nf-rtmv2-rtmgetregisteredentities?branch=master)

[**RtmReleaseEntities**](/windows/win32/Rtmv2/nf-rtmv2-rtmreleaseentities?branch=master)

## Opaque Pointer Functions

[**RtmLockDestination**](/windows/win32/Rtmv2/nf-rtmv2-rtmlockdestination?branch=master)

[**RtmGetOpaqueInformationPointer**](/windows/win32/Rtmv2/nf-rtmv2-rtmgetopaqueinformationpointer?branch=master)

## Export Method Functions

[**RtmGetEntityMethods**](/windows/win32/Rtmv2/nf-rtmv2-rtmgetentitymethods?branch=master)

[**RtmInvokeMethod**](/windows/win32/Rtmv2/nf-rtmv2-rtminvokemethod?branch=master)

[**RtmBlockMethods**](/windows/win32/Rtmv2/nf-rtmv2-rtmblockmethods?branch=master)

## Handle to Information Structure Functions

[**RtmGetEntityInfo**](/windows/win32/Rtmv2/nf-rtmv2-rtmgetentityinfo?branch=master)

[**RtmGetDestInfo**](/windows/win32/Rtmv2/nf-rtmv2-rtmgetdestinfo?branch=master)

[**RtmGetRouteInfo**](/windows/win32/Rtmv2/nf-rtmv2-rtmgetrouteinfo?branch=master)

[**RtmGetNextHopInfo**](/windows/win32/Rtmv2/nf-rtmv2-rtmgetnexthopinfo?branch=master)

[**RtmReleaseEntityInfo**](/windows/win32/Rtmv2/nf-rtmv2-rtmreleaseentityinfo?branch=master)

[**RtmReleaseDestInfo**](/windows/win32/Rtmv2/nf-rtmv2-rtmreleasedestinfo?branch=master)

[**RtmReleaseRouteInfo**](/windows/win32/Rtmv2/nf-rtmv2-rtmreleaserouteinfo?branch=master)

[**RtmReleaseNextHopInfo**](/windows/win32/Rtmv2/nf-rtmv2-rtmreleasenexthopinfo?branch=master)

## Routing Table Insertion and Deletion Functions

[**RtmAddRouteToDest**](/windows/win32/Rtmv2/nf-rtmv2-rtmaddroutetodest?branch=master)

[**RtmDeleteRouteToDest**](/windows/win32/Rtmv2/nf-rtmv2-rtmdeleteroutetodest?branch=master)

[**RtmHoldDestination**](/windows/win32/Rtmv2/nf-rtmv2-rtmholddestination?branch=master)

[**RtmGetRoutePointer**](/windows/win32/Rtmv2/nf-rtmv2-rtmgetroutepointer?branch=master)

[**RtmLockRoute**](/windows/win32/Rtmv2/nf-rtmv2-rtmlockroute?branch=master)

[**RtmUpdateAndUnlockRoute**](/windows/win32/Rtmv2/nf-rtmv2-rtmupdateandunlockroute?branch=master)

## Routing Table Query Functions

[**RtmGetExactMatchDestination**](/windows/win32/Rtmv2/nf-rtmv2-rtmgetexactmatchdestination?branch=master)

[**RtmGetMostSpecificDestination**](/windows/win32/Rtmv2/nf-rtmv2-rtmgetmostspecificdestination?branch=master)

[**RtmGetLessSpecificDestination**](/windows/win32/Rtmv2/nf-rtmv2-rtmgetlessspecificdestination?branch=master)

[**RtmGetExactMatchRoute**](/windows/win32/Rtmv2/nf-rtmv2-rtmgetexactmatchroute?branch=master)

[**RtmIsBestRoute**](/windows/win32/Rtmv2/nf-rtmv2-rtmisbestroute?branch=master)

## Next-Hop Insertion and Deletion Functions

[**RtmAddNextHop**](/windows/win32/Rtmv2/nf-rtmv2-rtmaddnexthop?branch=master)

[**RtmFindNextHop**](/windows/win32/Rtmv2/nf-rtmv2-rtmfindnexthop?branch=master)

[**RtmDeleteNextHop**](/windows/win32/Rtmv2/nf-rtmv2-rtmdeletenexthop?branch=master)

[**RtmGetNextHopPointer**](/windows/win32/Rtmv2/nf-rtmv2-rtmgetnexthoppointer?branch=master)

[**RtmLockNextHop**](/windows/win32/Rtmv2/nf-rtmv2-rtmlocknexthop?branch=master)

## Routing Table Enumeration Functions

[**RtmCreateDestEnum**](/windows/win32/Rtmv2/nf-rtmv2-rtmcreatedestenum?branch=master)

[**RtmGetEnumDests**](/windows/win32/Rtmv2/nf-rtmv2-rtmgetenumdests?branch=master)

[**RtmReleaseDests**](/windows/win32/Rtmv2/nf-rtmv2-rtmreleasedests?branch=master)

[**RtmCreateRouteEnum**](/windows/win32/Rtmv2/nf-rtmv2-rtmcreaterouteenum?branch=master)

[**RtmGetEnumRoutes**](/windows/win32/Rtmv2/nf-rtmv2-rtmgetenumroutes?branch=master)

[**RtmReleaseRoutes**](/windows/win32/Rtmv2/nf-rtmv2-rtmreleaseroutes?branch=master)

[**RtmCreateNextHopEnum**](/windows/win32/Rtmv2/nf-rtmv2-rtmcreatenexthopenum?branch=master)

[**RtmGetEnumNextHops**](/windows/win32/Rtmv2/nf-rtmv2-rtmgetenumnexthops?branch=master)

[**RtmReleaseNextHops**](/windows/win32/Rtmv2/nf-rtmv2-rtmreleasenexthops?branch=master)

[**RtmDeleteEnumHandle**](/windows/win32/Rtmv2/nf-rtmv2-rtmdeleteenumhandle?branch=master)

## Change Notification Functions

[**RtmRegisterForChangeNotification**](/windows/win32/Rtmv2/nf-rtmv2-rtmregisterforchangenotification?branch=master)

[**RtmGetChangedDests**](/windows/win32/Rtmv2/nf-rtmv2-rtmgetchangeddests?branch=master)

[**RtmReleaseChangedDests**](/windows/win32/Rtmv2/nf-rtmv2-rtmreleasechangeddests?branch=master)

[**RtmIgnoreChangedDests**](/windows/win32/Rtmv2/nf-rtmv2-rtmignorechangeddests?branch=master)

[**RtmGetChangeStatus**](/windows/win32/Rtmv2/nf-rtmv2-rtmgetchangestatus?branch=master)

[**RtmMarkDestForChangeNotification**](/windows/win32/Rtmv2/nf-rtmv2-rtmmarkdestforchangenotification?branch=master)

[**RtmIsMarkedForChangeNotification**](/windows/win32/Rtmv2/nf-rtmv2-rtmismarkedforchangenotification?branch=master)

[**RtmDeregisterFromChangeNotification**](/windows/win32/Rtmv2/nf-rtmv2-rtmderegisterfromchangenotification?branch=master)

## Route List Function

[**RtmCreateRouteList**](/windows/win32/Rtmv2/nf-rtmv2-rtmcreateroutelist?branch=master)

[**RtmInsertInRouteList**](/windows/win32/Rtmv2/nf-rtmv2-rtminsertinroutelist?branch=master)

[**RtmCreateRouteListEnum**](/windows/win32/Rtmv2/nf-rtmv2-rtmcreateroutelistenum?branch=master)

[**RtmGetListEnumRoutes**](/windows/win32/Rtmv2/nf-rtmv2-rtmgetlistenumroutes?branch=master)

[**RtmDeleteRouteList**](/windows/win32/Rtmv2/nf-rtmv2-rtmdeleteroutelist?branch=master)

## Handle Management Functions

[**RtmReferenceHandles**](/windows/win32/Rtmv2/nf-rtmv2-rtmreferencehandles?branch=master)

 

 




