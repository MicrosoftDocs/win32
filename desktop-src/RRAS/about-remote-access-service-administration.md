---
title: About Remote Access Service Administration
description: Windows 2000 and later operating systems provide a set of functions for administering user permissions and ports on RAS servers.
ms.assetid: 95c6dceb-e3a9-421e-b43f-88b18b9e64ff
keywords:
- Routing and Remote Access Service RRAS , RAS Administration
- Routing and Remote Access Service RRAS , RAS Administration, described
- RAS Administration RRAS
- RAS Administration RRAS , described
ms.topic: article
ms.date: 05/31/2018
---

# About Remote Access Service Administration

Windows 2000 and later operating systems provide a set of functions for administering user permissions and ports on RAS servers. Using these functions, you can develop a RAS server administration application to perform the following tasks:

-   Enumerate those users who have a specified set of RAS permissions
-   Assign or revoke RAS permissions for a specified user
-   Enumerate the configured ports on a RAS server
-   Get information and statistics about a specified port on a RAS server
-   Reset the statistics counters for a specified port
-   Disconnect a specified port

You can also install a RAS server administration DLL to audit user connections and assign IP addresses to dial-in users. The DLL exports a set of functions that the RAS server calls whenever a user tries to connect or disconnect.

This documentation describes the following topics:

-   [Function Comparison: Windows 2000 vs. RRAS Redistributable](function-comparison-windows-2000-versus-rras-redistributable.md)
-   [RAS User Administration](ras-user-administration.md)
-   [RAS Server and Port Administration](ras-server-and-port-administration.md)
-   [RAS Administration DLL](ras-administration-dll.md)
-   [RAS Administration DLL Registry Setup](ras-administration-dll-registry-setup.md)

 

 




