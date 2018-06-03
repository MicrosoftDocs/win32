---
title: Secondary Service Types
description: There are three secondary service types.
ms.assetid: 12fba32c-686a-4db5-b196-6de962c6dae1
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Secondary Service Types

There are three secondary service types. The use of secondary service types enable an application programmer to modify QOS service guarantees in different ways, such as enabling quality of service for only one direction of a bidirectional connection, disabling an existing QOS service guarantee, or disabling traffic control. Each of the following secondary service types are explained in this section:

-   [SERVICETYPE\_NOTRAFFIC](servicetype-notraffic.md)
-   [SERVICETYPE\_GENERAL\_INFORMATION](servicetype-general-information.md)
-   [SERVICETYPE\_NOCHANGE](servicetype-nochange.md)

There are also two secondary service types that an application programmer can use in conjunction with the all primary service types, and the previously mentioned secondary service types. Application programmers can use the bitwise OR operator (not on Windows Vista, see note below) with these following two service type values to further refine the service type behavior they require:

-   [SERVICE\_NO\_TRAFFIC\_CONTROL](service-no-traffic-control.md)
-   [SERVICE\_NO\_QOS\_SIGNALING](service-no-qos-signaling.md)

> [!Note]  
> RSVP signaling is not supported on Windows XP or later versions of Windows. In addition, WSAIoctl() under Windows Vista does not respect bit OR'ed flags.

 

 

 




