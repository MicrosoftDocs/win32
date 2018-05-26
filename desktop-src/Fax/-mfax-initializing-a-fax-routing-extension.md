---
Description: Each time the fax service starts, it calls the FaxRouteInitialize function once to initialize the fax routing extension.
ms.assetid: 6ea843b4-91f9-48c2-932b-170224f3bc32
title: Initializing a Fax Routing Extension
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Initializing a Fax Routing Extension

Each time the fax service starts, it calls the [**FaxRouteInitialize**](/windows/previous-versions/FaxRoute/nf-faxroute-faxrouteinitialize?branch=master) function once to initialize the fax routing extension. If the function succeeds, the fax service routes received faxes through the extension's fax routing methods, in order of priority. The fax routing extension must perform all necessary initialization when the fax service calls **FaxRouteInitialize**.

The fax service passes pointers to the [**FaxRouteAddFile**](/windows/previous-versions/FaxRoute/nc-faxroute-pfaxrouteaddfile?branch=master), [**FaxRouteDeleteFile**](/windows/previous-versions/FaxRoute/nc-faxroute-pfaxroutedeletefile?branch=master), [**FaxRouteGetFile**](/windows/previous-versions/FaxRoute/nc-faxroute-pfaxroutegetfile?branch=master), [**FaxRouteModifyRoutingData**](/windows/previous-versions/FaxRoute/nc-faxroute-pfaxroutemodifyroutingdata?branch=master), and [**FaxRouteEnumFiles**](/windows/previous-versions/FaxRoute/nc-faxroute-pfaxrouteenumfiles?branch=master) callback functions when the fax service calls [**FaxRouteInitialize**](/windows/previous-versions/FaxRoute/nf-faxroute-faxrouteinitialize?branch=master). The service passes the pointers in a [**FAX\_ROUTE\_CALLBACKROUTINES**](/windows/previous-versions/FaxRoute/ns-faxroute-_fax_route_callbackroutines?branch=master) structure. The extension's fax routing methods call these callback functions to manage the files in the fax file list associated with a received fax document. The fax routing extension must store these callback function pointers in a global variable for later use.

The fax routing extension must export the [**FaxRouteInitialize**](/windows/previous-versions/FaxRoute/nf-faxroute-faxrouteinitialize?branch=master) function.

For more information about registering with the fax service during installation, see [Fax Routing Extension Registration](-mfax-fax-routing-extension-registration.md).

 

 



