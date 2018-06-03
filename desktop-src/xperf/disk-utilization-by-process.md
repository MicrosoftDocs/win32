---
title: Disk Utilization by Process
description: Disk Utilization by Process
ms.assetid: 0a5c7982-12d3-4fad-9318-687cb13797dc
keywords:
- usage graph
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Disk Utilization by Process

**Overview:** Displays disk utilization aggregated by process, as shown in the following screen shot.

![screen shot of a window showing disk utilization aggregated by process](images/gr-img018.png)

**Graph Type:** Usage graph

**Y-axis Units:** Displays the percentage of disk throughput capacity being used at a given point in time

**Required Flags:** DISK\_IO+LOADER+PROC\_THREAD

**Events Captured:** Disk I/O events, Kernel and user mode Image Load/Unload events, Process and Thread create/delete

**Legend Description:** Lists processes that performed IO during the trace period.

**Graph Description:** Displays disk utilization by process. Using the legend to filter the data you can determine utilization by disk and by priority. In order to aggregate disk I/O across multiple disks use the summary table that can be open from this graph. See [Summary Tables](summary-tables.md) for more information on this topic.

Disk utilization by process is a key indicator of disk based bottlenecks as disk access is measured in milliseconds while CPU cycles are measured in nanoseconds representing an orders of magnitude difference of 106.

 

 




