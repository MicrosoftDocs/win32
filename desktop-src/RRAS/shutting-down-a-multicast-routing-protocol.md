---
title: Shutting Down a Multicast Routing Protocol
description: The following table summarizes a series of steps in a shutdown interaction between the multicast group manager and the routing protocol when the routing protocol is shutting down.
ms.assetid: d868218d-7939-45d1-9e2f-3415c40f1a62
ms.topic: article
ms.date: 05/31/2018
---

# Shutting Down a Multicast Routing Protocol

The following table summarizes a series of steps in a shutdown interaction between the multicast group manager and the routing protocol when the routing protocol is shutting down. The first column describes the actions that the routing protocol performs and the routing protocol's responses to the multicast group manager. The second column describes the multicast group manager's responses to the routing protocol and any actions the multicast group manager performs such as callbacks. The third column presents any additional information.

Each row of the table represents one step.



| Routing protocol action                                                                                                                                     | Multicast group manager action                                                                                                                                                                                                                                                                                                                                                                                                                                            | Notes                                                                     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| Release ownership of each interface that the routing protocol owns using the [**MgmReleaseInterfaceOwnership**](/windows/desktop/api/Mgm/nf-mgm-mgmreleaseinterfaceownership) function. | If IGMP is also running on the interface that was just released by a routing protocol, contact IGMP using the [**PMGM\_DISABLE\_IGMP\_CALLBACK**](/windows/win32/api/mgm/nc-mgm-pmgm_disable_igmp_callback) callback. Once all changes to multicast data regarding interface ownership have been made, contact IGMP again using [**PMGM\_ENABLE\_IGMP\_CALLBACK**](/windows/desktop/api/Mgm/nc-mgm-pmgm_enable_igmp_callback) callback.<br/> Delete all the forwarding entries associated with this interface.<br/> |                                                                           |
| Deregister with the multicast group manager using the [**MgmDeRegisterMProtocol**](/windows/desktop/api/Mgm/nf-mgm-mgmderegistermprotocol) function.                                    | Destroy the handle that was returned to the routing protocol by a previous call to the [**MgmDeRegisterMProtocol**](/windows/desktop/api/Mgm/nf-mgm-mgmderegistermprotocol) function.                                                                                                                                                                                                                                                                                                                 | The routing protocol can no longer use this handle to call MGM functions. |



 

 

