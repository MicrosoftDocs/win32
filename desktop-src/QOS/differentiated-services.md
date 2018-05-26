---
title: Differentiated Services
description: Differentiated services enables packets that pass through network devices operating on Layer 3 information, such as routers, to have their relative priority differentiated from one another.
ms.assetid: 0b4afa74-0198-482d-af72-9ddf135a8e2f
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Differentiated Services

Differentiated services enables packets that pass through network devices operating on Layer 3 information, such as routers, to have their relative priority differentiated from one another. Differentiated services uses 6 bits in the IP header to specify its value, called the DSCP (DiffServ code point); the first 6 bits of the TOS field, the first three of which were formerly used for IP precedence. Differentiated services has subsumed IP precedence, but maintains backward compatibility.

With differentiated services marking, Layer 3 devices can establish aggregated precedence-based queues and provide better service (when packet service is subject to queuing, as is the case under significant traffic loads) to packets that have higher relative priority. For differentiated services to be effective, Layer 3 devices must be DSCP-enabled.

 

 




