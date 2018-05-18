---
title: RSVP SP and RSVP
description: Below the RSVP SP sits the Resource Reservation Protocol, or RSVP.
ms.assetid: 'c80ba73f-f33a-495a-a6fd-cd17c4265aad'
keywords: ["Quality of Service QOS ,described, RSVP SP"]
---

# RSVP SP and RSVP

Below the RSVP SP sits the Resource Reservation Protocol, or RSVP. RSVP is an IETF-standardized protocol that ferries quality of service provision requests between end nodes, and interacts with all RSVP-enabled network devices in the path between end nodes. The RSVP SP—which invokes and facilitates all aspects of Microsoft Windows 2000 QOS, not just RSVP signaling—also enables application developers to fine-tune RSVP messages through the use of the [ProviderSpecific](the-providerspecific-buffer.md) buffer. Such fine-grained control of RSVP by an application enables the fine-tuning or special service requests to be made without depending on the RSVP SP to interpret conventional requests (through members in the [**QOS**](qos.md) structure) and pass such requests down to RSVP.

RSVP signaling is the primary mechanism employed by the RSVP SP to create an end-to-end QOS connection. When [ServiceType](service-types.md) in either the SendingFlowspec or ReceivingFlowspec member of the **QOS** structure is set to initiate Quality of Service over the connection in either direction (that is, when either parameter is set to a service type other than [SERVICETYPE\_BESTEFFORT](best-effort.md) or [SERVICETYPE\_NOTRAFFIC](servicetype-notraffic.md)), the RSVP SP initiates RSVP signaling.

Most application programmers will find that enabling an application to use the RSVP SP, which automatically initiates and maintains RSVP signaling on behalf of applications, is sufficient to enable their application to take advantage of QOS capabilities.

For those interested in the specifics of RSVP signaling, and how to get more granular control over its parameters and notifications, the following sections outline general RSVP concepts as they interact with the RSVP SP.

> [!Note]  
> RSVP signaling is not supported on Windows XP, Windows Server 2003, or later versions of Windows. The RSVP Service will continue to run on hosts, but only as a conduit between applications and traffic control components.

 

 

 




