---
title: Shutdown and Cleanup
description: For an application to terminate gracefully, it must perform the following cleanup operations.
ms.assetid: fc07adb8-103c-42d8-8187-3f5ee083c6d8
ms.topic: article
ms.date: 05/31/2018
---

# Shutdown and Cleanup

For an application to terminate gracefully, it must perform the following cleanup operations:

-   Remove all registered URLs from the URL group by calling the [**HttpRemoveUrlFromUrlGroup**](/windows/desktop/api/Http/nf-http-httpremoveurlfromurlgroup) function to deregister URLs previously registered in the call to [**HttpAddUrlToUrlGroup**](/windows/desktop/api/Http/nf-http-httpaddurltourlgroup).
-   Close the URL Group by calling the [**HttpCloseUrlGroup**](/windows/desktop/api/Http/nf-http-httpcloseurlgroup) function. All the URL groups created under a server session must be closed before closing the server session.
-   Close the server session by calling [**HttpCloseServerSession**](/windows/desktop/api/Http/nf-http-httpcloseserversession).
-   Close the handle to the request queue by calling [**HttpCloseRequestQueue**](/windows/desktop/api/Http/nf-http-httpcloserequestqueue).
-   Terminate the resources created by the HTTP Server API by calling the [**HttpTerminate**](/windows/desktop/api/Http/nf-http-httpterminate) function with matching flag settings for each call the application originally made to [**HttpInitialize**](/windows/desktop/api/Http/nf-http-httpinitialize). Each of these calls terminates all resources created in the call to [**HttpInitialize**](/windows/desktop/api/Http/nf-http-httpinitialize).

 

 




