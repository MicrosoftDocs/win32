---
description: CallHub tracking is a new feature in TAPI version 3.0.
ms.assetid: 29b6e585-6da8-46a2-a612-f42d0f65f68e
title: CallHub Support
ms.topic: article
ms.date: 05/31/2018
---

# CallHub Support

CallHub tracking is a new feature in TAPI version 3.0. CallHub functionality was added to the TAPI 2.1 programming elements with the delivery of Windows 2000. A *CallHub* represents a third-party view of a call, and TAPI's call handles represent the first-party view of a call. With CallHub tracking, the service provider is requested to follow CallHubs and give information about the call during the lifetime of a CallHub. As new parties join and leave the CallHub, the service provider should inform TAPI.

A service provider does not need to implement any new functions in order to support CallHub. It simply needs to fill in the **dwCallID** member of the [**LINECALLINFO**](/windows/win32/api/tapi/ns-tapi-linecallinfo) structure. In TAPI 3, TAPI collects all calls with the same **dwCallID** and creates a CallHub handle that the application can use to track the call.

 

 
