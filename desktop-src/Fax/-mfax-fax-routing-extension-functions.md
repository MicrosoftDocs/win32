---
Description: The Fax Routing Extension API includes the following functions and callback functions.
ms.assetid: 339f7fb6-64eb-403e-91be-210501042a25
title: Fax Routing Extension Functions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Fax Routing Extension Functions

The Fax Routing Extension API includes the following functions and callback functions.

Each fax routing extension must export the following functions.

-   [**FaxRouteDeviceChangeNotification**](/previous-versions/windows/desktop/api/FaxRoute/nf-faxroute-faxroutedevicechangenotification)
-   [**FaxRouteDeviceEnable**](/previous-versions/windows/desktop/api/FaxRoute/nf-faxroute-faxroutedeviceenable)
-   [**FaxRouteGetRoutingInfo**](/previous-versions/windows/desktop/api/FaxRoute/nf-faxroute-faxroutegetroutinginfo)
-   [**FaxRouteInitialize**](/previous-versions/windows/desktop/api/FaxRoute/nf-faxroute-faxrouteinitialize)
-   [**FaxRouteMethod**](/previous-versions/windows/desktop/api/FaxRoute/)
-   [**FaxRouteSetRoutingInfo**](/previous-versions/windows/desktop/api/FaxRoute/nf-faxroute-faxroutesetroutinginfo)

The following callback function name is a placeholder for a function defined by the fax routing extension.

-   [**FaxRouteEnumFile**](/previous-versions/windows/desktop/api/FaxRoute/nc-faxroute-pfaxrouteenumfile)

The fax service provides the following callback functions to manage the files in the fax file list associated with a received fax document.

-   [**FaxRouteAddFile**](/previous-versions/windows/desktop/api/FaxRoute/nc-faxroute-pfaxrouteaddfile)
-   [**FaxRouteDeleteFile**](/previous-versions/windows/desktop/api/FaxRoute/nc-faxroute-pfaxroutedeletefile)
-   [**FaxRouteEnumFiles**](/previous-versions/windows/desktop/api/FaxRoute/nc-faxroute-pfaxrouteenumfiles)
-   [**FaxRouteGetFile**](/previous-versions/windows/desktop/api/FaxRoute/nc-faxroute-pfaxroutegetfile)
-   [**FaxRouteModifyRoutingData**](/previous-versions/windows/desktop/api/FaxRoute/nc-faxroute-pfaxroutemodifyroutingdata)

 

 



