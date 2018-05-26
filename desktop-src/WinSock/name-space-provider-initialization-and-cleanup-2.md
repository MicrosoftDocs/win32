---
Description: Using NSPStartup and NSPCleanup for namespace provider initialization and cleanup in the Windows Sockets (Winsock) SPI.
ms.assetid: c9f55845-190d-440f-8b27-1be9585137e2
title: Namespace Provider Initialization and Cleanup
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Namespace Provider Initialization and Cleanup

-   [**NSPStartup**](/windows/win32/Ws2spi/nf-ws2spi-nspstartup?branch=master)
-   [**NSPCleanup**](/windows/win32/Ws2spi/nc-ws2spi-lpnspcleanup?branch=master)

As is the case for the transport SPI, a namespace provider is initialized with a call to [**NSPStartup**](/windows/win32/Ws2spi/nf-ws2spi-nspstartup?branch=master) and is terminated with a final call to [**NSPCleanup**](/windows/win32/Ws2spi/nc-ws2spi-lpnspcleanup?branch=master). Calls to the startup function may be nested, but will be matched by corresponding calls to the cleanup function. A provider should employ reference counting to determine when the final call to **NSPCleanup** has occurred.

 

 



