---
title: CPU Usage by Thread \ Thread Priority 0\
description: CPU Usage by Thread \ Thread Priority 0\
ms.assetid: bd75e07e-36bb-467d-ad2e-da626d2075ef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CPU Usage by Thread \[Thread Priority &gt;= 0\]

**Overview:** Displays CPU usage by process including the idle process which is disabled by default, as shown in the following screen shot.

![screen shot of a window showing cpu usage by process by thread where zero page thread is included](images/gr-img014.png)

**Graph Type:** Usage graph.

**Y-axis Units:** Percentage of CPU usage by thread

**Required Flags:** LOADER+PROC\_THREAD +CSWITCH

**Events Captured:** Kernel and user mode Image Load/Unload, Process and Thread Create/Delete, CPU Sample Profile, Context Switch

**Legend Description:** Lists all threads that were active during the trace.

**Graph Description:** Displays data sampled by ETW at millisecond intervals. Specific CPU sampling can be selected by choosing CPU data series from the legend. Since the zero page thread is a kernel thread that is not actionable it is excluded from this display. Note that the data displayed on this graph is calculated by sampling CPU activity as opposed to the CPU Usage graphs that calculate the usage based on context switch events.

Selecting "Set Minimum Priority" in the context menu controls the processes shown based on priority. Changes to the priority filtering are reflected in the graph heading. For more information on setting a minimum priority please see the[Set Minimum Priority Level](set-minimum-priority-level.md) in the Appendix of this document.

 

 




