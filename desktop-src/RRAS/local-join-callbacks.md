---
title: Local Join Callbacks
description: After the multicast group manager is notified by IGMP that new receivers are present for a group on an interface, the multicast group manager invokes the PMGM\_LOCAL\_JOIN\_CALLBACK callback to the routing protocol that owns the interface if one exists.
ms.assetid: 136f86e0-380d-4158-a9dd-c6de1c7f6689
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Local Join Callbacks

After the multicast group manager is notified by IGMP that new receivers are present for a group on an interface, the multicast group manager invokes the [**PMGM\_LOCAL\_JOIN\_CALLBACK**](/windows/win32/Mgm/nc-mgm-pmgm_local_join_callback?branch=master) callback to the routing protocol that owns the interface if one exists. This callback notifies the routing protocol of the change.

This callback and the [**PMGM\_LOCAL\_LEAVE\_CALLBACK**](/windows/win32/Mgm/nc-mgm-pmgm_local_leave_callback?branch=master) callback are used to synchronize forwarding between IGMP and routing protocols.

 

 




