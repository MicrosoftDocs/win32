---
title: SERVICE\_NO\_QOS\_SIGNALING
description: The SERVICE\_NO\_QOS\_SIGNALING service type may be set by the sending or receiving application.
ms.assetid: 664c586a-dacd-42d7-a43a-b49c2dc1ac31
keywords:
- SERVICETYPE_NO_QOS_SIGNALING service type
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SERVICE\_NO\_QOS\_SIGNALING

The SERVICE\_NO\_QOS\_SIGNALING service type may be set by the sending or receiving application. When this service type is specified, the RSVP SP does not invoke RSVP signaling, enabling the application to suppress the RSVP SP's invocation of RESV messages on the application's behalf.

This secondary service type can be invoked using the bitwise OR operator with the following primary and secondary service types to further specify an application's quality of service requirements:

-   [BEST EFFORT](best-effort.md)
-   [CONTROLLED LOAD](controlled-load.md)
-   [GUARANTEED](guaranteed.md)
-   [QUALITATIVE](qualitative.md)
-   [SERVICETYPE\_NOTRAFFIC](servicetype-notraffic.md)
-   [SERVICETYPE\_GENERAL\_INFORMATION](servicetype-general-information.md)
-   [SERVICETYPE\_NOCHANGE](servicetype-nochange.md)

> [!Note]  
> RSVP signaling is not supported on Windows XP or later versions of Windows. In addition, WSAIoctl() under Windows Vista does not respect bit OR'ed flags.

 

> [!Note]  

 

 

 




