---
title: IGMP Enable and Disable Callbacks
description: The multicast group manager uses two callbacks to IGMP to coordinate changes in interface ownership from IGMP to a routing protocol, and from a routing protocol to IGMP.
ms.assetid: e4b2be85-6c67-4801-9905-eb1990d4bbb6
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IGMP Enable and Disable Callbacks

The multicast group manager uses two callbacks to IGMP to coordinate changes in interface ownership from IGMP to a routing protocol, and from a routing protocol to IGMP. The callbacks enable IGMP to coexist on an interface with another routing protocol, such as DVMRP.

After the ownership of an interface changes, the multicast group manager first invokes the [**PMGM\_DISABLE\_IGMP\_CALLBACK**](/windows/win32/Mgm/nc-mgm-pmgm_disable_igmp_callback?branch=master) callback. IGMP must stop adding and deleting group memberships on the specified interface until the multicast group manager invokes the [**PMGM\_ENABLE\_IGMP\_CALLBACK**](/windows/win32/Mgm/nc-mgm-pmgm_enable_igmp_callback?branch=master) callback.

The multicast group manager invokes the [**PMGM\_ENABLE\_IGMP\_CALLBACK**](/windows/win32/Mgm/nc-mgm-pmgm_enable_igmp_callback?branch=master) callback after the change of interface ownership is complete.

 

 




