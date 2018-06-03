---
title: CPU Usage by CPU \ Thread Priority 1\
description: CPU Usage by CPU \ Thread Priority 1\
ms.assetid: 18824a19-80aa-47e4-9cc3-67db425e23fe
keywords:
- usage graph
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CPU Usage by CPU \[Thread Priority &gt;= 1\]

**Overview:** Displays CPU usage for those threads with a priority greater than or equal to 1, as shown in the following screen shot.

![screen shot of a window showing cpu usage by cpu \[thread priority &gt;= 1\]](images/gr-img013.png)

**Graph Type:** Usage graph.

**Y-axis Units:** CPU utilization as a percentage

**Required Flags:** LOADER+PROC\_THREAD+CSWITCH

**Events Captured:** Kernel and user mode Image Load/Unload, Process and Thread Create/Delete and Context Switch

**Legend Description:** Lists all active processes on the system. Selecting "Set Minimum Priority" in the context menu controls the threads that are included in the graph based on priority. For more information on filtering by priority please see the[Set Minimum Priority Level](set-minimum-priority-level.md) in the Appendix of this document.

**Graph Description:** Displays usage percentages based on the number and frequency of context switch events for a defined time interval. A specific CPU can be selected by choosing CPU data series from the legend. Threads with a Thread Priority of zero are associated with the System Idle process.

 

 




