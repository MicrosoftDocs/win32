---
description: Supplementary Telephony services are the collection of all the services defined by the API other than those included in the Basic Telephony subset.
ms.assetid: a2a30a0d-fbfd-4317-8e3a-d1e1e8b86ae0
title: Supplementary Telephony Services
ms.topic: article
ms.date: 05/31/2018
---

# Supplementary Telephony Services

Supplementary Telephony services are the collection of all the services defined by the API other than those included in the Basic Telephony subset. It includes all so-called supplementary features found on modern PBXs, such as hold, transfer, conference, park, and so on. All supplementary features are considered optional; that is, the service provider decides which of these services it does or does not provide.

An application can query a line or phone device for the set of supplementary services it provides using functions such as [**lineGetDevCaps**](/windows/win32/api/tapi/nf-tapi-linegetdevcaps) or [**lineGetAddressCaps**](/windows/win32/api/tapi/nf-tapi-linegetaddresscaps). A single supplementary service may consist of multiple function calls and messages. The Telephony API, and not the service provider developer, defines the behavior of each of these supplementary features. A service provider should provide a Supplementary Telephony service only if it can implement the exact meaning as defined by the API. If not, the feature should be provided as an Extended Telephony service.

As mentioned in Basic Telephony services, phone-device services are considered optional. Therefore, all phone-device services are part of Supplementary Telephony. For a list of the functions of Supplementary Telephony, see [TAPI Quick Function Reference](./tapi-quick-function-reference.md).

 

 
