---
title: Using SIO\_CHK\_QOS
description: SIO\_CHK\_QOS can be used in conjunction with the WSAIoctl function to obtain information on QOS traffic characteristics.
ms.assetid: a748f389-e2ca-406f-ae7d-ba3a47e7a131
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using SIO\_CHK\_QOS

\[RSVP signaling is not supported except on Windows 2000. See [RSVP Operates Only on Windows 2000](rsvp-operates-only-on-windows-2000.md) for more information.\]

SIO\_CHK\_QOS can be used in conjunction with the **WSAIoctl** function to obtain information on QOS traffic characteristics. During the transitional phase on the sending system between flow setup and the receipt of a RESV message (see [How the RSVP Service Invokes TC](how-the-rsvp-service-invokes-tc.md) for more information on the transitional phase), traffic associated with the flow is shaped based on service type ( [BEST EFFORT](best-effort.md), [CONTROLLED LOAD](controlled-load.md), or [GUARANTEED](guaranteed.md)). When the RSVP service on the sending host receives the RESV message, it communicates with traffic control to modify the BEST\_EFFORT flow according to the change in ServiceType in the [**FLOWSPEC**](/previous-versions/windows/desktop/api/Qos/ns-qos-_flowspec), and traffic control objects received in the RESV message.

Certain applications may find the results of shape/discard mode settings unacceptable, such as a CONTROLLED LOAD flow's nonconforming packets (in borrow mode) potentially being discarded. To avoid unnecessary discarding of packets, applications can use SIO\_CHK\_QOS immediately following QOS invocation. The results of the call may require that the application defer data transmission until receipt of the RESV message.

Note that the default setting for SIO\_CHK\_QOS allows the application to send data as BEST\_EFFORT before the reservation is in place. Network administrators in a given QOS-enabled network environment must explicitly override this setting on the ACS in order to exercise this control.

 

 




