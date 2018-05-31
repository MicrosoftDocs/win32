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

Each time the fax service starts, it calls the [**FaxRouteInitialize**](-mfax-faxrouteinitialize.md) function once to initialize the fax routing extension. If the function succeeds, the fax service routes received faxes through the extension's fax routing methods, in order of priority. The fax routing extension must perform all necessary initialization when the fax service calls **FaxRouteInitialize**.

The fax service passes pointers to the [**FaxRouteAddFile**](-mfax-faxrouteaddfile.md), [**FaxRouteDeleteFile**](-mfax-faxroutedeletefile.md), [**FaxRouteGetFile**](-mfax-faxroutegetfile.md), [**FaxRouteModifyRoutingData**](-mfax-faxroutemodifyroutingdata.md), and [**FaxRouteEnumFiles**](-mfax-faxrouteenumfiles.md) callback functions when the fax service calls [**FaxRouteInitialize**](-mfax-faxrouteinitialize.md). The service passes the pointers in a [**FAX\_ROUTE\_CALLBACKROUTINES**](-mfax-fax-route-callbackroutines-str.md) structure. The extension's fax routing methods call these callback functions to manage the files in the fax file list associated with a received fax document. The fax routing extension must store these callback function pointers in a global variable for later use.

The fax routing extension must export the [**FaxRouteInitialize**](-mfax-faxrouteinitialize.md) function.

For more information about registering with the fax service during installation, see [Fax Routing Extension Registration](-mfax-fax-routing-extension-registration.md).

 

 



