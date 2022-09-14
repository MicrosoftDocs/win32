---
title: About Windows Connect Now
description: Windows Connect Now (WCN) provides a simple and secure mechanism for network access points and devices (like printers, camera, and PCs) to connect and exchange settings.
ms.assetid: 5c654800-e58b-4a94-b7a6-9a603f540603
ms.topic: article
ms.date: 05/31/2018
---

# About Windows Connect Now

Windows Connect Now (WCN) provides a simple and secure mechanism for network access points and devices (like printers, camera, and PCs) to connect and exchange settings. This API is the Microsoft implementation of the Wi-Fi Protected Setup (WPS)/Wi-Fi Simple Configuration (WSC) protocol, which was created by the Wi-Fi Alliance as a solution for home networking and small businesses. This technology is not intended for enterprise scenarios.

> [!Note]  
> The specification name changed between version 1.0h and version 2. The version 1.0h specification was named Wi-Fi Protected Setup (WPS). Starting with version 2 specification, the specification is named Wi-Fi Simple Configuration (WSC). In our documentation, the terms WPS and WSC are used interchangeably unless noted.

 

Windows Connect Now enables applications to search for WCN-capable devices using the [Function Discovery API](/previous-versions/windows/desktop/fundisc/fd-portal). The scope of a search can be narrowed down to a specific SSID, state, category, or even broadened to include all WCN-capable devices. Once devices are located, the WCN API allows communication with the WCN-capable device in order to facilitate configuration or connectivity.

 

 