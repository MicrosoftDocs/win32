---
title: SERVICETYPE\_GENERAL\_INFORMATION
description: The SERVICETYPE\_GENERAL\_INFORMATION service type is used in the SendingFlowspec parameter of a QOS structure to indicate that the sender can operate properly within any of the services.
ms.assetid: '8c12c5eb-01ac-4aa5-80ec-4d86a80a620b'
keywords: ["SERVICETYPE_GENERAL_INFORMATION service type"]
---

# SERVICETYPE\_GENERAL\_INFORMATION

The SERVICETYPE\_GENERAL\_INFORMATION service type is used in the SendingFlowspec parameter of a [**QOS**](qos.md) structure to indicate that the sender can operate properly within any of the services. Note that SERVICETYPE\_GENERAL\_INFORMATION does not include any indication regarding the availability of the [QUALITATIVE](qualitative.md) service type.

SERVICETYPE\_GENERAL\_INFORMATION is only available to the sender; the RSVP SP returns an error if the receiver attempts to use the SERVICETYPE\_GENERAL\_INFORMATION service type.

It is worth noting that BEST EFFORT is almost always available, since it makes no particular guarantee for service quality. The RSVP SP will do its best to meet service level requests for BEST EFFORT flows. Therefore, the SERVICETYPE\_GENERAL\_INFORMATION can more effectively be interpreted as advertising that either CONTROLLED LOAD or GUARANTEED service types can be selected by the receiver for the flow.

Note, however, that routers in the path between end nodes may indicate that they do not support one or both of the (interesting) service types—CONTROLLED LOAD and GUARANTEED.

> [!Note]  
> RSVP signaling is not supported on Windows XP or later versions of Windows. In addition, WSAIoctl() under Windows Vista does not respect bit OR'ed flags.

 

 

 




