---
title: Upload Best Practices
description: Highloads may cause various server timeout conditions, which may in turn increase the load when the client retries.
ms.assetid: 8210f849-2aae-497b-b5dd-af25f6f4b8bf
ms.topic: article
ms.date: 05/31/2018
---

# Upload Best Practices

Highloads may cause various server timeout conditions, which may in turn increase the load when the client retries. Also, a large number of outstanding connections will consume more server resources and make the situation worse. On top of that, if backend app is not written to handle high load conditions, it may crash or mal-behave. The app shall perform the following steps to limit the load on the backend.

If the server application is not written to handle high volumes, timeout conditions may occur, which may in turn increase the load when the client retries. Also, a large number of outstanding connections will consume more server resources.

When testing your server application, test with highest load possible. You should use multiple client machines, each with several concurrent, foreground BITS jobs, and measure the maximum throughput at the backend. If you cannot measure the throughput, you will have to estimate the throughput.

The server application should reside on a different URL from the upload URL (see the BITS IIS property, **BITSServerNotificationURL**).

It is good practice to limit the load on the application server based on proven throughput values. You should use the IIS properties, **MaxBandwidth** and **MaxConnections**, to limit the load on the application server.

 

 




