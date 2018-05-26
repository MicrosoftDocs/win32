---
Description: The fax routing extension can export multiple FaxRouteMethod routing functions, one function for each routing method. Each function must have a unique name. FaxRouteMethod is a placeholder for an extension-defined fax routing method.
ms.assetid: f50c80f3-561f-4307-a08f-af7840200753
title: Routing a Fax
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Routing a Fax

The fax routing extension can export multiple [**FaxRouteMethod**](/windows/previous-versions/FaxRoute/?branch=master) routing functions, one function for each routing method. Each function must have a unique name. **FaxRouteMethod** is a placeholder for an extension-defined fax routing method.

The fax service passes the [**FAX\_ROUTE**](/windows/previous-versions/FaxRoute/ns-faxroute-_fax_route?branch=master) structure to the fax routing methods. The structure identifies the fax job connected with the received fax, and it contains routing information and data about the calling and receiving fax devices.

A fax routing method can call the [**FaxRouteModifyRoutingData**](/windows/previous-versions/FaxRoute/nc-faxroute-pfaxroutemodifyroutingdata?branch=master) callback function to change or append routing information in a [**FAX\_ROUTE**](/windows/previous-versions/FaxRoute/ns-faxroute-_fax_route?branch=master) structure that applies to a subsequent routing method. The routing method to modify must have a lower priority than the calling routing method, and must run after the calling method. (The priority level determines the relative order in which the fax service calls the fax routing methods when the service receives a fax document.)

The fax service passes a pointer to the [**FaxRouteModifyRoutingData**](/windows/previous-versions/FaxRoute/nc-faxroute-pfaxroutemodifyroutingdata?branch=master) callback function when the fax service calls the [**FaxRouteInitialize**](/windows/previous-versions/FaxRoute/nf-faxroute-faxrouteinitialize?branch=master) function. The service passes the pointer in a [**FAX\_ROUTE\_CALLBACKROUTINES**](/windows/previous-versions/FaxRoute/ns-faxroute-_fax_route_callbackroutines?branch=master) structure.

The [**FaxRouteGetRoutingInfo**](/windows/previous-versions/FaxRoute/nf-faxroute-faxroutegetroutinginfo?branch=master) function and the [**FaxRouteSetRoutingInfo**](/windows/previous-versions/FaxRoute/nf-faxroute-faxroutesetroutinginfo?branch=master) function retrieve and modify, respectively, fax routing configuration data for a specific fax device. The fax routing extension must export the **FaxRouteGetRoutingInfo** and **FaxRouteSetRoutingInfo** functions.

For information about enabling and disabling fax routing methods, see [Managing Fax Devices](-mfax-managing-fax-devices.md).

 

 



