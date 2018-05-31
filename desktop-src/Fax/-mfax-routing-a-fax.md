---
Description: The fax routing extension can export multiple FaxRouteMethod routing functions, one function for each routing method. Each function must have a unique name. FaxRouteMethod is a placeholder for an extension-defined fax routing method.
ms.assetid: f50c80f3-561f-4307-a08f-af7840200753
title: Routing a Fax
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Routing a Fax

The fax routing extension can export multiple [**FaxRouteMethod**](/previous-versions/windows/desktop/api/FaxRoute/) routing functions, one function for each routing method. Each function must have a unique name. **FaxRouteMethod** is a placeholder for an extension-defined fax routing method.

The fax service passes the [**FAX\_ROUTE**](/previous-versions/windows/desktop/api/FaxRoute/ns-faxroute-_fax_route) structure to the fax routing methods. The structure identifies the fax job connected with the received fax, and it contains routing information and data about the calling and receiving fax devices.

A fax routing method can call the [**FaxRouteModifyRoutingData**](/previous-versions/windows/desktop/api/FaxRoute/nc-faxroute-pfaxroutemodifyroutingdata) callback function to change or append routing information in a [**FAX\_ROUTE**](/previous-versions/windows/desktop/api/FaxRoute/ns-faxroute-_fax_route) structure that applies to a subsequent routing method. The routing method to modify must have a lower priority than the calling routing method, and must run after the calling method. (The priority level determines the relative order in which the fax service calls the fax routing methods when the service receives a fax document.)

The fax service passes a pointer to the [**FaxRouteModifyRoutingData**](/previous-versions/windows/desktop/api/FaxRoute/nc-faxroute-pfaxroutemodifyroutingdata) callback function when the fax service calls the [**FaxRouteInitialize**](/previous-versions/windows/desktop/api/FaxRoute/nf-faxroute-faxrouteinitialize) function. The service passes the pointer in a [**FAX\_ROUTE\_CALLBACKROUTINES**](/previous-versions/windows/desktop/api/FaxRoute/ns-faxroute-_fax_route_callbackroutines) structure.

The [**FaxRouteGetRoutingInfo**](/previous-versions/windows/desktop/api/FaxRoute/nf-faxroute-faxroutegetroutinginfo) function and the [**FaxRouteSetRoutingInfo**](/previous-versions/windows/desktop/api/FaxRoute/nf-faxroute-faxroutesetroutinginfo) function retrieve and modify, respectively, fax routing configuration data for a specific fax device. The fax routing extension must export the **FaxRouteGetRoutingInfo** and **FaxRouteSetRoutingInfo** functions.

For information about enabling and disabling fax routing methods, see [Managing Fax Devices](-mfax-managing-fax-devices.md).

 

 



