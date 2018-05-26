---
title: Shutdown and Cleanup
description: For an application to terminate gracefully, it must perform the following cleanup operations.
ms.assetid: fc07adb8-103c-42d8-8187-3f5ee083c6d8
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Shutdown and Cleanup

For an application to terminate gracefully, it must perform the following cleanup operations:

-   Remove all registered URLs from the URL group by calling the [**HttpRemoveUrlFromUrlGroup**](/windows/win32/Http/nf-http-httpremoveurlfromurlgroup?branch=master) function to deregister URLs previously registered in the call to [**HttpAddUrlToUrlGroup**](/windows/win32/Http/nf-http-httpaddurltourlgroup?branch=master).
-   Close the URL Group by calling the [**HttpCloseUrlGroup**](/windows/win32/Http/nf-http-httpcloseurlgroup?branch=master) function. All the URL groups created under a server session must be closed before closing the server session.
-   Close the server session by calling [**HttpCloseServerSession**](/windows/win32/Http/nf-http-httpcloseserversession?branch=master).
-   Close the handle to the request queue by calling [**HttpCloseRequestQueue**](/windows/win32/Http/nf-http-httpcloserequestqueue?branch=master).
-   Terminate the resources created by the HTTP Server API by calling the [**HttpTerminate**](/windows/win32/Http/nf-http-httpterminate?branch=master) function with matching flag settings for each call the application originally made to [**HttpInitialize**](/windows/win32/Http/nf-http-httpinitialize?branch=master). Each of these calls terminates all resources created in the call to [**HttpInitialize**](/windows/win32/Http/nf-http-httpinitialize?branch=master).

 

 




