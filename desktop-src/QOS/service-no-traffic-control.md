---
title: SERVICE\_NO\_TRAFFIC\_CONTROL
description: The SERVICE\_NO\_TRAFFIC\_CONTROL service type instructs the RSVP SP not to invoke kernel traffic control.
ms.assetid: '30945532-bce9-4fcf-b2aa-8a6441bf75be'
keywords: ["SERVICETYPE_NO_TRAFFIC_CONTROL service type"]
---

# SERVICE\_NO\_TRAFFIC\_CONTROL

The SERVICE\_NO\_TRAFFIC\_CONTROL service type instructs the RSVP SP not to invoke kernel traffic control. This secondary service type can be invoked using the bitwise OR operator with the following primary and secondary service types to further specify an application's quality of service requirements:

-   [BEST EFFORT](best-effort.md)
-   [CONTROLLED LOAD](controlled-load.md)
-   [GUARANTEED](guaranteed.md)
-   [QUALITATIVE](qualitative.md)
-   [SERVICETYPE\_NOTRAFFIC](servicetype-notraffic.md)
-   [SERVICETYPE\_GENERAL\_INFORMATION](servicetype-general-information.md)
-   [SERVICETYPE\_NOCHANGE](servicetype-nochange.md)

> [!Note]  
> RSVP signaling is not supported on Windows XP or later versions of Windows. In addition, WSAIoctl() under Windows Vista does not respect bit OR'ed flags.

 

 

 




