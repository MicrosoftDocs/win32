---
title: How the RSVP Service Invokes TC
description: The RSVP service and TC communicate in order to work together to provide overall quality of service for a given sending flow.
ms.assetid: 8ad05dba-8f1d-48b8-8d07-bcc7a83a1550
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# How the RSVP Service Invokes TC

\[RSVP signaling is not supported except on Windows 2000. See [RSVP Operates Only on Windows 2000](rsvp-operates-only-on-windows-2000.md) for more information.\]

The RSVP service and TC communicate in order to work together to provide overall quality of service for a given sending flow. When an application requests quality of service using the RSVP SP, the RSVP SP responds by initiating RSVP signaling and invoking kernel traffic control from local TC components (using the traffic control Interface). As such, traffic control and RSVP signaling are initiated concurrently upon flow setup.

In this transitional period (presuming [**QOS\_SD\_MODE**](/previous-versions/windows/desktop/api/Qos/ns-qos-_qos_sd_mode) has not been specifically set) the reservation has not been established, and therefore traffic control is configured to transmit traffic associated with the flow's specification, as follows:

-   [BEST\_EFFORT](best-effort.md) traffic is transmitted with its QOS\_SD\_MODE set to borrow mode (TC\_NONCONF\_BORROW)
-   [CONTROLLED LOAD](controlled-load.md) traffic is transmitted with its QOS\_SD\_MODE set to TC\_NONCONF\_BORROW
-   GUARANTEED traffic is shaped with its QOS\_SD\_MODE set to TC\_NONCONF\_SHAPE

> [!Note]  
> The above default configuration can be overridden by supplying the [**QOS\_SD\_MODE**](/previous-versions/windows/desktop/api/Qos/ns-qos-_qos_sd_mode) object in the [ProviderSpecific](the-providerspecific-buffer.md) buffer.

 

In this transitional period, all packets conforming to the flowspec for BEST\_EFFORT and CONTROLLED LOAD are sent immediately with the appropriate traffic control marking, and nonconforming packets are sent immediately with their host and network priority demoted. Transmission settings for any given flow are aligned with the allowed sending rate specified by the system (which is in turn determined by settings in the appropriate [**FLOWSPEC**](/previous-versions/windows/desktop/api/Qos/ns-qos-_flowspec)).

Sending applications can determine what the allowed sending rate is by querying the Allowed\_Rate using SIO\_CHK\_QOS. More information about using SIO\_CHK\_QOS is provided in [Using SIO\_CHK\_QOS](using-sio-chk-qos.md).

Once PATH messages arrive at the receiving host (or hosts; for simplicity, ongoing references will be singular), the host may request QOS provisioning for the flow in the form of RESV messages sent back toward the sender. When the RSVP SP on the receiver receives the RESV message, it communicates with traffic control to enable traffic control to update its transmission information, and if appropriate, to modify the BEST\_EFFORT flow according to the reservation indicated in the RESV message.

Note that it is possible to invoke traffic control without RSVP signaling, and to programmatically modify traffic control's treatment of a flow. RSVP signaling can be suppressed on a given flow if the SERVICE\_NO\_QOS\_SIGNALING service type is specified, and traffic control can be suppressed on a given flow if the SERVICE\_NO\_TRAFFIC\_CONTROL service type is specified. Additional control over the suppressing of RSVP signaling and traffic control can be achieved through the use of registry entries.

 

 




