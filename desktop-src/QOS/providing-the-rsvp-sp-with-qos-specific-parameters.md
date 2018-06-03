---
title: Providing the RSVP SP with QOS-specific Parameters
description: In order for the RSVP SP to act on behalf of an application, the RSVP SP must be provided with QOS-specific parameters.
ms.assetid: 772aac13-659a-4744-ab03-b44e7095d660
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Providing the RSVP SP with QOS-specific Parameters

In order for the RSVP SP to act on behalf of an application, the RSVP SP must be provided with QOS-specific parameters. These parameters come in the form of the following structures:

-   [**QOS**](/windows/desktop/api/Winsock2/ns-winsock2-_qualityofservice)
-   [**FLOWSPEC**](/previous-versions/windows/desktop/api/Qos/ns-qos-_flowspec)

The [**QOS**](/windows/desktop/api/Winsock2/ns-winsock2-_qualityofservice) structure is the all-encompassing structure for QOS-specific parameters, and is comprised of three parameters, two of which are [**FLOWSPEC**](/previous-versions/windows/desktop/api/Qos/ns-qos-_flowspec) structures (one for sending, one for receiving).

The[**FLOWSPEC**](/previous-versions/windows/desktop/api/Qos/ns-qos-_flowspec) structure includes flow members, which are **TokenRate**, **TokenBucketSize**, **PeakBandwidth**, **Latency**, **DelayVariation**, **ServiceType**, **MaxSduSize** (maximum packet size permitted in the traffic flow), and **MinimumPolicedSize**. When the application provides values for these parameters, the RSVP SP can characterize the service quality being requested; this enables the RSVP SP to make appropriate requests to corresponding components of quality of service.

The third parameter of the [**QOS**](/windows/desktop/api/Winsock2/ns-winsock2-_qualityofservice) structure is the **ProviderSpecific** buffer, which is used for additional provider-specific QOS parameters that cannot be specified in the [**FLOWSPEC**](/previous-versions/windows/desktop/api/Qos/ns-qos-_flowspec) structures. For more information about the **ProviderSpecific** buffer, see [Using the ProviderSpecific Buffer](using-the-providerspecific-buffer.md).

QOS parameters for the [**FLOWSPEC**](/previous-versions/windows/desktop/api/Qos/ns-qos-_flowspec) structure may be common among certain application types. This commonality lends itself to the establishment of standardized QOS parameters for a given type of transmission. The RSVP SP provides such standardization, and the ease of implementation that comes with prescribed service types, through the use of QOS templates. These templates are described in detail in the [QOS Templates](qos-templates.md) section.

Further details of the [**QOS**](/windows/desktop/api/Winsock2/ns-winsock2-_qualityofservice) structure and the [**FLOWSPEC**](/previous-versions/windows/desktop/api/Qos/ns-qos-_flowspec) structure can be found in their respective API entries.

> [!Note]  
> RSVP signaling is not supported on Windows XP or later versions of Windows.

 

 

 




