---
description: Defines a Mobile Broadband Profile.
ms.assetid: bfec0a1d-de17-4ebd-b9fb-570e230da317
title: Mobile Broadband Profile Schema Reference
ms.topic: reference
ms.date: 05/31/2018
---

# Mobile Broadband Profile Schema Reference

The Mobile Broadband Profile Schema defines a Mobile Broadband Profile.

Profiles store Mobile Broadband connection related user and network configuration parameters. They also store the user preferences for a connection.

The root element of a Mobile Broadband profile is the [**MBNProfile**](schema-mbnprofile-element.md) element. Each profile has exactly one root element. All Mobile Broadband Profile Schema elements used by Windows 7 are in the namespace `https://www.microsoft.com/networking/WWAN/profile/v1` and the elements used by Windows 8 are in the namespace `https://www.microsoft.com/networking/WWAN/profile/v2`.

The Mobile Broadband Profile Schema strictly enforces the order of the nodes. Nodes specified in a profile must adhere to the **Mobile Broadband Profile Schema** and appear in the order prescribed in the schema definition. For example, [**UserLogonCred**](schema-userlogoncred-contexttype-element.md) must be specified immediately after [**AccessString**](schema-accessstring-contexttype-element.md).

-   [Mobile Broadband Profile Schema v1](mobile-broadband-profile-schema.md)
-   [Mobile Broadband Profile Schema v2](mobile-broadband-profile-schema-v2.md)
-   [Mobile Broadband Profile Schema v3](mobile-broadband-profile-schema-v3.md)
-   [Mobile Broadband Profile Schema v4](/previous-versions/windows/desktop/legacy/mt243438(v=vs.85))

 

 
