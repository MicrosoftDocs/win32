---
title: User Authentication Information
description: The Remote Access Connection Manager service on the client computer sends a user name and password to the RAS server on the remote computer.
ms.assetid: b27bf520-d871-4314-8ed9-3a6a9583ab52
ms.topic: article
ms.date: 05/31/2018
---

# User Authentication Information

The Remote Access Connection Manager service on the client computer sends a user name and password to the RAS server on the remote computer. Before it establishes a connection, the remote server uses this information to authenticate the user. By default, the Remote Access Connection Manager sends the user name and password of the currently logged-on user. The RAS client can use the [**RASDIALPARAMS**](/previous-versions/windows/desktop/legacy/aa377238(v=vs.85)) structure specified in the [**RasDial**](/windows/desktop/api/Ras/nf-ras-rasdiala) call to specify a different user name and password.

If the remote server cannot authenticate the user with the specified information, it can allow the connection operation to enter a [paused state](paused-states.md) to enable the RAS client to collect different authentication data from the user.

 

 