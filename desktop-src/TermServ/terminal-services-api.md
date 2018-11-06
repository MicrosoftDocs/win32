---
title: Remote Desktop Services API
description: The Remote Desktop Services API is primarily useful to client/server applications and applications for Remote Desktop Services administration.
ms.assetid: 4bd10a15-78d6-4754-9e17-f2576ee8b9d0
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Remote Desktop Services API

Most applications run without modification in a Remote Desktop Services (formerly known as Terminal Services) environment and do not need to use the Remote Desktop Services API. The Remote Desktop Services API is primarily useful to client/server applications and applications for Remote Desktop Services administration.

The Remote Desktop Services API is a set of function calls into Wtsapi32.dll. To design your application to run in both Remote Desktop Services and non-Remote Desktop Services environments, use run-time dynamic linking to check for the presence of Wtsapi32.dll. For more information, see [Run-Time Linking to Wtsapi32.dll](run-time-linking-to-wtsapi32-dll.md).

The Remote Desktop Services API enables applications to perform the following tasks in a Remote Desktop Services environment:

-   [Remote Desktop Services Administration](terminal-services-administration.md), such as enumerating and managing Remote Desktop Session Host (RD Session Host) servers (formerly known as terminal servers) in a domain or enumerating and managing sessions and processes on an RD Session Host server.
-   Enhancing client/server applications in a Remote Desktop Services environment.
-   Using [Remote Desktop Services Virtual Channels](terminal-services-virtual-channels.md) to communicate between client and server modules of an application.
-   [Setting and retrieving Remote Desktop Services specific user configuration information](terminal-services-user-configuration.md).

 

 




