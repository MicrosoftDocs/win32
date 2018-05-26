---
Description: A fax routing method is a procedure defined by a fax routing extension DLL. Fax routing methods execute, in order of priority, when a fax port receives an inbound fax transmission.
ms.assetid: a2144af9-9101-478f-93b9-393101dc1936
title: Fax Routing Methods
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Fax Routing Methods

A fax routing method is a procedure defined by a fax routing extension DLL. Fax routing methods execute, in order of priority, when a fax port receives an inbound fax transmission. For more information, see [Managing Fax Routing Data](-mfax-managing-fax-routing-data.md).

A GUID is necessary to identify a fax routing method for the following reasons.

-   A fax routing extension DLL can support multiple routing methods.
-   A fax routing extension DLL can maintain unique configuration data for each routing method and for each fax device.
-   Multiple fax routing extension DLLs can export routing methods with the same name.

For more information about developing, installing, and registering a routing extension DLL, see [About the Fax Routing Extension API](-mfax-about-the-fax-routing-extension-api.md).

 

 



