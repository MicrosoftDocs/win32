---
description: Clouds are used by the Peer Grouping and Graphing Infrastructures.
ms.assetid: 01327211-0461-4922-925e-67bebe3e6158
title: Clouds
ms.topic: article
ms.date: 05/31/2018
---

# Clouds

Clouds are used by the Peer [Grouping](grouping-api.md) and [Graphing](graphing-api.md) Infrastructures. The [Peer Name Resolution Protocol (PNRP)](pnrp-namespace-provider-api.md) identifies a cloud as a set of peers that can communicate within the same IPv6 scope. Clouds are closely related to the IPv6 scopes. The following list identifies some of the unique cloud features:

-   A cloud is identified by a name, and available clouds can be enumerated by using [**WSALookupServiceBegin**](pnrp-and-wsalookupservicebegin.md).
-   If a computer is connected to the Internet, it is part of a global cloud, which is identified by the string "Global\_".
-   If a computer is connected to one or more local area networks (LAN), individual clouds are available for each link.
-   One computer can be connected to many networks by having multiple network adapters or by using a virtual private network (VPN), which means that a computer with one interface can be visible in many clouds.
-   You can use PNRP to register and resolve peer names in a specific cloud.

 

 



