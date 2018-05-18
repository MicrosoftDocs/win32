---
title: CPU Sampling by Thread
description: CPU Sampling by Thread
ms.assetid: 'def5484a-e4d0-4c83-a32f-63a986ed8c13'
---

# CPU Sampling by Thread

**Overview:** This graph presents a high level view of CPU usage by thread, as shown in the following screen shot.

![screen shot of a window showing cpu sampling by thread](images/gr-img033.png)

**Graph Type:** Usage graph

**Y-axis Units:** Percentage of CPU utilization

**Required Flags:** LOADER+PROC\_THREAD +PROFILE

**Events Captured:** Kernel and user mode Image Load/Unload, Process and Thread Create/Delete, CPU Sample Profile

**Legend Description:** Threads that were active during the trace capture

**Graph Description:** Displays data sampled by ETW at millisecond intervals for threads that were active during the trace capture.

> [!Note]  
> The data displayed in this graph is calculated by sampling CPU activity as opposed to the CPU Usage graphs that calculate the usage based on context switch events. For more information on calculating usage graphs please see [Notes on WPA Sampling](notes-on-wpa-sampling.md)

 

 

 




