---
Description: The Fax Routing Extension API includes the following functions and callback functions.
ms.assetid: 339f7fb6-64eb-403e-91be-210501042a25
title: Fax Routing Extension Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Fax Routing Extension Functions

The Fax Routing Extension API includes the following functions and callback functions.

Each fax routing extension must export the following functions.

-   [**FaxRouteDeviceChangeNotification**](/windows/previous-versions/FaxRoute/nf-faxroute-faxroutedevicechangenotification?branch=master)
-   [**FaxRouteDeviceEnable**](/windows/previous-versions/FaxRoute/nf-faxroute-faxroutedeviceenable?branch=master)
-   [**FaxRouteGetRoutingInfo**](/windows/previous-versions/FaxRoute/nf-faxroute-faxroutegetroutinginfo?branch=master)
-   [**FaxRouteInitialize**](/windows/previous-versions/FaxRoute/nf-faxroute-faxrouteinitialize?branch=master)
-   [**FaxRouteMethod**](/windows/previous-versions/FaxRoute/?branch=master)
-   [**FaxRouteSetRoutingInfo**](/windows/previous-versions/FaxRoute/nf-faxroute-faxroutesetroutinginfo?branch=master)

The following callback function name is a placeholder for a function defined by the fax routing extension.

-   [**FaxRouteEnumFile**](/windows/previous-versions/FaxRoute/nc-faxroute-pfaxrouteenumfile?branch=master)

The fax service provides the following callback functions to manage the files in the fax file list associated with a received fax document.

-   [**FaxRouteAddFile**](/windows/previous-versions/FaxRoute/nc-faxroute-pfaxrouteaddfile?branch=master)
-   [**FaxRouteDeleteFile**](/windows/previous-versions/FaxRoute/nc-faxroute-pfaxroutedeletefile?branch=master)
-   [**FaxRouteEnumFiles**](/windows/previous-versions/FaxRoute/nc-faxroute-pfaxrouteenumfiles?branch=master)
-   [**FaxRouteGetFile**](/windows/previous-versions/FaxRoute/nc-faxroute-pfaxroutegetfile?branch=master)
-   [**FaxRouteModifyRoutingData**](/windows/previous-versions/FaxRoute/nc-faxroute-pfaxroutemodifyroutingdata?branch=master)

 

 



