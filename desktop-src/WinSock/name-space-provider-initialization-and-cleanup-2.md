---
description: Using NSPStartup and NSPCleanup for namespace provider initialization and cleanup in the Windows Sockets (Winsock) SPI.
ms.assetid: c9f55845-190d-440f-8b27-1be9585137e2
title: Namespace Provider Initialization and Cleanup
ms.topic: article
ms.date: 05/31/2018
---

# Namespace Provider Initialization and Cleanup

-   [**NSPStartup**](/windows/desktop/api/Ws2spi/nf-ws2spi-nspstartup)
-   [**NSPCleanup**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpnspcleanup)

As is the case for the transport SPI, a namespace provider is initialized with a call to [**NSPStartup**](/windows/desktop/api/Ws2spi/nf-ws2spi-nspstartup) and is terminated with a final call to [**NSPCleanup**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpnspcleanup). Calls to the startup function may be nested, but will be matched by corresponding calls to the cleanup function. A provider should employ reference counting to determine when the final call to **NSPCleanup** has occurred.

 

 



