---
title: CPU Sampling by Process
description: CPU Sampling by Process
ms.assetid: '13f2f03b-063b-48c2-9fe9-2e58bc895e64'
keywords: ["usage graph"]
---

# CPU Sampling by Process

**Overview:** This graph presents a high level view of CPU usage aggregated by process, as shown in the following screen shot.

![screen shot of a window showing cpu usage by process](images/gr-img012.png)

**Graph Type:** Usage graph

**Y-axis Units:** Percentage of CPU used aggregated by process

**Required Flags:** LOADER+PROC\_THREAD+PROFILE

**Events Captured:** Kernel-mode and user-mode Image Load/Unload, Process and Thread Create/Delete, CPU Sample Profile

**Legend Description:** Lists all active processes on the system.

**Graph Description:** Displays data sampled by ETW at millisecond intervals. Specific threads can be selected in the legend.

> [!Note]  
> Although this graph is referred to as a "usage graph", the data displayed is calculated by sampling CPU activity as opposed to the CPU Usage graphs that calculate the usage based on context switch events. For more information on calculating usage graphs please see [Notes on WPA Sampling](notes-on-wpa-sampling.md).

 

 

 




