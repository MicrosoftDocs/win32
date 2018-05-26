---
title: Data Structure Growth Patterns
description: Data Structure Growth Patterns
ms.assetid: 82babc0b-306f-45ab-932f-eb1c7e77942e
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Data Structure Growth Patterns

If one or both of the following conditions exist in a call stack, possibly the growth strategy is too conservative.

-   A large number of small percentage increases in allocation size

-   Steady, incremental increase in the allocation size

Conversely, a small number of high percentage increases in the allocation size would be an indicator of too aggressive of a growth policy and would lead to overshooting of the buffer size and contribute to peak outstanding size issues.

Overshooting due to aggressive growth strategies can lead to excess heap outstanding size due to over capacity of the data structures. Extreme care should be taken to avoid unused allocations in long lived data structures. However, too conservative of a growth strategy can also lead to overshooting due to inappropriate initial sizes and can result in excess CPU usage from growth. Therefore it is important to understand the usage pattern of a data structure before changes in growth strategy or initial sizes are made.

 

 




