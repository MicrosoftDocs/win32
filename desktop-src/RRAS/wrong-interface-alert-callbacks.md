---
title: Wrong Interface Alert Callbacks
description: After the kernel forwarder receives multicast data from a specific source on the wrong interface, it notifies the multicast group manager.
ms.assetid: 7b20625e-286b-4c4f-8452-4d21563fd030
ms.topic: article
ms.date: 05/31/2018
---

# Wrong Interface Alert Callbacks

After the kernel forwarder receives multicast data from a specific source on the wrong interface, it notifies the multicast group manager. The multicast group manager then invokes the [**PMGM\_WRONG\_IF\_CALLBACK**](/windows/desktop/api/Mgm/nc-mgm-pmgm_wrong_if_callback) callback to the routing protocol that owns the interface on which the data incorrectly arrived.

> [!Note]  
> This callback is not currently implemented in this version of the MGM API.

 

 

 




