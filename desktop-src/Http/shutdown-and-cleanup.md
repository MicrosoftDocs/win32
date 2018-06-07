---
title: Shutdown and Cleanup
description: For an application to terminate gracefully, it must perform the following cleanup operations.
ms.assetid: fc07adb8-103c-42d8-8187-3f5ee083c6d8
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Shutdown and Cleanup

For an application to terminate gracefully, it must perform the following cleanup operations:

-   Remove all registered URLs from the URL group by calling the [**HttpRemoveUrlFromUrlGroup**](httpremoveurlfromurlgroup.md) function to deregister URLs previously registered in the call to [**HttpAddUrlToUrlGroup**](httpaddurltourlgroup.md).
-   Close the URL Group by calling the [**HttpCloseUrlGroup**](httpcloseurlgroup.md) function. All the URL groups created under a server session must be closed before closing the server session.
-   Close the server session by calling [**HttpCloseServerSession**](httpcloseserversession.md).
-   Close the handle to the request queue by calling [**HttpCloseRequestQueue**](httpcloserequestqueue.md).
-   Terminate the resources created by the HTTP Server API by calling the [**HttpTerminate**](httpterminate.md) function with matching flag settings for each call the application originally made to [**HttpInitialize**](httpinitialize.md). Each of these calls terminates all resources created in the call to [**HttpInitialize**](httpinitialize.md).

 

 




