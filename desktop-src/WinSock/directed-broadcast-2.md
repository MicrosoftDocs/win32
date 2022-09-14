---
description: Generally considered more network friendly than an all-routes broadcast, a directed broadcast limits itself to the local network that you specify.
ms.assetid: e2358580-5a65-434d-ba4c-a6b0615bccc3
title: Directed Broadcast
ms.topic: article
ms.date: 05/31/2018
---

# Directed Broadcast

Generally considered more network friendly than an all-routes broadcast, a directed broadcast limits itself to the local network that you specify. Fill **sa\_netnum** with the target network number and **sa\_nodenum** with binary ones. Routers forward this request to the destination network where it becomes a local broadcast. Intermediate networks do not see this packet as a broadcast.

 

 



