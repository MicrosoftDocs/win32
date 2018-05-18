---
title: SERVICETYPE\_NOTRAFFIC
description: Use of the SERVICETYPE\_NO\_TRAFFIC service type indicates (or specifies) that no QOS services are required in the associated direction.
ms.assetid: 'dd1c65cb-7810-4073-9eaa-c114334786fd'
keywords: ["SERVICETYPE_NOTRAFFIC service type"]
---

# SERVICETYPE\_NOTRAFFIC

Use of the SERVICETYPE\_NO\_TRAFFIC service type indicates (or specifies) that no QOS services are required in the associated direction. For example, if the SendingFlowspec specifies SERVICETYPE\_NOTRAFFIC, then traffic sent on the specified connection would not receive QOS service provisions. In other words, quality of service signaling for sent data would be disabled.

This service type is useful when QOS service guarantees are only required in one direction (and therefore not required in the opposite direction). The SERVICETYPE\_NOTRAFFIC service type is also useful when QOS service provisions are no longer required in a specific direction, in which case the SERVICETYPE\_NOTRAFFIC service type can be used in conjunction with the SERVICETYPE\_NOCHANGE service type to disable quality of service signaling in one direction, and leave the other direction's quality of service signaling unchanged.

> [!Note]  
> RSVP signaling is not supported on Windows XP or later versions of Windows. In addition, WSAIoctl() under Windows Vista does not respect bit OR'ed flags.

 

 

 




