---
description: TAPI divides communications services into Basic, Supplemental, and Extended. Please see TAPI Levels of Service for additional information.
ms.assetid: e2e6b113-b6b0-43a1-ac95-6e8e188a6120
title: TSPI Levels of Service
ms.topic: article
ms.date: 05/31/2018
---

# TSPI Levels of Service

TAPI divides communications services into Basic, Supplemental, and Extended. Please see [TAPI Levels of Service](./tapi-levels-of-service.md) for additional information.

A TSP is required to implement all Basic Telephony functions. [TSPI Basic Telephony Functions](tspi-basic-telephony-functions.md) contains a summary of these functions.

Supplementary Telephony includes features found on modern PBXs, such as hold, transfer, conference, park, and so on. A service provider should provide a supplementary telephony service only if it can implement the exact meaning as defined by TAPI. If not, the feature should be provided as an Extended Telephony service. All supplementary features are optional. A service provider specifies which services it supports through responses to functions such as [**TSPI\_lineGetDevCaps**](/windows/win32/api/tspi/nf-tspi-tspi_linegetdevcaps) or [**TSPI\_lineGetAddressCaps**](/windows/win32/api/tspi/nf-tspi-tspi_linegetaddresscaps). A single supplementary service can consist of multiple function calls and messages. Phone device services are part of Supplementary Telephony.

Extended Telephony services allow a provider to implement device-specific functions. The service provider must uniquely identify the extensions by using an *extension identifier*. Applications retrieve and use this unique identifier to determine what extensions the service provider supports.

The extensions can apply to several manufacturers. Special functions and messages such as [**lineDevSpecific**](/windows/win32/api/tapi/nf-tapi-linedevspecific) and [**phoneDevSpecific**](/windows/win32/api/tapi/nf-tapi-phonedevspecific) are provided in TAPI. They are used to allow the extension of the set of functions (in contrast to enumerations, bit flags, and data structure members) supported by the service provider. The parameters for each function are also defined by the service provider.

An identifier is assigned to a set of extensions (before distribution), not to each individual instance of an implementation of those extensions. The EXTIDGEN utility in TSPI generates unique extension identifiers for service providers. It uses an Ethernet-adapter address, a random number, and the time of day to generate an identifier, so it is extremely unlikely that the resulting extension identifier will conflict with any other service provider. As a result, there is no need for vendors to register extension identifiers.

The EXTIDGEN utility does not generate extension identifiers unless the computer on which it is run is also running NetBIOS or other network software.

 

 
