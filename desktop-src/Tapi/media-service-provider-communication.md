---
Description: Starting with Windows 2000 telephony service providers that negotiate a version of 3.0 or later must have a matching media service provider.
ms.assetid: 9235c631-77bc-42c6-8139-9208c9c254b4
title: Media Service Provider Communication
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Media Service Provider Communication

Starting with Windows 2000 telephony service providers that negotiate a version of 3.0 or later must have a matching media service provider. The precise division of operational responsibilities is implementation dependent. For example, a TSP might use the matching MSP to perform media type determination on an incoming session. However, the TSP must conform to the TSPI, which means getting that determination from the MSP and reporting it to TAPI.

TSPI provides the following functions and messages to allow a virtual connection between a TSP and an MSP:

-   [**TSPI\_lineCloseMSPInstance**](https://msdn.microsoft.com/en-us/library/ms725533(v=VS.85).aspx)
-   [**TSPI\_lineCreateMSPInstance**](https://msdn.microsoft.com/en-us/library/ms725539(v=VS.85).aspx)
-   [**TSPI\_lineMSPIdentify**](https://msdn.microsoft.com/en-us/library/ms725580(v=VS.85).aspx)
-   [**TSPI\_lineReceiveMSPData**](https://msdn.microsoft.com/en-us/library/ms725587(v=VS.85).aspx)
-   [**LINE\_QOSINFO**](line-qosinfo.md)
-   [**LINE\_SENDMSPDATA**](line-sendmspdata.md)

 

 



