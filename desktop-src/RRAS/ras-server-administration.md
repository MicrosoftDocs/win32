---
title: RAS Server Administration
description: Windows NT Server 4.0 provides a set of functions for administering user permissions and ports on Windows NT/Windows 2000 RAS servers.
ms.assetid: 0b517c4d-dcae-477b-b274-c3773bd172ef
keywords:
- Server Administration, RAS
- Administration, RAS Server
ms.topic: article
ms.date: 05/31/2018
---

# RAS Server Administration

Windows NT Server 4.0 provides a set of functions for administering user permissions and ports on Windows NT/Windows 2000 RAS servers. Windows 95 does not support these functions. Using these functions, you can develop a RAS server administration application to perform the following tasks:

-   Enumerate those users who have a specified set of RAS permissions
-   Assign or revoke RAS permissions for a specified user
-   Enumerate the configured ports on a RAS server
-   Get information and statistics about a specified port on a RAS server
-   Reset the statistics counters for a specified port
-   Disconnect a specified port

You can also install a RAS server administration DLL for auditing user connections and assigning IP addresses to dial-in users. The DLL exports a set of functions that the RAS server calls whenever a user tries to connect or disconnect.

 

 




