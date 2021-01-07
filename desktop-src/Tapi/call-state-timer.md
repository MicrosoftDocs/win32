---
description: Currently, all timing of calls is left up to applications.
ms.assetid: 9eb98b48-4bee-4f6d-b818-2f81b36591da
title: Call State Timer
ms.topic: article
ms.date: 05/31/2018
---

# Call State Timer

Currently, all timing of calls is left up to applications. This can be burdensome if the application is monitoring a large number of calls, and if multiple applications are present, possibly on multiple servers, it can be necessary for them to all maintain timers on the same calls. It therefore makes more sense for call state timing to be handled by the server.

The **tStateEntryTime** member in [**LINECALLSTATUS**](/windows/desktop/api/Tapi/ns-tapi-linecallstatus) allows timing of calls in states to be reported. The member (of type **SYSTIME**) indicates the time at which the current state was entered.

 

 



