---
title: About Routing Table Manager Version 1
description: The routing table manager is a central repository of routing information for all routing protocols that operate under Routing and Remote Access Service (RRAS).
ms.assetid: 6d0e7697-5c52-4a69-b2a1-9c893600191b
keywords:
- Routing and Remote Access Service RRAS , Routing Table Manager Version 1
- Routing and Remote Access Service RRAS , Routing Table Manager Version 1, described
- Routing Table Manager Version 1 RRAS
- Routing Table Manager Version 1 RRAS , described
ms.topic: article
ms.date: 05/31/2018
---

# About Routing Table Manager Version 1

**Windows Server 2003:** This API has been superseded by the [Routing Table Manager Version 2](about-routing-table-manager-version-2.md) API and will not be available beyond Windows Server 2003. New applications should use the Routing Table Manager Version 2 API.

The routing table manager is a central repository of routing information for all routing protocols that operate under Routing and Remote Access Service (RRAS). The routing table manager provides routing information to all interested components, such as routing protocols, management agents, and monitoring agents. The routing table manager also determines the best route to each destination network known to the routing protocols. It determines this route based on routing protocol priorities and on metrics associated with the routes. Note that the administrator is able to configure routing protocol priorities. The routing table manager then passes the best-route information on to the forwarders and back to the routing protocols.

Each routing protocol calls [**RtmRegisterClient**](rtmregisterclient.md) to register with the routing table manager. **RtmRegisterClient** returns a handle that is used by the routing protocol to add or delete route entries. **RtmRegisterClient** also allows the routing protocol to register an event object with the routing table manager. The routing table manager signals this event object to notify the routing protocol of changes in best-route information. All other components can obtain information stored in the routing table manager through route enumeration.

 

 




