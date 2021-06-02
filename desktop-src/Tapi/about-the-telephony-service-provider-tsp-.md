---
description: A TAPI telephony service provider (TSP) is a dynamic-link library (DLL) that supports communications device control through a set of exported service functions.
ms.assetid: 6e4fb295-940e-4f76-ad43-fad7da90094a
title: About the Telephony Service Provider (TSP)
ms.topic: article
ms.date: 05/31/2018
---

# About the Telephony Service Provider (TSP)

\[ The H323 and IPConf TSPs are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

A TAPI telephony service provider (TSP) is a dynamic-link library (DLL) that supports communications device control through a set of exported service functions. A TAPI application uses standardized commands, TAPI passes in formation to the telephony service provider, and the TSP handles the specific commands that must be exchanged with the device.

The following sections briefly describe the TSPs provided with Microsoft Windows:

-   [H323 TSP](h323-tsp.md)
-   [IPConf TSP](ipconf-tsp.md)
-   [Kernel-Mode Device Driver TSP](kernel-mode-device-driver-tsp.md)
-   [NDIS Proxy TSP](ndis-proxy-tsp.md)
-   [Remote TSP](remote-tsp.md)
-   [Third-Party TSP](third-party-tsp.md)
-   [Unimodem TSP](unimodem-tsp.md)

For detailed information, please see the Resource Kit for the target operating system. Third-party TSPs for specialized communications devices will typically be provided by the manufacturer and will be installed with the device.

The following topics describe how to create a TSP that will function properly within the Microsoft Telephony environment, and how to create a TSP/MSP pair:

-   [Telephony Service Provider Interface (TSPI)](telephony-service-provider-interface-tspi-.md)
-   [TSPI Reference](tspi-reference.md)
-   [Media Service Providers](./media-service-providers-start-page.md)

> [!Note]  
> A TSP is a user-created DLL. If you are creating a TSP for a 64-bit Windows platform, you must compile it as a 64-bit DLL or DLLs.

 

 

 
