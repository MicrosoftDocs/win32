---
title: RPF Alert Callbacks
description: After the multicast group manager receives notification of a packet from a new source or of a packet that is destined for a new group, the multicast group manager looks up the route to the source in the multicast view of the routing table.
ms.assetid: dacccca2-e6a5-417a-a217-06ff846d55f0
ms.topic: article
ms.date: 05/31/2018
---

# RPF Alert Callbacks

After the multicast group manager receives notification of a packet from a new source or of a packet that is destined for a new group, the multicast group manager looks up the route to the source in the multicast view of the routing table. The multicast group manager then invokes the [**PMGM\_RPF\_CALLBACK**](/windows/desktop/api/Mgm/nc-mgm-pmgm_rpf_callback) callback to the protocol that owns the interface the data arrived on.

After this callback is invoked, the routing protocol can change the incoming interface if the routing protocol must receive the data for the group on a different interface.

 

 




