---
title: Updating Routes Using RtmAddRouteToDest
description: If the client does not require efficiency when adding a route, it should use the following method of updating routes.
ms.assetid: bfa914ea-5d54-4ce9-a97c-903c497d135b
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Updating Routes Using RtmAddRouteToDest

If the client does not require efficiency when adding a route, it should use the following method of updating routes. This method is less efficient since it requires obtaining a handle to the route and passing the [**RTM\_ROUTE\_INFO**](/windows/win32/Rtmv2/ns-rtmv2-_rtm_route_info?branch=master) structure to and from the routing table manager. This method also takes more time. Since [**RtmAddRouteToDest**](/windows/win32/Rtmv2/nf-rtmv2-rtmaddroutetodest?branch=master) does not manipulate the routing table directly, using this method trades efficiency for simplicity.

For sample code that shows how to use these functions, see [Add and Update Routes Using RtmAddRouteToDest](add-and-update-routes-using-rtmaddroutetodest.md).

 

 




