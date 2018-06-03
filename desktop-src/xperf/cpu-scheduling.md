---
title: CPU Scheduling
description: CPU Scheduling
ms.assetid: d45336c7-97e3-4d02-a075-335911dd9a93
keywords:
- event graph
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CPU Scheduling

**Overview:** Displays all context switches by CPU, as shown in the following screen shot.

![screen shot of a graph showing cpu scheduling zoomed to 500 microseconds](images/gr-img026.png)

**Graph Type:** Event graph

**Y-axis Units:** CPUs

**Required Flags:** CSWITCH+DISPATCHER

**Events Captured:** Context switch events

**Legend Description:** Shows CPUs on the system.

**Graph Description:** Shows all context switches for a time interval aggregated by CPU. A tooltip displays detailed information on the context switch including the call stack for the new thread. Further information on the call stacks is available through the summary tables. Summary tables are accessed by right clicking from the graph and choosing **Summary Table**.

> [!Note]  
> Context switches can occur millions of times per second. In order to display the discrete structure of the context switch streams it is necessary to zoom to a short time interval.

 

 

 




