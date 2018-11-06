---
title: Local Leave Callbacks
description: After the multicast group manager is notified by IGMP that there are no more receivers present for a group on an interface, the multicast group manager invokes the PMGM\_LOCAL\_LEAVE\_CALLBACK callback to the routing protocol on that interface if one exists. This callback notifies the routing protocol of the change.
ms.assetid: 47696533-603c-459f-9aa7-3ce42fff3332
ms.topic: article
ms.date: 05/31/2018
---

# Local Leave Callbacks

After the multicast group manager is notified by IGMP that there are no more receivers present for a group on an interface, the multicast group manager invokes the [**PMGM\_LOCAL\_LEAVE\_CALLBACK**](/windows/desktop/api/Mgm/nc-mgm-pmgm_local_leave_callback) callback to the routing protocol on that interface if one exists. This callback notifies the routing protocol of the change.

This callback and the [**PMGM\_LOCAL\_JOIN\_CALLBACK**](/windows/desktop/api/Mgm/nc-mgm-pmgm_local_join_callback) callback are used to synchronize forwarding between IGMP and routing protocols.

 

 




