---
title: User Authentication
description: The authentication protocol itself can authenticate the user via Protected EAP (PEAP).
ms.assetid: 7e0ff5e3-3274-4b52-8c53-101ad01e3034
ms.topic: article
ms.date: 06/14/2023
ms.contributor: samyun
---

# User Authentication

The authentication protocol itself can authenticate the user via Protected EAP (PEAP). There are also two authentication providers built into the operating system: Windows domain authentication (accessed via Directory Services) and Remote Access Dial-In User Service (RADIUS).

In the case where RADIUS is the authentication provider, the EAP Plug-in is installed on the RADIUS server rather than on the wireless Access Point (AP) server, such as a RAS server. The AP server passes EAP packets directly from the client to the authentication service on the RADIUS server. The AP server does not process any of the information in the EAP packets, but it must accept the server-side, full strength (256 bit) PEAP generated encryption keys in order to create the secure connection.
