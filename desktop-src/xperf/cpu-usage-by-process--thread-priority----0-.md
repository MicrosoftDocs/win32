---
title: CPU Usage by Process \ Thread Priority 0\
description: CPU Usage by Process \ Thread Priority 0\
ms.assetid: 94fc33bd-b3d3-4bf6-88b7-f68d43c8d79b
keywords:
- usage graph
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CPU Usage by Process \[Thread Priority &gt;= 0\]

**Overview:** Displays CPU usage by process including the idle process which is disabled by default, as shown in the following screen shot.

![screen shot of a window showing cpu usage by process by thread where the zero page thread is included](images/gr-img014.png)

**Graph Type:** Usage graph.

**Y-axis Units:** Percentage of CPU usage by process

**Required Flags:** LOADER+ PROC\_THREAD+CSWITCH

**Events Captured:** Kernel and user mode Image Load/Unload, Process and Thread Create/Delete, CPU Sample Profile, Context Switch

**Legend Description:** Lists all active processes on the system.

**Graph Description:** Displays data sampled by ETW at millisecond intervals. Specific process and thread usage data can be selected from the legend.

Selecting "Set Minimum Priority" in the context menu controls the processes and threads shown based on priority. For more information on filtering by priority please see the[Set Minimum Priority Level](set-minimum-priority-level.md) in the Appendix of this document.

> [!Note]  
> Since the zero page thread is a kernel thread that is not actionable it is excluded from this display. Note that the data displayed on this graph is calculated by sampling CPU activity as opposed to the CPU Usage graphs that calculate the usage based on context switch events.

 

 

 




