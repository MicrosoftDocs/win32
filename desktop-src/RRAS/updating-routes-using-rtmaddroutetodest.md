---
title: Updating Routes Using RtmAddRouteToDest
description: If the client does not require efficiency when adding a route, it should use the following method of updating routes.
ms.assetid: 'bfa914ea-5d54-4ce9-a97c-903c497d135b'
---

# Updating Routes Using RtmAddRouteToDest

If the client does not require efficiency when adding a route, it should use the following method of updating routes. This method is less efficient since it requires obtaining a handle to the route and passing the [**RTM\_ROUTE\_INFO**](rtm-route-info.md) structure to and from the routing table manager. This method also takes more time. Since [**RtmAddRouteToDest**](rtmaddroutetodest.md) does not manipulate the routing table directly, using this method trades efficiency for simplicity.

For sample code that shows how to use these functions, see [Add and Update Routes Using RtmAddRouteToDest](add-and-update-routes-using-rtmaddroutetodest.md).

 

 




