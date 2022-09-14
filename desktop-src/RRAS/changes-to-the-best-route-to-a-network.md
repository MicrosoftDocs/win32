---
title: Changes to the Best Route to a Network
description: A change in any of the following values for the best route to a given destination network causes the routing table manager to generate a notification message sent to each registered client and to the forwarders
ms.assetid: 2864af0f-e05a-48d7-a78d-57cc9ac42246
ms.topic: article
ms.date: 05/31/2018
---

# Changes to the Best Route to a Network

**Windows Server 2003:** This API has been superseded by the [Routing Table Manager Version 2](about-routing-table-manager-version-2.md) API and will not be available beyond Windows Server 2003. New applications should use the Routing Table Manager Version 2 API.

A change in any of the following values for the best route to a given destination network causes the routing table manager to generate a notification message sent to each registered client and to the forwarders:

-   Protocol identifier
-   Interface index
-   Address of next-hop router
-   Protocol family-specific data that includes route metrics

A change in protocol identifier, interface index, or next-hop router address occurs when a new, better-route entry is added, or when the current best-route entry is deleted or aged out, and leaves another route as the new best route.

 

 




