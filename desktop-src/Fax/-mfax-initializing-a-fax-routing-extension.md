---
Description: Each time the fax service starts, it calls the FaxRouteInitialize function once to initialize the fax routing extension.
ms.assetid: 6ea843b4-91f9-48c2-932b-170224f3bc32
title: Initializing a Fax Routing Extension
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Initializing a Fax Routing Extension

Each time the fax service starts, it calls the [**FaxRouteInitialize**](/previous-versions/windows/desktop/api/FaxRoute/nf-faxroute-faxrouteinitialize) function once to initialize the fax routing extension. If the function succeeds, the fax service routes received faxes through the extension's fax routing methods, in order of priority. The fax routing extension must perform all necessary initialization when the fax service calls **FaxRouteInitialize**.

The fax service passes pointers to the [**FaxRouteAddFile**](/previous-versions/windows/desktop/api/FaxRoute/nc-faxroute-pfaxrouteaddfile), [**FaxRouteDeleteFile**](/previous-versions/windows/desktop/api/FaxRoute/nc-faxroute-pfaxroutedeletefile), [**FaxRouteGetFile**](/previous-versions/windows/desktop/api/FaxRoute/nc-faxroute-pfaxroutegetfile), [**FaxRouteModifyRoutingData**](/previous-versions/windows/desktop/api/FaxRoute/nc-faxroute-pfaxroutemodifyroutingdata), and [**FaxRouteEnumFiles**](/previous-versions/windows/desktop/api/FaxRoute/nc-faxroute-pfaxrouteenumfiles) callback functions when the fax service calls [**FaxRouteInitialize**](/previous-versions/windows/desktop/api/FaxRoute/nf-faxroute-faxrouteinitialize). The service passes the pointers in a [**FAX\_ROUTE\_CALLBACKROUTINES**](/previous-versions/windows/desktop/api/FaxRoute/ns-faxroute-_fax_route_callbackroutines) structure. The extension's fax routing methods call these callback functions to manage the files in the fax file list associated with a received fax document. The fax routing extension must store these callback function pointers in a global variable for later use.

The fax routing extension must export the [**FaxRouteInitialize**](/previous-versions/windows/desktop/api/FaxRoute/nf-faxroute-faxrouteinitialize) function.

For more information about registering with the fax service during installation, see [Fax Routing Extension Registration](-mfax-fax-routing-extension-registration.md).

 

 



