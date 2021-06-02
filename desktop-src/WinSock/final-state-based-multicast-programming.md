---
description: This section describes final-state-based multicast programming using IOCTLs instead of socket options. For an overview of how final-state-based multicast programming differs from change-based multicast programming, see Multicast Programming.
ms.assetid: 71c05393-3f8c-42c0-9060-e0df9b5e2578
title: Final-State-Based Multicast Programming
ms.topic: article
ms.date: 05/31/2018
---

# Final-State-Based Multicast Programming

This section describes final-state-based multicast programming using IOCTLs instead of socket options. For an overview of how final-state-based multicast programming differs from change-based multicast programming, see [Multicast Programming](multicast-programming.md).

The following table describes the Windows Sockets IOCTLs used for multicast programming on Windows. 

| IOCTL                       | Argument type                                   |
|-----------------------------|-------------------------------------------------|
| SIOCSMSFILTER               | [**GROUP\_FILTER**](/windows/desktop/api/Ws2ipdef/ns-ws2ipdef-group_filter) structure |
| SIOCGMSFILTER               | [**GROUP\_FILTER**](/windows/desktop/api/Ws2ipdef/ns-ws2ipdef-group_filter) structure |
| SIO\_GET\_MULTICAST\_FILTER | [**ip\_msfilter**](/windows/desktop/api/Ws2ipdef/ns-ws2ipdef-ip_msfilter) structure   |
| SIO\_SET\_MULTICAST\_FILTER | [**ip\_msfilter**](/windows/desktop/api/Ws2ipdef/ns-ws2ipdef-ip_msfilter) structure   |



 

Note that the **SIOCSMSFILTER** and **SIOCGMSFILTER** IOCTLS are available on Windows Vista and later.

Using these IOCTLs for multicast programming has performance benefits when working with large source lists. For more information about the parameters and settings associated with using SIO\_GET\_MULTICAST\_FILTER or SIO\_SET\_MULTICAST\_FILTER, consult the [**GROUP\_FILTER**](/windows/desktop/api/Ws2ipdef/ns-ws2ipdef-group_filter) reference page. For more information about the parameters and settings associated with using SIO\_GET\_MULTICAST\_FILTER or SIO\_SET\_MULTICAST\_FILTER, consult the [**ip\_msfilter**](/windows/desktop/api/Ws2ipdef/ns-ws2ipdef-ip_msfilter) reference page.

 

 



