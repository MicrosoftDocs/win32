---
description: Updates that require user interaction cannot be installed by Windows Update Agent (WUA) applications if the WUA applications are running in the context of the Secondary Logon service.
ms.assetid: 090cd730-cfcd-49fc-b748-f66e696edaf3
title: Using WUA from a Secondary Logon (Run As) Process
ms.topic: article
ms.date: 05/31/2018
---

# Using WUA from a Secondary Logon (Run As) Process

Updates that require user interaction cannot be installed by Windows Update Agent (WUA) applications if the WUA applications are running in the context of the Secondary Logon service.

If the process that is calling WUA is running in the context of the RunAs service or the Secondary Logon service, an attempt to install an update that requires user interaction fails and returns the **WU\_E\_NO\_INTERACTIVE\_USER** error.

In Microsoft Windows, you can run programs as a user who differs from the user who is currently logged on. To do this the Secondary Logon service must be running.

 

 



